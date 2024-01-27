from pyweb import pydom
from string import ascii_lowercase, ascii_uppercase


def displace(text, displacement):
    result = ""
    for character in text:
        if character in ascii_lowercase:
            result += chr((ord(character) - ord('a') + displacement) % 26 + ord('a'))
        elif character in ascii_uppercase:
            result += chr((ord(character) - ord('A') + displacement) % 26 + ord('A'))
        else:
            result += character
    return result


def encrypt(event):
    textarea_element = pydom["textarea#text-to-encrypt"][0]
    text = textarea_element.value

    key_element = pydom["input#encrypt-key-input"][0]
    key = int(key_element.value)

    decrypted_text_element = pydom["textarea#encrypted-text"][0]
    decrypted_text_element.value = displace(text, key)


def decrypt(event):
    textarea_element = pydom["textarea#text-to-decrypt"][0]
    text = textarea_element.value

    key_element = pydom["input#decrypt-key-input"][0]
    key = int(key_element.value)

    decrypted_text_element = pydom["textarea#decrypted-text"][0]
    decrypted_text = displace(text, -key)
    decrypted_text_element.value = decrypted_text


def sync_range_to_input(event):
    prefix = event.target.id.split("-")[0]
    key_range_element = pydom["input#{}-key-range".format(prefix)][0]
    key = key_range_element.value

    key_element = pydom["input#{}-key-input".format(prefix)][0]
    key_element.value = key


def sync_input_to_range(event):
    prefix = event.target.id.split("-")[0]
    key_element = pydom["input#{}-key-input".format(prefix)][0]
    key = key_element.value

    key_range_element = pydom["input#{}-key-range".format(prefix)][0]
    key_range_element.value = int(key) % 26
