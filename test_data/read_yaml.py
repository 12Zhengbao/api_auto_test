import yaml
import os

def read_login_data():
    """读取YAML格式的登录测试数据"""
    # 1. 获取项目根目录
    root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    # 2. 拼接YAML文件路径
    data_path = os.path.join(root_dir, "test_data", "data_yaml.yml")
    # 3. 读取YAML文件（注意：YAML读取用yaml.safe_load）
    with open(data_path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)  # 替代json.load，安全读取YAML

# 通用读取方法（适配所有YAML文件）
def read_yaml(file_name):
    root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    data_path = os.path.join(root_dir, "test_data", file_name)
    with open(data_path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)