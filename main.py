# _*_ coding:utf-8 _*_

from xmlrpc.server import SimpleXMLRPCServer
from socketserver import ThreadingMixIn
import xmlrpc.client
import subprocess
from lib.nodes_opt import OpsNodes
import lib.nodes_opt


class ThreadXMLRPCServer(ThreadingMixIn, SimpleXMLRPCServer):
    pass


def AddBscNode(id, type):
    """
    :param node: ops the node id
    :param type: bsc99 or bsc92
    :return:
    """
    ops = OpsNodes()
    res = ops.addone(id, type)
    return res


def DelBscNode(id, type):
    """
    :param node: ops the node id
    :param type: bsc99 or bsc92
    :return:
    """
    ops = OpsNodes()
    res = ops.delone(id, type)
    return res


def AddBscAll(type):
    """
    :param node: ops the node id
    :param type: bsc99 or bsc92
    :return:
    """
    ops = OpsNodes()
    res = ops.addall(type)
    return res

def DelBscAll(type):
    """
    :param node: ops the node id
    :param type: bsc99 or bsc92
    :return:
    """
    ops = OpsNodes()
    res = ops.delall(type)
    return res


def Transaction(node, type):
    """
    :arg1 交易节点  only 1-6
    转账单次执行操作
    """
    if type == "bsc99":
        cmd = "kubectl exec -it bsc99-sts-%s-0 -- Transaction Auto" % node
    elif type == "polygon":
        cmd = "kubectl logs --tail=5 polygon-sts-%s-0 " % node
    elif type == "bsc92":
        cmd = "kubectl exec -it bsc92-sts-%s-0 -- Transaction Auto" % node
    else:
        return "type input err!"
    # cmd = "kubectl exec -it bsc-sts-%s-0 -- Transaction Auto" % node
    result = subprocess.run(cmd, shell=True, timeout=30,
                            stderr=subprocess.PIPE,
                            stdout=subprocess.PIPE)
    # result = subprocess.run(cmd, shell=True, timeout=30)
    # 若执行成功，则returncode为0；若执行失败，则returncode为1；
    if result.returncode != 0:
        res = "node exec faild!"
        return res
    # return str(result.stdout)
    return result.stdout


def Getnodelogs(node, type):
    """
    :arg1 交易节点  only 1-6
    :arg2 type: polygon  bsc99 bsc92必须满足type类型
    获取当前节点执行的日志，最新5行
    """
    if type == "bsc99":
        cmd = "kubectl logs --tail=5 bsc99-sts-%s-0 " % node
    elif type == "polygon":
        cmd = "kubectl logs --tail=5 polygon-sts-%s-0 " % node
    elif type == "bsc92":
        cmd = "kubectl logs --tail=5 bsc92-sts-%s-0 " % node
    else:
        return "type input err!"

    result = subprocess.run(cmd, shell=True, timeout=30,
                            stderr=subprocess.PIPE,
                            stdout=subprocess.PIPE)
    # result = subprocess.run(cmd, shell=True, timeout=30)
    # 若执行成功，则returncode为0；若执行失败，则returncode为1；
    if result.returncode != 0:
        res = "node exec faild!"
        return res
    # return str(result.stdout)
    return result.stdout


if __name__ == '__main__':
    # 初始化
    server = ThreadXMLRPCServer(('0.0.0.0', 8881), allow_none=True)
    # 注册交易转账函数
    server.register_function(Transaction, "Transaction")
    # 注册get logs func
    server.register_function(Getnodelogs, "Getnodelogs")
    # 注册add bsc nodes
    server.register_function(AddBscNode, "AddBscNode")
    # 注册del bsc nodes
    server.register_function(DelBscNode, "DelBscNode")
    # 注册start all bsc nodes
    server.register_function(AddBscAll, "AddBscAll")
    # 注册remove all bsc nodes
    server.register_function(DelBscAll, "DelBscAll")

    print("Listening for Client")
    # 保持等待调用状态
    server.serve_forever()
