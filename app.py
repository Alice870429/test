# -*- coding: utf-8 -*-


from __future__ import unicode_literals
# 引入套件
from flask import Flask, request, abort
# 初始化Flask物件
app = Flask(__name__)

# 這裡定義服務存放的位置，也就是使用者連線的網址


@app.route("/", methods=['GET'])
# 這個服務對應的方法
def basic_url():
    # return 來回傳使用者要收到的資料
    return '<h1>Hello 我是Laura!</h1><p>是目前就讀陽明交通大學管理科學所的碩二生——陳欣婷，也可以叫我Laura。同時也是ASML的IT部門實習生，工作內容主要是在幫工程師進行軟硬體除錯，除此之外也正在進行資料庫及庫存系統的建立，方便部門進行查帳，而透過這個系統幫助部門成功節省約百分之五十的時間在進行查帳。</p>'


@app.route("/map/w01-6", methods=['GET'])
def map_w01_6():
    return app.send_static_file('W01-6.html')


if __name__ == "__main__":
    app.run()
