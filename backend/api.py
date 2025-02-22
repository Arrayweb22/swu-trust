from backend import database as db

def process_transaction(sender, receiver, amount):
    if db.get_balance(sender) < amount:
        return "Insufficient funds"
    db.create_transaction(sender, receiver, amount)
    return "Transaction Sent"

def fetch_notifications(swu_id):
    return db.get_notifications(swu_id)

# Report System
def submit_report(swu_id, text):
    db.add_report(swu_id, text)

def get_reports():
    return db.fetch_reports()

def delete_report(report_id):
    db.remove_report(report_id)
