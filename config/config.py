from test_case.test_api_login import TestLogin
# 提取公共配置 环境、地址

login = TestLogin()
# 地址
init_url = {
    '测试环境': 'http://jwzt.jiwusiwei.com/',
    '预生产环境': '',
    '生产环境': ''
}

# 具体接口地址
api_url = {
    'login': 'admin-api/system/auth/login',
    'brand': 'admin-api/product-center/base-brand/page',
    'spec': 'admin-api/product-center/base-unit/page',
    'tag': 'admin-api/product-center/base-tag/page',
    'allergen': 'admin-api/product-center/base-allergens/page',
    'dept' : 'admin-api/product-center/base-production-dept/list',
    'product_sub': 'admin-api/product-center/new-submission/create'

}
# url = init_url['测试环境'] + api_url['login']
url = init_url['测试环境']

# headers={
#             "Content-Type": "application/json",
#             "Accept": "application/json, */*",
#             'Authorization': login.test_login()
#         }
