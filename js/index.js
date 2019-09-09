import 'fonts/CSTM-Xprmntl-02/index';

import MobileMenu from './components/mobile-menu';
import AddClassOnScroll from './components/add-class-on-scroll';
import Carousel from './components/carousel/index';
import Tabs from './components/tabs';

const importedComponents = {
    MobileMenu,
    AddClassOnScroll,
    Carousel,
    Tabs,
};

const initComponents = (rootNode = document, COMPONENT_IDENTIFIER) => {
    [].forEach.call(rootNode.querySelectorAll(`[${COMPONENT_IDENTIFIER}]`), component => {
        const componentNameArr = component.getAttribute(COMPONENT_IDENTIFIER).split(',');

        componentNameArr.forEach(componentName => {
            component._initialisedComponent = component._initialisedComponent || {};

            if (!component._initialisedComponent[componentName]) {
                if (importedComponents.hasOwnProperty(componentName)) {
                    const Component = importedComponents[componentName];

                    try {
                        if (typeof Component === 'object') {
                            Component.get().then(({ default: asyncComponent }) => {
                                component._initialisedComponent[componentName] = new asyncComponent(
                                    component,
                                    componentName
                                );
                            });
                        } else {
                            component._initialisedComponent[componentName] = new Component(
                                component,
                                componentName
                            );
                        }
                    } catch (e) {
                        console.error(e);
                    }
                } else {
                    console.warn(`${componentName} has not been imported into this bundle`);
                }
            }
        });
    });
};

initComponents(document, 'data-component');
