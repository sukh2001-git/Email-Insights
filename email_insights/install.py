import frappe
from email_insights.app_config import APP_TITLE


def after_install():
    try:
        add_custom_fields_to_communication()
        add_custom_fields_to_email_campaign()
        print("Custom fields added successfully after installation.")
    except Exception as e:
        frappe.log_error(f"Error occured after installing {APP_TITLE} app:", e)


def add_custom_fields_to_communication():
    custom_fields = [
        {
            "dt": "Communication",
            "fieldname": "email_insights_tab",
            "fieldtype": "Tab Break",
            "label": "Email Insights",
            "module": "Email Insights",
            "name": "Communication-email_insights_tab",
            "insert_after": "feedback_request",
        },
        {
            "dt": "Communication",
            "fieldname": "all_emails",
            "fieldtype": "Table",
            "label": "All Emails",
            "module": "Email Insights",
            "name": "Communication-all_emails",
            "options": "Email Insights",
            "insert_after": "email_insights_tab",
        },
    ]

    for field in custom_fields:
        if not frappe.db.exists("Custom Field", field["name"]):
            new_field = frappe.get_doc({"doctype": "Custom Field", **field})
            new_field.insert()
    frappe.db.commit()


def add_custom_fields_to_email_campaign():
    custom_fields = [
        {
            "dt": "Email Campaign",
            "fieldname": "email_insights_tab",
            "fieldtype": "Tab Break",
            "label": "Email Insights",
            "module": "Email Insights",
            "name": "Email Campaign-email_insights_tab",
            "insert_after": "status",
        },
        {
            "dt": "Email Campaign",
            "fieldname": "all_emails",
            "fieldtype": "Table",
            "label": "All Emails",
            "module": "Email Insights",
            "name": "Email Campaign-all_emails",
            "options": "Email Insights",
            "insert_after": "email_insights_tab",
        },
    ]

    for field in custom_fields:
        if not frappe.db.exists("Custom Field", field["name"]):
            new_field = frappe.get_doc({"doctype": "Custom Field", **field})
            new_field.insert()
    frappe.db.commit()