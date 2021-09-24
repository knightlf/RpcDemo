from xmlrpc.client import ServerProxy
import xmlrpc.client

if __name__ == '__main__':
    server = ServerProxy("http://127.0.0.1:8881", allow_none=True)
    res=server.Transaction("1")
    # if res.returncode!=0:
    #     res = "node exec faild!"
    #     print(res)

    #print(xmlrpc.client.Binary(res["stdout"].read()))

    
    # print(server.get_string("cloudox"))
    # print(server.add(8, 8))
    # # 上传文件
    # put_handle = open("aaa.tx", 'rb')
    # server.image_put(xmlrpc.client.Binary(put_handle.read()))
    # put_handle.close()
    # # 下载文件
    # get_handle = open("aa.tx", 'wb')
    # get_handle.write(server.image_get().data)
    # get_handle.close()

