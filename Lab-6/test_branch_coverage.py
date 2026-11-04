"""Tests both outcomes of each decision in the movie ticket module."""

import pytest

from movie_tickets import group_discount, snack_combo, ticket_price


@pytest.mark.parametrize(
    ("seat", "base"),
    [("regular", 150), ("premium", 250), ("recliner", 400)],
)
@pytest.mark.parametrize(
    ("hour", "adjustment"), [(9, -50), (12, 0), (18, 30)],
)
@pytest.mark.parametrize("weekend", [False, True])
def test_ticket_price_seat_time_and_weekend_branches(seat, base, hour, adjustment, weekend):
    expected = base + adjustment + (40 if weekend else 0)
    assert ticket_price(seat, 25, hour, weekend) == expected


@pytest.mark.parametrize("age,expected", [(2, 0), (3, 75), (13, 150), (59, 150), (60, 75)])
def test_ticket_price_age_branches(age, expected):
    assert ticket_price("regular", age, 12, False) == expected


@pytest.mark.parametrize("seat", ["vip", "Regular"])
def test_invalid_seat_branch(seat):
    with pytest.raises(ValueError, match="unknown seat"):
        ticket_price(seat, 25, 12, False)


@pytest.mark.parametrize("hour", [-1, 24])
def test_invalid_hour_branch(hour):
    with pytest.raises(ValueError, match="invalid show time"):
        ticket_price("regular", 25, hour, False)


@pytest.mark.parametrize("tickets", [0, 1, 5, 10])
def test_ticket_count_branches(tickets):
    if tickets == 0:
        with pytest.raises(ValueError, match="no tickets"):
            group_discount(tickets, False)
    else:
        expected = 0 if tickets == 1 else 10 if tickets == 5 else 15
        assert group_discount(tickets, False) == expected


@pytest.mark.parametrize("tickets,expected", [(1, 0), (5, 15), (10, 20)])
def test_student_discount_branches(tickets, expected):
    assert group_discount(tickets, True) == expected


@pytest.mark.parametrize("size,price", [("small", 120), ("medium", 180), ("large", 250), ("other", 250)])
def test_snack_size_branches(size, price):
    assert snack_combo(size, False) == price


@pytest.mark.parametrize("coupon,expected", [(False, 180), (True, 130)])
def test_coupon_branches(coupon, expected):
    assert snack_combo("medium", coupon) == expected
