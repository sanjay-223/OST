def find_denomination(amount):
    denominations = [500, 200, 100, 50, 20, 10, 5, 2, 1]
    result = {}

    for denom in denominations:
        count = amount // denom
        if count > 0:
            result[denom] = count
            amount %= denom

    return result

amount = int(input("Enter the amount: "))

denomination_result = find_denomination(amount)

print("Denomination breakdown:")
for denom, count in denomination_result.items():
    print(f"{denom} rupees: {count} notes")
