
word = input("Podaj słowo: ")
def reverse (x):
    return x[::-1]
if (reverse(word) == word):
    print("Jest palidronem")
else:
    print("Nie jest palidronem")