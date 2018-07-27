numb = int(input("enter a number: "))

counting = True 
count = 0

while numb != 0:
    numb = numb // 10
    count += 1
    if numb ==0:
        counting = False

print(count)
