lst = []
dtypes = ['int','str','list','tuple']
for d in dtypes:
    lst.append(eval(d+"(input(f'Enter a {d} :'))"))
print(lst)  