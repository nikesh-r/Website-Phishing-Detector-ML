def phishApp(url):
    
    # url = 'http://google.com/'     # SAFE
    # url = 'http:////iedjpaypal.com/'     # INVALID
    # url = 'http://www.pubgasia.gamers.co.in/season-15/news/'     # PHISHING
    # url = 'https://www.formula1.com/'     # SAFE
    # url = 'https://eofem.com/'     # INVALID
    # url = 'https://www.vodafone.ie/en.html'     # 404
    # url = 'https://kyufukin-soumo-go-jp.xyz/'     # PHISHING
    # url = 'https://magnetmarket.by'     # PHISHING
    # url = 'https://nam10.safelinks.protection.outlook.com/?url=http%3A%2F%2Fby0556.customervoice360.com%2Fuc%2Fproject_manager%2Faafe%2F%3Fa%3D19905%26b%3D3d4a776d3cfeedd8%26c%3Dkrobles%40bcp.com.pe&data=04%7C01%7Ckrobles%40bcp.com.pe%7C36de14a50a3b44e2579b08d87474d6be%7C5d93ebccf76943808b7e289fc972da1b%7C0%7C1%7C637387392447326370%7CUnknown%7CTWFpbGZsb3d8eyJWIjoiMC4wLjAwMDAiLCJQIjoiV2luMzIiLCJBTiI6Ik1haWwiLCJXVCI6Mn0%3D%7C2000&sdata=inC%2Fwn2X3oRbmZUvHAvPCNiLCi396q5SIftzGPSTNys%3D&reserved=0'     # PHISHING
    # url = 'https://signinnowtouppgradeyouryahoomail.weebly.com/'     # PHISHING
    # url = 'http://wearhousesports.com/generate/info_update/admim-content/webmail.uregina.ca.htm'     # PHISHING
    # url = 'https://redeglobo.globo.com/'     # SAFE
    invalid_url = "URL Incorrect!"

    import requests

    try:
        r = requests.get(url)
        print(r.status_code)
        if(r.status_code != 200):
            print(invalid_url)
            return invalid_url
        else:
            print("good job")
    except:
        print(invalid_url)
        return invalid_url


    # using the ip address - using_ip
    import re

    using_ip = re.match('^(http|https)://\d+\.\d+\.\d+\.\d+\.*', url)
    if(using_ip):
        using_ip = 1
    else:
        using_ip = -1
    print(using_ip)



    # url length - url_len

    # url = "weweeeeeeeeddddddeeeeeeeeeeeeeeeddddddddddddddddddeeeeeeddddddddddddddeeeee"
    url_len = len(url)
    # print(url_len)
    if(url_len < 54):
        url_len = -1
    elif(url_len >= 54 and url_len <= 75):
        url_len = 0
    else:
        url_len = 1
    print(url_len)



    # short url service (tinyurl or bitly) - short_url
    # url = 'https://tinyurl.com/mmk'
    short_url = re.match('(http|https)://(bit\.ly|tinyurl\.com/)', url)
    if(short_url):
        short_url = 1
    else:
        short_url = -1
    print(short_url)



    # url contain '@' - contains_at

    # url = 'https://www.cdnfeatifdm.com'
    if '@' in url:
        contains_at = 1
    else:
        contains_at = -1
    print(contains_at)



    # contains '//' for redirecting - redirect

    # url = 'http:////iedjoek.com'
    index = 0
    redirect = 0
    index = url.rfind('//', 6)

    if (index > 6):
        redirect = 1
    else:
        redirect = -1
    print(redirect)



    # contains perfix / suffix separeated by '-' - contains_hyphen

    # url = 'http:////iedjpaypal.com/'
    index = url.find('-')
    if (index == -1):
        contains_hyphen = -1
    else:
        contains_hyphen = 1
    print(contains_hyphen)



    # sub domain and multi sub domain. count of '.' - dot_flag

    # url = "http://www.pubgasia.gamers.co.in/season-15/news/"
    # url = 'http://https-www-paypal-it-webapps-mpp-home.soft-hair.com/'

    url = url.split('/')
    sub_url = url[2]
    sub_url = sub_url.split('.')

    # print(url)
    # print(sub_url)

    with open('./tlds-alpha-by-domain.txt', 'r') as read_obj:
        for line in read_obj:
            line = line.strip().lower()
    #         print(line)
            if line in sub_url:
    #             continue
                sub_url.remove(line)

    sub_url = '.'.join(sub_url)
    url = '/'.join(url)

    # print(url)
    # print(sub_url)

    c = 0
    sub_url_len = len(sub_url)
    c = sub_url.count('.', 0, sub_url_len)
    if (c == 0):
        dot_flag = -1
    elif (c == 1):
        dot_flag = 0
    else:
        dot_flag = 1
    print(dot_flag)



    # presence of 'https' token - https_token

    # print(sub_url)
    index = sub_url.find('https')
    if (index == -1):
        https_token = -1
    else:
        https_token = 1
    print(https_token)



    # Website forwarding - website_forward

    import requests

    # url = 'https://tinyurl.com/cucpjq'

    try:
        response = requests.get(url)
    #     print(response.history)
    #     for resp in response.history:
    #         print(resp.status_code, resp.url)

        resp_len = len(response.history)

        if (resp_len <= 1):
            website_forward = -1
        elif (resp_len >= 2 and resp_len < 4):
            website_forward = 0
        else:
            website_forward = 1
        print(website_forward)
    except requests.exceptions.RequestException as e:
        # print('invalid')
        # website_forward = 1
        # print(website_forward)
        print(invalid_url)
        return invalid_url



    # disabling right click - right_click

    # url = 'https://retail.onlinesbi.com/retail/login.htm'
    try:
        r = requests.get(url)
        page_source = r.text
        right_click = -1
        index = page_source.find('oncontextmenu' or 'event.button==2')
        if(index != -1):
            right_click = 1
        print(right_click)
    except:
        # print('invalid')
        # right_click = 1
        # print(right_click)
        print(invalid_url)
        return invalid_url



    # using iframe frameborder property - iframe_frameborder

    # url = 'https://tinyurl.com/cucpjq'
    # url = 'https://www.formula1.com/'

    try:
        r = requests.get(url)
        page_source = r.text
        index = page_source.find('frameBorder')
        iframe_frameborder = -1
        if(index != -1):
            iframe_frameborder = 1
        print(iframe_frameborder)
    except:
        # print('invalid')
        # iframe_frameborder = 1
        # print(iframe_frameborder)
        print(invalid_url)
        return invalid_url



    # creating the dataFrame from derived data

    import pandas as pd

    featured_columns = ['having_IP_Address', 'URL_Length', 'Shortining_Service', 'having_At_Symbol', 'double_slash_redirecting', 'Prefix_Suffix', 'having_Sub_Domain', 'HTTPS_token', 'Redirect', 'RightClick', 'Iframe']

    url_data = [[using_ip, url_len, short_url, contains_at, redirect, contains_hyphen, dot_flag, https_token, website_forward, right_click, iframe_frameborder]]
    # print(url_data)
    url_df = pd.DataFrame(url_data, columns = featured_columns)
    print(url_df)



    # url_y_pred = decision_tree_model.predict(url_df)
    # print(url_y_pred)
    # if(url_y_pred == 1):
    #     print(url, ' - Its a PHISHING Website')
    # else:
    #     print('Website is NOT Phishing')


    import joblib
    url_checker_model = joblib.load("decision_tree_model_saved.pkl")
    phishing_prediction = url_checker_model.predict(url_df)
    print(phishing_prediction)

    if(phishing_prediction == 1):
        phish_result = "It's a PHISHING Website! Be Safe!"
        print(url, " - It's a PHISHING Website")
    else:
        phish_result = "Website is NOT Phishing. You are good to go!"
        print('Website is NOT Phishing')

    return phish_result




from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def home():
    if request.method == "POST":
        url = request.form["input_url"]
        print(url)
        phishResult = phishApp(url)
        print(phishResult)
        return render_template("outPage.html", phish_result = phishResult)
    else:
        return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)