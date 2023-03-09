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
---
```python
import time
menuDict = {1:"아메리카노",2:"라떼",3:"바닐라라떼",4:"녹차라떼",5:"콜드브루"}

def printMenu():
    print("1. 아메리카노")
    print("2. 라떼")
    print("3. 바닐라라떼")
    print("4. 녹차라떼")
    print("5. 콜드브루")

def orderMenu():
    opened=True

    inputKey = input("주문하실 메뉴를 번호로 입력하세요. : ")
    if inputKey=='x':
        inputMenu=None
        opened=False
    elif int(inputKey) > 0 and int(inputKey) < 6:
        inputMenu = int(inputKey)
        print(menuDict[inputMenu] + "를 주문하셨습니다.")

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
    f=open("cafeLog.txt",'a')
    f.write("주문하신 {}가 나왔습니다.\n".format(menuDict[inputMenu]))
    f.close()

newLog()
while True:
    printMenu()
    opened, inputMenu = orderMenu()
    if opened==False:
        print("영업을 종료합니다")
        break
    makedCoffee = makeMenu(inputMenu)

    writeLog(makedCoffee)
```