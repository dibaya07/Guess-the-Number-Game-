import random
import string

pass_len = 12
val = string.ascii_letters + string.digits + string.punctuation

password = ""
for i in range(pass_len) :
    password += random.choice(val)

print(password)