from os import system

system('cls')


file =open("otos.csv")
elso=True
data_array=[]
for row in file.readlines():
    if elso:
        elso=not elso
        continue
    data=[]
    data.append(int(row.split(';')[11]))
    data.append(int(row.split(';')[12]))
    data.append(int(row.split(';')[13]))
    data.append(int(row.split(';')[14]))
    data.append(int(row.split(';')[15]))
 
    data_array.append(data)


for i in range(len(data_array)):
    x = 0
    jelen = data_array[i]
    for j in range(3):
        if int(data_array[i][j])+1 == int(data_array[i][j+1]) and int(data_array[i][j])+2 == int(data_array[i][j+2]):
            x+=1
            print(f"{i+2}: ", end="")
            for k in range(5):
                print(f"{data_array[i][k]} ", end="")
            print()
        
        

print("Itt a vége!")
