string1 = input("Enter the First String : ")
string2 = input("Enter the Second String : ")
if sorted(string1.lower())==sorted(string2.lower()):
    print(f"{string1} and {string2} are anagrams.")
else:
    print(f"{string1} and {string2} are not anagrams.")