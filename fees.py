def management_fee(balance, rate_percent):
    """Return the annual fee for a balance at a given % rate."""
    return round(balance * rate_percent / 100, 2)
    