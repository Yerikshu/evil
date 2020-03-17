import json
import requests
from django.http import HttpResponse
from django.views import View


class VisitorView(View):
    def __init__(self):
        pass

    def get(self, request):
        print("11111")
        response_data = {'msg': "1111", 'status': "520", "code": "123"}
        return HttpResponse(json.dumps(response_data), content_type="application/json")

    def post(self, request):
        url = "https://www.baidu.com/"

        headers = {
            'accept': "application/json, text/javascript, */*; q=0.01",
            'user-agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36",
            'referer': "https://www.baidu.com/",
            'accept-encoding': "gzip, deflate, br",
            'accept-language': "en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7",
            'cookie': "BAIDUID=D4C0E004BEA731A6F303DABAD1731879:FG=1; BIDUPSID=D4C0E004BEA731A6F303DABAD1731879; PSTM=1539828347; MCITY=-257%3A; BDUSS=GsyVUZyWWdIOWlWUzFmUmY1eGpxcG4tRlg2M3VoOWppR284WkJxYlMxa09FY1JjQVFBQUFBJCQAAAAAAAAAAAEAAABSFvxJsKJ0cmVlZQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA6EnFwOhJxcU; sugstore=1; COOKIE_SESSION=5_0_2_2_2_0_0_0_2_0_0_0_4_0_6_0_1575604747_0_1575604741%7C2%230_0_1575604741%7C1; pgv_pvi=1749187584; BD_UPN=123353; BD_HOME=1; H_PS_PSSID=30971_1443_21080_30994_30824_26350_30717",
            'cache-control': "no-cache",
            'postman-token': "d021496c-9842-d8f8-c6a0-f9f82891ea0e"
        }

        response = requests.request("GET", url, headers=headers)

        print(response)

        # data = json.dumps(request)

        print(request)

        response_data = {'msg': "1111", 'status': "520", "code": "123123"}
        return HttpResponse(json.dumps(response_data), content_type="application/json")
