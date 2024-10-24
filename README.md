# PGPy GUI

<div align=center>
<img width=90% alt="PGPy GUI" src="https://github.com/libremomo/pgpy-gui/blob/master/docs/images/frontend.png">
</div>

A graphical user interface for PGP message encryption built with Flask and the PGPy library. I submitted this as the final project in my [Harvard CS50x (2022) course](https://certificates.cs50.io/2f767ba2-8d03-4a9c-be59-295309af62a3.pdf?size=letter).

[![Video Demo](https://img.shields.io/badge/Video-Demo-blue)](https://odysee.com/@libremomo:7/PGPy-GUI:0)

## Overview

PGPy GUI simplifies the process of encrypting messages using PGP (Pretty Good Privacy) encryption without requiring an email client. It leverages the PGPy library, which is a Python implementation of the OpenPGP specification (RFC 4880).

## Features

- Fetch public keys from the OpenPGP key server
- Encrypt messages using recipient's public key
- Simple web-based interface
- No email client required

## Installation

PGPy GUI requires Python 3.6 or higher. Install the required dependency using pip:

```bash
pip install PGPy
```

## Running the Application

Start the web application using Flask:

```bash
flask run
```

## How to Use

1. Enter the recipient's email address or HKP fingerprint
2. Type your message in the text area
3. Click "Encrypt"
4. Copy your encrypted message

The application will automatically fetch the recipient's public key from the OpenPGP key server. If no public key is found for the provided email or fingerprint, an error message will be displayed.

## Project Structure

- `app.py` - Flask routes and request handling
- `helpers.py` - Core functionality including API calls and encryption
- `layout.html` - Base template for the web interface

## Technical Details

### PGPy Library
PGPy is a Python implementation of the OpenPGP specification that prioritizes ease of use while maintaining full compliance with the standard. This project uses PGPy for all cryptographic operations.

### Implementation Notes
The application uses JavaScript's `fetch()` API for handling form submissions asynchronously, preventing page reloads during encryption operations.

## Future Enhancements

- [ ] File encryption/decryption support
- [ ] Manual PGP key import functionality
- [ ] Enhanced exception handling
- [ ] Support for multiple key servers
- [ ] Input validation and user alerts
- [ ] Responsive design implementation

## API Documentation

- [OpenPGP Key Server API](https://keys.openpgp.org/about/api)
- [PGPy Documentation](https://pgpy.readthedocs.io/en/latest/index.html)

## Acknowledgments

- [Alireza Shajari](https://github.com/mahooresorkh) - Assistance with AJAX implementation
- Aleksa Zatezalo - Article: ["Creating a PGP Encryption Tool With Python"](https://betterprogramming.pub/creating-a-pgp-encryption-tool-with-python-19bae51b7fd)
- [Keyoxide](https://keyoxide.org/) by Yarmo Mackenbach - Project inspiration

## Security Notice

This is experimental software intended for educational purposes. Use in production environments is not recommended.

## License

- PGPy is licensed under the BSD 3-Clause License
- This web application and its contents are licensed under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)
