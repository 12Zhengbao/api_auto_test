import pytest
import requests
from config.config import url, api_url
from log.log_loguru import setup_logger
from conftest import api_headers
# import allure

logger = setup_logger()

# @pytest.mark.usefixtures("api_headers")
class TestDept:
    """
    获取所有品牌信息
    """

    def test_dept(self, api_headers):

        params = {
            "pageNo": "1",
            "pageSize": "10",
        }
        try:
            logger.info('出品部门查询开始')
            res = requests.get(url=url+api_url['dept'], headers=api_headers, params=params, timeout=10)
            logger.info(f'响应内容：{res.json()}')
            assert res.json().get('msg') == '', logger.info(f'断言不通过，响应内容为：f{res.json().get('msg')}')
            # logger.info(f'断言内容f{res.json().get('msg')}')

        except AssertionError as ae:
            # 修复2：捕获断言异常，打日志后重新抛出（让pytest识别失败）
            logger.error(f'断言失败：{ae}')
            raise  # 关键：抛出异常，pytest才会标记用例FAILED
        except Exception as err:
            logger.error(f'接口执行异常：{err}')
            raise  # 其他异常也抛出
        finally:
            logger.info('出品部门查询结束')



if __name__ == '__main__':

    spec = TestDept()
    spec.test_dept(api_headers)
