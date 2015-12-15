#-*- encoding: utf-8 -*-
##############################################################################
#
#    Copyright (c) 2011-TODAY MINORISA (http://www.minorisa.net) All Rights Reserved.
#                             Minorisa <contact@minorisa.net>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from openerp import models, fields, api
import openerp.addons.decimal_precision as dp
import logging

_logger = logging.getLogger(__name__)

class StockProductionLot(models.Model):

    _inherit = 'stock.production.lot'

    @api.depends('product_id')
    def _get_qty_available(self):
        context = dict(self._context)
        for lot in self:
            context.update({'lot_id': lot.id})
            x = lot.product_id.with_context(context)._product_available()
            lot.qty_available = x[lot.product_id.id]['qty_available'] or 0.0

    qty_available = fields.Float(string="Quantity On Hand", digits=dp.get_precision('Product Unit of Measure'), compute='_get_qty_available')

    @api.multi
    def name_get(self):
        res = super(StockProductionLot, self).name_get()
        _logger.debug('01 MIN lot res %s' % (res))
        if not res:
            return []
        resd = dict(res)
        res1 =[]
        for lot in self:
            name_new = resd[lot.id] + '  [' + str(lot.qty_available) +' '+ lot.product_id.uom_id.name+']'
            _logger.debug('03 MIN lot name %s' % (name_new))
            l = (lot.id,name_new)
            res1.append(l)
        return res1
