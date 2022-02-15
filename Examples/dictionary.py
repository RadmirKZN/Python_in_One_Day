myDict = {"One":1.35, 2.5:"Two point Five", 3:"+", 7.9:2}
print(myDict)

print(myDict["One"])

print(myDict[7.9])

myDict[2.5] = "Two and a Half"
print(myDict)

myDict["New item"] = "I'm new"
print(myDict)

del myDict["One"]
print(myDict)

