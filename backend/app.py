from flask import Flask, request, jsonify
import sqlite3
from flask_cors import CORS
app = Flask(__name__)
CORS(app)
DATABASE = 'database.db'

def init_db():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS messages (
        id INTEGER PRIMARY KEY,
        name TEXT,
        email TEXT,
        message TEXT
    )''')
    conn.commit()
    conn.close()

@app.route('/messages', methods=['GET'])
def get_messages():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('SELECT name, email, message FROM messages')
    messages = cursor.fetchall()
    conn.close()
    return jsonify([{'name': msg[0], 'email': msg[1], 'message': msg[2]} for msg in messages])

@app.route('/messages', methods=['POST'])
def add_message():
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    message = data.get('message')
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('INSERT INTO messages (name, email, message) VALUES (?, ?, ?)', (name, email, message))
    conn.commit()
    conn.close()
    return jsonify({'message': 'Information added successfully!'})

if __name__ == '__main__':
    init_db()  # Initialize the database
    app.run(host='0.0.0.0', port=5000, debug=True)
