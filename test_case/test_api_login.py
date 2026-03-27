import pytest
import requests
from log.log_loguru import setup_logger
from test_data.read_yaml import read_login_data

logger = setup_logger()
login_data = read_login_data()

class TestLogin(object):
    """
    登录：
    """
    @pytest.mark.parametrize("case_name, case_data", login_data.items())
    def test_login(self, case_name, case_data):
        logger.info('开始登录测试')
        self.url = 'http://jwzt.jiwusiwei.com/admin-api/system/auth/login'
        self.headers = {
            "Content-Type": "application/json",
            "Accept": "application/json, */*"
        }
        try:

            res = requests.post(url=self.url, headers=self.headers, json=case_data['input'], timeout=10)
            logger.info(f'响应内容：{res.json()}')
            # assert res.json().get('msg') == '',  f'断言不通过'
            assert res.json().get('msg') == '', \
                f'[{case_name}] 断言失败：预期msg为空字符串，实际msg="{res.json().get("msg")}"'
            logger.success(f"登录成功，获取到token：{res.json().get('data').get('accessToken')}")
            return res.json().get('data').get('accessToken')
        except AssertionError as ae:
            # 修复2：捕获断言异常，打日志后重新抛出（让pytest识别失败）
            logger.error(f'断言失败：{ae}')
            raise  # 关键：抛出异常，pytest才会标记用例FAILED
        except Exception as err:
            logger.error(f'接口执行异常：{err}')
            raise  # 其他异常也抛出
        finally:
            logger.info('登录测试结束')



if __name__ == '__main__':
    login = TestLogin()
    login.test_login()