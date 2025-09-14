# from cryptosteganography import CryptoSteganography

# crypto_steg = CryptoSteganography('Yuvi#430861')

# # Encrypt + hide
# crypto_steg.hide('input.png','output.png', 'My bank password is 430430430')

# # Decrypt + Reveal
# secrect = crypto_steg.retrieve('output.png')
# print("Decoded:",secrect)





# from cryptosteganography import CryptoSteganography
# from PIL import Image

# # Step 1: Create a blank white image
# width, height = 300, 300
# blank_image_path = 'blank_input.png'
# blank_image = Image.new('RGB', (width, height), color='white')
# blank_image.save(blank_image_path)

# # Step 2: Initialize CryptoSteganography with a password
# crypto_steg = CryptoSteganography('Yuvi#430861')

# # Step 3: Encrypt and hide the message
# secret_message = 'My bank password is 430430430'
# output_image_path = 'output.png'
# crypto_steg.hide(blank_image_path, output_image_path, secret_message)

# # Step 4: Retrieve and print the hidden message
# retrieved_secret = crypto_steg.retrieve(output_image_path)
# print("Decoded:", retrieved_secret)

from flask import Flask, render_template_string, request, send_file
from cryptosteganography import CryptoSteganography
from PIL import Image
import os

app = Flask(__name__)

# HTML template
HTML_TEMPLATE = '''
<!DOCTYPE html>
<html>
<head>
    <title>CryptoSteganography Web Tool</title>
    <style>
        body { font-family: Arial; margin: 40px; background-color: #f4f4f4; }
        h1 { color: #333; }
        form { background: white; padding: 20px; margin-bottom: 30px; border-radius: 8px; box-shadow: 0 0 10px rgba(0,0,0,0.1); }
        input[type="file"], input[type="text"] { width: 100%; margin: 10px 0; padding: 10px; }
        button { padding: 10px 20px; background-color: #0078D7; color: white; border: none; border-radius: 5px; cursor: pointer; }
        button:hover { background-color: #005fa3; }
        .result { background: #fff; padding: 20px; border-radius: 8px; box-shadow: 0 0 5px rgba(0,0,0,0.1); }
    </style>
</head>
<body>

    <h1>🔐 Hide a Secret Message</h1>
    <form action="/hide" method="post">
        <label>Enter your secret message:</label>
        <input type="text" name="message" placeholder="Type your secret message here..." required>
        <button type="submit">Encrypt & Download Image</button>
    </form>

    <h1>🕵️ Reveal a Hidden Message</h1>
    <form action="/reveal" method="post" enctype="multipart/form-data">
        <label>Select an encoded image (PNG):</label>
        <input type="file" name="encoded_image" accept="image/png" required>

        <label>Enter the decryption key:</label>
        <input type="text" name="key" placeholder="Enter the key used for encryption" required>

        <button type="submit">Reveal Message</button>
    </form>

    {% if secret_message %}
    <div class="result">
        <h2>🔓 Decoded Message:</h2>
        <p>{{ secret_message }}</p>
        <form action="/download" method="post">
            <input type="hidden" name="message" value="{{ secret_message }}">
            <button type="submit">Download Message</button>
        </form>
    </div>
    {% endif %}
</body>
</html>
'''

from flask import Flask, render_template_string, request, send_file
from cryptosteganography import CryptoSteganography
from PIL import Image
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

HTML_TEMPLATE = '''
<!DOCTYPE html>
<html>
<head>
    <title>CryptoSteganography Web Tool</title>
    <style>
        body { font-family: Arial; margin: 40px; background-color: #f4f4f4; }
        h1 { color: #333; }
        form { background: white; padding: 20px; margin-bottom: 30px; border-radius: 8px; box-shadow: 0 0 10px rgba(0,0,0,0.1); }
        input[type="file"], input[type="text"] { width: 100%; margin: 10px 0; padding: 10px; }
        button { padding: 10px 20px; background-color: #0078D7; color: white; border: none; border-radius: 5px; cursor: pointer; }
        button:hover { background-color: #005fa3; }
        .result { background: #fff; padding: 20px; border-radius: 8px; box-shadow: 0 0 5px rgba(0,0,0,0.1); }
    </style>
</head>
<body>

    <h1>🔐 Hide a Secret Message</h1>
    <form action="/hide" method="post" enctype="multipart/form-data">
        <label>Select an image (PNG):</label>
        <input type="file" name="input_image" accept="image/png" required>

        <label>Enter your secret message:</label>
        <input type="text" name="message" placeholder="Type your secret message here..." required>

        <button type="submit">Submit</button>
    </form>

    {% if encrypted_ready %}
    <div class="result">
        <h2>✅ Data Encrypted successfully!</h2>
        <form action="/download_encrypted" method="get">
            <button type="submit">Download Encrypted Image</button>
        </form>
    </div>
    {% endif %}

    <h1>🕵️ Reveal a Hidden Message</h1>
    <form action="/reveal" method="post" enctype="multipart/form-data">
        <label>Select an encoded image (PNG):</label>
        <input type="file" name="encoded_image" accept="image/png" required>

        <label>Enter the decryption key:</label>
        <input type="text" name="key" placeholder="Enter the key used for encryption" required>

        <button type="submit">Reveal Message</button>
    </form>

    {% if secret_message %}
    <div class="result">
        <h2>🔓 Decrypted Data:</h2>
        <p>{{ secret_message }}</p>
        <form action="/download" method="post">
            <input type="hidden" name="message" value="{{ secret_message }}">
            <button type="submit">Download Message</button>
        </form>
    </div>
    {% endif %}
</body>
</html>
'''

@app.route('/', methods=['GET'])
def index():
    return render_template_string(HTML_TEMPLATE)

@app.route('/hide', methods=['POST'])
def hide():
    image = request.files['input_image']
    message = request.form['message']
    input_path = os.path.join(UPLOAD_FOLDER, 'user_input.png')
    output_path = os.path.join(UPLOAD_FOLDER, 'output.png')
    image.save(input_path)

    crypto_steg = CryptoSteganography('Yuvi#430861')
    crypto_steg.hide(input_path, output_path, message)

    return render_template_string(HTML_TEMPLATE, encrypted_ready=True)

@app.route('/download_encrypted', methods=['GET'])
def download_encrypted():
    return send_file(os.path.join(UPLOAD_FOLDER, 'output.png'), as_attachment=True)

@app.route('/reveal', methods=['POST'])
def reveal():
    encoded_image = request.files['encoded_image']
    key = request.form['key']
    encoded_path = os.path.join(UPLOAD_FOLDER, 'uploaded_encoded.png')
    encoded_image.save(encoded_path)

    crypto_steg = CryptoSteganography(key)
    secret = crypto_steg.retrieve(encoded_path)
    return render_template_string(HTML_TEMPLATE, secret_message=secret)

@app.route('/download', methods=['POST'])
def download():
    message = request.form['message']
    file_path = os.path.join(UPLOAD_FOLDER, 'decrypted_message.txt')
    with open(file_path, 'w') as f:
        f.write(message)
    return send_file(file_path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
