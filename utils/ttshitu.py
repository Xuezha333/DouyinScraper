import base64
import json
import requests
def base64_api(uname, pwd, img, typeid):
    with open(img, mode='rb') as f:  # s  
        base64_data = base64.b64encode(f.read())  
        b64 = base64_data.decode()
    
    data = {"username": uname, "password": pwd, "typeid": typeid, "image": b64, "remark": "点击两个形状相同的物体"}
    result = json.loads(
        requests.post("http://api.ttshitu.com/predict", json=data).text)
    if result['success']:
        return result["data"]["result"]
    else:
        #！！！！！！！注意：返回 人工不足等 错误情况 请加逻辑处理防止脚本卡死 继续重新 识别
        return result["message"]
  

if __name__ == "__main__":
    result = base64_api(uname='jingjjjjjie', pwd='Beida123', img="./image.png", typeid=27)
    print(result)
    