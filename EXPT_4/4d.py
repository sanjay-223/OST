f1 = open(input("Enter soruce file name: "),'r')
f2 = open(input("Enter Destination file name: "),'w')
f2.write(f1.read())
print('File Copied Successfully')
f1.close()
f2.close()