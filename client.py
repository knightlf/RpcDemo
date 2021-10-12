from xmlrpc.client import ServerProxy
import xmlrpc.client

# def testnodes():
#     #远程 公网地址调用，后续部署后， 可以改为内网192.168.1.99
#     server = ServerProxy("http://148.153.164.186:8881", allow_none=True)
#     # 参数为要执行的交易节点，id:  1-6
#     # bsc99 高性能节点,bsc92 低性能节点
#     # 增加快速节点2
#     addbsc99_res = server.AddBscNode("2", "bsc99")
#     print(addbsc99_res)
#     # 删除慢速节点1
#     delbsc92_res = server.DelBscNode("1", "bsc92")
#     print(delbsc92_res)
#     # 建立bsc慢链
#     addbsc92_res = server.AddBscAll("bsc92")
#     print(addbsc92_res)
#     # 删除bsc快链
#     delbsc99_res = server.DelBscAll("bsc99")
#     print(delbsc99_res)


if __name__ == '__main__':
    # 远程 公网地址调用，后续部署后， 可以改为内网192.168.1.99
    server = ServerProxy("http://148.153.164.186:8881", allow_none=True)
    # 参数为要执行的交易节点，node:  1-6  type: polygon bsc
    # logs_res = server.Getnodelogs("1","polygon")
    # bsc99 高性能节点,bsc92 低性能节点
    # logs_res = server.Getnodelogs("1", "bsc99")
    # print(logs_res)
    # print("*" * 100)
    # # 参数为要执行的交易节点，node:  1-6
    #transaction_res = server.Transaction("1", "bsc92")
    # # if res.returncode!=0:
    # #     res = "node exec faild!"
    # #     print(res)
    #print(transaction_res)

    # delbsc92_res = server.DelBscAll("bsc92")
    # print(delbsc92_res)

    # addbsc92_res = server.AddBscAll("bsc92")
    # print(addbsc92_res)

    # delbsc92_res = server.DelBscNode("1", "bsc92")
    # print(delbsc92_res)

    # delbsc92_res = server.DelBscNode("2", "bsc92")
    # print(delbsc92_res)

    addbsc92_res = server.AddBscNode("2", "bsc99")
    print(addbsc92_res)
