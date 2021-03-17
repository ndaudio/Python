a = [-40,1,2,3,5,6,7,8,9,10,11,-20,40,4000,2,4,10,7,-2325]

def lowest():

    #prints initial array
    #print(a)
    
    #Creates a new array for positive numbers
    posA =[]

    #Creates a loop to itterate through array a and create a new array of positive numbers
    for x in a:
        if x>0:
            posA.append(x)

    #Prints positive array
    #print(posA)

    #Arranges and prints array
    posA.sort()
    #print(posA)

    #Creates a loop to find lowest integer not contained in the array,
    # and sets initial value to 1. 

    x=1

    while True:

        if x in posA:
            x+=1

        else:
            print(x, "Is the lowest integer not in the array.")
            break
    
    
def main():
    lowest()
   
    
main()

