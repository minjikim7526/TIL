
n = int(input("숫자를 입력하세요 :"))

for i in range (1,n+1,1):
    myStr=str(i)
    cnt=0
    for j in myStr: # 핵심! myStr문자열을 한 글자씩 인식함!!
        if j=="3" or j=="6" or j=="9":
            cnt=cnt+1
            print("박수",end=" ") # end=" "를 통해 개행문자(줄바꿈문자) 제거해서 "박수 박수" 이렇게 나올 수 있도록 함
    if cnt>0:
        print() # 작은for문을 빠져나오면 줄바꿈
    else:
        print(myStr)