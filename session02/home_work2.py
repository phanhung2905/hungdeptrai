print:x = input("would you like to convert fahrenheit(f) or celsius(c)?")
if x == "f":
    y = input("what is the fahrenheit?")
    f = (int(y) - 32) * 5.0 / 9
    print (f)
elif x == "c":
    n = input("what is the celsius?")
    z = (int(n) * 9) / 5.0 + 32
    print ("and in fahrenheit, that is:")
    print (z)
