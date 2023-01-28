import time,socket,sys

print("\n Welcome to chat Room...")
print("Loading....")

time.sleep(1)

s=socket.socket()

host=socket.gethostname()
ip=socket.gethostbyname(host)

port=1234

s.bind((host,port))
print(host,"(",ip,")\n")

name=input(str("Enter the name"))

s.listen(1)

print("\n...Waiting for the Connection,....")

conn,addr=s.accept()

print("Receviced from Connection From",addr[0],"(",addr[1])

s_name=conn.recv(1024)

s_name=s_name.decode()

print(s_name,"has connected to the chatRoom")

conn.send(name.encode())

while True:
    message=input(str("Me : "))
    conn.send(message.encode())
    message=conn.recv(1024)
    message=message.decode()
    print(s_name,":",message)