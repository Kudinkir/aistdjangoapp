export default class subscribeForm {
    constructor(context, componentName) {
        this.context = context;
        this.form = this.context.querySelector('')
        this.nextButton = this.context.querySelector('[data-handle="next"]');

        console.log(componentName, '🚀');
    }

    events() {
        this.nextButton.addEventListener('click', this.handleShowNext);
        this.context.addEventListener('submit', this.handleSubmit);
    }

    handleShowNext = () => {
        this.
    }

    handleSubmit = e => {
        e.preventDefault();

        fetch('/subscribe', { method: 'POST', body: new FormData(this.context) }).then(resp => {
            console.log(resp);
        });
    };
}
