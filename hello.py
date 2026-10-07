password=input("Enter your password:")

has_upper=False
has_lower=False
has_digit=False
has_special=False

for char in password:
    if char.isupper():
        has_upper=True
    elif char.islower():
        has_lower=True
    elif char.isdigit():
        has_digit=True
    else:
        has_special=True

score=0
if len(password)>=8:
    score+=1
if has_upper:
    score+=1
if has_lower:
    score+=1
if has_digit:
    score+=1
if has_special:
    score+=1

print("Length:",len(password))
print("Uppercase:",has_upper)
print("Lowercase:",has_lower)
print("Number:",has_digit)
print("Special character:",has_special)

if score<=2:
    print("Password Strength:WEAK")
elif score<=4:
    print("Password Strength:MEDIUM")
else:
    print("Password Strength:STRONG")
    
