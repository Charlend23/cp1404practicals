"""
Emails
Estimate = 30 Minutes
Actual =
"""

def main():
    user_email = input("Email: ")
    split_names(user_email)
    key_to_value = {}

def split_names(email):
    email_list = email.split("@")[0]
    full_name = email_list.split(".")
    return full_name

main()