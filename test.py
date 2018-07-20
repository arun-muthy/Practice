test = 3/2
print(test)
t = "bye"
s = "hello"
print(s[::2])   #grad elements in step size of 2

s = s + 'lol'
print(s)  #concatenate / can do the same with lists

print("it is: %s,%s " ,s,t)  #attach variables to a string


x = 156.43
print('floating point number: %2.4f' %x) #insert floating point number

print("what did you say {},{}".format(x,s)) #print format


mylist = [1,2,3]
print(mylist)

mylist.remove(mylist[2])

print(mylist)

#tuples are immutable / mix object types


list = [x**2 for x in range(11)]  #list comprehension
print(list)

def vat(s):
    tax = s *15/100
    print("VAT:", tax)
    print("Net", s - tax)


vat(1300)
