user_text = input("Enter some text: ")
lower_text = user_text.lower()
check_text = []
reverse_text = []

for char in lower_text:
    if char != " ":
        check_text.append(char)

for item in check_text:
    reverse_text.insert(0, item)

if check_text == reverse_text:
    print("It's a palindrome.")
else:
    print("It's not a palindrome.")