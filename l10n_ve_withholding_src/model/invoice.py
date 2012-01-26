#!/usr/bin/python
# -*- encoding: utf-8 -*-
###########################################################################
#    Module Writen to OpenERP, Open Source Management Solution
#    Copyright (C) OpenERP Venezuela (<http://openerp.com.ve>).
#    All Rights Reserved
###############Credits######################################################
#    Coded by: Humberto Arocha <hbto@vauxoo.com>     
#    Planified by: Humberto Arocha / Nhomar Hernandez
#    Audited by: Vauxoo C.A.
#############################################################################
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
################################################################################

import time
from osv import fields, osv
from tools.translate import _
import decimal_precision as dp

class account_invoice(osv.osv):
    _inherit = 'account.invoice'
    
    _columns = {
        'wh_src_rate': fields.float('SRC Wh rate', digits_compute= dp.get_precision('Withhold'), readonly=True, states={'draft':[('readonly',False)]}, help="Social Responsibility Commitment Withholding Rate"),
        'wh_src_id': fields.many2one('account.wh.src', 'Wh. SRC Doc.', readonly=True, help="Social Responsibility Commitment Withholding Document"),        
    }

account_invoice()
