import socket
import select
import errno
import threading
import sys
import time

class readThread(threading.Thread):
    def __init__(self, username):
        threading.Thread.__init__(self)
        self.username = username
    
    def run(self):
        # print("jalankann" + self.username)
        readyok()
    

class writeThread(threading.Thread):
    def __init__(self, username):
        threading.Thread.__init__(self)
        self.username = username
        # self._running = True
    
    def run(self):
        # print("jalankann" + self.username)
        writeyok()

    # def terminate(self): 
    #     self._running = False

def readyok():
    global clientSock
    global terminate
    global thread2
    while True:
        message = input("")
        if message :
            if message.upper() == "EXIT":
                clientSock.sendto(message.encode(), (UDP_IP_ADDRESS, UDP_PORT_NO))
                terminate = True
                # thread2.terminate()
                # print(thread2._running)
                # print(thread2.is_alive())
                break

            clientSock.sendto(message.encode(), (UDP_IP_ADDRESS, UDP_PORT_NO))

def writeyok():
    global clientSock
    global terminate
    global thread2
    while True:
        if terminate == True:
            break
        try:
            while True:
                if terminate == True:
                    break
                data, addr = clientSock.recvfrom(1024)
                hasil = str(data.decode('utf-8'))
                print ("> ", hasil)
        except Exception as e:
            continue




UDP_IP_ADDRESS = "127.0.0.1"
UDP_PORT_NO = 6789
clientSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
terminate = False
clientSock.setblocking(False)

Message = input("username : ")
clientSock.sendto(Message.encode(), (UDP_IP_ADDRESS, UDP_PORT_NO))
print(f'{time.strftime("%H:%M:%S", time.localtime())} Connection accepted on {UDP_IP_ADDRESS}:{UDP_PORT_NO}...\n')
print(
    "Hello! Welcome to the Chatroom \nInstructions:\n1. Simply type the message to send broadcast to all active clients"
)
print("2. Type 'WHOSIN' without quotes to see list of active clients\n3. Type 'EXIT' without quotes to exit the chatroom\n")
threads = []

thread1 = readThread("READ INI")
thread2 = writeThread("WRITE INI")

thread1.start()
thread2.start()

# Add threads to thread list
threads.append(thread1)
threads.append(thread2)

# Wait for all threads to complete
for t in threads:
    t.join()

clientSock.close()

