def permute(s):
    if len(s) <= 1:
        return [s]
    perms = []
    for i, c in enumerate(s):
        for p in permute(s[:i] + s[i+1:]):
            perms.append(c + p)
    return perms

inp = input("Enter a string: ")
print("Permutations of '{}' are:".format(inp))
perms = permute(inp)
for p in perms:
    print(p)
