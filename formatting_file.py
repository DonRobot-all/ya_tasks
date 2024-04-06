n = int(input())
answer = 0
for i in range(n):
    space = int(input()) 
    answer += space // 4
    if space % 4 == 1 or space % 4 == 2:
        answer += space % 4 
    elif space % 4 == 3:
        answer += 2
print(answer)

# 1. число делится нацело на 4
# 2. space
# 3. space + space
# 4. tab - backspace

   
