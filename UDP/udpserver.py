import socket
import select
import time
## Here we define the UDP IP address as well as the port number that we have
## already defined in the client python script.
UDP_IP_ADDRESS = "127.0.0.1"
UDP_PORT_NO = 6789
## declare our serverSocket upon which
## we will be listening for UDP messages
serverSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
## One difference is that we will have to bind our declared IP address
## and port number to our newly declared serverSock
serverSock.bind((UDP_IP_ADDRESS, UDP_PORT_NO))
print(f'{time.strftime("%H:%M:%S", time.localtime())} Server waiting for Client on {UDP_IP_ADDRESS}:{UDP_PORT_NO}...')

clients = {}


while True :
    message, clientAddress = serverSock.recvfrom(1024)
    input_client = str(message.decode('utf-8'))
    client = clientAddress

    if client not in clients:
        clients[client] = input_client
        msg= "{} *** {} has joined the chat. ***".format(time.strftime("%H:%M:%S", time.localtime()), clients[client])
        for key in clients :
            if key != client :
                serverSock.sendto(str.encode(msg), key)
        
        print(msg)

    elif client in clients:
        if message is False or message.decode("utf-8").upper() == "EXIT" :
            msg = '{} {} left the chat.'.format(time.strftime("%H:%M:%S", time.localtime()), clients[clientAddress])
            print(msg)
            for key in clients :
                if key != client :
                    serverSock.sendto(str.encode(msg), key)
            del clients[clientAddress]
            continue
        
        if message.decode("utf-8").upper() == "WHOSIN":
            arr_client = []
            for key in clients :
                if key != client :
                    arr_client.append(clients[key])
            if len(arr_client) != 0:
                msg = "{} Group member: {}".format(time.strftime("%H:%M:%S", time.localtime()), ', '.join(map(str, arr_client)))
            else :
                msg = "{} You're Alone.".format(time.strftime("%H:%M:%S", time.localtime()))
            serverSock.sendto(str.encode(msg), client)
            continue
            
        msg = "{} {} : {}".format(time.strftime("%H:%M:%S", time.localtime()), clients[clientAddress], message.decode("utf-8"))
        for key in clients :
            if key != client :
                serverSock.sendto(str.encode(msg), key)
        
        print(msg)

            


    # modifiedMessage = message2 + " JARKOMDAT"
    # # hasil = str(modifiedMessage.decode('utf-8'))
    # serverSock.sendto(str.encode(modifiedMessage), clientAddress)
    # print("\nClient dengan request ke-", str(i))
    # print("Message dari client : ", message2)
    # print("Message hasil : ", modifiedMessage)

# while True:
#     data, addr = serverSock.recvfrom(1024)
#     print ("Message: ", data)
  