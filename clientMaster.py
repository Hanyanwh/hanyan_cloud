from socket import socket, AF_INET, SOCK_STREAM
from PyQt5 import QtGui, QtWidgets, Qt
import requests
import CouldUi
import struct
import threading
import os
import time
import ast
import sys

SERVER = '148.70.105.33'
POST = 52527
SUCCESSFUL_LINK_SERVER = 1
NO_NETWORK = 2
UNABLE_CONNECT_SERVER = 3
LINK_PC = 4

INIT_INFORMATION = 'init_information'


class HanyanCould(CouldUi.MainUi):
    def __init__(self):
        super().__init__()
        self.host = '127.0.0.1'
        self.child_address = {}
        self.child_onlink = []
        self.heard_struct = struct.Struct('!I')
        self.status = SUCCESSFUL_LINK_SERVER
        self.clientSocket = socket(AF_INET, SOCK_STREAM)
        self.connect_server()
        self.ping()
        self.child_online = []

    # 初始化数据
    def get_information(self):
        self.send_all(SERVER, INIT_INFORMATION)
        message = self.recv_all()
        print(message)
        self.host = message["gold_address"]
        cookie = message["content"].keys()
        host_information = {}
        for _cookie in cookie:
            self.child_address.update({message["content"][_cookie]['ip']: _cookie})
            ip_info = ast.literal_eval(requests.get("http://ip.taobao.com/service/getIpInfo.php?ip={}".
                                                    format(message["content"][_cookie]['ip'])).text)["data"]
            pc_info = message["content"][_cookie]["data"]
            info = [_cookie, ip_info['country'], ip_info['region']+ip_info['city'], ip_info['ip'], ip_info['isp'],
                    "离线", pc_info['time'], pc_info['username'], pc_info['homename'], pc_info['System'],
                    pc_info['disk'], pc_info['memory'], pc_info['cpu']]
            host_information.update({_cookie: info})
            self.addTable(int(_cookie), info)

    # 设置连接状态
    def set_status(self):
        if self.status == SUCCESSFUL_LINK_SERVER:
            self.right_server_label.setPixmap(QtGui.QPixmap('./resource/img/cloud.png'))
            self.right_state_report_text.setText("已连接到服务器")
            self.right_state_information_text.setText("服务器IP:  {}\n"
                                                      "本机IP:  {}\n".format(SERVER, self.host))
        elif self.status == NO_NETWORK:
            self.right_server_label.setPixmap(QtGui.QPixmap('./resource/img/break.png'))
            self.right_state_report_text.setText("无网络")
            self.right_state_information_text.setText("服务器IP:  {}\n"
                                                      "本机IP:  {}\n".format(SERVER, self.host))
        elif self.status == UNABLE_CONNECT_SERVER:
            self.right_server_label.setPixmap(QtGui.QPixmap('./resource/img/break.png'))
            self.right_state_report_text.setText("远程服务器拒绝连接")
            self.right_state_information_text.setText("服务器IP:  {}\n"
                                                      "本机IP:  {}\n".format(SERVER, self.host))
        elif self.status == LINK_PC:
            self.right_server_label.setPixmap(QtGui.QPixmap('./resource/img/server.png'))
            self.right_controlled_label.setPixmap(QtGui.QPixmap('./resource/img/computer.png'))
            self.right_state_report_text.setText("已于被控端建立连接")

    # 连接服务器(初始化数据)
    def connect_server(self):
        def daemon_thread():
            while True:
                try:
                    self.clientSocket.connect((SERVER, POST))
                    self.status = SUCCESSFUL_LINK_SERVER
                    self.get_information()
                    break
                except ConnectionRefusedError as e:
                    self.status = UNABLE_CONNECT_SERVER
                    print(e)
                except OSError as e:
                    print(e)
                    self.status = NO_NETWORK
                finally:
                    self.set_status()
                    time.sleep(5)

        link = threading.Thread(target=daemon_thread)
        link.setDaemon(True)
        link.start()

    # 检验存活
    def ping(self):
        def daemon_thread():
            while True:
                child_online = []
                for _ip in list(self.child_address.keys()):
                    command = 'ping -n 1 %s' % _ip
                    result = os.system(command)
                    if not result:
                        child_online.append(_ip)
                        newItem = QtWidgets.QTableWidgetItem("在线")
                        newItem.setForeground(Qt.QBrush(Qt.QColor(0, 191, 255)))
                        self.right_information_table.setItem(self.child_address[_ip]-1, 5, newItem)
                    else:
                        newItem = QtWidgets.QTableWidgetItem("离线")
                        self.right_information_table.setItem(int(self.child_address[_ip]) - 1, 5, newItem)
                self.child_online = child_online
                time.sleep(60)

        link = threading.Thread(target=daemon_thread)
        link.setDaemon(True)
        link.start()

    def information_agreement(self):
        message = {"id": "master", "gold_address": SERVER,
                   "function": "init_information", "content": ""}
        return message

    def main_agreement(self, gold_address, _function, content):
        _id = "master"
        message = {"id": _id, "gold_address": gold_address,
                   "function": _function, "content": content}
        return message

    # 发送报文方法
    def send_all(self, gold_address, _function, content={}):
        block = str(self.main_agreement(gold_address, _function, content)).encode('utf-8')
        block_length = len(block)
        self.clientSocket.sendall(self.heard_struct.pack(block_length))
        self.clientSocket.sendall(block)

    # 接受报文方法
    def recv_all(self):
        data = self.recvall(self.heard_struct.size)
        (content_length,) = self.heard_struct.unpack(data)
        return ast.literal_eval(self.recvall(content_length).decode('utf-8'))

    # 接受定长报文
    def recvall(self, length):
        blocks = []
        while length:
            block = self.clientSocket.recv(length)
            if not block:
                raise EOFError('socket closed with %d bytes left in this content'.format(length))
            length -= len(block)
            blocks.append(block)
        return b''.join(blocks)


def main():
    app = QtWidgets.QApplication(sys.argv)
    gui = HanyanCould()
    gui.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
