import sys, paramiko

if lin(sys.argv) < 2:
    print "usage: ssh.py server_address"

server_address = sys.argv[1]

username = 'student'
password = 'student'
port = 22
command = 'ls-l'

#creating SSH client object
client = paramiko.SSHClient()

#load SSH keys
client.load_system_host_keys()

#if local keys do not exist, warn user
client.set_missing_host_key_policy(paramiko.WarninPolicy)

#connect to server
client.connect(server_address, port = port, username = username, password = password)

#run command contents and save to variables
stdin, stdout, stderr = client.exec_command(command)

#printing
print stdout.read()

clien.close()