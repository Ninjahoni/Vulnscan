import unittest
import sys
import os

# Add src folder to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from Scanner import Scanner
from port_scanner import PortScanner
from cve_engine import CVEENGINE
from risk import RiskCalculator
from result import ReportGenerator


class TestVulnScanPro(unittest.TestCase):

    # ------------------------
    # Scanner Tests
    # ------------------------

    def test_scanner_creation(self):
        scanner = Scanner()
        self.assertIsNotNone(scanner)

    def test_scanner_run_scan_returns_string(self):
        scanner = Scanner()
        result = scanner.run_scan("127.0.0.1", [80])
        self.assertIsInstance(result, str)

    def test_scanner_run_scan_not_empty(self):
        scanner = Scanner()
        result = scanner.run_scan("127.0.0.1", [80])
        self.assertTrue(len(result) > 0)


    # ------------------------
    # Port Scanner Tests
    # ------------------------

    def test_port_scanner_creation(self):
        ps = PortScanner()
        self.assertIsNotNone(ps)

    def test_scan_port_returns_boolean(self):
        ps = PortScanner()
        result = ps.scan_port("127.0.0.1", 80)
        self.assertIn(result, [True, False])

    def test_scan_ports_returns_list(self):
        ps = PortScanner()
        result = ps.scan_ports("127.0.0.1", [80, 22])
        self.assertIsInstance(result, list)


    # ------------------------
    # CVE Engine Tests
    # ------------------------

    def test_cve_engine_creation(self):
        engine = CVEENGINE()
        self.assertIsNotNone(engine)

    def test_identify_vulnerabilities_returns_list(self):
        engine = CVEENGINE()
        result = engine.identify_vulnerabilities([80])
        self.assertIsInstance(result, list)

    def test_identify_vulnerabilities_empty(self):
        engine = CVEENGINE()
        result = engine.identify_vulnerabilities([])
        self.assertEqual(result, [])


    # ------------------------
    # Risk Calculator Tests
    # ------------------------

    def test_risk_calculator_creation(self):
        risk = RiskCalculator()
        self.assertIsNotNone(risk)

    def test_calculate_risk_returns_integer(self):
        risk = RiskCalculator()
        score = risk.calculate_risk(5)
        self.assertIsInstance(score, int)

    def test_calculate_risk_correct_value(self):
        risk = RiskCalculator()
        score = risk.calculate_risk(5)
        self.assertEqual(score, 20)


    # ------------------------
    # Report Generator Tests
    # ------------------------

    def test_report_generator_creation(self):
        rg = ReportGenerator()
        self.assertIsNotNone(rg)

    def test_generate_report_returns_string(self):
        rg = ReportGenerator()
        result = rg.generate("127.0.0.1", [80], [])
        self.assertIsInstance(result, str)

    def test_generate_report_contains_target(self):
        rg = ReportGenerator()
        result = rg.generate("127.0.0.1", [80], [])
        self.assertIn("127.0.0.1", result)


# Run tests
if __name__ == "__main__":
    unittest.main()
