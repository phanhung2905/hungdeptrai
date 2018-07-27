from random import randint

numb = randint(0, 100)
count = 0
playing = True
while playing:
    guess = int(input("guess my nuber (0, 100)"))
    if guess > numb:
        print("too lagre :<")
    elif guess < numb:
        print("too small :>")
    else:
        print("bingo")
        break
    count += 1
    if count ==7:
        print("you lose")
        playing = False


