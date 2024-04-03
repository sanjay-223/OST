a = [chr(65+i) for i in range(26)]
s = int(input("Enter a step value: "))
f = open("alphabets.txt",'w')
i = 0
while i<= len(a):
    f.write(''.join(a[i:i+s])+'\n')
    i += s
f = open("alphabets.txt",'r')
print(f.read())
f.close()