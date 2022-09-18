import socket
import threading
import getpass
myp=socket.SOCK_DGRAM
afn=socket.AF_INET 
s=socket.socket(myp,afn)
ip="172.31.7.83"
port= 4321
s.bind((ip,port))

def send():
    while True:
        yourMessg=input("")
        s.sendto(yourMessg.encode(),("13.234.120.219",1234))
        #print("             172.31.7.83" + ": "  + yourMessg)

def recv():
    while True:
        data=s.recvfrom(20)
        ClientIP=data[1][0]
        messg=data[0].decode()
        print("\n           "+ ClientIP + ": " + messg)

task1=threading.Thread(target=send)
task2=threading.Thread(target=recv)
task1.start()
task2.start()
send()
recv()

