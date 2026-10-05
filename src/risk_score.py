"""Deterministic scoring example for synthetic ML engineering exercises."""


def score_risk(features: dict[str, float]) -> float:
    """Return an illustrative bounded score; this is not a trained model."""
    if not features or any(not isinstance(value, (int, float)) for value in features.values()):
        raise ValueError("features must be a non-empty numeric mapping")
    weighted = sum(float(value) for value in features.values()) / len(features)
    return max(0.0, min(1.0, weighted))
