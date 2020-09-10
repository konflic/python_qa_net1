import paramiko

HOST = "192.168.1.75"

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(HOST, username="ubuntu", port=22)
stin, stout, ster = ssh.exec_command("touch file.py")
stin, stout, ster = ssh.exec_command("ls -la")
print(stout.read().decode("utf-8"))

if ssh is not None:
    # https://github.com/paramiko/paramiko/issues/1078
    ssh.close()
    del ssh, stin
