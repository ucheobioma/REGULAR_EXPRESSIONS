import re

# 8 chrs long
# any special character
# print error or confirmation message

while True:
    test_email = input("enter your email\n")
    check_email = re.compile(r"(^(\w+[.|\w])*@(\w+[.])*\w+$)")
    if check_email.fullmatch(test_email):
        break
    else:
        print('enter better email')
    break

while True:
    test_password = input("enter your password\n")
    check_password = re.compile(r"(\w+[#%$@&]){8}")
    if check_password.fullmatch(test_password):
        print('all good...logged in')
        break
    else:
        print('long and valid please')
        test_password = input("enter your password\n")
    break
