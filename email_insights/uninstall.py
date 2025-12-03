import frappe
from email_insights.app_config import APP_TITLE

def after_uninstall():
    try:
        remove_custom_fields_from_communication()
        remove_custom_fields_from_email_campaign()
    except Exception as e:
        frappe.log_error(f"Error occured after uninstalling {APP_TITLE} app:", e)


def remove_custom_fields_from_communication():
    custom_field_names = [
        "Communication-email_insights_tab",
        "Communication-all_emails",
    ]

    for field_name in custom_field_names:
        if frappe.db.exists("Custom Field", field_name):
            frappe.delete_doc("Custom Field", field_name)
    
    frappe.db.commit()

def remove_custom_fields_from_email_campaign():
    custom_field_names = [
        "Email Campaign-email_insights_tab",
        "Email Campaign-all_emails",
    ]

    for field_name in custom_field_names:
        if frappe.db.exists("Custom Field", field_name):
            frappe.delete_doc("Custom Field", field_name)
    
    frappe.db.commit() 