import hashlib

# There is string s = "Python Bootcamp". Write the code that hashes string.
s = "Python Bootcamp"

hashvar = hashlib.sha256(s.encode())

print(hashvar.hexdigest())

#output - b30103af390903d16b7b16264caeda25e986014787cbaa37a57ecc3b9eae15c0
