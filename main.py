from time import sleep
import random
import threading
from playsound import playsound

isrun=True
startmoney=500 # 시작 금액
coinmoney=100 # 초기 코인가격 
haveconin=0 # 초기 소유 코인의 양
usermoney=startmoney # 돈
def setcoinmoney(): # 코인 가격 갱신 함수
    global coinmoney
    while isrun:
        if random.randrange(2)==0:
            coinmoney=int(coinmoney*1.08)
        else:
            coinmoney=int(coinmoney*0.92)
        print("코인의 가격 : " + str(coinmoney) +  ", 보유 코인의 수 : " + str(haveconin)+ "개" + ", 돈 : " + str(usermoney))
        sleep(1)

t = threading.Thread(target=setcoinmoney)
t.start()
while True:  
    inputbox = input()
    if inputbox=="end":
        isrun=False
        break
    inputbox = inputbox.split()
    if inputbox[0] == "0":
        pass
    elif usermoney < coinmoney*int(inputbox[0]): 
        print("(매수) *실패* 보유 금액이 부족합니다.")
    else:
        haveconin += int(inputbox[0])
        usermoney -= int(inputbox[0]) * int(coinmoney)
        print("(매수) *성공* " + str(inputbox[0])+ "개의 코인을" + str(coinmoney) + "원에 매수 했습니다!"+" (-"+str(int(inputbox[0])*int(coinmoney))+")")
        playsound("/Users/seojun/Desktop/coin/1.wav")

    if inputbox[1] == "0":
        pass
    elif haveconin < int(inputbox[1]):
        print("(매도) *실패* 보유 코인이 부족합니다.")
    else:
        usermoney += int(inputbox[1]) * int(coinmoney)
        haveconin -= int(inputbox[1])
        print("(매도) *성공* " + str(inputbox[1])+ "개의 코인을" + str(coinmoney) + "원에 매도 했습니다!"+" (+"+str(int(inputbox[1])*int(coinmoney))+")")
        playsound("/Users/seojun/Desktop/coin/2.wav")
    
if startmoney <= usermoney:
    print("수익률 +" + str(usermoney/startmoney*100)+"%")
else:
    print("수익률 "+str((usermoney-startmoney)/startmoney*100)+"%")