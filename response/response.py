import validators

print("valid") if validators.email(input("email\n")) else print("invalid")