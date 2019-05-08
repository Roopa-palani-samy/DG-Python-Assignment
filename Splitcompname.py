# 7. Assuming that we have some email addresses in the "username@companyname.com"
# format, write a program to print the company name of a given email address. Both user
# names and company names are composed of letters only

email = 'user@example.com'

first=email.index('@')
last=email.index('.')

domain = email[first+1:last]
print(domain)