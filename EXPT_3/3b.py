dict1 = {i:i+1 for i in range(1,5)}
dict2 = {i:i+1 for i in range(3,5)}

common_pairs = {key: dict1[key] for key in dict1 if key in dict2 and dict1[key] == dict2[key]}
print("Common key-value pairs:")
for key, value in common_pairs.items():
    print(f"{key}: {value}")