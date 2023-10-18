
def Bin(low,high,key,a):
    mid=int(low+high/2)
    
    if a[mid]==key:
        return mid
    elif low>high:
        return -1
    elif a[mid]>key:
        return Bin(low,mid,key,a)
    
    else:
        return Bin(mid,high,key,a)

if __name__=="__main__":
    Nos=int(input("Enter the numbe of Elements\n"))
    a=[]
    print("Enter the number in Ascending order\n")
    for i in range(Nos):
        a.append(int(input(f"Enter the {i}th Element")))
    
    key=int(input("Enter the key element to be searched\n"))
    pos=Bin(0,Nos-1,key,a)
    print(f"Element {key} found at {pos+1} in {a}")
        


