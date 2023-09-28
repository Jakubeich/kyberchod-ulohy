from urllib.parse import unquote

def decode_percent_encoding(encoded_str):
  return unquote(encoded_str)

encoded_str = input("Vlož zakódovaný řetězec: ")
decoded_str = decode_percent_encoding(encoded_str)
print("Dekódovaný řetězec: " + decoded_str)