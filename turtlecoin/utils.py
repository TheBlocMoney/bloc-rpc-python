import random
import string
import binascii


def generate_payment_id():
    """
    Generate a random payment_id for transactions
    """
    return ''.join(random.choices(string.hexdigits, k=64)).lower()


def format_amount(amount):
    """
    Format amount into user-friendly format
    """
    return float(amount/100)


def parse_amount(amount):
    """
    Format amount from user-friendly format to internal representation
    """
    return int(amount*100)


def convert_bytes_to_hex_str(data):
    """
    Converts binary data into its hexadecimal representation and return
    it's decoded string. This can be used in the `extra` field when
    sending a transaction
    """
    return binascii.hexlify(data).decode()
