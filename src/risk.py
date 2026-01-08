class RiskCalculator:
    def calculate_risk(self, severity):
        exposure = 2
        impact = 2
        return severity * exposure * impact
