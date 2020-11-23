
# Finding patterns of text with irregullar expressions.

def isPhoneNumber(text):
    if len(text) != 12:
        return False
    for i in range(0,3):
        if not text[i].isdecimal():
            return False
    if text[3] != '-':
        return False
    for i in range(4,7):
        if not text[i].isdecimal():
            return False
    if text[7] != '-':
        return False
    for i in range(8,12):
        if not text[i].isdecimal():
            return False
    return True

print(isPhoneNumber("123-456-7890"))

tex = "My office Phone is 123-456-7890. but call me at 456-234-9088"
def RecognizePhoneNumber(text):
    for i in range(len(text)):
        chunk = text[i:i+12]
        if isPhoneNumber(chunk):
            print("Found Phone Number: " + chunk)
    print("Done")

RecognizePhoneNumber(tex)        

# Finding pattern of text in regular expressions

# using re library
# create and match regex object

import re

is_phone = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = is_phone.search('My number is 123-123-1234')
print("Phone is: " + mo.group())

is_phone= re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = is_phone.search("My number is 415-555-4242.")
print(mo.group(1))

          ## Checking for Country Numbers

codes = {'92':"Pakistan", '93':'India'       }
is_phone = re.compile(r'(\d\d)-(\d\d\d)-(\d\d\d\d\d\d\d)')

inp = input("Enter Text")

mo= is_phone.search(str(inp))
for code in codes:
    if code == mo.group(1):
        print(f"Phone Number Detected! \n {mo.group()} \n This is {codes[code]} number \n Call?")
    else:
         continue

