export default class {
    constructor(context) {
        context.addEventListener('submit', this.onSubmit.bind(this));
        this.email = context.querySelector('input[name="email"]');
        this.phone = context.querySelector('input[name="phone"]');
    }

    reset() {
        this.email.classList.remove('error');
        this.phone.classList.remove('error')
    }

    validate() {
        if (!/(\w|-){1,}\@\w{1,}\.\w+/g.test(this.email.value)) {
            setTimeout(() => this.email.classList.add('error'));
            return false;
        }

        if (!/^(\+)?(\(\d{2,3}\) ?\d|\d)(([ \-]?\d)|( ?\(\d{2,3}\) ?)){5,12}\d$/g.test(this.phone.value)) {
            setTimeout(() => this.phone.classList.add('error'));
            return false;
        }

        return true;
    }

    onSubmit = e => {
        e.preventDefault();
        this.reset();
        if (this.validate()) {
            e.target.submit();
        }
    }

}