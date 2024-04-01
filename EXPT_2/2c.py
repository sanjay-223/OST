def replace(s, r, t):
    return s.replace(r, '###').replace(t,r).replace("###",t)
s = input("Enter a string: ")
t = input("Enter the word to replace: ")
r = input("Enter the replacement word: ")

result = replace(s, t, r)

print(f"Modified: {result}")
