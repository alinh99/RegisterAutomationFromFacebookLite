import subprocess

def get_devices():
    devices = subprocess.check_output("adb devices")
    p = str(devices).replace("b'List of devices attached", "").replace("\\r\\n", "").replace(" ", "")
    if len(p) > 0:
        list_devices = p.split("\\tdevice")
        list_devices.pop()
        return list_devices
    else:
        return []