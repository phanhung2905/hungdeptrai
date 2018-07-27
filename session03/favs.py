favs = ["netflix", "teaching", "death note"]
print("hi there,your favs")
print("* " * 10)

for index, item in enumerate(favs):
    print ("{}. {}".format(index + 1, item))
print("* " * 20)

pos = int(input("position you want to up"))
update_fav = input("your replacing fav:" )
favs[pos - 1] = update_fav


for index, item in enumerate(favs):
    print ("{}. {}".format(index + 1, item))
print("* " * 20)