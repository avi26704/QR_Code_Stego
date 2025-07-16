from flask import Flask, render_template, request, send_file # type: ignore
import os
from stego import generate_qr, encode_lsb, decode_lsb

app = Flask(__name__)
UPLOAD_FOLDER = '/tmp/uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        action = request.form.get('action')

        if action == 'encode':
            data = request.form['data']
            secret = request.form['secret']
            key=request.form['key']
            qr_path = os.path.join(UPLOAD_FOLDER, 'qr.png')
            generate_qr(data, qr_path)
            stego_path = os.path.join(UPLOAD_FOLDER, 'stego_qr.png')
            encode_lsb(qr_path, secret, key, stego_path)
            result = 'Encoded successfully. Download below.'
            return render_template('index.html', result=result, image='stego_qr.png')

        elif action == 'decode':
            key = request.form['key']
            file = request.files['file']
            path = os.path.join(UPLOAD_FOLDER, 'uploaded.png')
            file.save(path)
            message = decode_lsb(path,key)
            if(message=="Wrong decryption key or ciphertext corrupted"):
                result = f'Error: {message}'
            else:
                result = f'Decoded Message: {message}'

    return render_template('index.html', result=result)

@app.route('/download/<filename>')
def download_file(filename):
    return send_file(os.path.join(UPLOAD_FOLDER, filename), as_attachment=True)

