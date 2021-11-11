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
    return '<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8"></meta>
    <title>安安</title>
    <style type="text/css">
    .head{
        background-color: #005AB5; color: white; font-weight: bold; font-size: 20px;
        text-align: center; padding: 10px;
    }

    .content{
        width:1000px; margin-left: auto; margin-right: auto;
    }

    .box{
        width: 280px; padding:10px; margin: 10px; background-color: white;
        display: inline-block; vertical-align: top;
        text-align: center;  height: 150px; line-height: 30px;
    }

    .title{font-weight: bold;}
    </style>
</head>
<body style="margin: 0px; background-color: #EEEEEE;">
    <div class="head">陳欣婷 Laura Chen</div>
    <div class="content">
        <div class="box">
            <div class="title">我的基本資料</div>
            <div>安安你好</div>
            <div>安安你好</div>
            <div>安安你好</div>
        </div>
        <div class="box">
            <div class="title">我的個人興趣</div>
            <div>安安你好</div>
            <div>安安你好</div>
            <div>安安你好</div>
        </div>
        <div class="box">
            <div class="title">觀迎與我聯絡</div>
            <div>安安你好</div>
            <div>安安你好</div>
            <div>安安你好</div>
        </div>
    </div>
</body>
</html>'


@app.route("/map/w01-6", methods=['GET'])
def map_w01_6():
    return app.send_static_file('W01-6.html')


if __name__ == "__main__":
    app.run()
