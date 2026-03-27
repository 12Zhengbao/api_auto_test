import requests
from config.config import url, api_url
from conftest import api_headers
from log.log_loguru import setup_logger

logger = setup_logger()
class TestAllergen:
    """
    获取所有品牌信息
    """

    def test_allergen(self,api_headers):

        params = {
            "pageNo": "1",
            "pageSize": "10",
            "sortingFields[0]": "",  # 对应 sortingFields%5B0%5D
            "sortingFields[1]": ""   # 对应第二个 sortingFields%5B0%5D（实际是 [1]）
        }
        try:
            logger.info('过敏原查询开始')
            res = requests.get(url=url+api_url['allergen'], headers=api_headers, params=params, timeout=10)
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
            logger.info('过敏原查询结束')



if __name__ == '__main__':
    spec = TestAllergen()
    spec.test_allergen()
