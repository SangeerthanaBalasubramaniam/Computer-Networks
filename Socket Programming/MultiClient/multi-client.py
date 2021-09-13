import socket
import json
import pandas as pd
PORT = 5055
FORMAT = 'utf-8'
HOST = socket.gethostbyname(socket.gethostname())
ADDR = (HOST, PORT)
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

print("Enter the operation \n I for Insert or Add employee \n V for View \n D1 for display employee details using ID \n C for changing value of a cell")
value=str(input())
#print(value)
client.send(value.encode(FORMAT))

if value == 'I':
            Name = input("Enter name: ")
            client.send(Name.encode(FORMAT))
            eID = input("Enter id: ")
            client.send(eID.encode(FORMAT))
            Gender = input("Enter Gender: ")
            client.send(Gender.encode(FORMAT))
            DateOfhire = input("Enter Date: ")
            client.send(DateOfhire.encode(FORMAT))
            EmployementStatus = input("Enter status: ")
            client.send(EmployementStatus.encode(FORMAT))
            Position = input("Enter Position: ")
            client.send(Position.encode(FORMAT))
elif value == 'V':
    filename = client.recv(1024).decode(FORMAT)
    df = pd.read_csv(filename)
    print(df)
elif value == 'D1':
    filename = client.recv(1024).decode(FORMAT)
    df = pd.read_csv(filename)
    eID = input("Enter id: ")
    print(df.loc[df['eID'] == eID])
elif value == 'C':
    x = input("Enter the column name: ")
    client.send(x.encode(FORMAT))
    y = input("Enter the employee ID: ")
    client.send(y.encode(FORMAT))
    z = input("Enter the value to be assigned to column of that employee: ")
    client.send(z.encode(FORMAT))
    
    
    
