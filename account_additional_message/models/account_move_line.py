from odoo import api, fields, models, _
from odoo.exceptions import UserError


class AccountMoveLine(models.Model):
    _inherit = 'account.move.line'

    @api.constrains('account_id', 'journal_id')
    def _check_constrains_account_id_journal_id(self):
        for line in self.filtered(lambda x: x.display_type not in ('line_section', 'line_note')):
            account = line.account_id
            journal = line.move_id.journal_id

            if account.deprecated:
                raise UserError(_('The account %s (%s) is deprecated.') % (account.name, account.code))

            account_currency = account.currency_id
            if account_currency and account_currency != line.company_currency_id and account_currency != line.currency_id:
                raise UserError(_('The account selected on your journal entry forces to provide a secondary currency. You should remove the secondary currency on the account.'))

            if account.allowed_journal_ids and journal not in account.allowed_journal_ids:
                raise UserError(_('You cannot use this account (%s) in this journal, check the field \'Allowed Journals\' on the related account.', account.display_name))

            if account in (journal.default_account_id, journal.suspense_account_id):
                continue

            is_account_control_ok = not journal.account_control_ids or account in journal.account_control_ids
            is_type_control_ok = not journal.type_control_ids or account.user_type_id in journal.type_control_ids

            if not is_account_control_ok or not is_type_control_ok:
                raise UserError(f"No puedes usar esta cuenta {account.display_name} en"
                                f" este diario: {journal.display_name}, consulte la sección 'Control-Acceso' en "
                                "pestaña 'Configuración avanzada' en la diario relacionado.")

