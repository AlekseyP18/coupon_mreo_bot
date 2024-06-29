import requests

from fake_useragent import UserAgent

# from db import get_last_settings


cookies = {
    'WEBCHSID2': 'mdkcvtvn6ovtm1jihu0qfa772p',
    '_identity': '933c2ccad13e0b5bddb44ae6bdc24a80c804621e3938da63e04d47ff3c427df6a%3A2%3A%7Bi%3A0%3Bs%3A9%3A%22_identity%22%3Bi%3A1%3Bs%3A20%3A%22%5B1088915%2Cnull%2C28800%5D%22%3B%7D',
    '_csrf': '99cdb728961f6c417ea1833f1fbf1fe2d0f6702754bcbac38438db4acbdd9a3ba%3A2%3A%7Bi%3A0%3Bs%3A5%3A%22_csrf%22%3Bi%3A1%3Bs%3A32%3A%22o7Nva72FulOcXGcSUb3OCSbba8357Ayd%22%3B%7D',
}

headers = {
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.9,ru;q=0.8,uk;q=0.7',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'Cookie': 'WEBCHSID2=mdkcvtvn6ovtm1jihu0qfa772p; _identity=933c2ccad13e0b5bddb44ae6bdc24a80c804621e3938da63e04d47ff3c427df6a%3A2%3A%7Bi%3A0%3Bs%3A9%3A%22_identity%22%3Bi%3A1%3Bs%3A20%3A%22%5B1088915%2Cnull%2C28800%5D%22%3B%7D; _csrf=99cdb728961f6c417ea1833f1fbf1fe2d0f6702754bcbac38438db4acbdd9a3ba%3A2%3A%7Bi%3A0%3Bs%3A5%3A%22_csrf%22%3Bi%3A1%3Bs%3A32%3A%22o7Nva72FulOcXGcSUb3OCSbba8357Ayd%22%3B%7D',
    'Origin': 'https://eq.hsc.gov.ua',
    'Referer': 'https://eq.hsc.gov.ua/site/step2?chdate=2024-06-30&question_id=49&id_es=',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'X-CSRF-Token': '3tFOJoBw5g-MVhuXqH36cK7pv79MKSrMUKn1jcTyJlux5gBQ4UfUSfk6VPTwOpkj-4uM8A96SK4xkca487NfPw==',
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Linux"',
}



def send_request_to_hsc(data: str) -> dict:
    global headers, cookies
    # api_settings = get_last_settings()
    headers['User-Agent'] = UserAgent().random

    # cookies['WEBCHSID2'] = api_settings.WEBCHSID2
    # cookies['_csrf'] = api_settings._csrf
    
    # headers['X-CSRF-Token'] = api_settings.X_CSRF_Token
    
    data_request = {
        'office_id': '145',
        'date_of_admission': '2024-06-30',
        'question_id': '49',
        'es_date': '',
        'es_time': '',
    }
    response = requests.post('https://eq.hsc.gov.ua/site/freetimes',
                             cookies=cookies, headers=headers,
                             data=data_request, verify=False)
    
    return response.json()
