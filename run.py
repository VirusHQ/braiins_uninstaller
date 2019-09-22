import os

filepath = os.path.dirname(os.path.realpath(__file__))

print("Installing libraries")
os.system("python3 -m pip install -r files/requirements.txt")


print("\n\nRunning uninstaller")

filename = filepath + "/iplist.txt"
f = open(filename,"r")
filelines = f.readlines()
iplist = []
for x in filelines:
    if x != "\n":
        x = x.replace("\n","")
        iplist.append(x)
        
for x in iplist:
    if x != iplist[-1]:
        perstr = "python3 files/restore2factory.py --factory-image Antminer-S9-all-201812051512-autofreq-user-Update2UBI-NF.tar.gz " + str(x) + " &"
    else:
        perstr = "python3 files/restore2factory.py --factory-image Antminer-S9-all-201812051512-autofreq-user-Update2UBI-NF.tar.gz " + str(x)
    os.system(perstr)
    