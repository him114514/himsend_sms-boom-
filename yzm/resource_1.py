
Get=['sxk']
def preparingnumber(number):
    game_url = 'https://m.bigplayers.com/api/user/v1/smsCode/sendLoginSmsV2'
    game_payload = {
        "phoneNumber": f"86{number}",

        "areaCode": "86",
        "captchaVerifyParam": "{\"sceneId\":\"1ns8ckkp\",\"certifyId\":\"x5uU0wAifK\",\"deviceToken\":\"...\"}"
    }
    game_headers = {
        "accept": "application/json, text/plain, */*",
        "accept-encoding": "gzip, deflate, br, zstd",
        "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
        "clienttype": "0",
        "content-type": "application/json;charset=UTF-8",
        "cookie": "...",
        "countryid": "26",
        "distinctid": "...",
        "istoken": "false",
        "languageid": "6",
        "latestreferrer": "https://m.bigplayers.com/preview?fromPcPage=%2F",
        "latestreferrerhost": "https://m.bigplayers.com",
        "origin": "https://m.bigplayers.com",
        "os": "2",
        "priority": "u=1, i",
        "referer": "https://m.bigplayers.com/",
        "screenheight": "591",
        "screenwidth": "400",
        "sec-ch-ua": "\"Not)A;Brand\";v=\"8\", \"Chromium\";v=\"138\", \"Microsoft Edge\";v=\"138\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 Edg/138.0.0.0"
    }
    Game = [game_url, game_payload, game_headers]

    hxx_url = 'https://api.hexiaoxiang.com/cerberus/turingtest'
    hxx_payload = {
        "cellphone": number,
        "session_id": "...",
        "sig": "...",
        "token": "...",
        "scene": "ic_message_h5"
    }
    hxx_headers = {
        "accept": "application/json, text/plain, */*",
        "accept-encoding": "gzip, deflate, br, zstd",
        "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
        "content-length": "658",
        "content-type": "application/json;charset=UTF-8",
        "origin": "https://www.hexiaoxiang.com",
        "priority": "u=1, i",
        "referer": "https://www.hexiaoxiang.com/",
        "sec-ch-ua": "\"Not)A;Brand\";v=\"8\", \"Chromium\";v=\"138\", \"Microsoft Edge\";v=\"138\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 Edg/138.0.0.0"
    }
    Hxx = [hxx_url, hxx_payload, hxx_headers]

    ks_url = "https://id.kuaishou.com/pass/kuaishou/sms/requestMobileCode"
    ks_payload = {
        "sid": "kuaishou.server.webday7",
        "type": 53,
        "countryCode": "+86",
        "phone": number,
        "account": "",
        "ztIdentityVerificationType": "",
        "ztIdentityVerificationCheckToken": "",
        "channelType": "UNKNOWN",
        "encryptHeaders": ""
    }
    ks_headers = {}
    Ks = [ks_url, ks_payload, ks_headers]

    sdc_url = 'https://passport.shuidihuzhu.com/api/account/v3/verify-code-send'
    sdc_payload = {
        "mobile": number,
        "key": "REG-CFANPBDE"
    }
    sdc_headers = {
        "accept": "*/*",
        "accept-encoding": "gzip, deflate, br, zstd",
        "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
        "authorizationv2": "",
        "content-length": "45",

        "content-type": "application/json",
        "origin": "https://www.shuidichou.com",
        "priority": "u=1, i",
        "referer": "https://www.shuidichou.com/",
        "sec-ch-ua": "\"Not)A;Brand\";v=\"8\", \"Chromium\";v=\"138\", \"Microsoft Edge\";v=\"138\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "cross-site",
        "shuidi-app-code": "",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 Edg/138.0.0.0"
    }
    Sdc = [sdc_url, sdc_payload, sdc_headers]

    sjzg_url = "https://www.vcg.com/graphql/sendCode"
    sjzg_payload = {
        "value": number,
        "type": "mobile"
    }
    sjzg_headers = {
        "accept": "application/json",
        "accept-encoding": "gzip, deflate, br, zstd",
        "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
        "connection": "keep-alive",
        "content-length": "39",
        "content-type": "application/json",
        "cookie": "...",
        "host": "www.vcg.com",
        "origin": "https://www.vcg.com",
        "referer": "https://www.vcg.com/",
        "sec-ch-ua": "\"Not)A;Brand\";v=\"8\", \"Chromium\";v=\"138\", \"Microsoft Edge\";v=\"138\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 Edg/138.0.0.0"
    }
    Sjzg = [sjzg_url, sjzg_payload, sjzg_headers]

    sxk_url = f'https://cq.sankuanyun.com/register/sms?phone_number={number}'
    sxk_payload = {'phone_number': number}
    sxk_headers = {
        "accept": "application/json, text/plain, */*",
        "accept-encoding": "gzip, deflate, br, zstd",
        "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
        "cookie": "...",
        "priority": "u=1, i",
        "referer": "https://cq.sankuanyun.com/",
        "sec-ch-ua": "\"Not)A;Brand\";v=\"8\", \"Chromium\";v=\"138\", \"Microsoft Edge\";v=\"138\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 Edg/138.0.0.0",
        "x-requested-with": "XMLHttpRequest"
    }
    Sxk = [sxk_url, sxk_payload, sxk_headers]

    zmn_url = 'https://c.xiujiadian.com/uac/mobile/sendCaptchaWithType'
    zmn_payload = {
        "mobile": number,
        "type": 300,
        "meid": "cb7c61f43145c0408df712180d10f378"
    }
    zmn_headers = {
        "accept": "*/*",
        "accept-encoding": "gzip, deflate, br, zstd",
        "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
        "channelid": "40002",
        "cityid": "500100",
        "content-length": "77",
        "content-type": "application/json",
        "cooperationid": "40002",
        "origin": "https://prc.zmn.cn",
        "platid": "10",
        "priority": "u=1, i",
        "provinceid": "500000",
        "referer": "https://prc.zmn.cn/",
        "sec-ch-ua": "\"Not)A;Brand\";v=\"8\", \"Chromium\";v=\"138\", \"Microsoft Edge\";v=\"138\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "cross-site",
        "token": "",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 Edg/138.0.0.0"
    }
    Zmn = [zmn_url, zmn_payload, zmn_headers]

    conclusion={'game': Game,'hxx': Hxx,'kuaishou': Ks,'sdc': Sdc,'sjzg': Sjzg,'sxk': Sxk,'zmn': Zmn}
    return conclusion