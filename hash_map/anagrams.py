def check_anagrams(s1, s2):
    a = s1.replace(" ", "").lower()
    b = s2.replace(" ", "").lower()
    if len(a) != len(b): return "Not an Anagram"
    else:
        count = {}
        for ch in a:
            count[ch] = count.get(ch, 0)+1
        for ch in b:
            if ch not in count:
                return "Not an Anagram" 
                break

            count[ch] -= 1

            if count [ch]<0:
                return "Not an Anagram"
                break
            else:
                return "Is an Anagram"

str1 = input("Enter your first string: ")
str2 = input("Enter your second string: ")
print(check_anagrams(str1,str2))

        