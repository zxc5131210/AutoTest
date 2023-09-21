import subprocess
import uiautomator2 as u2
import time

# 初始化连接到设备
d = u2.connect('172.21.10.20')
d(resourceId='com.viewsonic.sidetoolbar:id/save').click()

toast = d.toast.get_message(wait_timeout=5)
file = toast.split("/")[-1]


# ADB命令，用于检查文件是否存在
adb_command = f'adb shell ls /sdcard/pictures/{file}'

# 使用subprocess执行ADB命令
try:
    result = subprocess.run(adb_command, check=False, stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE, shell=True, text=True)

    # 检查命令是否成功执行
    if result.returncode == 0:
        # 如果文件存在，输出文件的完整路径
        file_exists = bool(result.stdout.strip())  # 去除输出结果的空格和换行符
        if file_exists:
            print("文件存在:", result.stdout.strip())
        else:
            print("文件不存在")
    else:
        # 输出错误消息
        error_message = result.stderr
        print(f"命令执行失败: {error_message}")
except subprocess.CalledProcessError as e:
    # 捕获命令执行失败的异常
    error_message = e.stderr
    print(f"命令执行失败: {error_message}")
