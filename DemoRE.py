#DemoRE.py
#정규표현식을 사용하는 경우

import re



#일반적인 검색(함정 추가) - 빈칸이 들어가 있어도 찾음
result = re.search("[0-9]*th", "  35th")
print(result)
print(result.group())

cut()

#정확하게 일치
# result = re.match("[0-9]*th", "  35th")
# print(result)
# print(result.group())

result = re.search("\d{4}","올해는 2023년")
print(result.group()) #.group() : 찾은 문자열만 리턴해줌

result = re.search("\d{5}","우리 동네는 51200")
print(result.group())

cut()

import re

def check_email_address(email):
    # Define the regular expression pattern for a basic email address
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

    # Use the search function to find a match
    match = re.search(pattern, email)

    # Check if the email address is valid
    if match:
        return True
    else:
        return False

# Test 10 sample email addresses
sample_emails = [
    'user@example.com',
    'john.doe@gmail.com',
    'invalid-email',
    'missing_at_sign.com',
    'user@company',
    'user@company..com',
    'user@company.co.uk',
    'user123@domain123.co',
    'user@company_with_underscore.com',
    '@missing_username.com',
]

for email in sample_emails:
    if check_email_address(email):
        print(f'{email} is a valid email address.')
    else:
        print(f'{email} is not a valid email address.')


cut()
import re

def check_resident_registration_number(rrn):
    # Define the regular expression pattern for Korea's resident registration number
    pattern = r'^(\d{2})(\d{2})(\d{2})[-]?[1-4]\d{6}$'

    # Use the search function to find a match
    match = re.search(pattern, rrn)

    # Check if the resident registration number is valid
    if match:
        return True
    else:
        return False

# Test 10 sample resident registration numbers
sample_rrns = [
    '900101-1123456',
    '950203-2123456',
    '010304-3123456',
    '020405-4123456',
    '081006-5123456',
    '070707-6123456',
    '120818-7123456',
    '111111-8123456',
    '021212-9123456',
    '990101-1123456',
]

for rrn in sample_rrns:
    if check_resident_registration_number(rrn):
        print(f'{rrn} is a valid resident registration number.(Korean)')#한국인은 뒷자리가 1-4까지, 1,3은 남자, 2,4는 여자(9,0은 대부분 사망)
    else:
        print(f'{rrn} is not a valid resident registration number.(Foreiner)')#외국인은 5-8까지 있음

cut()
import re

def check_resident_registration_number(rrn):
    # Define the regular expression pattern for Korea's resident registration number
    pattern = r'^(\d{2})(\d{2})(\d{2})[-]?([1-4])\d{6}$'

    # Use the search function to find a match
    match = re.search(pattern, rrn)

    # Check if the resident registration number is valid
    if match:
        birth_year = match.group(1)
        birth_month = match.group(2)
        birth_day = match.group(3)
        gender_digit = match.group(4)

        # Determine gender based on the last digit
        gender = "Male" if int(gender_digit) in [1, 3, 5, 7] else "Female"

        # Check if the person is Korean or a foreigner based on the first digit of the last 7 digits
        nationality = "Korean" if int(gender_digit) in [1, 2, 3, 4] else "Foreigner"

        return f'{rrn} is a valid resident registration number. ({nationality}, {gender}, DOB: {birth_year}-{birth_month}-{birth_day})'
    else:
        return f'{rrn} is not a valid resident registration number.(Foreinger)'

# Test 10 sample resident registration numbers
sample_rrns = [
    '900101-1123456',
    '950203-2123456',
    '010304-3123456',
    '020405-4123456',
    '081006-5123456',
    '070707-6123456',
    '120818-7123456',
    '111111-8123456',
    '021212-9123456',
    '990101-1123456',
]

for rrn in sample_rrns:
    print(check_resident_registration_number(rrn))
