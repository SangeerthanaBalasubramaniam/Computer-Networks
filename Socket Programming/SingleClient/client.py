# client
import socket
import pandas as pd
s = socket.socket()             
host = socket.gethostname()    
port = 60000          
s.connect((host, port))
n = input("Insertion-I, Modification-M, View-V, Update-U,\nDisplay product details-F1, Stock Details-F2: ")
s.send(n.encode("utf-8"))
if n == 'I':
    a = int(input("How many records should be inserted? "))
    s.send(str(a).encode("utf-8"))
    while a > 0:
            Date = input("Enter date: ")
            s.send(Date.encode("utf-8"))
            productid = input("Enter productid: ")
            s.send(productid.encode("utf-8"))
            quantity = input("Enter quantity: ")
            s.send(quantity.encode("utf-8"))
            cost = input("Enter cost: ")
            s.send(cost.encode("utf-8"))
            a = a - 1
elif n == 'V':
    filename = s.recv(1024).decode("utf-8")
    df = pd.read_csv(filename)
    print(df)        
elif n == 'F1':
    filename = s.recv(1024).decode("utf-8")
    df = pd.read_csv(filename)
    pid = input("Enter productId: ")
    print(df.loc[df['productid'] == pid])
elif n=='F2':
    date = input("Enter Date: ")
    filename = s.recv(1024).decode("utf-8")
    df = pd.read_csv(filename)
    g = df.groupby('Date')
    print(g.get_group(date))
