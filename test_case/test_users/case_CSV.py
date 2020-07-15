import pytest

from tools.api import request_tool
from tools.data import excel_tool

data1 = excel_tool.get_test_case("E:\\auto_api_kds\\test_case\\test_users\\充值接口测试数据(1).xlsx")
'''
自动生成 数字 20,80   #生成20到80之间的数字 例：56
自动生成 字符串 5 中文数字字母特殊字符 xuepl        #生成以xuepl开头加上长度2到5位包含中文数字字母特殊字符的字符串，例子：xuepl我1
自动生成 地址
自动生成 姓名
自动生成 手机号
自动生成 邮箱
自动生成 身份证号
'''


@pytest.mark.parametrize("account_name,balance,expected",data1[1],ids=data1[0])
def test_kds_recharge(pub_data,account_name,balance,expected):
    pub_data["account_name"] = account_name
    pub_data["balance"] = balance
    pub_data["expected"] = expected
    method = "POST"  #请求方法，全部大写
    feature = "用户模块"  # allure报告中一级分类
    story = '用户充值'  # allure报告中二级分类
    title = "全字段正常流_1"  # allure报告中用例名字
    uri = "/acc/recharge"  # 接口地址
    status_code = 200  # 响应状态码
    expect = "${expected}"  # 预期结果
    json_data='''{
  "accountName": "${account_name}",
  "changeMoney": "${balance}"
}'''

    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    request_tool.request(method=method,url=uri,pub_data=pub_data,status_code=status_code,expect=expect,feature=feature,story=story,title=title,json_data=json_data)




