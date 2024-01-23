import requests
import json
from flask import Flask,request, jsonify


app = Flask(__name__)


@app.route('/checkvalid', methods=['POST', 'GET'])
def checkvalid():
    print(request.args)
    user= request.args.get('user','')
    hd1 = {
        'authority': 'accounts.google.com',
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
        'google-accounts-xsrf': '1',
        'origin': 'https://accounts.google.com',
        'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
        'sec-ch-ua-arch': '"x86"',
        'sec-ch-ua-bitness': '"64"',
        'sec-ch-ua-full-version': '"120.0.6099.225"',
        'sec-ch-ua-full-version-list': '"Not_A Brand";v="8.0.0.0", "Chromium";v="120.0.6099.225", "Google Chrome";v="120.0.6099.225"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-model': '""',
        'sec-ch-ua-platform': '"Windows"',
        'sec-ch-ua-platform-version': '"10.0.0"',
        'sec-ch-ua-wow64': '?0',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'x-same-domain': '1',
    }
    hd2 = {
        'authority': 'www.google.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'cache-control': 'max-age=0',
        'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
        'sec-ch-ua-arch': '"x86"',
        'sec-ch-ua-bitness': '"64"',
        'sec-ch-ua-full-version': '"120.0.6099.225"',
        'sec-ch-ua-full-version-list': '"Not_A Brand";v="8.0.0.0", "Chromium";v="120.0.6099.225", "Google Chrome";v="120.0.6099.225"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-model': '""',
        'sec-ch-ua-platform': '"Windows"',
        'sec-ch-ua-platform-version': '"10.0.0"',
        'sec-ch-ua-wow64': '?0',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'x-client-data': 'CIa2yQEIprbJAQipncoBCNHpygEIlaHLAQiFoM0BCI7hzQEI3OnNAQii7s0BCMnuzQEIg/DNAQiF8M0BCL7xzQEI1vHNAQik8s0BCPvzzQEIzfTNAQiP9c0BCJH1zQEY/ZjNARin6s0BGPnyzQE=',
    }
    session= requests.session()
    getcc1 = requests.get("https://accounts.google.com/signup", headers=hd1)
    cc = getcc1.cookies.get_dict()
    cook1 = json.dumps(cc, indent=2)
    cook2 = json.loads(cook1)
    HostGAPS = cook2.get("__Host-GAPS", None)
    a = getcc1.text
    b = a.split("%3Dglif%26TL%3D")[1].split("'")[0]
    loaibo = r'\x26hl\x3den-US'
    TL = b.replace(loaibo, '')

    getdata=requests.get("https://accounts.google.com/",headers=hd1).text
    ifkv=getdata.split(";ifkv=")[1].split("&amp;")[0]
    dsh=getdata.split('"dsh","')[1].split('"')[0]

    getcc2=requests.get("https://google.com", headers=hd2)
    getNID=session.cookies.get_dict()
    NID1=json.dumps(getNID,indent=2)
    ccNID=json.loads(NID1)
    NID=ccNID.get("NID", None)
    headers = {
        'authority': 'accounts.google.com',
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
        'google-accounts-xsrf': '1',
        'origin': 'https://accounts.google.com',
        'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
        'sec-ch-ua-arch': '"x86"',
        'sec-ch-ua-bitness': '"64"',
        'sec-ch-ua-full-version': '"120.0.6099.225"',
        'sec-ch-ua-full-version-list': '"Not_A Brand";v="8.0.0.0", "Chromium";v="120.0.6099.225", "Google Chrome";v="120.0.6099.225"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-model': '""',
        'sec-ch-ua-platform': '"Windows"',
        'sec-ch-ua-platform-version': '"10.0.0"',
        'sec-ch-ua-wow64': '?0',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'x-same-domain': '1',
    }

    cookies = {
        'OTZ': '7393538_28_28__28_',
        'NID': NID,
        '__Host-GAPS': HostGAPS,
    }

    params = {
        'hl': 'en',
        'TL': TL,
        '_reqid': '259911',
        'rt': 'j',
    }

    data = f'TL={TL}&continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&dsh={dsh}&emr=1&flowEntry=SignUp&followup=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&hl=en-US&ifkv={ifkv}&osid=1&service=mail&theme=glif&f.req=%5B%22TL%3A{TL}%22%2C%22{user}%22%2C1%2C0%2C1%2Cnull%2C0%2C3875%5D&azt=AFoagUVU0mkwWecg95R1a6cB7a502TM-jA%3A1705916277891&cookiesDisabled=false&deviceinfo=%5Bnull%2Cnull%2Cnull%2Cnull%2Cnull%2C%22VN%22%2Cnull%2Cnull%2Cnull%2C%22GlifWebSignIn%22%2Cnull%2C%5B%5D%2Cnull%2Cnull%2Cnull%2Cnull%2C1%2Cnull%2C0%2C1%2C%22%22%2Cnull%2Cnull%2C2%2C2%5D&gmscoreversion=undefined&flowName=GlifWebSignIn&checkConnection=youtube%3A487&checkedDomains=youtube&pstMsg=1&'

    response = session.post(
        'https://accounts.google.com/_/signup/usernameavailability',
        params=params,
        cookies=cookies,
        headers=headers,
        data=data,
    ).text
    if '[[["gf.uar",1' in response:
        print(f'Die user : {user}')
        return jsonify({"message":f"Die user {user}"}),200
    elif '[[["gf.uar",2' in response:
        print(f'Live user : {user}')
        return jsonify({"message":f"Live user {user}"}),200
    else:
        print(f'error user : {user}')
        return jsonify({"message":f"Error user {user}"}),400
if __name__ == '__main__':
    app.run(debug=True, port=5001)