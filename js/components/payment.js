export default class {
    constructor(context) {      
        this.context = context;
        
        window.onload = () => {
            this.renderForm();
            this.renderHiddenFields();
            this.initialize();
        };
    }

    renderForm() {
        this.newForm = this.context.cloneNode();
        const inputs = this.context.querySelector('table').querySelectorAll('input');
        [].forEach.call(inputs, input => {
            if (input.type !== 'hidden') {
                const container = document.createElement('div');
                container.className = 'field-group';
    
                const label = document.createElement('label');
                label.className = 'input';
    
                const span = document.createElement('span');
                span.textContent = this.getLabel(input);
                span.className = 'input__label input__label--white';
    
                input.className = input.type === 'submit' ? 'button button--middle button--adaptive button--secondary' : 'input__field';

                if (input.type === 'submit') input.removeAttribute('name');
                
                label.appendChild(span);
                label.appendChild(input);
                container.appendChild(label);
                this.newForm.appendChild(container);
            }
        })
    }

    getLabel(input) {
        const labelField = input.closest('tr').querySelector('.ea_name_field');
        if (!labelField) return;

        let label = labelField.textContent;
        label = input.closest('tr').querySelector('.ea_required_text') ? `${label} *` : label;
        return label;
    }

    renderHiddenFields() {
        const inputs = this.context.querySelector('table').querySelectorAll('input[type="hidden"]');
        [].forEach.call(inputs, input => {
            this.newForm.appendChild(input);
        })
        this.context.parentNode.insertBefore(this.newForm, this.context);
        this.context.parentNode.removeChild(this.context);
    }

    initialize() {
        this.newForm.addEventListener('submit', this.onSubmit.bind(this));
        this.email = this.newForm.querySelector('input[name="email"]');
        this.phone = this.newForm.querySelector('input[name="phone"]');
        this.product = this.newForm.querySelector('input[name="tovar_id"]');

        this.id = new URLSearchParams(window.location.search).get('id');
        this.product.value = this.id;
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
        if (!this.id) {
            alert('Неверный id продукта');
            return;
        };
        this.reset();
        if (this.validate()) {
            e.target.submit();
        }
    }

}