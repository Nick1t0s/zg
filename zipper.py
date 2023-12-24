import zipfile,wget,os,subprocess
url='https://github.com/Nick1t0s/tr/archive/refs/heads/main.zip'
wget.download(url)
with zipfile.ZipFile('tr-main.zip', 'r') as zip_ref:
    zip_ref.extractall()
path=os.getcwd()
path=path.split('\\')
t=path.index('tx')
path=path[:t+1]
path.append('tr-main')
path.append('main.py')
path='\\'.join(path)
print(path)
subprocess.call(path, shell=True)
