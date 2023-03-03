import paramiko

# Set up SSH client
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# Connect to remote server
hostname = "example.com"   #insert hostname
username = "myusername"    #insert username
password = "mypassword"    #insert password

ssh.connect(hostname, username=username, password=password)

# Execute a command on the remote server
stdin, stdout, stderr = ssh.exec_command("ls")

# Read the output of the command
output = stdout.read().decode("utf-8")
print(output)

# Close the SSH connection
ssh.close()
