from flask import Flask, request, jsonify, send_from_directory
from cryptography.fernet import Fernet

app = Flask(__name__, static_url_path='', static_folder='.')

# Generate a key for encryption/decryption
# In a real application, you should save this key securely and not regenerate it each time the server starts
key = Fernet.generate_key()
cipher_suite = Fernet(key)

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/encrypt', methods=['POST'])
def encrypt():
    data = request.json
    text = data['text']
    encrypted_text = cipher_suite.encrypt(text.encode())
    return jsonify({'encrypted_text': encrypted_text.decode()})

@app.route('/decrypt', methods=['POST'])
def decrypt():
    data = request.json
    encrypted_text = data['encrypted_text']
    decrypted_text = cipher_suite.decrypt(encrypted_text.encode())
    return jsonify({'decrypted_text': decrypted_text.decode()})

if __name__ == '__main__':
    app.run(debug=True)
