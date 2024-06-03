#print the frist natural numbers
for i in range(1,11):
    print(i)
 
#cualculate the sum of all elements in alist
x=[1,2,4,5,6]
sum=0
for i in x:
    sum+=i
print(sum)

#print each character of astring in a new line
new=("is this all")
for i in new:
    print(i)

#for the purpose of finding factorial of a given number
number=int(input("enter numebr: "))
count=1
prod=1
while count<=number:
    prod=prod*count
    count+=1
print(prod)


