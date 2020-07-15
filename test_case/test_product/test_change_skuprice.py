
from tools.api import request_tool


'''
自动生成 数字 20,80   #生成20到80之间的数字 例：56
自动生成 字符串 5 中文数字字母特殊字符 xuepl        #生成以xuepl开头加上长度2到5位包含中文数字字母特殊字符的字符串，例子：xuepl我1
自动生成 地址
自动生成 姓名
自动生成 手机号
自动生成 邮箱
自动生成 身份证号
'''


def test_addprod(pub_data):
    pub_data["productCode"] = "自动生成 字符串 4 数字 kds"
    method = "POST"  #请求方法，全部大写
    feature = "产品模块"  # allure报告中一级分类
    story = '创建产品'  # allure报告中二级分类
    title = "全字段正常流_1"  # allure报告中用例名字
    uri = "/product/addProd"  # 接口地址
    status_code = 200  # 响应状态码
    expect = "创建产品成功"  # 预期结果
    headers = {"token": pub_data["token"]}
    json_data='''{
  "brand": "乐视",
  "colors": [
    "白色",
    "黑色"
  ],
  "price": 3000,
  "productCode": "${productCode}",
  "productName": "乐视电视",
  "sizes": [
    "X"
  ],
  "type": "epic"
}'''
    # json path，参数类型为列表 根据jsonpath提取响应正文中的数据
    json_path = [{"skuCode": '$.data[0].skuCode'}]
    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    request_tool.request(json_path=json_path,headers=headers,method=method,url=uri,pub_data=pub_data,status_code=status_code,expect=expect,feature=feature,story=story,title=title,json_data=json_data)


def test_changePrice(pub_data):
    method = "POST"  #请求方法，全部大写
    feature = "用户模块"  # allure报告中一级分类
    story = '用户登录'  # allure报告中二级分类
    title = "全字段正常流_1"  # allure报告中用例名字
    uri = "/product/changePrice"  # 接口地址
    status_code = 200  # 响应状态码
    expect = "价格更新成功"  # 预期结果
    headers = {"token": pub_data["token"]}
    data={'SKU': '${skuCode}', 'price': '2000'}

    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    request_tool.request(headers=headers,method=method,url=uri,pub_data=pub_data,status_code=status_code,expect=expect,feature=feature,story=story,title=title,data=data)


def test_getSKU(pub_data):
    method = "GET"  #请求方法，全部大写
    feature = "用户模块"  # allure报告中一级分类
    story = '用户登录'  # allure报告中二级分类
    title = "全字段正常流_1"  # allure报告中用例名字
    uri = "/product/getSKU"  # 接口地址
    headers = {"token": pub_data["token"]}
    status_code = 200  # 响应状态码
    expect = "查询成功"  # 预期结果
    params={'SKU': '${skuCode}'}

    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    request_tool.request(method=method,url=uri,pub_data=pub_data,status_code=status_code,headers=headers,expect=expect,feature=feature,story=story,title=title,params=params)
