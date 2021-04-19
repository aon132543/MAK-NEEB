import socket
from _thread import *
import sys

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server = 'localhost'
port = 5555

server_ip = socket.gethostbyname(server)

try:
    s.bind((server, port))

except socket.error as e:
    print(str(e))

s.listen(2)
print("Waiting for a connection")

currentId = "0"
pos = ["0:50,50", "1:100,100"]
listcon = []

lst = "None"
turn = "0"
yes = "yes"
no = "no"
state ="1"
def threaded_client(conn):
    global currentId, pos,turn,lst,state
    conn.send(str.encode(currentId))
    currentId = "1"
    reply = ''
    while True:
        #print(turn)
        try:
            data = conn.recv(2048)
            reply = data.decode('utf-8')
            if not data:
                conn.send(str.encode("Goodbye"))
                break
            else:
                #print("Recieved: " + reply)
                arr = reply.split(":")
                id = int(arr[0])
                #print("ID :",id)
                #pos[id] = reply
                if arr[1] == "request" :
                    if str(id) == turn:
                        reply = "1"
                    else:
                        reply = "0"
                
                elif arr[1] == "get":
                    if reply != "None":
                        #print(lst)
                        reply = lst
                    else:
                        reply = "None"
                elif arr[1] == "clear":
                    lst = "None" 
                
                elif arr[1] == "turnnow":
                    reply = turn
                elif arr[1] == "move":
                    lst=arr[2]
                    #print(lst)
                    state ="2"
                    reply = lst
                    if turn == "1":
                        turn = "0"
                        print(lst)
                        print("Change Turn")
                    else:
                        turn = "1"
                        print(lst)
                        print("Change Turn")                            
                #reply = pos[nid][:]
                #print("Sending: " + reply)

            conn.sendall(str.encode(reply))
        except:
            break

    print("Connection Closed")
    conn.close()

while True:
    conn, addr = s.accept()
    listcon.append(conn)
    print(len(listcon))
    print("Connected to: ", addr)
    #threaded_client(conn)
    start_new_thread(threaded_client, (conn,))