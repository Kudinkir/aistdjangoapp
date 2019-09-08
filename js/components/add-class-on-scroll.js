import { throttle } from 'utils';

export default class AddClassOnScroll {
    constructor(context, componentName) {
        this.context = context;
        this.isVisible = false;
        this.height = context.getBoundingClientRect();

        this.handleVisibility();
        window.addEventListener('scroll', this.handleVisibility.bind(this));

        console.log(componentName, 'loaded');
    }

    handleVisibility() {
        const visibility = window.scrollY > 0;

        if (visibility === this.isVisible) return;

        this.isVisible = visibility;
        this.context.classList[visibility ? 'add' : 'remove']('sticky');
    }
}
