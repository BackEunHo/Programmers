n,m = map(int,input().split())
sum = 0
cards = list(map(int,input().split()))
for i in range(len(cards)-2): # (len(cards) = 5, i = 0,1,2
    a = cards[i] # 첫번째 카드
    for j in range(i+1,len(cards)): # (len(cards) = 4, j = 1,2,3
        b = cards[j] # 두번째 카드
        for k in range(j+1,len(cards)): # (len(cards) = 3, k = 2,3,4
            c = cards[k] # 세번째 카드
            if(sum < a+b+c <= m):
                sum = a + b + c
print(sum)