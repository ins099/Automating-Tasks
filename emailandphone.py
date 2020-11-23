# phoneAndEmail.py - Finds phone numbers and email addresses on the clipboard.

import re 
import pyperclip

#Creating Phone Regex
phoneRegex = re.compile(r'''(
    (\d{2} | \(\d{2}\) | \d{3} | \(\d{3}\))?
    (\s | - | \.)?
    (\d{3})
    (\s | - | \.)?
    (\d{4})
    (\s*(ext|x|ext.)\s*(\d{2,5}))?

)''', re.VERBOSE)


#Todo Email Regex Object
emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+
    @ 
    [a-zA-Z0-9.-]+
    (\.[a-zA-z]{2,4})
)''', re.VERBOSE)

#find matches

#find matches in clipboard
text = str(pyperclip.paste())

matches = []
for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups[1],groups[3],groups[5]])
    if groups[8] != '':
        phoneNum += ' x' +groups[8]
    matches.append(phoneNum)

for groups in emailRegex.findall(text):
    matches.append(groups[0])

#copy results
if len(matches) >0:
    pyperclip.copy('\n'.join(matches))
    print('Copied To Clipoard: ')
    print('\n'.join(matches))
else:
    print("none found")