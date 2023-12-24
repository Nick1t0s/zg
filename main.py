import os,webbrowser,wget
#webbrowser.open('https://www.python.org/ftp/python/3.12.1/python-3.12.1-amd64.exe')
path=os.getcwd()
path=path.split('\\')
t=path.index('Users')+1
path=path[:t+1]
path.append('Downloads')
path='\\'.join(path)
wget.download('https://www.python.org/ftp/python/3.12.1/python-3.12.1-amd64.exe',out=path)
os.system(path+'/python-3.12.1-amd64.exe')
print(path)
