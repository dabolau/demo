import os

from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer


def main():
    # 实例化一个虚拟授权者来管理“虚拟”用户
    authorizer = DummyAuthorizer()

    # 定义一个拥有完整权限的新用户
    authorizer.add_user('dabolau', '123456', '.', perm='elradfmwMT')
    # 匿名用户
    authorizer.add_anonymous(os.getcwd())

    # 实例化FTP处理程序类
    handler = FTPHandler
    handler.authorizer = authorizer

    # 定义一个自定义的横幅（客户端连接时返回的字符串）
    handler.banner = 'pyftpdlib based ftpd ready.'
    # 指定一个伪装的地址和端口范围使用被动连接
    # 如果你在一个NAT后面去分解
    # handler.masquerade_address = '151.25.42.11'
    # handler.passive_ports = range(60000, 65535)

    # 实例化FTP服务器类并在0.0.0.0:2121上监听
    address = ('', 2121)
    server = FTPServer(address, handler)

    # 设置连接限制
    server.max_cons = 256
    server.max_cons_per_ip = 5

    # 启动FTP服务器
    server.serve_forever()


if __name__ == '__main__':
    print(os.getcwd())
    main()
