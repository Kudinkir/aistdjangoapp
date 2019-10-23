export default class ContactForm {
    constructor(context, componentName) {
        this.context = context;
        this.context.addEventListener('submit', this.onSubmit)
    }

    onSubmit = e => {
        e.preventDefault();
        const body = new FormData(this.context);

        fetch('/callback', { method: 'POST', body })
            .finally(() => this.context.reset())
            .then(resp => resp.json())
            .catch(console.log)
    }
}
