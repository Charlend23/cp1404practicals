"""
Emails
Estimate = 30 Minutes
Actual =
"""

def main():
    user_email = input("Email: ")
    email_to_name = {}
    while user_email != "":
        user_name = split_names(user_email)
        full_name = " ".join(convert_to_title(user_name))
        name_confirmation = input(f"Is Your Name {full_name}? (Y/n) ").lower()
        if name_confirmation != "" or "y":
            name_confirmation = input("Name: ")
        email_to_name[user_email] = name_confirmation

def split_names(email):
    email_list = email.split("@")[0]
    full_name = email_list.split(".")
    return full_name

def convert_to_title(names):
    return [name.title() for name in names]
main()