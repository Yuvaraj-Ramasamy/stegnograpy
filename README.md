# stegnograpy
Steganography Tool – Encrypt &amp; Decrypt Data in Images

🔐 CryptoSteganography Web Tool
This is a simple Flask web application that allows users to hide and reveal secret messages inside PNG images using CryptoSteganography. It combines encryption and steganography to securely embed messages within images and retrieve them using a secret key.

🚀 Features
Hide a Secret Message:
Upload a PNG image and enter a secret message. The app encrypts the message and hides it inside the image using a predefined key.

Reveal a Hidden Message:
Upload an encoded PNG image and provide the decryption key to extract the hidden message.

Download Options:

Download the encrypted image after hiding the message.
Download the revealed message as a .txt file.


🛠️ Technologies Used
Flask – Web framework for Python
CryptoSteganography – Python library for hiding encrypted messages in images
Pillow (PIL) – Image processing
HTML/CSS – Frontend styling with embedded templates

📁 Folder Structure
uploads/ – Stores uploaded and processed images
app.py – Main Flask application


🔧 How to Run
Install dependencies:

Shell
pip install flask cryptosteganography pillow

Run the app:

Shell
python app.py

Open your browser and go to http://127.0.0.1:5000

📸 Screenshots
(Optional: Add screenshots of the UI here)

🔐 Default Encryption Key
The default encryption key used in the app is:

You can replace the Yuvi#430861 key to your specifc key
