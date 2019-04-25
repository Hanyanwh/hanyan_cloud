import wmi
import socket
import getpass
import datetime
"""
    被控端各项功能的实现模块
    
"""


class SystemInfo:
    def __init__(self):
        self.c = wmi.WMI()

    # 获取操作系统版本
    def get_sys_version(self):
        version = ""
        for sys_info in self.c.Win32_OperatingSystem():
            version = sys_info.Caption + sys_info.OSArchitecture
        return version

    # 获取CPU类型
    def get_cpu(self):
        cpu = ""
        for processor in self.c.Win32_Processor():
            cpu = processor.Name.strip()
        return cpu

    # 获取内存大小
    def get_mem(self):
        memory = ""
        for Memory in self.c.Win32_PhysicalMemory():
            memory = str(int(Memory.Capacity) / 1048576.0)+"MB"
        return memory

    # 获取硬盘大小
    def get_disk_info(self):
        disk = ""
        for physical_disk in self.c.Win32_DiskDrive():
            disk = disk + physical_disk.Caption + ": " + str(int(int(physical_disk.Size)/1024/1024/1024)) + "GB  "
        return disk

    # 获取用户名
    def get_username(self):
        return getpass.getuser()

    # 获取主机名
    def get_home_name(self):
        return socket.gethostname()

    # 获取当前时间
    def get_time(self):
        return datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

