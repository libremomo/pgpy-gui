# PGPy GUI
#### Video Demo: <https://odysee.com/@libremomo:7/PGPy-GUI:0>

A graphic user interface for message encryption with PGPy Python library, written in Flask.

## What is PGPy
PGPy is a Python implementation of the OpenPGP specification, as described in RFC 4880.

It aims to be easy to use above all else, but also to eventually embody a complete, compliant implementation of the specification.

## Description
Suppose that you want to send a PGP encrypted message to a friend. We usually leave the task of working with keys and encrypt/decrypt operations to our email clients such as Mozilla Thunderbird. But what if you don't have access to your email client and all of the keys that you have previously imported?

Here comes the power of our tool. If your recipient has already published his/her public key on the [OpenPGP key server](https://keys.openpgp.org/), you can just sit back and ask the key server to provide it for you. The rest is quite simple. We handle both of the recipient's key and your message to our tiny app and here is your encrypted message! The one that can only be decrypted via the recipient's private key.
## How to Run

The app depends on PGPy package to work. You can install it from pip. Notice that PGPy requires Python >= 3.6.

```bash
pip install PGPy
```
You can run the web app simply by entering the following command:
```bash
flask run
```

## Usage
1. Enter recipient's email address or HKP fingerprint
2. Enter your message and press "Encrypt"
3. Receive your encrypted message. If the mentioned email or fingerprint is not associated with any public key on the server, an Error will be thrown.

## What's inside
#### app.py
Contains the routes of the web application and handles the GET and POST requests coming from client side.
#### helpers.py
Contains the definition of the functions. One for calling the OpenPGP server API and two other for loading key and encryption.
#### layout.html
Base template for other pages, extended by jinja placeholders.

## Challenges
Using request.get.form with POST method to obtain the user input caused the entire page to reload. I had to use either AJAX or pure JS fetch() method to prevent that. I chose the second way.

## Documentation
- [OpenPGP API docs](https://keys.openpgp.org/about/api)
- [PGPy docs](https://pgpy.readthedocs.io/en/latest/index.html)

## Roadmap
- [ ] file encryption/decryption
- [ ] adding the ability to load PGP manually
- [ ] better exception handling
- [ ] add the ability to call other key servers
- [ ] adding alerts and validations
- [ ] responsive design

## Acknowledgements
Many thanks to my friend Alireza Shajari who helped me fix the page reloading issue.
Special thanks to Aleksa Zatezalo for his informative article "[Creating a PGP Encryption Tool With Python](https://betterprogramming.pub/creating-a-pgp-encryption-tool-with-python-19bae51b7fd)".
Last but not least [keyoxide](https://keyoxide.org/) was a true inspiration. I thank Yarmo Mackenbach for that.


## Disclaimer
This is an experimental software. Use at your own risk.

## License
PGPy is distributed under a BSD 3-Clause licensed.
The web app and its contents are licensed under CC BY-SA 4.0.