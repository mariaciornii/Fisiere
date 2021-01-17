with open('globulet.txt', 'r') as f:
    albe=int(f.readline())
rosii=albe+3
albastre=rosii+albe-2
with open('bradut.txt', 'w') as f:
    f.write(str(albe+rosii+albastre))