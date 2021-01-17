with open('numere.txt', 'r') as f:
    a=f.readline()
    b=f.readline()
with open('minim.txt', 'w') as f:
    if a<b:
        f.write(a)
    if b<a:
        f.write(b)
