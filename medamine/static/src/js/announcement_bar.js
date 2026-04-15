/** @odoo-module **/

import publicWidget from "@web/legacy/js/public/public_widget";

publicWidget.registry.AnnouncementBar = publicWidget.Widget.extend({
    selector: '#announcement_bar',

    start() {
        const announcementId = this.el.dataset.announcementId;
        const storageKey = `announcement_bar_closed_${announcementId}`;

        // Already closed in this session: remove from DOM to avoid layout shift
        if (sessionStorage.getItem(storageKey)) {
            this.el.remove();
            return this._super(...arguments);
        }

        const closeBtn = this.el.querySelector('.announcement-bar-close');
        if (closeBtn) {
            closeBtn.addEventListener('click', () => {
                try {
                    sessionStorage.setItem(storageKey, '1');
                } catch (_) {}
                this.el.classList.add('announcement-bar--hidden');
                this.el.addEventListener('transitionend', () => {
                    this.el.remove();
                }, { once: true });
                // Fallback if transitionend never fires (e.g. prefers-reduced-motion)
                setTimeout(() => this.el.remove(), 400);
            });
        }

        return this._super(...arguments);
    },
});
