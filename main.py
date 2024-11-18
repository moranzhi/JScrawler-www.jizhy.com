import requests
import hashlib
import time
def req(page):
    ts = ts = time.time_ns() / 1e6
    signStr = f"{{app_id=98357f659cf8fb6001cff80f7c6b85f2&diploma_id=7&page={page}&page_len=20&platform=desktop&rank_type=us&ts={ts}&v=210&wenli=0}}&key=146fd1e66513611ac7af69f21f1d7725"

    md5_hash = hashlib.md5()
    # 更新哈希对象，传入要进行加密的字符串
    md5_hash.update(signStr.encode('utf-8'))
    # 获取十六进制格式的MD5哈希值
    sign = md5_hash.hexdigest()

    headers = {
        "accept": "application/json, text/plain, */*",
        "accept-language": "zh-CN,zh;q=0.9",
        "priority": "u=1, i",
        "referer": "https://www.jizhy.com/44/rank/us",
        "sec-ch-ua": "\"Chromium\";v=\"130\", \"Google Chrome\";v=\"130\", \"Not?A_Brand\";v=\"99\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36"
    }
    cookies = {
        "Hm_lvt_2610e5c202b60841b30a62960fbef0ad": "1731662095",
        "HMACCOUNT": "41B1006B0C923DCE",
        "PI": "44",
        "b-user-id": "aa42f09e-5f5c-15aa-fe3b-8c4adc4e2932",
        "Hm_lpvt_2610e5c202b60841b30a62960fbef0ad": "1731667755"
    }
    url = "https://www.jizhy.com/open/sch/third-rank-list"
    params = {
        "page": page,
        "page_len": "20",
        "diploma_id": "7",
        "wenli": "0",
        "rank_type": "us",
        "app_id": "98357f659cf8fb6001cff80f7c6b85f2",
        "ts": time.time_ns() / 1e6,
        "platform": "desktop",
        "v": "210",
        "sign": sign
    }
    response = requests.get(url, headers=headers, cookies=cookies, params=params)
    print(response)
    print(response.text)



# 请求1-4页的数据
for page in range(1, 5):
    req(page)
