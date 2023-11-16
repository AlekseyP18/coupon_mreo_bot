import requests

from fake_useragent import UserAgent

# from db import get_last_settings


cookies = {
    'WEBCHSID2': '6bve2fvr7o4l2ienrf1a5df9fn',
    '_identity': 'afb6f43e0dd4d1333d8bb6664d0cf0797ca6b61f162714f34dd5a73599fdf760a%3A2%3A%7Bi%3A0%3Bs%3A9%3A%22_identity%22%3Bi%3A1%3Bs%3A20%3A%22%5B1366662%2Cnull%2C28800%5D%22%3B%7D',
    '_csrf': 'dae8dee7a9f15a75d0fd0013eac036601977bfacca1e0ed48264626ce86c5293a%3A2%3A%7Bi%3A0%3Bs%3A5%3A%22_csrf%22%3Bi%3A1%3Bs%3A32%3A%228aXdEx6xuLlJFBbmnS2L2-wRGJ0jVqB5%22%3B%7D',
}

headers = {
    'Accept': '*/*',
    'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'Cookie': 'WEBCHSID2=6bve2fvr7o4l2ienrf1a5df9fn; _identity=afb6f43e0dd4d1333d8bb6664d0cf0797ca6b61f162714f34dd5a73599fdf760a%3A2%3A%7Bi%3A0%3Bs%3A9%3A%22_identity%22%3Bi%3A1%3Bs%3A20%3A%22%5B1366662%2Cnull%2C28800%5D%22%3B%7D; _csrf=dae8dee7a9f15a75d0fd0013eac036601977bfacca1e0ed48264626ce86c5293a%3A2%3A%7Bi%3A0%3Bs%3A5%3A%22_csrf%22%3Bi%3A1%3Bs%3A32%3A%228aXdEx6xuLlJFBbmnS2L2-wRGJ0jVqB5%22%3B%7D',
    'Origin': 'https://eq.hsc.gov.ua',
    'Referer': 'https://eq.hsc.gov.ua/site/step2?chdate=2023-11-08&question_id=56&id_es=',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
    'X-CSRF-Token': '_4EQ9xoVhBH22_Nh2FoV7jq89CvC1zJ0dzSQm9oXaonH4EiTX22yaYOXnyueGHeDVO_GZ_D6RSYwfqDxjGYovA==',
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua': '"Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}


def send_request_to_hsc(data: str) -> dict:
    global headers, cookies
    # api_settings = get_last_settings()
    headers['User-Agent'] = UserAgent().random

    # cookies['WEBCHSID2'] = api_settings.WEBCHSID2
    # cookies['_csrf'] = api_settings._csrf
    
    # headers['X-CSRF-Token'] = api_settings.X_CSRF_Token
    
    data_request = {
        'office_id': '20',
        'date_of_admission': data,
        'question_id': '56',
        'es_date': '',
        'es_time': '',
    }
    response = requests.post('https://eq.hsc.gov.ua/site/freetimes',
                             cookies=cookies, headers=headers,
                             data=data_request, verify=False)
    
    return response.json()
