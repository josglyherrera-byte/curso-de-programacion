def validar_email(email):
    return "@" in email and " " not in email and email.endswith(".com")

emails = [input(f"Email {i+1}: ") for i in range(int(input("¿Cuántos emails? ")))]

print("\nEmails válidos:")
for e in emails:
    if validar_email(e):
        print(f"✓ {e}")