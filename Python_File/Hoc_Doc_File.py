file=open("demofile2.txt",'r') 
for line in file:
    data=line.strip()
    print(data)
file.close
