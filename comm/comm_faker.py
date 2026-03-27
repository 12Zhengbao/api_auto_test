from faker import Faker
import random
from datetime import datetime

# 1. 初始化Faker（支持中文）
fake = Faker(locale='zh_CN')  # 指定中文环境，默认是en_US


# ===================== 2. 基础数据生成（直接可用） =====================
def generate_basic_data():
    """生成基础随机数据"""
    # 个人信息
    name = fake.name()  # 随机姓名：如 "张三"
    phone = fake.phone_number()  # 随机手机号：如 "13812345678"
    id_card = fake.ssn()  # 随机身份证号
    email = fake.email()  # 随机邮箱：如 "zhangsan@example.com"

    # 地址信息
    address = fake.address()  # 随机地址：如 "上海市徐汇区虹桥路123弄45号678室"
    province = fake.province()  # 省份：如 "广东省"
    city = fake.city()  # 城市：如 "深圳市"

    # 公司信息
    company = fake.company()  # 公司名称：如 "北京科技发展有限公司"
    job = fake.job()  # 职位：如 "软件工程师"

    # 文本/数字
    text = fake.text(max_nb_chars=100)  # 随机文本
    number = fake.random_int(min=1, max=1000)  # 随机整数
    float_num = fake.pyfloat(left_digits=3, right_digits=2, positive=True)  # 随机浮点数

    # 时间
    date = fake.date()  # 随机日期：如 "2025-06-18"
    datetime_str = fake.date_time().strftime("%Y-%m-%d %H:%M:%S")  # 随机时间

    return {
        "姓名": name,
        "手机号": phone,
        "身份证号": id_card,
        "邮箱": email,
        "地址": address,
        "公司名称": company,
        "职位": job,
        "随机文本": text,
        "随机整数": number,
        "随机日期": date,
        "随机时间": datetime_str
    }


# ===================== 3. 自定义生成规则（适配你的业务场景） =====================
class CustomFaker(Faker):
    """自定义Faker类，适配你的新品提报压测场景"""

    def fake_product_name(self):
        """生成随机菜品名称"""
        # 自定义菜品前缀+随机后缀
        prefixes = ["香辣", "清蒸", "红烧", "爆炒", "凉拌", "油炸", "酱香"]
        foods = ["牛肉", "排骨", "鱼块", "茄子", "土豆", "鸡翅", "虾仁", "豆腐"]
        return f"{random.choice(prefixes)}{random.choice(foods)}"

    def fake_brand_id(self):
        """生成随机品牌ID（数字格式）"""
        return fake.random_int(min=10, max=99)  # 生成10-99的随机品牌ID

    def fake_spec_name(self):
        """生成随机规格名称"""
        units = ["份", "斤", "克", "升", "瓶", "包"]
        return f"{fake.random_int(min=1, max=5)}{random.choice(units)}"

    def fake_product_desc(self):
        """生成随机产品描述"""
        adjectives = ["美味", "可口", "新鲜", "正宗", "特色", "秘制"]
        contents = ["精选食材制作", "口感丰富", "营养均衡", "老少皆宜", "回味无穷"]
        return f"{random.choice(adjectives)}的菜品，{random.choice(contents)}。"

    def fake_tag_name(self):
        """生成随机标签名称"""
        tags = ["家常菜", "网红菜", "下饭菜", "招牌菜", "新品", "特惠", "爆款"]
        return random.choice(tags)


# ===================== 4. 结合你的压测场景使用 =====================
def generate_test_data_for_stress_test():
    """生成适配你新品提报压测的随机数据"""
    # 初始化自定义Faker
    custom_fake = CustomFaker(locale='zh_CN')

    # 生成随机测试数据
    test_data = {
        "newSubmission": {
            "brandId": str(custom_fake.fake_brand_id()),  # 随机品牌ID
            "productName": custom_fake.fake_product_name(),  # 随机菜品名称
            "bigCategoryId": str(fake.random_int(min=368055927510702110, max=368055927510702199)),
            "smallCategoryId": str(fake.random_int(min=368056882339813464, max=368056882339813499)),
            "bigCategoryName": "厨房",
            "smallCategoryName": "早午餐",
            "productDescription": custom_fake.fake_product_desc(),  # 随机产品描述
            "productAdvantage": fake.text(max_nb_chars=50),  # 随机产品优势
            "userId": str(fake.random_int(min=1, max=100)),
            "submissionPurpose": str(fake.random_int(min=1, max=5)),
            "state": "0"
        },
        "remarkTagRelation": {
            # 随机生成1-3个标签
            "productTagList": [
                {
                    "id": str(fake.random_int(min=400, max=500)),
                    "parentId": str(fake.random_int(min=300, max=400)),
                    "code": f"{fake.random_int(min=1, max=99)}",
                    "name": custom_fake.fake_tag_name(),  # 随机标签名称
                    "enableStr": "可用",
                    "remark": fake.text(max_nb_chars=20),
                    "createTime": fake.date_time().strftime("%Y%m%d%H%M%S"),
                    "creatorName": fake.name(),
                    "updateTime": fake.date_time().strftime("%Y%m%d%H%M%S"),
                    "updaterName": fake.name(),
                    "parentName": None,
                    "type": str(fake.random_int(min=1, max=5)),
                    "enable": "1",
                    "creator": str(fake.random_int(min=1, max=100)),
                    "updater": str(fake.random_int(min=1, max=100))
                } for _ in range(random.randint(1, 3))
            ],
            "remarkTagList": [
                {
                    "id": str(fake.random_int(min=400, max=500)),
                    "parentId": str(fake.random_int(min=300, max=400)),
                    "code": f"{fake.random_int(min=1, max=99)}",
                    "name": custom_fake.fake_tag_name(),
                    "enableStr": "可用",
                    "remark": fake.text(max_nb_chars=20),
                    "createTime": fake.date_time().strftime("%Y%m%d%H%M%S"),
                    "creatorName": fake.name(),
                    "updateTime": fake.date_time().strftime("%Y%m%d%H%M%S"),
                    "updaterName": fake.name(),
                    "parentName": None,
                    "type": str(fake.random_int(min=1, max=5)),
                    "enable": "1",
                    "creator": str(fake.random_int(min=1, max=100)),
                    "updater": str(fake.random_int(min=1, max=100))
                }
            ]
        },
        "specRelationList": [
            {
                "specId": str(fake.random_int(min=1000, max=2000)),
                "name": custom_fake.fake_spec_name(),  # 随机规格名称
                "standardWeight": str(fake.random_int(min=1, max=50)),
                "weightUnit": str(fake.random_int(min=1000, max=2000)),
                "displayName": custom_fake.fake_spec_name(),
                "estimatedPrice": str(fake.pyfloat(left_digits=2, right_digits=2, positive=True)),
                "bomRelationList": [
                    {
                        "code": fake.pystr(min_chars=8, max_chars=12),
                        "name": fake.word(),
                        "itemName": fake.word(),
                        "specDesc": fake.text(max_nb_chars=30),
                        "categoryName": fake.word(),
                        "unitPriceIncludingTax": "0",
                        "supplierName": fake.company(),
                        "brandName": fake.company_prefix(),
                        "netMaterialRate": "100",
                        "allergensName": fake.word(),
                        "relationProductNum": str(fake.random_int(min=1, max=10)),
                        "enableName": "启用",
                        "createName": fake.name(),
                        "createTime": fake.date_time().strftime("%Y%m%d%H%M%S"),
                        "updateName": fake.name(),
                        "updateTime": fake.date_time().strftime("%Y%m%d%H%M%S"),
                        # 省略其他固定字段...
                        "isPrimaryIngredient": "1"
                    }
                ],
                "isDisplayNameTouched": "False",
                "unit1": str(fake.random_int(min=1000, max=2000))
            }
        ],
        "competitorRelationList": []
    }
    return test_data


# ===================== 5. 调用示例 =====================
if __name__ == "__main__":
    # 示例1：生成基础随机数据
    basic_data = generate_basic_data()
    print("=== 基础随机数据 ===")
    for key, value in basic_data.items():
        print(f"{key}: {value}")

    # 示例2：生成自定义压测数据
    stress_test_data = generate_test_data_for_stress_test()
    print("\n=== 自定义压测数据 ===")
    print(f"随机生成的菜品名称：{stress_test_data['newSubmission']['productName']}")
    print(f"随机生成的品牌ID：{stress_test_data['newSubmission']['brandId']}")
    print(f"随机生成的产品描述：{stress_test_data['newSubmission']['productDescription']}")