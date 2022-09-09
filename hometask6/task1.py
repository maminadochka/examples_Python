bytes = b'r\xc3\xa9sum\xc3\xa9'
print("Bytes = ", bytes)

str_decoded = bytes.decode()
print('\nDecoded String =', str_decoded)

bytes_latin = str_decoded.encode("Latin1")
print('\nEncoded String Latin1 =', bytes_latin)

string_decode = bytes_latin.decode("Latin1")
print('\nDecoded String =', string_decode)
