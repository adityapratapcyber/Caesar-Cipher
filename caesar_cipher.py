text = input("Enter Text: ")
shift = 3

result = ""

for char in text:
    result += chr(ord(char) + shift)

print("Encrypted Text:")
print(result)
