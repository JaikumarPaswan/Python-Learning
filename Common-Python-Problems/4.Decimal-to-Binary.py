def decimal_to_binary(n):
    return bin(n).replace("0b", "")

print(decimal_to_binary(10))


def binary_to_decimal(b):
    return int(str(b),2)

print(binary_to_decimal(1010))