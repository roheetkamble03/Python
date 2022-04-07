i = 0
j = 5
name = "Rohit";
lastName = "Kamble";
print (i < j and i == 0)
print (name, lastName, "Test")
print (name + lastName)
print (name + " " + lastName)
print ("R" in name)


number = '10'
print ("Changing data type from string to int:",int(number))

print 5.0**3

integer = 10
floatNumber = 10.5
complexNumber = 23 + 43j
setType = {33, 45, 'Rohit'}
listType = [1, 45, 11, 12.34]
listType[3] = "Rohit"

tupleType = (12, 34, "Rohit")
dictionary = {"key":"value", "2":12, 22:"rohit"}
print ("printing dictionary[22]:"+dictionary[22])
print dictionary
print dictionary.keys()
print dictionary.values()

print (type(integer))
print (type(floatNumber))
print (type(complexNumber))
print (setType,type(setType))
print (type(listType))
print (type(tupleType))
print (type(dictionary))

# inputOne = eval(input("Value1:"))
# inputTwo = eval(input("Value2:"))
# print (inputOne+inputTwo)

longList = [1, "Rohit", "test", 2.22, 13232143243L, 23+55J]
smallList = [3, "smallList"]

print longList[0:10]
print len(longList)
