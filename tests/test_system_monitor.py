from personaos.services.monitors.system_monitor import SystemMonitor


def test_monitor_creation():
    monitor = SystemMonitor()

    assert monitor is not None
