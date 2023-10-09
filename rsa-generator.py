import argparse
import binascii
import json

from cryptography.exceptions import InvalidSignature
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding, rsa


def pad_hex_string(hex_str):
    """
    Pad the hexadecimal string with leading zeros.
    This is often required for cryptographic operations.
    """
    return "0" * (512 - len(hex_str)) + hex_str


def decipher_data(public_key, signature, data):
    """
    Decipher the signature using the public key.
    This provides a way to verify that the signature was created
    using the corresponding private key.
    """
    try:
        public_key.verify(signature, data, padding.PKCS1v15(), hashes.SHA256())
        deciphered_hex = (
            "0x0001"
            + "f" * 478
            + "003031300d060960864801650304020105000420"
            + binascii.hexlify(data).decode()
        )
        return deciphered_hex
    except InvalidSignature:
        return "Signature verification failed"


def generate_rsa_key_pair():
    """
    Generate RSA Key Pair.
    RSA involves a public key and a private key.
    The public key is used for encryption,
    and the private key is used for decryption.
    """
    return rsa.generate_private_key(
        public_exponent=65537, key_size=2048, backend=default_backend()
    )


def get_public_key(private_key):
    """
    Get the public key from a private key.
    In RSA, the public key consists of a modulus and an exponent.
    """
    return private_key.public_key()


def sign_data(private_key, data):
    """
    Sign the given data using RSA digital signature.
    Digital Signature provides a way to verify the origin of messages.
    """
    return private_key.sign(data, padding.PKCS1v15(), hashes.SHA256())


def get_modulus_and_exponent(public_key):
    """
    Get the modulus and exponent from a public key.
    In RSA, the public key is represented as (n, e) where n is the modulus and e is the exponent.
    """
    public_numbers = public_key.public_numbers()
    return public_numbers.n, public_numbers.e


def compute_sha256_hash(data):
    """
    Compute the SHA-256 hash of the given data.
    Hash functions take an input and produce a fixed size string of characters.
    """
    digest = hashes.Hash(hashes.SHA256(), backend=default_backend())
    digest.update(data)
    return digest.finalize()


def main(data_to_sign):
    """
    Main function to demonstrate RSA key generation, signing and relevant value extraction.
    """
    # Generate RSA key pair
    private_key = generate_rsa_key_pair()

    # Get the public key
    public_key = get_public_key(private_key)

    # Convert the data to bytes and sign it
    data = data_to_sign.encode()
    signature = sign_data(private_key, data)

    # Extract modulus and exponent
    modulus, exponent = get_modulus_and_exponent(public_key)

    # Compute the SHA-256 hash of the data
    sha256_hashed = compute_sha256_hash(data)

    # Pad the exponent with leading zeros
    padded_exponent = pad_hex_string(hex(exponent).replace("0x", ""))

    result = {
        "DIGEST": 'hex"' + binascii.hexlify(sha256_hashed).decode() + '"',
        "SHA256_HASHED": 'hex"' + binascii.hexlify(sha256_hashed).decode() + '"',
        "EXPONENT": 'hex"' + padded_exponent + '"',
        "SIGNATURE": 'hex"' + binascii.hexlify(signature).decode() + '"',
        "MODULUS": 'hex"' + hex(modulus).replace("0x", "") + '"',
    }

    # Decipher the data
    decipher_result = decipher_data(public_key, signature, data)
    result["DECIPHER_RESULT"] = decipher_result
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Generate RSA key pair, sign data, and output relevant values."
    )
    parser.add_argument("data_to_sign", help="The data to sign.")
    args = parser.parse_args()

    main(args.data_to_sign)
