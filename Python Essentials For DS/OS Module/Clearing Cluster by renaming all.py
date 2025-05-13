import os
files=os.listdir("D:\Java Imp")
print(os.listdir("D:\Java Imp"))
for i in range (len(files)):
    path=os.path.join("D:\Java Imp",files[i])
    os.rename(path,f"D:\Java Imp\{i}.png")