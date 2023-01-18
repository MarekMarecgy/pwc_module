# -*- coding: utf-8 -*-

from odoo import models, fields, api
import datetime


class SaleOrderArchive(models.Model):
	_name = "sale.order.archive"
	_description = "Sales Order Archive model"

	name = fields.Char(string="Name")
	order_create_date = fields.Date(string="Order create date")
	customer_id = fields.Many2one('res.partner', string="Customer")
	sale_person_id = fields.Many2one('res.users', string="Sale person")
	order_total_amount = fields.Monetary(currency_field='order_currency_id', string="Order total amount")
	order_currency_id = fields.Many2one('res.currency', string="Currency")
	count_of_order_lines = fields.Integer(string="Number of order lines")

	def sale_orders_to_archive(self):
		date = datetime.datetime.today() - datetime.timedelta(days=7)
		check_date = date.strftime("%Y-%m-%d")
		domain = [('create_date', '<', check_date)]
		orders_to_archive = self.env['sale.order'].search(domain)
		if orders_to_archive:
			for record in orders_to_archive:
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
			orders_to_archive.unlink()

# EoF
