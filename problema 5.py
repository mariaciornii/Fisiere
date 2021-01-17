with open('numar.txt', 'r') as f:
    a=int(f.readline())
with open('inmultire.txt', 'w') as f:
    for i in range(1,11):
        n=i*a
        f.write(str(a)+'*'+str(i)+'='+str(n)+'\n')
