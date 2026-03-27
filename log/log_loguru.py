from loguru import logger
import os
import sys
import time
from datetime import datetime

# 全局缓存：避免重复添加处理器，防止日志串文件/丢失
HANDLER_CACHE = {}

def setup_logger():
    """
    自动识别执行模式，全程仅改此文件，run.py不动：
    - 批量执行（pytest）：按测试文件分日志
    - 单个执行（直接运行py）：按当前文件生成日志
    """
    # 1. 只移除默认处理器一次，避免日志丢失
    if not HANDLER_CACHE:
        logger.remove()

    # 核心：过滤Windows非法文件名字符（解决OSError）
    def clean_filename(name):
        for char in ['<', '>', ':', '"', '/', '\\', '|', '?', '*']:
            name = name.replace(char, '_')
        return name

    # 2. 识别执行场景 + 获取合法日志名
    try:
        # 批量执行（pytest）：找test_case下的真实测试文件
        if "pytest" in sys.argv[0]:
            frame = sys._getframe()
            target_file = None
            while frame:
                f_path = frame.f_code.co_filename
                if "test_case" in f_path and f_path.endswith(".py"):
                    target_file = f_path
                    break
                frame = frame.f_back
            log_name = clean_filename(os.path.splitext(os.path.basename(target_file))[0]) if target_file else f"batch_{int(time.time())}"
        # 单个执行：直接用当前运行的文件名称
        else:
            current_file = sys.argv[0]
            log_name = clean_filename(os.path.splitext(os.path.basename(current_file))[0])
    except:
        # 兜底：防止异常，生成唯一名称
        log_name = f"test_{int(time.time())}"

    # 3. 日志目录 + 文件名（确保路径合法）
    log_dir = os.path.join(os.path.dirname(__file__), 'logs')
    os.makedirs(log_dir, exist_ok=True)
    log_file = os.path.join(log_dir, f"{log_name}_{datetime.now().strftime('%Y-%m-%d')}.log")

    # 4. 每个日志文件只添加一次处理器，避免重复写入
    if log_name not in HANDLER_CACHE:
        # 文件处理器：只写入当前文件的日志，彻底防串
        file_id = logger.add(
            log_file,
            encoding="utf-8",
            format="{time:YYYY-MM-DD HH:mm:ss} | {level:8} | {file}:{function}:{line} | {message}",
            rotation="00:00",
            retention="30 days",
            enqueue=True,
            filter=lambda r: clean_filename(os.path.splitext(os.path.basename(r["file"].path))[0]) == log_name
        )
        HANDLER_CACHE[log_name] = file_id

    # 5. 控制台输出（只加一次，带颜色，run.py执行时也能显示）
    if "console" not in HANDLER_CACHE:
        console_id = logger.add(
            sys.stdout,
            format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level:8}</level> | <cyan>{file}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> | <level>{message}</level>",
            level="INFO",
            colorize=True
        )
        HANDLER_CACHE["console"] = console_id

    return logger

# 保留你要求的全局初始化，无递归、无空日志
logger = setup_logger()