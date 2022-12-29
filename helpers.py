import pgpy
import requests


def call(query):
    # Contact OpenPGP Key Server
    try:
        url = f"https://keys.openpgp.org/pks/lookup?op=get&options=mr&search={query}"
        response = requests.get(url)
        response.raise_for_status()
    except requests.RequestException:
        return None

    # Parse response
    try:
        key = response.content
        return key
    except (KeyError, TypeError, ValueError):
        return None


def load_key(text):

    # Creates a PGP public key from user input.
    key, _ = pgpy.PGPKey.from_blob(text)
    return key


def pgpy_encrypt(key, data):

    # Encrypts data using key.
    message = pgpy.PGPMessage.new(data)
    encrypted_message = key.encrypt(message)
    return encrypted_message