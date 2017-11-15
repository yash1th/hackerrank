# import time
# stime = time.time()

# a = input()
# print(any(c.isalnum() for c in a))
# print(any(c.isalpha() for c in a))
# print(any(c.isdigit() for c in a))
# print(any(c.islower() for c in a))
# print(any(c.isupper() for c in a))

# the following one is a little bit faster (0.5 seconds) than the above
a = input()
foundAlNum = False
foundAlpha = False
foundDigit = False
foundLower = False
foundUpper = False
for i in a:
    if not foundAlNum and i.isalnum():
        foundAlNum = True
    if i.isalpha() and not foundAlpha:
        foundAlpha = True
    if not foundDigit and i.isdigit():
        foundDigit = True
    if not foundLower and i.islower():
        foundLower = True
    if not foundUpper and i.isupper():
        foundUpper = True

print(foundAlNum)
print(foundAlpha)
print(foundDigit)
print(foundLower)
print(foundUpper)

# print(time.time()-stime)
