from src.risk_score import score_risk


def test_score_risk_bounds_synthetic_values():
    assert score_risk({"a": 0.2, "b": 0.8}) == 0.5
    assert score_risk({"a": 2.0}) == 1.0
