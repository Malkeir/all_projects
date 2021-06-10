# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1024))
s.listen(5)

while(True):
    clt, adr=s.accept()
    print(f"connection to {adr} established")
    clt.send(bytes("socket programming in python" , "utf-8"))

#
#this is a comment to just update git real quick
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
