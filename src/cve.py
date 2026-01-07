class CVEEngine:
    def __init__(self):
        self.cve_database = {
            21: {"service": "FTP", "cve": "CVE-2019-0708", "severity": 7},
            22: {"service": "SSH", "cve": "CVE-2018-15473", "severity": 6},
            80: {"service": "HTTP", "cve": "CVE-2021-41773", "severity": 8},
            443: {"service": "HTTPS", "cve": "CVE-2020-3452", "severity": 5}
        }

    def identify_vulnerabilities(self, open_ports):
        vulnerabilities = []
        for port in open_ports:
            if port in self.cve_database:
                vulnerabilities.append(self.cve_database[port])
        return vulnerabilities
