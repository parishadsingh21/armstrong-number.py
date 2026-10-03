hile True:
    exp=input("calculate karo ya exit ikho") #jaise 5+3*2
    if exp == 'exit':
        break
    try:
        print("result:",eval(exp))
    except:
        print("wrong input fir se daalo")
