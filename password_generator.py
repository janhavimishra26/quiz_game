import random
import string
letter_count=int(input("how many letters do you want?"))
digits_count=int(input("how many digits do you want?"))
symbols_count=int(input("how many symbols do you want?"))
letters=list(string.ascii_letters)
digits=list(string.digits)
symbols=list('@!#$%^&*()_+{}[],.<>')
password_chars=[]
password_chars+=random.choices(letters,k=letter_count)
password_chars+=random.choices(digits,k=digits_count)
password_chars+=random.choices(symbols,k=symbols_count)
random.shuffle(password_chars)
password=''.join(password_chars)
print("Your generated password is:",password)

