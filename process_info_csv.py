import psutil
import csv

# 文件路径
file_path = "process_info.csv"

# 获取所有进程的信息
processes = []
for proc in psutil.process_iter(['pid', 'name', 'username', 'cpu_percent', 'memory_info']):
    try:
        # 获取每个进程的信息
        proc_info = proc.info
        processes.append(proc_info)
    except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
        # 忽略无法访问的进程
        pass

# 将进程信息保存到 CSV 文件
with open(file_path, mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=['pid', 'name', 'username', 'cpu_percent', 'memory_info'])
    writer.writeheader()
    writer.writerows(processes)

print(f"进程信息已保存到 {file_path}")
