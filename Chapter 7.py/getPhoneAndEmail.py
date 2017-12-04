import re, pyperclip

phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?                # area code
    (\s|-|\.)?                        # separator
    (\d{3})                           # first 3 digits
    (\s|-|\.)                         # separator
    (\d{4})                           # last 4 digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))?    # extension
    )''', re.VERBOSE)

emailRegex = re.compile(r'''(
	[a-zA-Z0-9._%+-]+       # username
	@                       # @ symbol
	[a-zA-Z0-9.-]+          # domain name
	(\.[a-zA-Z]{2,4})       # dot-something
	)''', re.VERBOSE)

#TODO find all matches on clipboard
text = pyperclip.paste()
matches = []
for groups in phoneRegex.findall(text):
	phoneNum = "-".join([groups[1], groups[3], groups[5]])
	if groups[8] != ' ':
		phoneNum += ' x' + groups[8]
	matches.append(phoneNum)

print(matches)

#TODO copy all matches to clipboard

#TODO print message displaying results