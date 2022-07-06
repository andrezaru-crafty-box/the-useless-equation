it = int(input("Enter a number: "))
c = 0
i = 1
while i < it:
    i = i + 1
    num = i
    c = 0
    #print(num)
    while num > 1:
        if (num % 2) == 0:
            
            num = num / 2
            c = c + 1
        else:
            
            num = (num * 3) + 1
            c = c + 1 
    print("steps = ",c,"starting number = ",i)