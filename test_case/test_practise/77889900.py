import random

import allure
import requests

from config.conf import API_URL


@allure.feature("用户管理")  # 一级分类
@allure.story("用户充值模块")  # 二级分类
@allure.title("充值接口-全字段正常流")  # 修改用例标题
def test_kds_recharge(db):
    with allure.step("第一步，执行SQL语句"):
        res = db.select_execute("SELECT `account_name` FROM `t_cst_account` WHERE `status` = 0 AND `account_name` IS NOT NULL;")
        allure.attach("SELECT `account_name` FROM `t_cst_account` WHERE `status` = 0 AND `account_name` IS NOT NULL;",
                      "执行的SQL语句",allure.attachment_type.TEXT)
    with allure.step("第二步，从查询结果中随机获取一条，取第一个数据"):
        account_name = random.choice(res)[0]
        allure.attach(account_name,"选取的数据",allure.attachment_type.TEXT)
    with allure.step("第三步，准备请求数据"):
        data = {
            "accountName": account_name,
            "changeMoney": 1000000
        }
        allure.attach(f"accountName: {account_name},changeMoney: 1000000","准备的请求数据",allure.attachment_type.TEXT)
    with allure.step("第四步，发送请求"):
        r = requests.post(f"{API_URL}/acc/recharge", json=data)
        allure.attach(f"requests.post({API_URL}/acc/recharge, json=data)","请求内容",allure.attachment_type.TEXT)
    with allure.step("第五步，获取请求内容"):
        allure.attach(r.request.method,"请求方法",allure.attachment_type.TEXT)
        allure.attach(r.request.url,"请求url",allure.attachment_type.TEXT)
        allure.attach(str(r.request.headers),"请求头",allure.attachment_type.TEXT)
        allure.attach(r.request.body,"请求正文",allure.attachment_type.TEXT)
    with allure.step("第六步，获取响应内容"):
        allure.attach(str(r.status_code),"响应状态码",allure.attachment_type.TEXT)
        allure.attach(str(r.headers),"响应头",allure.attachment_type.TEXT)
        allure.attach(r.text,"响应正文",allure.attachment_type.TEXT)
    with allure.step("第七步，断言"):
        allure.attach(r.text,"实际结果",allure.attachment_type.TEXT)
        allure.attach("充值成功","期望结果",allure.attachment_type.TEXT)
        assert "充值成功" in r.text


'''
# 首先生成报告
pytest 文件路径 --alluredir=reports/xml   # 等于号后面是报告储存位置
# 报告格式转换
allure generate reports/xml -o reports/html      # 前面是转换前的报告位置，后面是转换后的
'''
