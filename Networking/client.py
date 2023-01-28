import time,socket,sys

print("\n Welcome to chat Room...")
print("Loading....")

time.sleep(1)

s=socket.socket()

shost=socket.gethostname()
ip=socket.gethostbyname(shost)

port=1234
print(shost,"(",ip,")\n")

host=input(str("Enter the Address to connect..."))
name=input(str("Enter your name.."))

print("\n  trying to connect ",host)
time.sleep(1)

s.connect((shost,port))
print("Connected...")
s.send(name.encode())
s_name=s.recv(1024)

s_name=s_name.decode()

print(s_name,"joined to the chat Box...")

while True:
    message=s.recv(1024)
    message= message.decode()
    print(s_name,":",message)
    message=input(str("Me: "))
    s.send(message.encode())












