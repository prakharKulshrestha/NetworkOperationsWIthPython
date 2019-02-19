import socket


mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('wiki.python.org', 80))
cmd = 'GET https://wiki.python.org/moin/ HTTP/1.0\r\n\r\n'.encode()
handler=mysock.send(cmd)


while True:
	data=mysock.recv(512)
	if len(data)<1:
		break
	print (data.decode())
	
mysock.close()
