import re

# Names: capitalized, can include hyphens/apostrophes, 1+ words
name = r"^[A-Z][a-zA-Z'’-]*(?: [A-Z][a-zA-Z'’-]*)*$"
name_regex = re.compile(name)

# Phone numbers: unchanged
phone_number = r"^(\+?\d{1,2}\s?)?(\(?\d{3}\)?)[\s.-]?\d{3}[\s.-]?\d{4}$"
phone_regex = re.compile(phone_number)

# Emails: must start with a letter
email_address = r"^[A-Za-z][A-Za-z0-9._%+-]*@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"
email_regex = re.compile(email_address)
