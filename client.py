from xmlrpc.client import ServerProxy
import xmlrpc.client

if __name__ == '__main__':
    #远程 公网地址调用，后续部署后， 可以改为内网192.168.1.99
    server = ServerProxy("http://148.153.164.186:8881", allow_none=True)
    # 参数为要执行的交易节点，node:  1-6  type: polygon bsc
    #logs_res = server.Getnodelogs("1","polygon")
    logs_res = server.Getnodelogs("1", "bsc")
    print(logs_res)
    print("*"*100)
    #参数为要执行的交易节点，node:  1-6
    transaction_res=server.Transaction("1")
    # if res.returncode!=0:
    #     res = "node exec faild!"
    #     print(res)
    print(transaction_res)





