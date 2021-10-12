# _*_ coding:utf-8 _*_

import subprocess
import config


class OpsNodes():
    def __init__(self):
        self.stsnode92 = config.bsc92_yaml
        self.stsnode99 = config.bsc99_yaml

    def addone(self, id, type):
        if type == "bsc92":
            sts = self.stsnode92
        elif type == "bsc99":
            sts = self.stsnode99
        else:
            return "type input err!"
        cmd = "kubectl apply -f  " + sts + "bsc-sts-" + id + ".yaml"
        result = subprocess.run(cmd, shell=True, timeout=30,
                                stderr=subprocess.PIPE,
                                stdout=subprocess.PIPE)
        # result = subprocess.run(cmd, shell=True, timeout=30)
        # 若执行成功，则returncode为0；若执行失败，则returncode为1；
        if result.returncode != 0:
            res = "node add faild!"
            return res
        # return str(result.stdout)
        return result.stdout

    def addall(self, type):
        if type == "bsc92":
            sts = self.stsnode92
        elif type == "bsc99":
            sts = self.stsnode99
        else:
            return "type input err!"
        cmd = "kubectl apply -f  %s" % sts
        result = subprocess.run(cmd, shell=True, timeout=30,
                                stderr=subprocess.PIPE,
                                stdout=subprocess.PIPE)
        # result = subprocess.run(cmd, shell=True, timeout=30)
        # 若执行成功，则returncode为0；若执行失败，则returncode为1；
        if result.returncode != 0:
            res = "add all faild!"
            return res
        # return str(result.stdout)
        return result.stdout

    def delone(self, id, type):
        if type == "bsc92":
            sts = self.stsnode92
        elif type == "bsc99":
            sts = self.stsnode99
        else:
            return "type input err!"
        cmd = "kubectl delete -f  " + sts + "bsc-sts-" + id + ".yaml"
        result = subprocess.run(cmd, shell=True, timeout=30,
                                stderr=subprocess.PIPE,
                                stdout=subprocess.PIPE)
        # result = subprocess.run(cmd, shell=True, timeout=30)
        # 若执行成功，则returncode为0；若执行失败，则returncode为1；
        if result.returncode != 0:
            res = "node add faild!"
            return res
        # return str(result.stdout)
        return result.stdout

    def delall(self,type):
        if type == "bsc92":
            sts = self.stsnode92
        elif type == "bsc99":
            sts = self.stsnode99
        else:
            return "type input err!"
        cmd = "kubectl delete -f  %s" % sts
        result = subprocess.run(cmd, shell=True, timeout=30,
                                stderr=subprocess.PIPE,
                                stdout=subprocess.PIPE)
        # result = subprocess.run(cmd, shell=True, timeout=30)
        # 若执行成功，则returncode为0；若执行失败，则returncode为1；
        if result.returncode != 0:
            res = "add all faild!"
            return res
        # return str(result.stdout)
        return result.stdout


if __name__ == '__main__':
    pass
