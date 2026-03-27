import requests
from config.config import url, api_url
from conftest import get_api_headers
from log.log_loguru import setup_logger
import time
from datetime import datetime
# from comm.comm_faker import CustomFaker
from faker import Faker

# fakers = CustomFaker()
logger = setup_logger()

fake = Faker(locale='zh_CN')


# 压测配置
TOTAL_REQUEST_NUM = 50  # 总请求数
REQUEST_INTERVAL = 0.1  # 每次请求间隔（秒），0表示无间隔
REPORT_FILE = "新品提报压力测试报告.html"  # HTML报告文件名


class NewProduct:
    """
    进行新品提报的压力测试
    """

    def product_submission(self, get_api_headers):
        """
        新品提报压测
        :return:
        """
        logger.info("开始压力测试")
        try:
            number = fake.random_int(min=1, max=99999)
            api_json = {
                "newSubmission": {
                    "brandId": "39",
                    "productName": f"菜品{number}",
                    "bigCategoryId": "368055927510702110",
                    "smallCategoryId": "368056882339813464",
                    "bigCategoryName": "厨房",
                    "smallCategoryName": "早午餐",
                    "productDescription": "这是新品描述",
                    "productAdvantage": "这是新品优势",
                    "userId": 1,
                    "submissionPurpose": 1,
                    "state": "0"
                },
                "remarkTagRelation": {
                    "productTagList": "[{\"id\":437,\"parentId\":434,\"code\":\"03\",\"name\":\"测试\",\"enableStr\":\"可用\",\"remark\":\"这是说明\\n\",\"createTime\":1770176880000,\"creatorName\":\"优海管理员\",\"updateTime\":1771032993000,\"updaterName\":\"郑宝宝\",\"parentName\":null,\"type\":1,\"enable\":1,\"creator\":\"1\",\"updater\":\"151\"},{\"id\":436,\"parentId\":434,\"code\":\"02\",\"name\":\"女士专属\",\"enableStr\":\"可用\",\"remark\":\"\\\\\",\"createTime\":1770176880000,\"creatorName\":\"优海管理员\",\"updateTime\":1770176880000,\"updaterName\":\"优海管理员\",\"parentName\":null,\"type\":1,\"enable\":1,\"creator\":\"1\",\"updater\":\"1\"},{\"id\":435,\"parentId\":434,\"code\":\"01\",\"name\":\"无辣不欢\",\"enableStr\":\"可用\",\"remark\":\"\\\\\",\"createTime\":1770176880000,\"creatorName\":\"优海管理员\",\"updateTime\":1770176880000,\"updaterName\":\"优海管理员\",\"parentName\":null,\"type\":1,\"enable\":1,\"creator\":\"1\",\"updater\":\"1\"}]",
                    "remarkTagList": "[{\"id\":433,\"parentId\":432,\"code\":\"009961\",\"name\":\"0203备注标签\",\"enableStr\":\"可用\",\"remark\":\"这是0203的备注标签\",\"createTime\":1770106680000,\"creatorName\":\"郑宝宝\",\"updateTime\":1770106680000,\"updaterName\":\"郑宝宝\",\"parentName\":null,\"type\":2,\"enable\":1,\"creator\":\"151\",\"updater\":\"151\"}]"
                },
                "specRelationList": [
                    {
                        "specId": 1397,
                        "name": "规格1",
                        "standardWeight": "12",
                        "weightUnit": 1453,
                        "displayName": "菜品-1/大份",
                        "estimatedPrice": "12",
                        "bomRelationList": [
                            {
                                "code": "1110012",
                                "name": "冰霖葡萄味烧酒360ML",
                                "itemName": "冰霖葡萄味烧酒360ML",
                                "specDesc": "360ML*20瓶/箱",
                                "categoryName": "酒水饮料\\烧酒",
                                "unitPriceIncludingTax": 0,
                                "supplierName": "\\",
                                "brandName": "\\",
                                "netMaterialRate": 100,
                                "allergensName": "\\",
                                "relationProductNum": 7,
                                "enableName": "启用",
                                "createName": "郑宝宝",
                                "createTime": 1771898855000,
                                "updateName": "优海管理员",
                                "updateTime": 1772266888000,
                                "searchValue": None,
                                "remark": None,
                                "params": None,
                                "prop": None,
                                "orderNum": None,
                                "operationCode": None,
                                "itemId": 23673,
                                "promotionName": None,
                                "englishName": None,
                                "otherName": None,
                                "inputCode": "BLPTWSJ360ML",
                                "isUseQualityGuaranteePeriod": False,
                                "qualityGuaranteePeriod": None,
                                "qualityGuaranteePeriodUnit": None,
                                "bigCategoryId": 1877,
                                "smallCategoryId": 1894,
                                "category1": None,
                                "costType": None,
                                "isForceEnterProductionDate": False,
                                "isConsumables": False,
                                "enable": 1,
                                "isOrderingPolicy": False,
                                "isShared": True,
                                "warehouseQuantity": 0,
                                "itemIds": None,
                                "barcode": None,
                                "deptId": None,
                                "otherWarehouseId": None,
                                "centerInvoiceTaxRate": 0,
                                "supplierIdList": None,
                                "taxClassificationCode": "1030306000000000000",
                                "taxClassificationName": "酒",
                                "isShowImage": False,
                                "fileUrl": None,
                                "checkBoxGauge": False,
                                "warmArea": None,
                                "isTaxFree": None,
                                "fileUrlList": None,
                                "isVerified": None,
                                "isPurchaseType": None,
                                "bigCategoryName": "酒水饮料",
                                "smallCategoryName": "烧酒",
                                "category1Name": None,
                                "costTypeName": None,
                                "isSharedLabel": None,
                                "specCode": None,
                                "warehouseId": None,
                                "supplyTypeId": None,
                                "stockQuantity": 0,
                                "exportQuantity": 0,
                                "unitName": None,
                                "unitId": None,
                                "deptName": None,
                                "itemWarehouseId": None,
                                "upperLimit": None,
                                "lowerLimit": None,
                                "deptIds": None,
                                "categories": None,
                                "supplierId": None,
                                "allergens": None,
                                "updater": "1",
                                "creator": "151",
                                "brandId": None,
                                "relationProductList": [
                                    {
                                        "bomId": 304250,
                                        "itemId": 23673,
                                        "submissionId": 24327,
                                        "dishDevelopmentId": None,
                                        "productReleaseId": None,
                                        "dishCode": "XP000999",
                                        "submissionCode": "XP000999",
                                        "type": 1
                                    },
                                    {
                                        "bomId": 304250,
                                        "itemId": 23673,
                                        "submissionId": None,
                                        "dishDevelopmentId": None,
                                        "productReleaseId": None,
                                        "dishCode": "2511200009",
                                        "submissionCode": None,
                                        "type": 4
                                    },
                                    {
                                        "bomId": 304250,
                                        "itemId": 23673,
                                        "submissionId": None,
                                        "dishDevelopmentId": None,
                                        "productReleaseId": None,
                                        "dishCode": "2050124",
                                        "submissionCode": None,
                                        "type": 4
                                    },
                                    {
                                        "bomId": 304250,
                                        "itemId": 23673,
                                        "submissionId": None,
                                        "dishDevelopmentId": None,
                                        "productReleaseId": None,
                                        "dishCode": "1070037",
                                        "submissionCode": None,
                                        "type": 4
                                    },
                                    {
                                        "bomId": 304250,
                                        "itemId": 23673,
                                        "submissionId": None,
                                        "dishDevelopmentId": None,
                                        "productReleaseId": None,
                                        "dishCode": "XP12012345",
                                        "submissionCode": None,
                                        "type": 4
                                    },
                                    {
                                        "bomId": 304250,
                                        "itemId": 23673,
                                        "submissionId": None,
                                        "dishDevelopmentId": None,
                                        "productReleaseId": None,
                                        "dishCode": "XXX1110012",
                                        "submissionCode": None,
                                        "type": 4
                                    },
                                    {
                                        "bomId": 304250,
                                        "itemId": 23673,
                                        "submissionId": None,
                                        "dishDevelopmentId": None,
                                        "productReleaseId": None,
                                        "dishCode": "1150095XXX",
                                        "submissionCode": None,
                                        "type": 4
                                    }
                                ],
                                "creatorName": "郑宝宝",
                                "updaterName": "优海管理员",
                                "itemMinimumUnitName": None,
                                "itemMinimumUnit": None,
                                "originOfRawMaterials": None,
                                "type": 110,
                                "bomId": 304250,
                                "source": 110,
                                "estimatedUsage": "12.00",
                                "unit": 1460,
                                "isPrimaryIngredient": 1
                            }
                        ],
                        "isDisplayNameTouched": False,
                        "unit1": 1453
                    }
                ],
                "competitorRelationList": []
            }
            start_time = time.time()
            rep = requests.post(
                url=url + api_url["product_sub"], headers=get_api_headers, json=api_json, timeout=10
            )
            end_time = time.time()
            elapsed = round((end_time - start_time) * 1000, 2)  # 耗时（毫秒）

            # 断言响应结果
            rep_json = rep.json()
            if rep_json.get('msg') != '':
                raise AssertionError(f"响应msg非空：{rep_json.get('msg')}")
            return {
                "success": True,
                "elapsed_ms": elapsed,
                "status_code": rep.status_code,
                "error_msg": ""
            }

        except Exception as e:
            end_time = time.time() if 'start_time' in locals() else time.time()
            elapsed = round((end_time - start_time) * 1000, 2) if 'start_time' in locals() else 0
            return {
                "success": False,
                "elapsed_ms": elapsed,
                "status_code": getattr(rep, 'status_code', '未知') if 'rep' in locals() else '无响应',
                "error_msg": str(e)
            }
        finally:
            logger.info('单次接口请求结束')


# ===================== 压测执行与报告生成 =====================
def run_stress_test():
    """执行单线程压力测试并生成包含全量压测数据的HTML报告"""
    # 初始化
    new_product = NewProduct()
    headers = get_api_headers()  # 获取请求头字典
    start_time = datetime.now()
    total_start = time.time()

    # 统计数据（扩展全量压测指标）
    stats = {
        "total_request": TOTAL_REQUEST_NUM,
        "success": 0,
        "failed": 0,
        "total_elapsed_ms": 0,
        "max_elapsed_ms": 0,
        "min_elapsed_ms": float('inf'),
        "failed_cases": [],
        "response_times": [],  # 存储每次成功请求的响应时间
        "status_code_dist": {}  # 状态码分布统计
    }

    # 执行压测
    print(f"[{datetime.now()}] 开始单线程压力测试 | 总请求数：{TOTAL_REQUEST_NUM}")
    for i in range(TOTAL_REQUEST_NUM):
        print(f"[{datetime.now()}] 执行第 {i + 1}/{TOTAL_REQUEST_NUM} 次请求...")
        result = new_product.product_submission(headers)

        # 更新状态码分布
        code = result["status_code"]
        if code in stats["status_code_dist"]:
            stats["status_code_dist"][code] += 1
        else:
            stats["status_code_dist"][code] = 1

        # 更新核心统计
        if result["success"]:
            stats["success"] += 1
            stats["total_elapsed_ms"] += result["elapsed_ms"]
            stats["max_elapsed_ms"] = max(stats["max_elapsed_ms"], result["elapsed_ms"])
            stats["min_elapsed_ms"] = min(stats["min_elapsed_ms"], result["elapsed_ms"])
            stats["response_times"].append(result["elapsed_ms"])
        else:
            stats["failed"] += 1
            stats["failed_cases"].append({
                "request_num": i + 1,
                "error_msg": result["error_msg"],
                "status_code": result["status_code"],
                "elapsed_ms": result["elapsed_ms"]
            })

        # 请求间隔
        if REQUEST_INTERVAL > 0 and i < TOTAL_REQUEST_NUM - 1:
            time.sleep(REQUEST_INTERVAL)

    # 计算全量压测指标
    total_end = time.time()
    total_elapsed = round((total_end - total_start), 2)  # 总耗时（秒）
    avg_elapsed = round(stats["total_elapsed_ms"] / stats["success"], 2) if stats["success"] > 0 else 0
    success_rate = round(stats["success"] / stats["total_request"] * 100, 2) if stats["total_request"] > 0 else 0
    error_rate = round(stats["failed"] / stats["total_request"] * 100, 2) if stats["total_request"] > 0 else 0
    qps = round(stats["success"] / total_elapsed, 2) if total_elapsed > 0 else 0  # 每秒成功请求数
    throughput = round(stats["total_request"] / total_elapsed, 2) if total_elapsed > 0 else 0  # 总吞吐量

    # 计算响应时间分位值（P90/P95/P99）
    p90 = 0.0
    p95 = 0.0
    p99 = 0.0
    if stats["response_times"]:
        sorted_times = sorted(stats["response_times"])
        p90_idx = int(len(sorted_times) * 0.9) - 1 if len(sorted_times) >= 10 else len(sorted_times) - 1
        p95_idx = int(len(sorted_times) * 0.95) - 1 if len(sorted_times) >= 20 else len(sorted_times) - 1
        p99_idx = int(len(sorted_times) * 0.99) - 1 if len(sorted_times) >= 100 else len(sorted_times) - 1

        p90 = round(sorted_times[max(0, p90_idx)], 2)
        p95 = round(sorted_times[max(0, p95_idx)], 2)
        p99 = round(sorted_times[max(0, p99_idx)], 2)

    # 生成包含全量数据的HTML报告
    end_time = datetime.now()
    html_content = f'''
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>新品提报压力测试报告</title>
    <style>
        /* 全局极简样式 */
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: "Microsoft YaHei", Arial, sans-serif;
        }}
        body {{
            background: #f8f9fa;
            padding: 20px;
            color: #333;
        }}
        .report-wrapper {{
            max-width: 1200px;
            margin: 0 auto;
            background: white;
            padding: 30px;
            border-radius: 8px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.08);
        }}
        .report-header {{
            border-bottom: 1px solid #eee;
            padding-bottom: 20px;
            margin-bottom: 20px;
        }}
        .report-header h1 {{
            font-size: 22px;
            color: #2c3e50;
            margin-bottom: 10px;
        }}
        .report-header .meta {{
            font-size: 14px;
            color: #666;
        }}
        .section {{
            margin-bottom: 25px;
        }}
        .section-title {{
            font-size: 16px;
            color: #2c3e50;
            margin-bottom: 15px;
            font-weight: 600;
        }}
        /* 核心指标卡片 - 扩展为6列 */
        .metrics-card {{
            display: grid;
            grid-template-columns: repeat(6, 1fr);
            gap: 15px;
            margin-bottom: 20px;
        }}
        .metrics-card-2 {{
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 15px;
            margin-bottom: 20px;
        }}
        .metric-item {{
            background: #f5f7fa;
            padding: 15px;
            border-radius: 6px;
            text-align: center;
        }}
        .metric-item .label {{
            font-size: 13px;
            color: #666;
            margin-bottom: 5px;
        }}
        .metric-item .value {{
            font-size: 18px;
            font-weight: 600;
        }}
        .metric-item.success {{
            color: #27ae60;
        }}
        .metric-item.failed {{
            color: #e74c3c;
        }}
        .metric-item.normal {{
            color: #2c3e50;
        }}
        .metric-item.warning {{
            color: #f39c12;
        }}
        /* 表格样式 */
        table {{
            width: 100%;
            border-collapse: collapse;
            background: white;
            border-radius: 6px;
            overflow: hidden;
        }}
        th {{
            background: #f5f7fa;
            padding: 12px 15px;
            text-align: left;
            font-size: 13px;
            font-weight: 600;
            color: #2c3e50;
        }}
        td {{
            padding: 12px 15px;
            font-size: 13px;
            border-bottom: 1px solid #eee;
            color: #333;
        }}
        td.error {{
            color: #e74c3c;
        }}
        /* 图表区域 */
        .chart-area {{
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 20px;
            margin-top: 15px;
        }}
        .chart-box {{
            background: #f5f7fa;
            padding: 15px;
            border-radius: 6px;
            height: 300px;
        }}
        canvas {{
            width: 100%;
            height: 100%;
        }}
        /* 响应式适配 */
        @media (max-width: 1024px) {{
            .metrics-card {{
                grid-template-columns: repeat(3, 1fr);
            }}
            .metrics-card-2 {{
                grid-template-columns: repeat(2, 1fr);
            }}
        }}
        @media (max-width: 768px) {{
            .metrics-card, .metrics-card-2 {{
                grid-template-columns: repeat(2, 1fr);
            }}
            .chart-area {{
                grid-template-columns: 1fr;
            }}
        }}
        @media (max-width: 480px) {{
            .metrics-card, .metrics-card-2 {{
                grid-template-columns: 1fr;
            }}
        }}
    </style>
    <!-- 引入极简Chart.js（CDN方式，无需本地依赖） -->
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
</head>
<body>
    <div class="report-wrapper">
        <!-- 报告头部 -->
        <div class="report-header">
            <h1>新品提报接口压力测试报告</h1>
            <div class="meta">
                <p>测试时间：{start_time.strftime('%Y-%m-%d %H:%M:%S')} - {end_time.strftime('%Y-%m-%d %H:%M:%S')}</p>
                <p>接口地址：{url + api_url["product_sub"]} | 总请求数：{TOTAL_REQUEST_NUM} | 请求间隔：{REQUEST_INTERVAL}秒</p>
            </div>
        </div>

        <!-- 核心压测指标 -->
        <div class="section">
            <div class="section-title">核心压测指标</div>
            <div class="metrics-card">
                <div class="metric-item normal">
                    <div class="label">总请求数</div>
                    <div class="value">{stats['total_request']}</div>
                </div>
                <div class="metric-item success">
                    <div class="label">成功请求数</div>
                    <div class="value">{stats['success']}</div>
                </div>
                <div class="metric-item failed">
                    <div class="label">失败请求数</div>
                    <div class="value">{stats['failed']}</div>
                </div>
                <div class="metric-item normal">
                    <div class="label">成功率</div>
                    <div class="value">{success_rate}%</div>
                </div>
                <div class="metric-item failed">
                    <div class="label">错误率</div>
                    <div class="value">{error_rate}%</div>
                </div>
                <div class="metric-item warning">
                    <div class="label">QPS</div>
                    <div class="value">{qps}</div>
                </div>
            </div>
            <div class="metrics-card-2">
                <div class="metric-item warning">
                    <div class="label">总吞吐量</div>
                    <div class="value">{throughput} req/s</div>
                </div>
                <div class="metric-item normal">
                    <div class="label">测试总耗时</div>
                    <div class="value">{total_elapsed} s</div>
                </div>
                <div class="metric-item normal">
                    <div class="label">平均响应耗时</div>
                    <div class="value">{avg_elapsed} ms</div>
                </div>
                <div class="metric-item normal">
                    <div class="label">响应耗时中位数</div>
                    <div class="value">{round(sorted(stats['response_times'])[len(stats['response_times']) // 2], 2) if stats['response_times'] else 0} ms</div>
                </div>
            </div>
        </div>

        <!-- 响应时间详细统计 -->
        <div class="section">
            <div class="section-title">响应时间统计（ms）</div>
            <div class="metrics-card-2">
                <div class="metric-item normal">
                    <div class="label">最小响应耗时</div>
                    <div class="value">{stats['min_elapsed_ms'] if stats['min_elapsed_ms'] != float('inf') else 0}</div>
                </div>
                <div class="metric-item normal">
                    <div class="label">最大响应耗时</div>
                    <div class="value">{stats['max_elapsed_ms']}</div>
                </div>
                <div class="metric-item normal">
                    <div class="label">P90响应耗时</div>
                    <div class="value">{p90}</div>
                </div>
                <div class="metric-item normal">
                    <div class="label">P95响应耗时</div>
                    <div class="value">{p95}</div>
                </div>
            </div>
            <div class="metrics-card-2" style="margin-top: 10px;">
                <div class="metric-item normal">
                    <div class="label">P99响应耗时</div>
                    <div class="value">{p99}</div>
                </div>
                <div class="metric-item normal">
                    <div class="label">总响应耗时</div>
                    <div class="value">{stats['total_elapsed_ms']} ms</div>
                </div>
                <div class="metric-item normal">
                    <div class="label">响应耗时标准差</div>
                    <div class="value">{round((sum([(t - avg_elapsed) ** 2 for t in stats['response_times']]) / len(stats['response_times'])) ** 0.5, 2) if stats['response_times'] else 0} ms</div>
                </div>
                <div class="metric-item normal">
                    <div class="label">响应耗时方差</div>
                    <div class="value">{round(sum([(t - avg_elapsed) ** 2 for t in stats['response_times']]) / len(stats['response_times']), 2) if stats['response_times'] else 0} ms²</div>
                </div>
            </div>
        </div>

        <!-- 状态码分布 -->
        <div class="section">
            <div class="section-title">状态码分布</div>
            <table>
                <tr>
                    <th>HTTP状态码</th>
                    <th>出现次数</th>
                    <th>占比</th>
                </tr>
                {
    ''.join([f'<tr><td>{code}</td><td>{count}</td><td>{round(count / stats["total_request"] * 100, 2)}%</td></tr>'
             for code, count in stats["status_code_dist"].items()])
    }
            </table>
        </div>

        <!-- 可视化图表 -->
        <div class="section">
            <div class="section-title">测试结果可视化</div>
            <div class="chart-area">
                <!-- 成功率饼图 -->
                <div class="chart-box">
                    <canvas id="successRateChart"></canvas>
                </div>
                <!-- 响应时间趋势图 -->
                <div class="chart-box">
                    <canvas id="responseTimeChart"></canvas>
                </div>
            </div>
        </div>

        <!-- 失败详情 -->
        <div class="section">
            <div class="section-title">失败请求详情</div>
            <table>
                <tr>
                    <th>请求序号</th>
                    <th>状态码</th>
                    <th>耗时(ms)</th>
                    <th>错误信息</th>
                </tr>
                {
    '<tr><td colspan="4" style="text-align:center; color:#666;">无失败请求</td></tr>'
    if not stats['failed_cases']
    else
    ''.join([f'<tr><td>{case["request_num"]}</td><td>{case["status_code"]}</td><td>{case["elapsed_ms"]}</td><td class="error">{case["error_msg"]}</td></tr>' for case in stats['failed_cases']])
    }
            </table>
        </div>
    </div>

    <script>
        // 1. 成功率饼图
        const pieCtx = document.getElementById('successRateChart').getContext('2d');
        new Chart(pieCtx, {{
            type: 'pie',
            data: {{
                labels: ['成功请求', '失败请求'],
                datasets: [{{
                    data: [{stats['success']}, {stats['failed']}],
                    backgroundColor: ['#27ae60', '#e74c3c'],
                    borderWidth: 0
                }}]
            }},
            options: {{
                responsive: true,
                maintainAspectRatio: false,
                plugins: {{
                    legend: {{
                        position: 'bottom',
                        labels: {{
                            font: {{ size: 12 }}
                        }}
                    }},
                    title: {{
                        display: true,
                        text: '请求成功率分布',
                        font: {{ size: 14, weight: 'bold' }}
                    }}
                }}
            }}
        }});

        // 2. 响应时间趋势图
        const lineCtx = document.getElementById('responseTimeChart').getContext('2d');
        new Chart(lineCtx, {{
            type: 'line',
            data: {{
                labels: {list(range(1, len(stats['response_times']) + 1)) if stats['response_times'] else []},  // 请求序号
                datasets: [{{
                    label: '响应耗时(ms)',
                    data: {stats['response_times']},
                    borderColor: '#3498db',
                    backgroundColor: 'rgba(52, 152, 219, 0.1)',
                    borderWidth: 2,
                    fill: true,
                    tension: 0.2
                }}]
            }},
            options: {{
                responsive: true,
                maintainAspectRatio: false,
                plugins: {{
                    legend: {{
                        display: false
                    }},
                    title: {{
                        display: true,
                        text: '单次请求响应时间趋势',
                        font: {{ size: 14, weight: 'bold' }}
                    }}
                }},
                scales: {{
                    y: {{
                        title: {{
                            display: true,
                            text: '耗时(毫秒)'
                        }},
                        beginAtZero: true
                    }},
                    x: {{
                        title: {{
                            display: true,
                            text: '请求序号'
                        }}
                    }}
                }}
            }}
        }});
    </script>
</body>
</html>
    '''

    # 保存报告文件
    with open(REPORT_FILE, "w", encoding="utf-8") as f:
        f.write(html_content)

    # 控制台输出全量汇总
    print("\n" + "=" * 80)
    print("压测完成！全量汇总结果：")
    print(f"  基础指标：成功率 {success_rate}% | 错误率 {error_rate}% | QPS {qps} | 总吞吐量 {throughput} req/s")
    print(f"  响应时间：平均 {avg_elapsed}ms | P90 {p90}ms | P95 {p95}ms | P99 {p99}ms")
    print(f"  经典版HTML报告已保存到：{REPORT_FILE}")
    print("=" * 80)


if __name__ == '__main__':
    # 执行压测并生成报告
    run_stress_test()