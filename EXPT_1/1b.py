def to_bin(dec):
    if dec == 0:
        return '0'
    
    bin_result = ''
    while dec > 0:
        bin_result = str(dec % 2) + bin_result
        dec //= 2
    
    return bin_result

def to_oct(dec):
    if dec == 0:
        return '0'
    
    oct_result = ''
    while dec > 0:
        oct_result = str(dec % 8) + oct_result
        dec //= 8
    
    return oct_result

def to_hex(dec):
    if dec == 0:
        return '0'
    
    hex_result = ''
    hex_chars = '0123456789ABCDEF'
    
    while dec > 0:
        hex_result = hex_chars[dec % 16] + hex_result
        dec //= 16
    
    return hex_result

num = int(input("Enter a decimal number: "))
base = int(input("""Enter the target base 
                 1. binary, 
                 2. octal, 
                 3. hexadecimal
                 > """))

map = {
    1:to_bin,
    2:to_oct,
    3:to_hex
}

result = map[base](num)

print(f"{num} in base {base}: {result}")
