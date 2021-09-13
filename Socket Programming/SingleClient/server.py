# server
import socket
import pandas as pd
df = pd.read_csv("Stationary.csv")
filename = "Stationary.csv"
port = 60000                   
s = socket.socket()            
host = socket.gethostname()    
s.bind((host, port))           
s.listen(10)
print ('Server listening....')
while True:
    clt, adr = s.accept()
    print(df)
    print ('Got connection from', adr)
    n = clt.recv(1024).decode("utf-8")
    if n == 'I':
        a = clt.recv(1024).decode("utf-8")
        b = int(a)
        while b > 0:
            Date = clt.recv(1024).decode("utf-8")
            productid = clt.recv(1024).decode("utf-8")
            quantity = clt.recv(1024).decode("utf-8")
            cost = clt.recv(1024).decode("utf-8")
            list1=  [[Date, productid, quantity, cost]]
            df = pd.DataFrame(list1, columns =['Date','productid','Quantity','cost'])
            df.to_csv('Stationary.csv', mode='a', index=False, header=False)
            b = b-1
    elif n == 'V':
        clt.send(filename.encode("utf-8"))        
    elif n == 'M':
        #print(df.dtypes)
        df['Totalcost'] = df['Quantity']*df['cost']
        df.to_csv('Stationary.csv', mode='w', index=False, header=True)
    elif n == 'U':
        df['Category'] = df['Totalcost'].apply(lambda x: 'A' if x <= 1000 and x>=1 else ('B' if x>1000 else 'NaN'))       
        df.to_csv('Stationary.csv', mode='w', index=False, header=True)
    elif n == 'F1':
        clt.send(filename.encode("utf-8"))
    elif n == 'F2':
        clt.send(filename.encode("utf-8"))        
    clt.close()


