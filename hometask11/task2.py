import re
str = "pp@fv--fv.com"
a = re.findall(r"\w[\w.!#%&\'*+\-/=?^_{|}~]*[^\.]@[A-z0-9][A-z0-9-]{1,60}[A-z0-9]\.[A-z0-9][A-z0-9-]{1,60}[A-z0-9]", str)

print(a)