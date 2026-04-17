m = int(input())
n = int(input())
count = 0
for pal in range(m,n+1):
    if str(pal) == str(pal)[::-1]:
        count += 1
print(count)