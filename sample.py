import random
import bs4
total = 2000
n = 400
x = [random.random() for i in range(n)]
e = [int(i / sum(x) * (total - n)) + 1 for i in x] #每人留一分,剩余随机分，用四舍五入可能会超过总数
re = total - sum(e)
u = [random.randint(0, n - 1) for i in range(re)] #截断取整剩的零头再随机给各人 1 分
for i in range(re):
    e[u[i]] += 1

print(e)
print(sum(e))

