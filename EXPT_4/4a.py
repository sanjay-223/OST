string = input("Enter a sting: ")
l = string.split()
l.sort(key=lambda x:x[0].lower())
print(' '.join(l))