import psutil

def get_ports():
    connections = psutil.net_connections()
    ports = []
    for conn in connections:
        process = psutil.Process(conn.pid)
        process_name = process.name()
        if process_name == "Appium.exe":
            ports.append(conn.laddr.port)
    return ports