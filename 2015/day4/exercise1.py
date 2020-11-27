import hashlib

key = "bgvyzdsv"

i = 1
while True:
    phrase = key + str(i)
    result = hashlib.md5(phrase.encode("utf-8")).hexdigest()
    if result[0:5] == "00000":
        break
    i += 1

print(i)
