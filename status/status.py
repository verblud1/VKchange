import vk_api
import random
import time
import sys
idu=[]
tok=[]
hu=[]
def load_accs():      
        file = open(sys.path[0] + '/tokenVK.txt', 'r',encoding = 'utf-8-sig').readlines()
        for q in file:
        
            try:
                q = q.strip()
                tmp = q.split(':',1)
                idu.append(tmp[0])
                tok.append([bytes(tmp[1].strip(), 'UTF-8') ])
                
                
                print('загружен', tmp[0])
            except:
                print('не удалось загрузить аккаунт, array=',tmp)
def check():
        for i in tok:
                    try:                
                        d = vk_api.VkApi(token=i).get_api() 
                        d.account.getInfo(fields = 'country')
                        hu.append(i)
                    except:
                        print('Неверный access_token. Возможно, аккаунт забанен, array =','[ token:',i,']')
        print('загружено', len(hu), 'аккаунтов')
def status():
    go=input('введите первое слово:')
    pza=input('введите второе слово:')
    wh=int(input('циклов:'))
    zad=int(input('введите задержку:'))
    f=[go,pza]
    
    
    for i in hu:
        for st in range (wh):
            random.shuffle(f)
            a=random.choice(f)
            jo=random.choice(f)
            haz=a+' '+jo
            try:
                d = vk_api.VkApi(token=i).get_api()
            #print(d.users.get())
                d.status.set(text=haz)
                time.sleep(zad)
                print('cтатус изменен')
            except Exception as er:
                print(er)
            

load_accs()
check()
status()