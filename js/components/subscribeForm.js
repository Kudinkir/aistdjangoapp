const AMOUNT_MIN = 1;

export default class SubscribeForm {
    constructor(context, componentName) {
        this.context = context;
        this.nextButton = this.context.querySelector('[data-type="next"]');
        this.prevButton = this.context.querySelector('[data-type="prev"]');
        this.email = this.context.querySelector('input[name="email"]');
        this.submitButton = this.context.querySelector('[data-handle="submit"]');

        this.amount = this.context.querySelector('[data-handle="amount"]');
        this.amountValue = parseInt(this.amount.value, 10);
        this.views = [...this.context.querySelectorAll('[data-handle="view"]')];

        this.views.forEach(item => {
            const { active } = item.dataset;
            const isActive = typeof active !== 'undefined' ? true : false;

            item.classList[isActive ? 'remove' : 'add']('hidden');
        });
        this.activeView = 0;

        this.events();
        console.log(componentName, '🚀');
    }

    events() {
        this.amountIncrement = this.context.querySelector('[data-handle="increment"]');
        this.amountDecrement = this.context.querySelector('[data-handle="decrement"]');

        [this.amountIncrement, this.amountDecrement].forEach(item => {
            item.addEventListener('click', this.handeChangeAmount);
        });

        this.nextButton.addEventListener('click', this.handleShow);
        this.prevButton.addEventListener('click', this.handleShow);
        this.submitButton.addEventListener('click', this.handleSubmit);
    }

    handeChangeAmount = event => {
        event.preventDefault();

        const {
            dataset: { handle: type },
        } = event.target;

        if (type === 'decrement' && this.amountValue !== AMOUNT_MIN) {
            this.amountValue -= 1;
        }

        if (type === 'increment') {
            this.amountValue += 1;
        }

        this.amount.value = this.amountValue;
    };

    handleShow = event => {
        const {
            target: {
                dataset: { type },
            },
        } = event;
        const isNext = type === 'next';

        this.email.classList.remove('error');
        if (!/(\w|-){1,}\@\w{1,}\.\w+/g.test(this.email.value)) {
            setTimeout(() => this.email.classList.add('error'));

            return;
        }

        this.activeView = isNext ? this.activeView + 1 : this.activeView - 1;
        this.views.forEach((item, index) => {
            item.classList[index === this.activeView ? 'remove' : 'add']('hidden');
        });
    };

    handleSubmit = event => {
        event.preventDefault();

        const body = new FormData(this.context);

        fetch('/subscribe', { method: 'POST', body }).then(r => r.json()).then(resp => {
            console.log(resp);
        });
    };
}
