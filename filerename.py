import os

for f in os.listdir():
    if f.startswith('deepin'):
        
        nf = f.replace(" ",'-')
        print(f,nf)
        os.rename(f,nf)