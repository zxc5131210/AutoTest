import subprocess
import uiautomator2 as u2
import datetime
import time

# 初始化连接到设备
d = u2.connect()


# 定义录制视频的文件名，以当前日期和时间作为文件名
output_file = f"screen_record_{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.mp4"

# 启动屏幕录制
adb_command = f"adb shell screenrecord /sdcard/{output_file}"+""+"&"
try:
    result = subprocess.run(adb_command, stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE, shell=True, text=True)

    # 检查命令是否成功执行
    if result.returncode == 0:
        # 输出命令的标准输出结果
        output = result.stdout
        print("命令输出:")
        print(output)
    else:
        # 输出错误消息
        error_message = result.stderr
        print(f"命令执行失败: {error_message}")
except subprocess.CalledProcessError as e:
    # 捕获命令执行失败的异常
    error_message = e.stderr
    print(f"命令执行失败: {error_message}")
# 等待一段时间，让录制运行一段时间（例如，录制10秒）
# time.sleep(10)
# adb_command = "adb shell kill -l"
# subprocess.run(adb_command, shell=True)


# # 停止录制并将视频保存到本地
# adb_command = f"adb pull /sdcard/{output_file} {output_file}"
# subprocess.run(adb_command, shell=True)
