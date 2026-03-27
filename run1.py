import subprocess
from log.log_loguru import setup_logger
import os
import shutil

logger = setup_logger()
# ========== 核心配置 ==========
TEST_DIR = "test_case/"
REPORT_DIR = "./reports/html"
# 生成Pytest原生测试报告（junit格式，Allure可解析）
JUNIT_DIR = "./reports/junit"
os.makedirs(JUNIT_DIR, exist_ok=True)
os.makedirs(REPORT_DIR, exist_ok=True)

# ========== 步骤1：执行用例，生成junit格式报告（Allure可解析） ==========
logger.info("===== 开始执行所有用例 =====")
pytest_cmd = [
    "pytest", TEST_DIR, "-vs",
    "--junitxml", os.path.join(JUNIT_DIR, "results.xml")  # 生成junit格式报告
]
result = subprocess.run(
    pytest_cmd,
    shell=True,
    cwd=os.getcwd(),
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    text=True,
    encoding="utf-8"
)
logger.info(f"Pytest执行日志：\n{result.stdout}")
if result.stderr:
    logger.warning(f"Pytest警告：\n{result.stderr}")
logger.info("===== 所有用例执行结束 =====")

# ========== 步骤2：用Allure解析junit报告，生成可视化HTML ==========
if os.path.exists(os.path.join(JUNIT_DIR, "results.xml")):
    # 清空旧报告
    shutil.rmtree(REPORT_DIR, ignore_errors=True)
    # 核心命令：Allure解析junit格式数据生成报告
    allure_cmd = f"allure generate {JUNIT_DIR} -o {REPORT_DIR} --clean"
    os.system(allure_cmd)
    print(f"\n✅ 测试报告生成成功！")
    print(f"✅ 报告路径：{os.path.abspath(REPORT_DIR)}/index.html")
    # 自动打开报告（Windows）
    os.startfile(os.path.join(REPORT_DIR, "index.html"))
else:
    print("\n❌ 未生成junit报告，请检查用例执行是否正常！")