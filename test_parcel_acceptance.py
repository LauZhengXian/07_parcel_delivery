from parcel_acceptance import is_parcel_accepted
import pytest


def test_parcel_accepted_at_200_cm():
    assert is_parcel_accepted(1000, 200) is True

def test_parcel_accepted_at_199_cm():
    assert is_parcel_accepted(1000, 199) is True


def test_parcel_rejected_at_201_cm():
    assert is_parcel_accepted(1000, 201) is False

def test_parcel_rejects_zero_weight():
    assert is_parcel_accepted(0, 100) is False

@pytest.mark.parametrize("weight, length", [(1, 1), (20000, 100)])
def test_parcel_accepts_valid_measurement_limits(weight, length):
    assert is_parcel_accepted(weight, length) is True


@pytest.mark.parametrize("weight, length", [(1000, 0), (20001, 100)])
def test_parcel_rejects_zero_length_or_excess_weight(weight, length):
    assert is_parcel_accepted(weight, length) is False


@pytest.mark.parametrize("weight, length", [(-1, 100), (1000, -1)])
def test_parcel_raises_value_error_for_negative_measurement(weight, length):
    with pytest.raises(ValueError):
        is_parcel_accepted(weight, length)


@pytest.mark.parametrize("invalid_value", [True, 1.5, "100"])
def test_parcel_rejects_non_integer_weight(invalid_value):
    with pytest.raises(TypeError):
        is_parcel_accepted(invalid_value, 100)


@pytest.mark.parametrize("invalid_value", [True, 1.5, "100"])
def test_parcel_rejects_non_integer_length(invalid_value):
    with pytest.raises(TypeError):
        is_parcel_accepted(1000, invalid_value)