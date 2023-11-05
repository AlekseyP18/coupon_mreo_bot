import requests

from fake_useragent import UserAgent

from db import get_last_settings


cookies = {
    '_ga': 'GA1.3.617879063.1698791832',
    '_identity': '933c2ccad13e0b5bddb44ae6bdc24a80c804621e3938da63e04d47ff3c427df6a%3A2%3A%7Bi%3A0%3Bs%3A9%3A%22_identity%22%3Bi%3A1%3Bs%3A20%3A%22%5B1088915%2Cnull%2C28800%5D%22%3B%7D',
}

headers = {
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.9,ru;q=0.8,uk;q=0.7',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Origin': 'https://eq.hsc.gov.ua',
    'Pragma': 'no-cache',
    'Referer': 'https://eq.hsc.gov.ua/site/step2?chdate=2023-11-15&question_id=56&id_es=',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua': '"Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}


def send_request_to_hsc(data: str) -> dict:
    global headers, cookies
    api_settings = get_last_settings()
    headers['User-Agent'] = UserAgent().random
    
    cookies['_gid'] = api_settings._gid
    cookies['_gat'] = api_settings._gat
    cookies['_ga_3GVV2WPF7F'] = api_settings._ga_3GVV2WPF7F
    cookies['WEBCHSID2'] = api_settings.WEBCHSID2
    cookies['_csrf'] = api_settings._csrf
    
    headers['X-CSRF-Token'] = api_settings.X_CSRF_Token
    
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
