from core.result_base import ResultBase


def res_deal(res):
    result = ResultBase
    result.success = False
    if res.json()["code"] == 0 and res.json()["data"] is not None:
        result.success = True
    else:
        res.error = "接口的返回码：【{}】，接口返回的信息：{}".format(res.json()["code"], res.json()["msg"])
    result.data = res.json()["data"]
    result.response = res
    return result

