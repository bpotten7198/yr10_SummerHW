#paste code here
### Time table program v1.0 ###
def tTP(amount,num):
    aT = 0
    for x in range(amount+1):
        print("{0} * {1} = {2}".format(num,aT,aT*num))
        aT+=1

amount1 = int(input("How many times will it loop? ")) 
num2 = int(input("Enter the num to times: "))
tTP(amount1,num2) 
### End of program ###
