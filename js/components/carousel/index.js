import LeftArrow from 'svgIcons/arrow-left-secondary.svg';
import RightArrow from 'svgIcons/arrow-right-secondary.svg';

import styles from './styles.css';

export default class Carousel {
    constructor(context, componentName) {
        this.context = context;
        this.initially = false;

        if (!this.initially && window.innerWidth < 1024) {
            this.init();
            this.initially = true;
        } else {
            window.matchMedia('(max-width: 1024px)').addListener(event => {
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
        const items = document.querySelectorAll('.carousel__item');
        const direction = type === 'left' ? -1 : 1;
        const pos = Math.round((this.itemsWrapper.scrollLeft / items[0].offsetWidth) + direction) * items[0].offsetWidth;       
        this.scroll(this.itemsWrapper, pos)
    }

    scroll(target, pos, offset = 0) {
        if (window.animId) cancelAnimationFrame(window.animId);
        const newOffset = (target.scrollLeft - pos) / 8;
        if(target.scrollLeft === pos || newOffset === offset) return;
        target.scrollLeft -= newOffset;
        window.animId = requestAnimationFrame(() => this.scroll(target, pos, newOffset));
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
