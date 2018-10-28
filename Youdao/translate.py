# -*- coding: utf-8 -*-
import requests
import hashlib
import time
import json
import random

'''
var r = function(e) {
            var t = "" + ((new Date).getTime() + parseInt(10 * Math.random(), 10));
            return {
                salt: t,
                sign: n.md5("fanyideskweb" + e + t + "6x(ZHw]mwzX#u0V7@yfwK")
            }
        };
t.recordUpdate = function(e) {
                var t = e.i,
                    i = r(t);
                n.ajax({
                    type: "POST",
                    contentType: "application/x-www-form-urlencoded; charset=UTF-8",
                    url: "/bettertranslation",
                    data: {
                        i: e.i,
                        client: "fanyideskweb",
                        salt: i.salt,
                        sign: i.sign,
                        tgt: e.tgt,
                        modifiedTgt: e.modifiedTgt,
                        from: e.from,
                        to: e.to
                    },
                    success: function(e) {},
                    error: function(e) {}
                })
            },
'''
# salt: t, -->"" + ((new Date).getTime() + parseInt(10 * Math.random(), 10))
# sign: n.md5("fanyideskweb" + e + t + "6x(ZHw]mwzX#u0V7@yfwK") -->n.md5("fanyideskweb" + e + salt + "6x(ZHw]mwzX#u0V7@yfwK")
# e为要翻译的内容
class Youdao(object):
    def __init__(self, msg):
        self.msg = msg
        self.url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
        self.salt = self.get_salt()
        self.sign = self.get_sign()

    def get_md(self,value):
        m = hashlib.md5()
        m.update(value.encode('utf-8'))
        return m.hexdigest()

    def get_salt(self):
        # ((new Date).getTime() + parseInt(10 * Math.random(), 10))
        salt = time.time()+random.randint(0, 10)
        return str(salt)

    def get_sign(self):
        # n.md5("fanyideskweb" + e + t + "6x(ZHw]mwzX#u0V7@yfwK") -->n.md5("fanyideskweb" + e + salt + "6x(ZHw]mwzX#u0V7@yfwK")
        s = "fanyideskweb" + self.msg+self.salt+"6x(ZHw]mwzX#u0V7@yfwK"
        return self.get_md(s)

    def get_result(self):
        headers={
            "Host":"fanyi.youdao.com",
            "Referer":"http://fanyi.youdao.com/",
            "User-Agent":"Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36",
            "Cookie":"OUTFOX_SEARCH_USER_ID=-1844872243@10.168.8.61; JSESSIONID=aaauMEFbbRO4vfKFef5Aw; OUTFOX_SEARCH_USER_ID_NCOO=1005302795.9300351; ___rl__test__cookies=1540709227673",
            "X-Requested-With": "XMLHttpRequest"
        }
        data={
            "i": self.msg,
            "from": "AUTO",
            "to": "AUTO",
            "smartresult": "dict",
            "client": "fanyideskweb",
            "salt":self.salt,
            "sign": self.sign,
            "doctype": "json",
            "version": "2.1",
            "keyfrom": "fanyi.web",
            "action": "FY_BY_REALTIME",
            "typoResult": "false"
        }

        response = requests.post(self.url,data=data,headers=headers)
        html = response.text
        w = json.loads(html)
        print(w["translateResult"][0][0]["tgt"])
        if 'smartResult' in w:
            results = [x for x in w["smartResult"]["entries"]]
            for i in results:
                print(i)



if __name__ == '__main__':
    while True:
        words = input('输入要翻译的内容：(输入0退出)')
        if words=='0':
            break
        y = Youdao(words)
        y.get_result()
