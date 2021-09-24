# _*_ coding:utf-8 _*_

from xmlrpc.server import SimpleXMLRPCServer
from socketserver import ThreadingMixIn
import xmlrpc.client
import subprocess

class ThreadXMLRPCServer(ThreadingMixIn, SimpleXMLRPCServer):
    pass

"""
:arg1 交易节点  only 1-6
转账单次执行操作
"""
def Transaction(node):
    cmd="kubectl exec -it bsc-sts-%s-0 -- Transaction Auto" % node
    result = subprocess.run(cmd, shell=True, timeout=30,
                             stderr=subprocess.PIPE,
                             stdout=subprocess.PIPE)
    #result = subprocess.run(cmd, shell=True, timeout=30)
    # 若执行成功，则returncode为0；若执行失败，则returncode为1；
    if result.returncode!=0:
        res="node exec faild!"
        return res
    #return str(result.stdout)
    return result.stdout

"""
:arg1 交易节点  only 1-6
:arg2 type: polygon  bsc必须满足type类型
获取当前节点执行的日志，最新5行
"""
def Getnodelogs(node,type):
    if type=="bsc":
        cmd="kubectl logs --tail=5 bsc-sts-%s-0 " % node
    elif type=="polygon":
        cmd = "kubectl logs --tail=5 polygon-sts-%s-0 " % node
    else:
        return "type input err!"

    result = subprocess.run(cmd, shell=True, timeout=30,
                             stderr=subprocess.PIPE,
                             stdout=subprocess.PIPE)
    #result = subprocess.run(cmd, shell=True, timeout=30)
    # 若执行成功，则returncode为0；若执行失败，则returncode为1；
    if result.returncode!=0:
        res="node exec faild!"
        return res
    #return str(result.stdout)
    return result.stdout

if __name__ == '__main__':
    # 初始化
    server = ThreadXMLRPCServer(('0.0.0.0', 8881), allow_none=True)
    # 注册交易转账函数
    server.register_function(Transaction, "Transaction")
    # 注册get logs func
    server.register_function(Getnodelogs, "Getnodelogs")

    print("Listening for Client")
    # 保持等待调用状态
    server.serve_forever()

