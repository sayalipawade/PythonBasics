#For loop
sum=0
for val in range(1,6):
    sum=sum+val
print(sum)

#variables
dict={}
flag=0
size=0

#function to taking elements from user
size=int(input('Enter size:'))
print('Enter elements:')
for i in range(0,size):
    dict[i]=int(input())
print(dict)

#Code to finding the element in dictionary
def searchElement():
    element=int(input('Enter element to be search:'))
    for i in range(0,size):
        if dict[i]==element:
            flag=1
            break
    if flag==1:
        print('element found')
    else:
        print('element not found')

#Function calling
searchElement() 

