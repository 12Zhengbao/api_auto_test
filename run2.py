import subprocess
import os
from log.log_loguru import setup_logger

logger = setup_logger()

def main():
    # 核心目录配置（和 pytest.ini 里的 --alluredir 对应）
    temp_dir = "./reports/temp"    # Allure原始数据目录
    report_dir = "./reports/html"  # 最终HTML报告目录

    logger.info("===== 开始执行所有用例 =====")
    # 1. 执行 pytest，去掉 check=True，允许用例失败
    # 等价于：pytest -vs --alluredir=./reports/temp
    subprocess.run(["pytest", '-vs'], shell=True)
    logger.info("===== 所有用例执行结束 =====")

    # 2. 检查是否生成了原始数据（先创建目录，避免报错）
    os.makedirs(temp_dir, exist_ok=True)
    if not os.listdir(temp_dir):
        logger.error("❌ 未生成Allure原始数据，请检查用例执行是否成功！")
        return

    logger.info("===== 正在生成Allure测试报告 =====")

    # ==============================================
    # 【只改这一句！！！原来的是列表，现在改成字符串】
    # ==============================================
    subprocess.run(
        f"allure generate {temp_dir} -o {report_dir} --clean",  # 就这一行变了
        shell=True
    )

    logger.info("✅ 测试报告生成成功！")
    logger.info(f"📊 报告路径：{os.path.abspath(report_dir)}/index.html")

    # 4. 自动打开报告（可选）
    logger.info("🔍 正在打开报告...")
    report_html = os.path.join(os.path.abspath(report_dir), "index.html")
    if os.path.exists(report_html):
        os.startfile(report_html)
    else:
        logger.warning(f"⚠️ 报告文件不存在：{report_html}")

if __name__ == "__main__":
    main()