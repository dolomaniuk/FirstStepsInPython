import os

from builtins import print

f = open("myfile", "w")
f.write("First line with necessary newline character\n")
f.write("Second line to write to the file\n")
f.close()
f = open("myfile")
line1 = f.readline()
line2 = f.readline()
f.close()
print(line1, line2)
print(os.getcwd())
# os.chdir(os.path.join("c:", "Users", "User", "PycharmProjects", "test"))

filename = os.path.join("c:\\", "Users", "User", "PycharmProjects", "test", "myfile")
print(filename)
f= open(filename, "r")
print(f.readline())
f.close()
