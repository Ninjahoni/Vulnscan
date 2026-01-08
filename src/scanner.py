from port_scanner import PortScanner
from cve_engine import CVEEngine
from risk_calculator import RiskCalculator
from report_generator import ReportGenerator

class Scanner:
    def __init__(self):
        self.port_scanner = PortScanner()
        self.cve_engine = CVEEngine()
        self.risk_calculator = RiskCalculator()
        self.report_generator = ReportGenerator()

    def run_scan(self, target, ports):
        open_ports = self.port_scanner.scan_ports(target, ports)
        vulnerabilities = self.cve_engine.identify_vulnerabilities(open_ports)

        for v in vulnerabilities:
            v["risk_score"] = self.risk_calculator.calculate_risk(v["severity"])

        return self.report_generator.generate(target, open_ports, vulnerabilities)
