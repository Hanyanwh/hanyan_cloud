from socket import socket, AF_INET, SOCK_STREAM, SOL_SOCKET, SO_REUSEADDR
from threading import Thread
import time
import _md5
import struct
import ast

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
        self.clock_flag = 0

    # 初始化信息方法
    def information_agreement(self, address, content):
        message = {"id": "SERVER", "gold_address": address, "function": "init_information", "content": content}
        return message

    # 消息处理
    def message_processing(self, address, message):
        if message["id"] == "master" and message["function"] == "init_information":
            # 请求为主控端的初始化信息请求时，回送被控端主机信息
            self.send_all(self.master, self.information_agreement(address, self.childInformation))

        elif message["id"] != "master" and message["function"] == "init_information":
            # 请求为被控端的初始化信息请求时，保留主机信息
            message["content"].update({'ip': address})
            self.childInformation.update({message["cookie"]: message['content']})

        elif message["id"] != "master" and message["function"] == "get_cookie":
            # 请求为被控端的的cookie请求时，回送cookie
            self.clock()    # 加忙等待锁
            self.childInformation.update({str(len(self.childInformation)+1): "init"})
            self.send_all(self.child_address[address], {"cookie": str(len(self.childInformation))})
            self.unclock()  # 解锁

        elif message["function"] != "init_information":
            # 其他请求交换数据
            if message["id"] == "master":
                self.send_all(self.child_address[message["gold_address"]], message)
            else:
                self.send_all(self.master, message)

    # 发送报文方法
    def send_all(self, sock, block):
        block = str(block).encode('utf-8')
        block_length = len(block)
        sock.sendall(self.heard_struct.pack(block_length))
        sock.sendall(block)

    # 接受报文方法
    def recv_all(self, sock):
        data = self.recvall(sock, self.heard_struct.size)
        (content_length,) = self.heard_struct.unpack(data)
        return ast.literal_eval(self.recvall(sock, content_length).decode('utf-8'))

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

    def clock(self):
        # 忙等待锁
        if self.clock_flag == 0:
            self.clock_flag = 1
        else:
            while self.clock_flag == 1:
                pass

    def unclock(self):
        self.clock_flag = 0

    # 持续监听
    def listen_forever(self):
        print("服务器开始工作....")

        def listen_thread():
            while True:
                client_socket, address = self.serverSocket.accept()
                message = self.recv_all(client_socket)
                if message['id'] == 'master':
                    self.master = client_socket
                else:
                    self.child_address.update({address[0]: client_socket})
                self.message_processing(address[0], message)

        threads = []
        while True:
            for thread in threads:
                if not thread.is_alive():
                    threads.remove(thread)
            while len(threads) < self.listen_num:
                child = Thread(target=listen_thread)
                child.start()
                threads.append(child)
            time.sleep(10)


if __name__ == '__main__':
    server = HanyanCloud(20)
    server.listen_forever()
