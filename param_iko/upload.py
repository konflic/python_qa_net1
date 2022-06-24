import os
import paramiko

from config import HOST

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(HOST, key_filename=os.path.expanduser("~/.ssh/otus"))

sftp = ssh.open_sftp()
sftp.put("config.yml", "config_with_empty_line.yml")

ssh.close()
