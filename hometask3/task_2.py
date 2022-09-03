text = input("Enter text: ")

while "(" in text or ")" in text:
    open_bkt = text.rfind("(")
    close_bkt = text.find(")", open_bkt)
    text = text.replace(text[open_bkt:close_bkt+1], "")
print(text)
