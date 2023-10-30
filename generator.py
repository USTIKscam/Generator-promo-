import socket
import random
import os
import time

print('\u001b[32mВнимание! Шансы на ловлю промокода очень малы! Но в случае если вы успешно словите промокод Он появится в файле Promocode By Xindos.txt')
time.sleep(2)
print('\u001b[32mТак же вводите верный айди! в случае чего запросы не будут работать!')
time.sleep(1)
bb = int(input("Введите ваш ID: "))
print('\u001b[32mАйди который вы ввели:',bb)
time.sleep(1)
print('\u001b[32mНачало через:')
time.sleep(1)
print('\u001b[32m3')
time.sleep(1)
print('\u001b[32m2')
time.sleep(1)
print('\u001b[32m1')
time.sleep(1)
print('\u001b[32mЗапросы идут на айди:', bb)

symbot = '123456789'
symbot2 = 'ABCDEFGHIJKLMNOPQRSTUVWXZ'
symbot3 = symbot2.upper()
symbot4 = symbot +symbot2 +symbot3 
ls = list(symbot4)
random.shuffle(ls)

pws = ''.join([random.choice(ls) for x in range(12)])
print('\u001b[31m Не рабочий промо - ',pws)


        
ip = '3.65.178.116' #moscow
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((ip, 2222))

while 1:
    ticket = ''
    for _ in range(32):
    	  a = random.choice(pws)
    	  ticket = ticket + a
    ticket_hex = ticket.encode("utf-8").hex()
    token = "000000740a2435353537333038632d643430312d343334312d613364652d336231386662333030376239121648616e647368616b6552656d6f7465536572766963651a0e70726f746f48616e647368616b6522241a220a20" + ticket_hex
    s.send(bytes.fromhex(token))
    o = s.recv(1024).decode("utf-8", errors="ignore")
    pws = ''.join([random.choice(ls) for x in range(12)])
    if o[3] == '(':
        print('\u001b[32m','Найдено! -', pws)
        with open('Promocode by Xindos.txt', 'w') as f:
            f.write(f'{ticket}\n')
    else:
        print('\u001b[31m Не рабочий промо - ', pws)
        
       
        