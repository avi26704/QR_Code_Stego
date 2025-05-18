import qrcode # type: ignore
from PIL import Image # type: ignore
import numpy as np # type: ignore

def generate_qr(data, filename='qr.png'):
    qr = qrcode.QRCode(
        version=1,
        box_size=10,
        border=4
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white')
    img.save(filename)
    return filename

def encode_lsb(image_path, secret_message, output_path='stego_qr.png'):
    img = Image.open(image_path).convert('RGB')
    data = np.array(img)
    flat_data = data.flatten()

    binary_message = ''.join(format(ord(i), '08b') for i in secret_message)
    binary_message += '1111111111111110' 

    if len(binary_message) > len(flat_data):
        raise ValueError("Message too large to encode in image.")

    for i in range(len(binary_message)):
        flat_data[i] = (flat_data[i] & 0b11111110) | int(binary_message[i])

    new_data = flat_data.reshape(data.shape)
    new_img = Image.fromarray(new_data.astype(np.uint8))
    new_img.save(output_path)
    print(f"Message embedded in {output_path}")

def decode_lsb(stego_image_path):
    img = Image.open(stego_image_path)
    data = np.array(img).flatten()

    binary_data = ''
    for i in range(len(data)):
        binary_data += str(data[i] & 1)

        if binary_data.endswith('1111111111111110'): 
            break

    binary_data = binary_data[:-16] 
    decoded_chars = [chr(int(binary_data[i:i+8], 2)) for i in range(0, len(binary_data), 8)]
    return ''.join(decoded_chars)
