# QR Code Steganography using LSB (Least Significant Bit)

This project demonstrates how to embed a secret message into a QR code image using Least Significant Bit (LSB) steganography. It now also supports AES-128 encryption for enhanced security of the hidden message. Users can securely hide and retrieve encrypted messages inside QR images.

## Website Link -- [https://qr-code-stego.vercel.app/](https://qr-code-stego.vercel.app/)

<br />

![UI Image](static/images/UI.png)

## Features

- Generate QR codes from text input.
- Hide a secret message inside the QR image using LSB.
- Encrypt the secret message using AES-128 encryption before embedding.
- Decode and retrieve the hidden message from the modified image.
- Decrypt the extracted message using the correct AES key.

### Prerequisites

Install the required Python libraries:

- `qrcode[pil]`
- `pillow`
- `numpy`
- `pycryptodome`

## How It Works

This project combines QR code generation, AES-128 encryption, and Least Significant Bit (LSB) steganography to hide secret messages securely inside QR images.

1. **QR Code Generation**
   A QR code is created from user-provided text or a URL using the `qrcode` library. This image (`qr.png`) serves as the carrier.

2. **AES Encryption**
   The secret message is first encrypted using AES-128 in ECB mode with a user-provided key. The ciphertext is base64 encoded before embedding. This adds a layer of security, ensuring that the hidden message cannot be read without the correct decryption key.

3. **Message Encoding with LSB**
   The encrypted (or plain) message is converted to binary and embedded into the pixel data of the QR image by modifying the least significant bit of each pixel value. A special delimiter (`1111111111111110`) is added to indicate the end of the message.

4. **Saving the Stego Image**
   The modified image, which visually looks the same as the original QR code, is saved as `stego_qr.png`.

5. **Message Decoding**
   To retrieve the hidden message, the stego image is read and the least significant bits of the pixel data are extracted. The binary stream is then converted back to base64-encoded ciphertext (if encrypted), stopping at the delimiter.

6. **AES Decryption**
   If the message was encrypted, it is decrypted using the same AES key that was used during embedding. If the key is incorrect or the ciphertext is corrupted, decryption will fail with an error message.

This process ensures the QR code remains scannable while secretly carrying an additional encrypted message.

## Advantages

- Combines overt QR data with covert hidden messages using steganography.
- Adds a layer of encryption using AES for stronger confidentiality.
- Error correction in QR codes allows minor modifications without breaking scanability.
- Stego QR codes appear visually unchanged, enhancing secrecy and stealth.
- Easily implemented using common Python libraries with minimal overhead.
