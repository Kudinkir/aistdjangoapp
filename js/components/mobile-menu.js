export default class MobileMenu {
    constructor(context, componentName) {
        this.context = context;

        this.active = false;

        this.button = this.context.querySelector('[data-trigger="menu"]');
        this.menu = this.context.querySelector('[data-content="menu"]');
        this.main = document.querySelector('main');

        this.button.addEventListener('click', event => {
            event.preventDefault();

            this.toggleMenu();
        });

        window.addEventListener('resize', () => {
            this.active = false;
            this.toggleMenu();
        });

        console.log(componentName, 'loadedd');
    }

    toggleMenu() {
        this.button.classList[this.active ? 'add' : 'remove']('active');
        this.menu.classList[this.active ? 'add' : 'remove']('active');
        this.context.classList[this.active ? 'add' : 'remove']('active');
        document.body.style.overflow = this.active ? 'hidden' : '';
        document.body.style.paddingRight = this.active ? '15px' : '';
        this.main.style.overflow = this.active ? 'hidden' : '';        

        this.active = !this.active;
    }
}
