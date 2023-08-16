import random

ans = []
guess = []
it=1

#隨機產生4個不重覆且介於0~9的整數做為答案
while len(ans)<4:
    x = random.randrange(10)
    if x not in ans:
        ans.append(x)

#[1.使用者猜數字->2.程式判斷是否為答案]的迴圈，直到玩家猜對才會跳出迴圈
while guess!=ans:
    tip = [0,0]
    guess = []

    #1.使用者猜數字
    inputnum=input(f'第{it}次猜輸入4個不重覆且介於0~9的整數(i.e. 7895)\n')
    for i in inputnum:
        guess.append(int(i))

    #2.程式判斷是否為答案
    for i in range(4):
        for j in range(4):
            if guess[i]==ans[j] and i==j:
                tip[0]+=1
            if guess[i]==ans[j]:
                tip[1]+=1
    tip[1] = tip[1]-tip[0]

    if guess==ans:
        break
    
    it+=1
    print(f'你輸入的是:{guess}  提示:{tip[0]}A{tip[1]}B')
print('finish'+f'答案是{ans}')