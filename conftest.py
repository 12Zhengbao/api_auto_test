# conftest.py
import pytest
import requests
import allure

# 登录+登出夹具（session级别：全局只执行1次登录+1次登出）
@pytest.fixture(scope="session")
def token():
    """前置：登录获取token；后置：登出清理"""
    # ====== 前置操作：登录 ======
    login_url = 'http://jwzt.jiwusiwei.com/admin-api/system/auth/login'
    login_data = {"tenantName": "优海源码", "username": "13335397327", "password": "123456", "rememberMe": True}
    res = requests.post(login_url, headers={"Content-Type":"application/json"}, json=login_data, timeout=10)
    token = res.json()['data']['accessToken']
    print("【前置】登录成功，获取token：", token[:10], "...")

    # yield返回token给用例，yield后是后置操作
    yield token

    # ====== 后置操作：登出 ======
    # logout_url = 'http://jwzt.jiwusiwei.com/admin-api/system/auth/logout'  # 替换成真实登出接口
    # try:
    #     logout_res = requests.post(logout_url, headers={"token": token}, timeout=10)
    #     print("【后置】登出成功，状态码：", logout_res.status_code)
    # except Exception as e:
    #     print("【后置】登出失败：", e)

# 带token的请求头夹具（无需改）
@pytest.fixture(scope="function")
def api_headers(token):    # 只能使用pytest时调用
    """生成带token的请求头（纯dict，无任何对象嵌套）"""
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {token}",  # 优先试这个！
        "Accept": "application/json, */*"
    }
    # 仅返回纯字典，避免Pytest识别为夹具对象
    return headers

#=======================================压力测试专用获取token=============================================
# 压力测试调用
def get_api_headers():
    """脱离 pytest 夹具，直接定义获取请求头的函数"""

    # 先手动获取 token（复用你的 token 逻辑）
    def get_token():
        # ====== 前置操作：登录 ======
        login_url = 'http://jwzt.jiwusiwei.com/admin-api/system/auth/login'
        login_data = {"tenantName": "优海源码", "username": "13335397327", "password": "123456", "rememberMe": True}
        res = requests.post(login_url, headers={"Content-Type": "application/json"}, json=login_data, timeout=10)
        new_token = res.json()['data']['accessToken']
        print("【前置】登录成功，获取token：", new_token[:10], "...")
        return new_token  # 替换为真实 token 获取逻辑

    token = get_token()
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {token}",
        "Accept": "application/json, */*"
    }
    return headers

# ========== Allure 全局钩子：用例失败时自动记录详情 ==========
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    捕获用例执行结果，失败时自动添加详情到Allure报告
    （单例/批量执行时，失败用例都会自动记录）
    """
    # 获取用例执行结果
    outcome = yield
    rep = outcome.get_result()

    # 只处理用例执行阶段（call）的失败
    if rep.when == "call" and rep.failed:
        # 添加失败原因到Allure报告
        allure.attach(
            f"用例失败详情：{rep.longrepr}",
            name="失败原因",
            attachment_type=allure.attachment_type.TEXT
        )
        # 添加用例名称到报告
        allure.attach(
            f"用例名称：{item.nodeid}",
            name="用例标识",
            attachment_type=allure.attachment_type.TEXT
        )


# ========== 自定义命令行参数（可选，不影响报告生成） ==========
def pytest_addoption(parser):
    # 添加环境参数（比如：--env=test/prod）
    parser.addoption("--env", default="test", help="运行环境：test/生产")


# ========== 全局Fixture：获取运行环境（可选） ==========
@pytest.fixture(scope="session")
def env(request):
    return request.config.getoption("--env")