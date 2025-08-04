from SshToServer import SshToServer
import time
my_ssh = SshToServer(r"C:\Users\edrik_cgifjkr\Desktop\Course_4_CLOUD_TECHNOLOGY\my_key_pair.pem", "16.171.171.26", "ubuntu")
result = my_ssh.runRemoteCommand("date")
stdout, stderr = my_ssh.runRemoteCommand("asdasdsa")
#print(stdout, stderr)

print(my_ssh.result_of_command("date"))
time.sleep(3)
print(my_ssh.result_of_command("13232"))
time.sleep(3)
print(my_ssh.result_of_command("server"))
