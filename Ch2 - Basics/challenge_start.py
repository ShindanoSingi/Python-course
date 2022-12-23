
def tester(word):
    reversedword = word[::-1];
    if word == reversedword:
        print("Yes, it is a palindrome!");
    else:
        print("No, it is not a palindrome!");

bool = True

# while (bool):
#     word = input("Enter your string to test for palindrome or 'exit': ")

#     if word == "exit":
#         bool = False
#         break

#     word = word.lower()

#     newString = ''
#     for s in word:
#         if s.isalnum():
#             newString+=s

#     tester(newString)

var = '123456789'
print(var[1:6:2])