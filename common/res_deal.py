from core.result_base import ResultBase


def res_deal(res):
    result = ResultBase
    result.success = False
    if res.json()["code"] == 0 and "success" in res.json()["msg"]:
        result.success = True
        result.code = 0
        result.msg = "success"
    else:
        result.error = "接口的返回码：【{}】，接口返回的信息：{}".format(res.json()["code"], res.json()["msg"])
    if "data" in res.json():
        result.data = res.json()["data"]
    result.response = res
    return result

