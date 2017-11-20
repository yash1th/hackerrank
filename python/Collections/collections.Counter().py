from collections import Counter
_ = input()
shoes = Counter([int(i) for i in input().strip().split(' ')])
money_earned = 0
for _ in range(int(input())):
    size, price = (int(i) for i in input().strip().split(' '))
    if shoes[size]:
        money_earned += price
        shoes[size] -= 1
print(money_earned)