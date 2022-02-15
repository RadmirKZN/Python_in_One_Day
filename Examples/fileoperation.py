# f = open ('my_file.txt', 'r')
# firstline = f.readline()
# secondline = f.readline()
# print (firstline)
# print (secondline)
# f.close()

# f = open ('my_file.txt', 'r')
# for line in f:
#     print (line, end = '')
# f.close()

# f = open ('my_file.txt', 'a')
# f.write('\nThis sentence will be appended.')
# f.write('\nPython is Fun!')
# f.close()

inputFile = open ( 'my_file.txt', 'r')
outputFile = open ('myoutputfile.txt', 'w')
msg = inputFile.read(10)
while len(msg):
    outputFile.write(msg)
    msg = inputFile.read(10)
inputFile.close()
outputFile.close()