from pyweb import pydom
from random import randint


def decrypt(event):
    textarea_element = pydom["textarea#text-to-decrypt"][0]
    print(textarea_element.value)

    decrypted_text_element = pydom["textarea#decrypted-text"][0]
    decrypted_text_element.value = "{}-{}".format(textarea_element.value, randint(1, 100))

    decrypted_text_container_element = pydom["div#decrypted-text-container"][0]
    decrypted_text_container_element.visible = True


def sync_range_to_input(event):
    key_range_element = pydom["input#key-range"][0]
    key = key_range_element.value

    print(key)

    key_element = pydom["input#key"][0]
    key_element.value = key


def sync_input_to_range(event):
    key_element = pydom["input#key"][0]
    key = key_element.value

    print(key)

    key_range_element = pydom["input#key-range"][0]
    key_range_element.value = int(key) % 26
