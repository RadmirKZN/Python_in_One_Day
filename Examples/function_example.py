# def checkIfPrime (numberToCheck):
#     for x in range(2, numberToCheck):
#         if (numberToCheck%x == 0):
#             return False
#     return True
#
# checkIfPrime(1)
# answer = checkIfPrime(12)
# print(answer)

# def someFunction(a, b, c=1, d=2, e=3):
#     print(a, b, c, d, e)
#
# someFunction(10, 20, 30, 40, 50)

# def addNumbers(*num):
#     sum = 0
#     for i in num:
#         sum = sum + i
# print(sum)
#
# addNumbers(1, 2, 3, 4, 5)

def printMemberAge(**age):
    for i, j in age.items():
        print("Name = %s, Age = %s" %(i, j))

printMemberAge(Peter = 5, John = 7)

printMemberAge(Peter = 5, John = 7, Yvonne = 10)