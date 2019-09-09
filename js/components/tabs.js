export default class Tabs {
    constructor(context, componentName) {
        this.context = context;

        const { active: activeProp } = this.context.dataset;

        const trigger = this.context.querySelector('[data-handle="trigger"]');
        const content = this.context.querySelector('[data-handle="content"]');
        let active = active || false;

        trigger.addEventListener('click', e => {
            e.preventDefault();

            active = !active;
            trigger.classList[active ? 'add' : 'remove']('active');
            content.classList[active ? 'add' : 'remove']('active');
        });
    }
}
