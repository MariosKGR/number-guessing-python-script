#define start and end
front = 1
rear = int(input("Input End: "))
found = False

while front <= rear and not(found):
    #Divide And Conquer
    middle = int((rear + front) / 2)
    print("Is your number:", str(middle), "? (Y/N)")
    ans = input()

    if ans == "Y":
        #Found Number
        found = True
        key = middle
    else:
        #Not Found Number - Higher or Lower
        print("Higher or Lower? (H/L)")
        ans = input()
        
        if ans == "H":
            front = middle + 1
        else:
            rear = middle - 1

if found:
    print("Found your number. Your number is:", str(key))
else:
    print("You cheated.")