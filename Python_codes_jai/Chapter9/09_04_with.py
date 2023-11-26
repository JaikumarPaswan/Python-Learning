with open('sample.txt', 'r') as f: #No need to close, as close is automated
    a = f.read()
with open('sample.txt', 'w') as f:
    a = f.write('me')
print(a)