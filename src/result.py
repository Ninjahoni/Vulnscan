class ReportGenerator:
    def generate(self, target, open_ports, vulnerabilities):
        report = []
        report.append(f"Target: {target}")
        report.append(f"Open Ports: {open_ports}")
        report.append("\nVulnerabilities Detected:")

        if not vulnerabilities:
            report.append("No known vulnerabilities found.")

        for v in vulnerabilities:
            report.append(
                f"- Service: {v['service']} | CVE: {v['cve']} | "
                f"Severity: {v['severity']} | Risk Score: {v['risk_score']}"
            )

        return "\n".join(report)
