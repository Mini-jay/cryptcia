from main import *

def run_script():
    msg = "SECRETATTACKATDAWN"
    key = "TOMATO"
    
    # Encrypt
    encrypted = myszowski_encrypt(msg, key)
    print(f"Ciphertext: {encrypted}")
    
    # Decrypt
    decrypted = myszowski_decrypt(encrypted, key)
    print(f"Decrypted:  {decrypted}")

if __name__ == "__main__":
    run_script()
