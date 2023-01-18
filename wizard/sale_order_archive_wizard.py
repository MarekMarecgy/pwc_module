# -*- coding: utf-8 -*-
from odoo import api, fields, models, _


class SaleOrderArchiveWizard(models.TransientModel):
	_name = "sale.order.archive.wizard"

	@api.model
	def _add_sale_orders(self):
		selected_ids = (self._context.get('active_ids', []))
		selected_records = self.env['sale.order'].browse(selected_ids)
		return selected_records

	sale_order_ids = fields.Many2many('sale.order', default=_add_sale_orders)

	def archive_selected_records(self):
		for record in self.sale_order_ids:
			self.env['sale.order.archive'].create({
				'name': record.name,
				'order_create_date': record.create_date,
				'customer_id': record.partner_id.id,
				'sale_person_id': record.user_id.id,
				'order_total_amount': record.amount_total,
				'order_currency_id': record.currency_id.id,
				'count_of_order_lines': len(record.order_line)
			})
			record.action_cancel()
			record.unlink()


# EoF
