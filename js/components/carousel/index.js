import LeftArrow from 'svgIcons/arrow-left-secondary.svg';
import RightArrow from 'svgIcons/arrow-right-secondary.svg';

import styles from './styles.css';

export default class Carousel {
    constructor(context, componentName) {
        this.context = context;
        this.initially = false;

        if (!this.initially && window.innerWidth < 768) {
            this.init();
            this.initially = true;
        } else {
            window.matchMedia('(max-width: 768px)').addListener(event => {
                if (!this.initially && event.matches) {
                    this.init();

                    this.initially = true;
                }
            });
        }
        console.log(componentName, 'loaded');
    }

    init() {
        this.childrens = [...this.context.children];

        const wrapper = this.context.cloneNode();
        wrapper.classList = '';
        wrapper.classList.add('carousel');

        this.context.parentNode.insertBefore(wrapper, this.context);
        this.context.remove();
        this.context = wrapper;

        this.itemsWrapper = document.createElement('div');
        this.itemsWrapper.classList.add('carousel__items');
        this.childrens.forEach(item => {
            item.classList.add('carousel__item');
            this.itemsWrapper.appendChild(item);
        });

        this.context.appendChild(this.itemsWrapper);
        this.context.appendChild(this.renderNavigation());
    }

    handleClick(event, type) {
        console.log(event, type);

        const { clientWidth, scrollWidth, scrollLeft } = this.itemsWrapper;

        const [children] = this.childrens;
        const { clientWidth: widthChild } = children;
        console.dir(widthChild);

        const visibleItems = Math.round(clientWidth / widthChild);
        const allItems = Math.round(scrollWidth / widthChild);

        // todo last

        if (scrollWidth / scrollLeft < visibleItems) {
            this.itemsWrapper.scrollLeft = scrollWidth;
        }

        if (type === 'left') {
            this.itemsWrapper.scrollLeft -= widthChild;
        } else {
            this.itemsWrapper.scrollLeft += widthChild;
        }

        // console.info(scrollLeft, scrollWidth);
        // console.dir(this.itemsWrapper);
    }

    renderNavigation() {
        const container = document.createElement('div');
        container.classList.add('carousel__nav');

        const button = (icon, type) => {
            const foo = document.createElement('button');

            foo.classList.add('carousel__arrow');
            foo.setAttribute('type', 'button');
            foo.innerHTML = icon;
            foo.addEventListener('click', this.handleClick.bind(this, this, type));

            return foo;
        };

        [{ type: 'left', icon: LeftArrow }, { type: 'right', icon: RightArrow }]
            .map(item => button(`<img src="${item.icon}" alt="" />`, item.type))
            .forEach(item => container.appendChild(item));

        return container;
    }
}
