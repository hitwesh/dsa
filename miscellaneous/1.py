s1 = input("Enter the string: ")
words = s1.split()
total = 0
for word in words:
    total += len(word)
print("Average length =", total / len(words))