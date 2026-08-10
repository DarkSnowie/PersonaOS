import platform
import time
import psutil
from pathlib import Path

class SystemMonitor:

    @staticmethod
    def cpu_percent():
        return psutil.cpu_percent(interval=None)

    @staticmethod
    def ram_percent():
        return psutil.virtual_memory().percent

    @staticmethod
    def ram_used():
        return psutil.virtual_memory().used / (1024 ** 3)

    @staticmethod
    def disk_percent():
        return psutil.disk_usage("/").percent

    @staticmethod
    def cpu_name():
        try:
            with open("/proc/cpuinfo") as f:
                for line in f:
                    if line.startswith("model name"):
                        return line.split(":")[1].strip()
        except Exception:
            pass

        return "Unknown CPU"

    @staticmethod
    def cpu_freq():
        freq = psutil.cpu_freq()
        return freq.current if freq else 0

    @staticmethod
    def cpu_threads():
        return psutil.cpu_count()

    @staticmethod
    def ram_total():
        return psutil.virtual_memory().total / (1024**3)

    @staticmethod
    def disk_used():
        usage = psutil.disk_usage("/")
        return usage.used / (1024**3)

    @staticmethod
    def battery():
        return psutil.sensors_battery()

    @staticmethod
    def uptime():

        seconds = int(time.time() - psutil.boot_time())

        hours = seconds // 3600
        minutes = (seconds % 3600) // 60

        return f"{hours}h {minutes}m"

    @staticmethod
    def kernel():
        return platform.release()

    @staticmethod
    def os_name():
        return platform.system()

    @staticmethod
    def gpu_percent():
        path = Path("/sys/class/drm/card1/device/gpu_busy_percent")

        if path.exists():
            try:3
                return int(path.read_text().strip())
            except Exception:
                return None

        return None
