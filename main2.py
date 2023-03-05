import socket
def portScan(targethost,targetport):
    try:
         sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #socket.socket objesi 2 parametre albiliyor. AF_INET TCP ve UDP için IPv4 protokolleri SOCK_STREAM: TCP bağlantı tipi anlamina geliyor
         sock.connect((targethost, targetport)) #ip ve portu connect objesiyle cekiyoruz.
         print(f"{targetport} =>> Open ")#portlar aciksa open ciktisini veriyor.
    except:
         print(f"{targetport} =>> Close")#degilse close ciktisini veriyor.
    finally:
         sock.close()

portScan("google.com",443)