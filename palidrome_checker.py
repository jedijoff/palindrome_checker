user_text = input("Enter some text: ")
lower_text = user_text.lower()
check_text = []


for char in lower_text:
    if char != " ":
        check_text.append(char)


if check_text == check_text[::-1]:
    print("It's a palindrome.")
else:
    print("It's not a palindrome.")