# fileStream = open("FileHandling.txt")
# data = fileStream.read()
# print(data)

# data = fileStream.readline()
# print(data)
# data = fileStream.readline()
# print(data)
# data = fileStream.readline()
# print(data)
# data = fileStream.readline()
# print(data)
# data = fileStream.readline()
# print(data)

# print(fileStream.read(50))
# fileStream.close()


# fileStream = open("FileHandling2.txt", "w")
# fileStream.write("hello python")
# fileStream.close()


fileStream = open("FileHandling2.txt", "a")
fileStream.write("everyone")
fileStream.close()
