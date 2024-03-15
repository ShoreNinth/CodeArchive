import time

def login_activity():
    with open(file='log.txt',mode='a', encoding='utf-8') as f:
        f.write(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
def register_activity():
    with open(file='log.txt',mode='a', encoding='utf-8') as f:
        f.write(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
