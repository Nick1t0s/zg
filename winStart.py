def downloadFlask():
    os.system("pip3 install flask")
def downloadLocalServ()
import subprocess,time,os

# Запуск второго файла в отдельном процессе
process = subprocess.Popen(['python', 'second_file.py'])

# ждем некоторое время, прежде чем прервать выполнение
time.sleep(5)

# Прерывание выполнения второго файла
process.terminate()