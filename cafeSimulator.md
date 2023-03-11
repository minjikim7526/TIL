# cafeSimulator 복습 on Mar. 9th. 2023

### 1. 메뉴를 출력
1. 아메리카노
2. 라떼
3. 바닐라라떼
4. 녹차라떼
5. 콜드브루

### 2. 번호로 입력 받아서 주문을 받음

### 3. 음료를 만드는데 시간
sleep()함수를 통해서 만드는 시간 모델링
1. 1초
2. 2초
3. 3초
4. 3초
5. 1초

### 4. 음료가 만들어지면 log.txt파일에 남긴다.


```python
import time
menuDict = {1:"Americano",2:"Caffe Latte",3:"Cold Brew",4:"Capuccino",5:"Flat White"}
priceDict = {1:2000,2:2500,3:3000,4:3500,5:4000}
n=0
sales=0

def printMenu():
    for i in range(1,6):
        print("{}.{:<30}{:.>10}원".format(i,menuDict[i],priceDict[i]))

def orderMenu():
    opened=True
    rightKey = True
    while rightKey:
        try:
            inputKey = input("주문하실 메뉴를 번호로 입력하세요 : ")
            inputMenu = int(inputKey)
            if inputMenu>0 and inputMenu<6 :
                print(menuDict[inputMenu] + "를 주문하셨습니다")
                rightKey=False
            # elif inputKey=='x':
            #     opened=False
            else:
                print("메뉴번호를 다시 확인해주세요")
                continue
        except:
            print("숫자가 아닙니다!")
            continue

    return opened,inputMenu

def makeMenu(inputMenu):
    if int(inputMenu)==1:
        time.sleep(1)
    elif int(inputMenu)==2:
        time.sleep(2)
    elif int(inputMenu)==3:
        time.sleep(3)
    elif int(inputMenu)==4:
        time.sleep(3)
    elif int(inputMenu)==5:
        time.sleep(1)
    return inputMenu

def newLog():
    f=open("cafeLog.txt",'w')
    f.close()

def writeLog(inputMenu):
    f = open("cafeLog.txt",'a')
    f.write("{}. {}({}원)\n".format(n,menuDict[inputMenu],priceDict[inputMenu]))
    f.close()
    print("주문하신 {}가 나왔습니다. {}원입니다.".format(menuDict[inputMenu],priceDict[inputMenu]))


def pay(inputMenu):
    paying=True
    while paying:
        try:
            inputPay = int(input("낸 돈을 입력하세요. : "))
        except:
            inputPay = 0
        else:
            paying=False
            change = inputPay - priceDict[inputMenu]
            f = open("cafeLog.txt", 'a')
            f.write("{}원을 받음.\n거스름돈 : {}원\n--------------------\n".format(inputPay,change))
            f.close()
            print("{}원을 받았습니다. 거스름돈은 {}원입니다.".format(inputPay,change))
            print("-"*44)


newLog()
while True:
    n=n+1
    print("{}번째 주문".format(n))
    printMenu()
    opened, inputMenu = orderMenu()
    if opened==False:
        f = open("cafeLog.txt", 'a')
        f.write("당일 영업 마감!\n매출액 : {}원".format(sales))
        f.close()
        print("영업을 종료합니다.\n오늘 주문건수는 {}건, 매출액은 {}원 입니다.".format(n,sales))
        break

    writeLog(inputMenu)
    sales = sales + priceDict[inputMenu]
    pay(inputMenu)

    time.sleep(2)
```