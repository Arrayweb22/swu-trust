import sqlite3

DB_FILE = "data/swu_trust.db"

def get_db():
    return sqlite3.connect(DB_FILE, check_same_thread=False)

def get_users():
    conn = get_db()
    cur = conn.cursor()
    cur.execute("SELECT swu_id, password_hash, is_admin FROM SWUusers")
    users = {row[0]: {"password": row[1], "is_admin": row[2]} for row in cur.fetchall()}
    conn.close()
    return users

def is_admin(swu_id):
    conn = get_db()
    cur = conn.cursor()
    cur.execute("SELECT is_admin FROM SWUusers WHERE swu_id = ?", (swu_id,))
    result = cur.fetchone()
    conn.close()
    return result[0] if result else False

def get_balance(swu_id):
    conn = get_db()
    cur = conn.cursor()
    cur.execute("SELECT balance FROM SWUusers WHERE swu_id = ?", (swu_id,))
    result = cur.fetchone()
    conn.close()
    return result[0] if result else 0.0

def create_transaction(sender, receiver, amount):
    conn = get_db()
    cur = conn.cursor()
    cur.execute("INSERT INTO transactions (sender, receiver, amount, status) VALUES (?, ?, ?, 'pending')",
                (sender, receiver, amount))
    conn.commit()
    conn.close()

def get_pending_transactions():
    conn = get_db()
    cur = conn.cursor()
    cur.execute("SELECT id, sender, receiver, amount FROM transactions WHERE status = 'pending'")
    transactions = [{"id": row[0], "sender": row[1], "receiver": row[2], "amount": row[3]} for row in cur.fetchall()]
    conn.close()
    return transactions

def approve_transaction(transaction_id):
    conn = get_db()
    cur = conn.cursor()
    cur.execute("UPDATE transactions SET status = 'approved' WHERE id = ?", (transaction_id,))
    conn.commit()
    conn.close()

def reject_transaction(transaction_id):
    conn = get_db()
    cur = conn.cursor()
    cur.execute("UPDATE transactions SET status = 'rejected' WHERE id = ?", (transaction_id,))
    conn.commit()
    conn.close()

def send_notification(swu_id, message):
    conn = get_db()
    cur = conn.cursor()
    cur.execute("INSERT INTO notifications (swu_id, message) VALUES (?, ?)", (swu_id, message))
    conn.commit()
    conn.close()

def get_notifications(swu_id):
    conn = get_db()
    cur = conn.cursor()
    cur.execute("SELECT message FROM notifications WHERE swu_id = ? OR swu_id = 'all'", (swu_id,))
    notifications = [row[0] for row in cur.fetchall()]
    conn.close()
    return notifications

# Report System
def add_report(swu_id, text):
    conn = get_db()
    cur = conn.cursor()
    cur.execute("INSERT INTO reports (swu_id, text) VALUES (?, ?)", (swu_id, text))
    conn.commit()
    conn.close()

def fetch_reports():
    conn = get_db()
    cur = conn.cursor()
    cur.execute("SELECT id, swu_id, text FROM reports")
    reports = [{"id": row[0], "swu_id": row[1], "text": row[2]} for row in cur.fetchall()]
    conn.close()
    return reports

def remove_report(report_id):
    conn = get_db()
    cur = conn.cursor()
    cur.execute("DELETE FROM reports WHERE id = ?", (report_id,))
    conn.commit()
    conn.close()
