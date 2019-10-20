import LeftArrow from 'svgIcons/arrow-left-secondary.svg';
import RightArrow from 'svgIcons/arrow-right-secondary.svg';

export default class CarouselItems {
    constructor(context) {
        this.context = context;
        this.itemsWrapper = context.querySelector('.course-page__benefits');
        this.renderNavigation()
    }

    handleClick(event, type) {        
        const items = document.querySelectorAll('.course-page__benefit');
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
        container.classList.add('course-page__carousel');

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

        this.context.appendChild(container);
    }
}