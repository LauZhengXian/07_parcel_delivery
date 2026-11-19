from src.parcel_fee import delivery_fee
import pytest


def test_delivery_fee_at_1000_grams():
    assert delivery_fee(1000) == 500

def test_delivery_fee_below_1000_grams():
    assert delivery_fee(999) == 500


def test_delivery_fee_above_1000_grams():
    assert delivery_fee(1001) == 1000

def test_delivery_fee_rejects_zero_weight():
    with pytest.raises(ValueError):
        delivery_fee(0)

@pytest.mark.parametrize("weight, expected_fee", [(1, 500), (20000, 1000)])
def test_delivery_fee_at_minimum_and_maximum_weight(weight, expected_fee):
    fee = delivery_fee(weight)
    assert type(fee) is int
    assert fee == expected_fee


@pytest.mark.parametrize("weight", [-1, 20001])
def test_delivery_fee_rejects_out_of_range_weight(weight):
    with pytest.raises(ValueError):
        delivery_fee(weight)


@pytest.mark.parametrize("weight", [True, 1000.5, "1000"])
def test_delivery_fee_rejects_non_integer_weight(weight):
    with pytest.raises(TypeError):
        delivery_fee(weight)