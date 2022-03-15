paisA = 80000
paisB = 200000
anos = 0

while paisA <= paisB:
    paisA = paisA * 1.03  # 3%
    paisB = paisB * 1.015  # ,15%
    anos += 1

print(anos)
