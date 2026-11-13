from fees import management_fee

def test_one_percent_fees():
    assert management_fee(10000, 1) == 100

def test_fractional_rate():
    assert management_fee(250000, 0.75) == 1875

def test_zero_balance():
    assert management_fee(0, 1.5) == 0
