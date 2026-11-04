"""Tests that execute every statement in the movie ticket module."""

import pytest

from movie_tickets import group_discount, snack_combo, ticket_price


def test_ticket_price_statements():
    assert ticket_price("regular", 25, 9, False) == 100
    assert ticket_price("premium", 8, 15, True) == 145
    assert ticket_price("recliner", 60, 18, False) == 215
    assert ticket_price("regular", 2, 12, False) == 0
    with pytest.raises(ValueError, match="unknown seat"):
        ticket_price("vip", 25, 12, False)
    with pytest.raises(ValueError, match="invalid show time"):
        ticket_price("regular", 25, 24, False)


def test_group_discount_statements():
    with pytest.raises(ValueError, match="no tickets"):
        group_discount(0, False)
    assert group_discount(2, False) == 0
    assert group_discount(5, True) == 15
    assert group_discount(10, False) == 15


def test_snack_combo_statements():
    assert snack_combo("small", True) == 70
    assert snack_combo("medium", False) == 180
    assert snack_combo("large", False) == 250
