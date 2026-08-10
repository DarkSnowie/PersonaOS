from pathlib import Path


@staticmethod
def gpu_percent():
    path = Path("/sys/class/drm/card1/device/gpu_busy_percent")

    if path.exists():
        try:
            return int(path.read_text().strip())
        except Exception:
            pass

    return None
