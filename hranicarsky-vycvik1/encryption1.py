cipher_text_hex = "0000000000000000003009071714260b1b08325400041e22060c012f04"
key = "KyberChod"

# Převedeme zašifrovaný text a klíč na bajty
cipher_text_bytes = bytes.fromhex(cipher_text_hex)
key_bytes = bytes(key, 'utf-8')

# XOR operace mezi zašifrovanou zprávou a opakovaným klíčem
decrypted_bytes = bytes(a ^ b for a, b in zip(cipher_text_bytes, key_bytes * len(cipher_text_bytes)))

# Převedeme výsledek zpět na string
decrypted_text = decrypted_bytes.decode('utf-8', errors='replace')

print(decrypted_text)