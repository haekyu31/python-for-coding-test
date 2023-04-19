n = int(input())

count = 0

# 큰 단위 화폐부터 
coins = [500, 100, 50, 10]

for coin in coins:
    count += n // coin      # 화폐로 거슬러 줄수 있는 최대 동전 만큼
    n %= coin
    
print(count)