import socket
import sys
import time as t
server = "xeroxirc.net"       #settings
channel = input("channel name: ")
botnick = input("bot name: ")
username = 'botty1'
irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #defines the socket
print("connecting to:"+server)
irc.connect((server, 6667))
#connects to the server
irc.send(bytes("USER "+ botnick +" "+ botnick +" "+ botnick +" :This is a fun bot!\n", 'utf8')) #user authentication
irc.send(bytes("NICK "+ botnick +"\n", 'utf8'))
t.sleep(10)
#sets nick
irc.send(bytes("PRIVMSG nickserv :iNOOPE\r\n", 'utf8') )   #auth
irc.send(bytes("JOIN "+ channel +"\n", 'utf8')  )      #join the chan

    
while 1:    #puts it in a loop
   text=irc.recv(2040)  #receive the text
   print( text )  #print text to console
   
   if text.find(bytes('yay', 'utf8')) != -1:
      t.sleep(.1)#check if 'PING' is found
      irc.send(bytes(f'PRIVMSG {channel} :yay\r\n', 'utf8')) #returnes 'PONG' back to the server (prevents pinging out!)
   if text.find(bytes('awesome', 'utf8')) != -1:                          #check if 'PING' is found
      irc.send(bytes(f'PRIVMSG {channel} : well thats nice\r\n', 'utf8')) #returnes 'PONG' back to the server (prevents pinging out!)
   if text.find(bytes('.ping', 'utf8')) != -1:
      splitone = text.split(bytes(".ping", 'utf8'))
      splittwo = splitone[1].split(bytes(" ", 'utf8'))
      for x in range(int(splittwo[1])):
         print(splittwo)
         print("#"*10)
         print(splitone)
         irc.send(bytes(f'PRIVMSG {channel} : {splittwo[2]}\r\n', 'utf8')) #returnes 'PONG' back to the server (prevents pinging out!)
   
   
