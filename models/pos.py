from odoo import models, fields, api, _
from odoo.addons import decimal_precision as dp
import logging
from odoo.exceptions import except_orm, Warning, RedirectWarning
import datetime
_logger = logging.getLogger(__name__)


class PosSession(models.Model):
    _inherit = "pos.session"


    def action_print_control(self):
        res = self.get_control_pos()
        if len(res['docs']) == 0:
            raise Warning('Aucun résultats trouvés')
        return self.env.ref('pos_extend.report_pos_session').report_action(self)


    def get_control_pos(self):
        print('hello')
        query = """
                        select pc."name",sum(pol.price_subtotal) as subtotal,ppm.name from pos_order po inner join pos_order_line pol ON pol.order_id =po.id 
                        inner join product_product pp on pp.id=pol.product_id 
                        left join product_template pt on pt.id=pp.product_tmpl_id 
                        left join product_category pc on pc.id=pt.categ_id 
                        left join (select distinct session_id,payment_method_id  from pos_payment) pp2 on pp2.session_id =po.session_id 
                        left join pos_payment_method ppm on pp2.payment_method_id =pp.id 
                        where po.session_id =""" + str(self.id) + """
                        group by pc."name",ppm.name
                    """

        self.env.cr.execute(query)
        res = self.env.cr.fetchall()
        all_details = []

        for line in res:
            all_details.append({
                'famille': line[0],
                'total': line[1],
                'methode': line[2],
            })

        print(all_details)
        return  all_details

# class PosSessionReport(models.AbstractModel):
#     _name = 'report.optipack.vgm_template'
#
#     def get_data(self, data=None):
#         query = """
#                         select pc."name",sum(pol.price_subtotal) as subtotal,ppm.name from pos_order po inner join pos_order_line pol ON pol.order_id =po.id
#                         inner join product_product pp on pp.id=pol.product_id
#                         left join product_template pt on pt.id=pp.product_tmpl_id
#                         left join product_category pc on pc.id=pt.categ_id
#                         left join (select distinct session_id,payment_method_id  from pos_payment) pp2 on pp2.session_id =po.session_id
#                         left join pos_payment_method ppm on pp2.payment_method_id =pp.id
#                         where po.session_id =
#                     """
#         query += " " + str(data['id'])
#         query += " group by pc.name,ppm.name"
#
#         self.env.cr.execute(query)
#         res = self.env.cr.fetchall()
#
#         docs = []
#
#         for line in res:
#             docs.append({
#                 'famille': line[0],
#                 'total': line[1],
#                 'methode': line[2],
#                 })
#
#         print(docs)
#         return {
#         'docs': docs,
#             }
#
#     @api.model
#     def get_report_values(self, docids, data=None):
#         return data