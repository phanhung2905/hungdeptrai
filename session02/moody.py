from random import randint
mood = randint (0, 100)

if mood < 30: 
    print("sad")
elif mood < 60: 
    print("ok")
else:
    print("oh yeah")

