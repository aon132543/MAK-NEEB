import socket
from _thread import *
import sys

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server = 'localhost'
port = 5556

server_ip = socket.gethostbyname(server)

try:
    s.bind((server, port))

except socket.error as e:
    print(str(e))

s.listen(2)
print("[loginserver] : Waiting for a connection")

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
                if arr[1] == "len" :
                    if len(listcon) == 2:
                        reply = "1"
                    else:
                        reply = "0"                   
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
    #print(len(listcon))
    #print("Connected to: ", addr)
    #threaded_client(conn)
    start_new_thread(threaded_client, (conn,))
