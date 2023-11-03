import requests

from fake_useragent import UserAgent


cookies = {
    '_ga': 'GA1.3.617879063.1698791832',
    '_gid': 'GA1.3.289807276.1698961591',
    '_ga_3GVV2WPF7F': 'GS1.3.1699028926.4.0.1699028926.0.0.0',
    'WEBCHSID2': 's2t00i1hs2s55mgr878m29q6eg',
    '_identity': '933c2ccad13e0b5bddb44ae6bdc24a80c804621e3938da63e04d47ff3c427df6a%3A2%3A%7Bi%3A0%3Bs%3A9%3A%22_identity%22%3Bi%3A1%3Bs%3A20%3A%22%5B1088915%2Cnull%2C28800%5D%22%3B%7D',
    '_csrf': 'b19f28c08d09b6c4d91a2dddffdff5f217b46dc84e13405b3b0c8a6077bd16caa%3A2%3A%7Bi%3A0%3Bs%3A5%3A%22_csrf%22%3Bi%3A1%3Bs%3A32%3A%22BwfOPOPbo7_XurOd_sgGrhrsQjv1DXY5%22%3B%7D',
}

headers = {
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.9,ru;q=0.8,uk;q=0.7',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'Cookie': '_ga=GA1.3.617879063.1698791832; _gid=GA1.3.289807276.1698961591; _ga_3GVV2WPF7F=GS1.3.1699028926.4.0.1699028926.0.0.0; WEBCHSID2=s2t00i1hs2s55mgr878m29q6eg; _identity=933c2ccad13e0b5bddb44ae6bdc24a80c804621e3938da63e04d47ff3c427df6a%3A2%3A%7Bi%3A0%3Bs%3A9%3A%22_identity%22%3Bi%3A1%3Bs%3A20%3A%22%5B1088915%2Cnull%2C28800%5D%22%3B%7D; _csrf=b19f28c08d09b6c4d91a2dddffdff5f217b46dc84e13405b3b0c8a6077bd16caa%3A2%3A%7Bi%3A0%3Bs%3A5%3A%22_csrf%22%3Bi%3A1%3Bs%3A32%3A%22BwfOPOPbo7_XurOd_sgGrhrsQjv1DXY5%22%3B%7D',
    'Origin': 'https://eq.hsc.gov.ua',
    'Pragma': 'no-cache',
    'Referer': 'https://eq.hsc.gov.ua/site/step2?chdate=2023-11-15&question_id=56&id_es=',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
    'X-CSRF-Token': 'jhogD6iARcUrCPJVu3aFL6SI1FRYaY8b-FU6UYra3yvMbUZA-M8Vp0Q_rQ3OBMpL-_uzEyoB_WipP0xgzoKGHg==',
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua': '"Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}


def send_request_to_hsc(data: str) -> dict:
    global headers, cookies
    headers['User-Agent'] = UserAgent().random
    
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