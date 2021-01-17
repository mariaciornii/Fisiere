with open('input.txt', 'r') as f:
    a=int(f.readline())
with open('output.txt', 'w') as f:
    f.write(str(a-2))
    f.write(' ')
    f.write(str(a-1))
    f.write(' ')
    f.write(str(a))
    f.write(' ')
    f.write(str(a+1))
    f.write(' ')
    f.write(str(a+2))