import subprocess
import csv
import re

# 运行 adb 命令获取设备日志
adb_command = ['adb', 'logcat', '-d']  # -d 表示仅获取当前日志，不实时更新
result = subprocess.run(adb_command, stdout=subprocess.PIPE,
                        stderr=subprocess.PIPE, text=True)
log_output = result.stdout

# 从日志输出中解析日志信息
log_info = []
log_lines = log_output.splitlines()
log_pattern = re.compile(r'(\d+-\d+-\d+ \d+:\d+:\d+)\.\d+.*? - (.*?)$')
for line in log_lines:
    match = log_pattern.match(line)
    if match:
        timestamp, message = match.groups()
        log_info.append({'timestamp': timestamp, 'message': message})
# 将日志信息写入 CSV 文件
csv_file_path = 'log_info.csv'
with open(csv_file_path, 'w', newline='') as csv_file:
    csv_writer = csv.DictWriter(csv_file, fieldnames=['timestamp', 'message'])
    csv_writer.writeheader()
    csv_writer.writerows(log_info)

print(f'日志信息已从 adb 中获取并写入到 {csv_file_path}')
