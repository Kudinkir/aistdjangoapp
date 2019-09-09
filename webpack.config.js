const path = require('path');
const webpack = require('webpack');

const CaseSensitivePathsPlugin = require('case-sensitive-paths-webpack-plugin');
const CleanWebpackPlugin = require('clean-webpack-plugin');
const MiniCssExtractPlugin = require('mini-css-extract-plugin');
const OptimizeCSSAssetsPlugin = require('optimize-css-assets-webpack-plugin');
const safePostCssParser = require('postcss-safe-parser');
const TerserPlugin = require('terser-webpack-plugin');
const { BundleAnalyzerPlugin } = require('webpack-bundle-analyzer');
const BundleTracker = require('webpack-bundle-tracker');

const isProd = process.env.NODE_ENV === 'production';
const isAnalyze = process.env.ANALYZE || false;

const cssFilename = isProd ? '[name].[contenthash:8].css' : '[name].css';

const PATHS = {
    web: path.join(__dirname, 'public/build'),
    public: '/static/build/',
};

module.exports = {
    mode: isProd ? 'production' : 'development',
    devtool: isProd ? '' : 'cheap-module-source-map',
    entry: [path.join(__dirname, 'js/index.js'), path.join(__dirname, 'styles/index.css')],
    output: {
        path: PATHS.web,
        filename: isProd ? '[name].[contenthash:8].js' : '[name].js',
        chunkFilename: isProd ? '[name].[contenthash:8].chunk.js' : '[name].chunk.js',
        publicPath: PATHS.public,
    },
    optimization: {
        minimize: isProd,
        minimizer: [
            new TerserPlugin({
                terserOptions: {
                    parse: {
                        ecma: 8,
                    },
                    compress: {
                        ecma: 5,
                        warnings: false,
                        comparisons: false,
                        inline: 2,
                        pure_funcs: ['console.log'],
                    },
                    mangle: {
                        safari10: true,
                    },
                    output: {
                        ecma: 5,
                        comments: false,
                        ascii_only: true,
                    },
                },
                parallel: true,
                cache: true,
                sourceMap: false,
            }),
            new OptimizeCSSAssetsPlugin({
                cssProcessorOptions: {
                    parser: safePostCssParser,
                    discardComments: {
                        removeAll: true,
                    },
                    // map: {
                    //     inline: false,
                    //     annotation: true,
                    // },
                },
            }),
        ],
        concatenateModules: isProd,
        noEmitOnErrors: isProd,
        namedModules: !isProd,
        runtimeChunk: false,
        splitChunks: isProd
            ? {
                  chunks: 'all',
                  // name: 'vendors',
              }
            : false,
    },
    module: {
        strictExportPresence: true,
        rules: [
            {
                parser: {
                    requireEnsure: false,
                },
            },
            {
                oneOf: [
                    {
                        test: /\.(js|jsx)$/,
                        loader: require.resolve('babel-loader'),
                        options: {
                            compact: isProd,
                            cacheCompression: isProd,
                            cacheDirectory: true,
                        },
                    },
                    {
                        test: /\.css$/,
                        loader: [
                            !isProd && require.resolve('css-hot-loader'),
                            MiniCssExtractPlugin.loader,
                            {
                                loader: require.resolve('css-loader'),
                                options: {
                                    importLoaders: 1,
                                    // url: true,
                                    sourceMap: false,
                                },
                            },
                            {
                                loader: require.resolve('postcss-loader'),
                                options: {
                                    ident: 'postcss',
                                    plugins: [
                                        require('postcss-easy-import'),
                                        require('postcss-atrule-bem'),
                                        require('postcss-preset-env')({
                                            autoprefixer: {
                                                grid: true,
                                                flexbox: 'no-2009',
                                            },
                                            preserve: false,
                                            stage: 0,
                                            importFrom: './styles/base.css',
                                        }),
                                        require('postcss-flexbugs-fixes'),
                                        require('postcss-hexrgba'),
                                        require('postcss-color-function'),
                                    ],
                                },
                            },
                        ].filter(Boolean),
                    },
                    {
                        loader: require.resolve('file-loader'),
                        exclude: [/\.(ejs|js|jsx|mjs)$/, /\.html$/, /\.json$/, /\.css$/],
                        options: {
                            name: 'media/[name].[hash:8].[ext]',
                        },
                    },
                ],
            },
        ],
    },
    plugins: [
        new BundleTracker({ filename: './webpack-stats.json' }),
        new MiniCssExtractPlugin({
            filename: cssFilename,
        }),
        isProd
            ? new CleanWebpackPlugin([PATHS.web], {
                  beforeEmit: true,
                  verbose: true,
              })
            : new CaseSensitivePathsPlugin(),
        !isProd && new webpack.HotModuleReplacementPlugin(),
        isAnalyze && new BundleAnalyzerPlugin(),
    ].filter(Boolean),
    resolve: {
        extensions: ['.js', '.css'],
        modules: ['node_modules', path.resolve(__dirname, 'js')],
        alias: {
            svgIcons: path.resolve(__dirname, 'svg'),
            fonts: path.resolve(__dirname, 'fonts'),
        },
    },
    devServer: {
        proxy: {
            '*': 'http://127.0.0.1:8000',
        },
        compress: true,
        historyApiFallback: {
            disableDotRule: true,
        },
        hot: true,
        stats: 'errors-only',
        overlay: true,
    },
    stats: {
        hash: false,
        version: false,
        children: false,
        modules: false,
        warnings: false,
        entrypoints: false,
    },
    performance: false,
};
