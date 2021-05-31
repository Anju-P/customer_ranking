# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "customer_ranking"
app_title = "Customer Ranking by Sales_Collection"
app_publisher = "Anju Prasannan"
app_description = "Customer Ranking by Sales_Collection"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "anjuprasannan321@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/customer_ranking/css/customer_ranking.css"
# app_include_js = "/assets/customer_ranking/js/customer_ranking.js"

# include js, css files in header of web template
# web_include_css = "/assets/customer_ranking/css/customer_ranking.css"
# web_include_js = "/assets/customer_ranking/js/customer_ranking.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "customer_ranking.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "customer_ranking.install.before_install"
# after_install = "customer_ranking.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "customer_ranking.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"customer_ranking.tasks.all"
# 	],
# 	"daily": [
# 		"customer_ranking.tasks.daily"
# 	],
# 	"hourly": [
# 		"customer_ranking.tasks.hourly"
# 	],
# 	"weekly": [
# 		"customer_ranking.tasks.weekly"
# 	]
# 	"monthly": [
# 		"customer_ranking.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "customer_ranking.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "customer_ranking.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "customer_ranking.task.get_dashboard_data"
# }

