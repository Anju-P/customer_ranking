from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		
		{
			"label": _("Key Reports"),
			"icon": "fa fa-table",
			"items": [
				{
					"type": "report",
					"is_query_report": True,
					"name": "Customer Ranking by Sales Collection",
					"doctype": "Sales Invoice",
					"onboard": 1,
				},
				
			]
		},
		
		
	]
