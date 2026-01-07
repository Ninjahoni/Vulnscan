import socket

class PortScanner:
    def __init__(self, timeout=1):
        self.timeout = timeout

    def scan_port(self, target, port):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(self.timeout)
            result = sock.connect_ex((target, port))
            sock.close()
            return result == 0
        except:
            return False

    def scan_ports(self, target, ports):
        open_ports = []
        for port in ports:
            if self.scan_port(target, port):
                open_ports.append(port)
        return open_ports

