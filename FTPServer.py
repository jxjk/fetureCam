from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer
import os

def main():
    # 实例化一个虚拟用户管理器
    authorizer = DummyAuthorizer()

    # 添加一个用户，用户名为 "user"，密码为 "12345"，主目录为当前目录
    authorizer.add_user('CNC', 'CNC', '.', perm='elradfmwMT')

    # 添加一个匿名用户，主目录为当前目录
    authorizer.add_anonymous(os.getcwd())

    # 实例化 FTP 处理器，并将虚拟用户管理器绑定到处理器
    handler = FTPHandler
    handler.authorizer = authorizer

    # 指定监听地址和端口
    address = ('0.0.0.0', 21)

    # 实例化 FTP 服务器
    server = FTPServer(address, handler)

    # 设置最大连接数
    server.max_cons = 256
    server.max_cons_per_ip = 5

    # 启动 FTP 服务器
    server.serve_forever()

if __name__ == '__main__':
    main()