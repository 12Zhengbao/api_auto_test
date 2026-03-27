import subprocess
from log.log_loguru import setup_logger
import os
import shutil

logger = setup_logger()
logger.info("===== 开始执行所有用例 =====")
subprocess.run(["pytest", "test_case/", "-vs"], shell=True)
logger.info("===== 所有用例执行结束 =====")
