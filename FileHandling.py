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


# fileStream = open("FileHandling2.txt", "a")
# fileStream.write("everyone")
# fileStream.close()

# fileStream = open("FileHandling.txt", "r+")
# data = fileStream.read()
# print(data)
# fileStream.write("\nsome new data written using r+ mode")
# fileStream.close

# fileStream = open("FileHandling2.txt", "w+")
# fileStream.write("how are you")
# fileStream.seek(0)
# data = fileStream.read()
# print(data)
# fileStream.close()

# fileStream = open("FileHandling.txt", "a+")
# fileStream.write("\nsome new data written using a+ mode")
# fileStream.seek(0)
# data = fileStream.read()
# print(data)
# fileStream.close()


fileStream = open("watch.jpeg", "rb")
data = fileStream.read(10500)
# print(data)
fileStream.close()

fileStream = open("watch-copy.jpeg", "wb")
fileStream.write(data)
fileStream.close()
