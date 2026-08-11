import platform
import socket
import subprocess
import time
from pathlib import Path

import distro
import psutil


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

        if freq:
            return freq.current / 1000.0   # MHz -> GHz

        return 0.0

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

        days = seconds // 86400
        hours = (seconds % 86400) // 3600
        minutes = (seconds % 3600) // 60

        if days:
            return f"{days}d {hours}h"

        return f"{hours}h {minutes}m"

    @staticmethod
    def kernel():
        return platform.release()

    @staticmethod
    def os_name():
        return distro.name(pretty=True)

    @staticmethod
    def gpu_percent():
        path = Path("/sys/class/drm/card1/device/gpu_busy_percent")

        if path.exists():
            try:
                return int(path.read_text().strip())
            except Exception:
                return None

        return None

    @staticmethod
    def cpu_temperature():
        temps = psutil.sensors_temperatures()

        if "k10temp" in temps:
            return temps["k10temp"][0].current

        return None

    @staticmethod
    def gpu_temperature():
        try:
            for hwmon in Path("/sys/class/hwmon").glob("hwmon*"):

                name = (hwmon / "name").read_text().strip()

                if name == "amdgpu":

                    temp = (
                        hwmon / "temp1_input"
                    ).read_text().strip()

                    return int(temp) / 1000

        except Exception:
            pass

        return None

    @staticmethod
    def hostname():
        return socket.gethostname()

    @staticmethod
    def ram_available():
        return psutil.virtual_memory().available / (1024**3)

    @staticmethod
    def disk_free():
        return psutil.disk_usage("/").free / (1024**3)

    @staticmethod
    def cpu_logical():
        return psutil.cpu_count()

    @staticmethod
    def cpu_physical():
        return psutil.cpu_count(logical=False)


    @staticmethod
    def disk_total():
        return psutil.disk_usage("/").total / (1024**3)


    @staticmethod
    def gpu_name():
        return "AMD Radeon Vega 3"


    @staticmethod
    def cpu_temp():
        temps = psutil.sensors_temperatures()

        if "k10temp" in temps:
            return temps["k10temp"][0].current

        return None


    @staticmethod
    def gpu_temp():
        temps = psutil.sensors_temperatures()

        if "amdgpu" in temps:
            return temps["amdgpu"][0].current

        return None
