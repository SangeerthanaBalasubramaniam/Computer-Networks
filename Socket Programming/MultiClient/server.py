import socket
import threading
import pandas as pd
import json
PORT = 5055
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

df = pd.read_csv('HRcsv.csv')

def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")
    value = conn.recv(1024).decode(FORMAT)
    print(" ", value)
    if value == 'I':
        Name = conn.recv(1024).decode(FORMAT)
        eID = conn.recv(1024).decode(FORMAT)
        Gender = conn.recv(1024).decode(FORMAT)
        DateOfhire = conn.recv(1024).decode(FORMAT)
        EmployementStatus = conn.recv(1024).decode(FORMAT)
        Position = conn.recv(1024).decode(FORMAT)
        list1=  [[Name, eID, Gender, DateOfhire,EmployementStatus, Position]]
        df = pd.DataFrame(list1, columns =['Name','eID', 'Gender','DateOfhire', 'EmployementStatus','Position'])
        df.to_csv('HRcsv.csv', mode='a', index=False, header=False)        
    elif value == 'V' or value == 'D1':
        conn.send("HRcsv.csv".encode(FORMAT))
    elif value == 'C':
        df1 = pd.read_csv('HRcsv.csv')
        x = conn.recv(1024).decode(FORMAT)
        y = conn.recv(1024).decode(FORMAT)
        z = conn.recv(1024).decode(FORMAT)
        index = int(df1[df1["eID"]==y].index.values)
        df1.loc[index,x] = z
        df1.to_csv('HRcsv.csv', mode='w', index=False, header=True)                     

    conn.close()
    
def start():
    server.listen()
    print(f"[LISTENING] Server----listening on {SERVER}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")

print("[STARTING] server---starting...")
start()
