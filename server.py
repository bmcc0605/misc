#Bob

from socket import *
from Crypto.Cipher import AES
from Crypto import Random
from methods import *
from random import getrandbits
import sys

s = socket()
host = gethostname()
port = 8001
s.bind((host, port))

#private key NOTE: WIKI CLAIMS 1 <= a <= q-1
a = getrandbits(32)

#defined constants
p = 4094027087
q = 2047013543
g = 1659252438 #alpha

print "Starting server on host", host
s.listen(0)

while True:
	c, addr = s.accept()
	
	c.send(str(g))
	print "Sent alpha"
	beta = square_and_multiply(g, a, p)
	c.send(str(beta))
	print "sent beta"

	y1 = int(c.recv(port))
	print "recieved y1: ",y1

	y2 = square_and_multiply(y1, a, p)
	print "Y2: ",y2

	#y1 = c1, y2 = s
	ciphertext = int(c.recv(port))
	print "Ciphertext: ", ciphertext

	#find inverse of s
	x = (ciphertext * modinv(y2, p)) % p
	print "1: ", x
	x = square_and_multiply(ciphertext, modinv(y2, p), 1)
	print "2: ", x

	#cipher = AES.new(key, AES.MODE_CFB, iv)
	#message = cipher.decrypt(c.recv(8001))

	#print message
	c.close()


#alpha = 'public base', or 'a' in the video
#a = 'r'
#k = 
#exchange 
