from html_report import TestReport
import uiautomator2 as u2

d = u2.connect()
# 創建一個 TestReport 實例
test_report = TestReport()
app_version = []
app_list = {
    "vlauncher": "com.viewsonic.vlauncher",
    "STB": "com.viewsonic.sidetoolbar",
    "screenlock": "com.viewsonic.screenlock",
    "quicksettings": "com.viewsonic.quicksettings",
    "wallpaper": "com.viewsonic.wallpaperpicker",
    "authenticator": "com.viewsonic.authenticator",
}

for app_name, package_name in app_list.items():
    version_info = d.app_info(package_name)
    version_name = version_info["versionName"]
    app_version.append(app_name)
    app_version.append(version_name)

test_report.add_version_info("model", "fw version", app_version=app_version)
# 添加一個測試項目到 "vlauncher" 類別下的 "功能測試" 子類別
test_report.add_entry(
    category="vlauncher",
    subcategory="功能測試",
    testcase="測試案例1",
    detail="這是測試案例1的詳細描述。",
    steps={"步驟1": "Pass", "步驟2": "Pass"},
    status="Pass",
    comment="這是測試案例1的備註。",
)

# 添加一個測試項目到 "STB" 類別下的 "連接測試" 子類別
test_report.add_entry(
    category="STB",
    subcategory="連接測試",
    testcase="測試案例2",
    detail="這是測試案例2的詳細描述。",
    steps={"步驟1": "Pass", "步驟2": "Fail"},
    status="Fail",
    comment="這是測試案例2的備註。",
)

# 添加一個測試項目到 "vlauncher" 類別下的 "性能測試" 子類別
test_report.add_entry(
    category="vlauncher",
    subcategory="性能測試",
    testcase="測試案例3",
    detail="這是測試案例3的詳細描述。",
    steps={"步驟1": "Pass", "步驟2": "Pass"},
    status="Pass",
    comment="這是測試案例3的備註。",
)

# 生成 HTML 報告並保存到文件
test_report.save_to_file("test_report.html")
