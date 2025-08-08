import requests
import time
import sys
import resource_1
def sendsms(keys, url, payload, headers):
    try:
        
        if keys in resource_1.Get:
            response = requests.get(url, params=payload, headers=headers)
        else:
            response = requests.post(url, json=payload, headers=headers)

        if response.status_code == 200:
            print(f"{keys} 请求成功,返回结果：{response.text}")
        else:
            print(f"{keys} 请求失败,返回结果：{response.text}")
    except requests.RequestException as e:
        print(f"{keys} 请求异常,返回结果：", e)



if __name__ == "__main__":
    number = input("请输入手机号：").strip()
    if not number.isdigit() or len(number)!= 11:
        print("手机号格式不正确，请重新输入")
        sys.exit(1)
    print("手机号格式正确")
    print("开始发送短信验证码")
    dicts = resource_1.preparingnumber(number)
    while True:
        for key, items in dicts.items():
            sendsms(key, items[0], items[1], items[2])
            time.sleep(3)