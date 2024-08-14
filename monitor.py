import psutil

import psutil

# 查看 CPU 使用率
cpu_usage = psutil.cpu_percent(interval=1)
print(f"CPU 使用率: {cpu_usage}%")
