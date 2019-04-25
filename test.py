from socket import socket, AF_INET, SOCK_STREAM, SOL_SOCKET, SO_REUSEADDR
import subprocess
import struct
import time
import json

PORT = 52527


class HanyanCloud:
    def __init__(self, listen_num):
        self.serverSocket = socket(AF_INET, SOCK_STREAM)
        self.serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        self.serverSocket.bind(('', PORT))
        self.listen_num = listen_num
        self.serverSocket.listen(listen_num)
        self.master = socket()
        self.child_address = {}
        self.childInformation = {}
        self.child_online = []
        self.heard_struct = struct.Struct('!I')

    # 检验存活
    def ping(self):
        while True:
            time.sleep(5*60)
            child_online = []
            ip = list(self.child_address.keys())
            file = open('/dev/null', 'w')
            for _ip in ip:
                command = 'ping -c 3 -W 1 %s' % ip
                result = subprocess.call(command,
                                         shell=True, stdout=file, stderr=file)
                if not result:
                    child_online.append(_ip)
            self.child_online = child_online
            file.close()

    # 初始化信息方法
    def information_agreement(self, content):
        message = {"id": "SERVER","function": "init_information", "content": content}
        return message

    # 消息处理
    def message_processing(self, address, message):
        if message["id"] == "master" and message["function"] == "init_information":
            self.send_all(self.master, self.information_agreement(self.childInformation))
        elif message["id"] != "master" and message["function"] == "init_information":
            self.childInformation.update({address[0]: message['content']})
        elif message["function"] != "init_information":
            if message["id"] == "master":
                self.send_all(self.child_address[message["gold_address"]], message)
            else:
                self.send_all(self.master, message)

    # 发送报文方法
    def send_all(self, sock, block):
        block = str(block).encode('utf-8')
        block_length = len(block)
        sock.sendall(block_length)
        sock.sendall(block)

    # 接受报文方法
    def recv_all(self, sock):
        data = self.recvall(sock, self.heard_struct.size)
        (content_length,) = self.heard_struct.unpack(data)
        return self.recvall(sock, content_length).decode('utf-8')

    # 接受定长报文
    def recvall(self, sock, length):
        blocks = []
        while length:
            block = sock.recv(length)
            if not block:
                raise EOFError('socket closed with %d bytes left in this content'.format(length))
            length -= len(block)
            blocks.append(block)
        return b''.join(blocks)

    # 持续监听
    def listen_forever(self):
        print("服务器开始工作....")
        while True:
            client_socket, address = self.serverSocket.accept()
            message = self.recv_all(client_socket)
            if message['id'] == 'master':
                self.master = client_socket
            else:
                self.child_address.update({address[0]: client_socket})
            print(message)


server = HanyanCloud(20)
server.listen_forever()

