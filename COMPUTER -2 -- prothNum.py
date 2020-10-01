print('Proth Number Checker')
# A program that checks porth numbers

def isPowerOfTwo(y):  
        
    return (y and (not(y & (y - 1))))

def isprothnum(x):
    k = 1
    while k < (x//k):
        if (x % k == 0) :
            if(isPowerOfTwo(x//k)):
                return True

        k = k+2    

#this function is the function that allows the program restart after completion
def mainMenu():
    print('')
    num = str(input('\tPlease enter number for checking\n\t'))
    
    #to check if a number or something else was entered so we don't get errors
    if num.isdigit():
        #convert to integer
        num = int(num)
        myFunc = isprothnum(num-1)
        if (myFunc == True):
            print ("YES IT IS")
            return mainMenu()
        else:
            print ("NO IT ISN'T")
            return mainMenu()

    else:
        print('\tINVALID ENTRY\n')
        return mainMenu()
    
    
    #else:
     #   print('\tINVALID ENTRY\n')
      #  return mainMenu()
print(mainMenu())
# END

