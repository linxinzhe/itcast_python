import socket

dest = ("<broadcast>", 7788)  # 用<broadcast>，系统帮你判断并替换成真正广播IP  
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

s.sendto("Hi", dest)

print("等待对方恢复（按ctrl+c退出）")

while True:
    (buf, address) = s.recvfrom(2048)
    print("Received from %s: %s".format(address, buf))
