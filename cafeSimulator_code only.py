import time
import datetime
menuDict = {1:"Americano",2:"Caffe Latte",3:"Cold Brew",4:"Capuccino",5:"Flat White"}
priceDict = {1:2000,2:2500,3:3000,4:3500,5:4000}
nowDate = datetime.datetime.now().strftime("%Y-%m-%d_%H%M") #파일명에 사용
n=0
sales=0

# .format으로 문자열을 정렬하기 위해 메뉴이름을 영어로 바꿈
def printMenu():
    for i in range(1,6):
        print("{}.{:<30}{:.>10}원".format(i,menuDict[i],priceDict[i]))

def orderMenu():
    opened=True # exit를 입력하기 전까지 반복하기 위한 장치
    rightKey = True # 원하는 입력값을 얻을 때까지 반복하기 위한 장치
    while rightKey: 
        inputKey = input("주문하실 메뉴를 번호로 입력하세요 : ")
        # 메뉴번호, exit 외에는 오류 발생하도록 함
        if inputKey !='exit': 
            try: # exit외에 문자열을 입력하면 int변환이 안 되므로 오류가 발생할 수 있음(except로 처리)
                inputMenu = int(inputKey)
                if inputMenu>0 and inputMenu<6 : #정상주문
                    print(menuDict[inputMenu] + "를 주문하셨습니다")
                    rightKey=False
                else: #메뉴번호에 없는 번호를 입력하면 다시 처음부터
                    print("메뉴번호를 다시 확인해주세요")
                    continue
            except: # 문자열을 입력하면 오류가 발생함..다시 처음부터
                print("올바른 입력이 아닙니다")
                inputMenu=None
                continue
        else: # exit를 입력하면 프로그램 종료
            opened=False
            rightKey=False
            inputMenu=None

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
    f=open(nowDate+".txt",'w')
    f.close()

def writeLog(inputMenu):
    f = open(nowDate+".txt",'a')
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
            f = open(nowDate+".txt",'a')
            f.write("{}원을 받음.\n거스름돈 : {}원\n--------------------\n".format(inputPay,change))
            f.close()
            print("{}원을 받았습니다. 거스름돈은 {}원입니다.".format(inputPay,change))
            print("-"*44)

#프로그램 시작
newLog()
while True:
    n=n+1
    print("주문번호 : {}".format(n))
    printMenu()
    opened, inputMenu = orderMenu()
    if opened==False:
        n=n-1 #영업종료할 때는 주문번호 체크하지 않기 위함
        f = open(nowDate+".txt",'a')
        f.write("<<당일 영업 마감>>\n- 매출액 : {}원".format(sales))
        f.close()
        print("영업을 종료합니다.\n오늘 주문건수는 {}건, 매출액은 {}원 입니다.".format(n,sales))
        break

    writeLog(inputMenu)
    sales = sales + priceDict[inputMenu]
    pay(inputMenu)

    time.sleep(2)
