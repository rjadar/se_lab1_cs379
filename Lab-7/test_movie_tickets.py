import re

import pytest
from hypothesis import given, strategies as st

from movie_tickets import average_rating, parse_seat, total_price


SEAT_PATTERN = re.compile(r"^[A-Za-z][1-9][0-9]*$")
PRICES_PATTERN = re.compile(r"^[0-9]+(?:,[0-9]+)*$")
RATINGS_PATTERN = re.compile(r"^[0-9]+(?:\s+[0-9]+)*$")


@given(row=st.sampled_from("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"), number=st.integers(min_value=1, max_value=9999))
def test_parse_seat_valid_seats(row, number):
    assert parse_seat(f"{row}{number}") == (row.upper(), number)


@given(seat=st.text().filter(lambda value: SEAT_PATTERN.fullmatch(value) is None))
def test_parse_seat_rejects_malformed_text(seat):
    with pytest.raises(ValueError):
        parse_seat(seat)


@given(seat=st.one_of(st.none(), st.integers(), st.binary()))
def test_parse_seat_rejects_unexpected_types(seat):
    with pytest.raises(TypeError):
        parse_seat(seat)


@given(prices=st.lists(st.integers(min_value=0, max_value=100000), min_size=1, max_size=20))
def test_total_price_for_valid_csv(prices):
    prices_csv = ",".join(map(str, prices))
    assert total_price(prices_csv) == round(sum(prices) * 1.18, 2)


@given(prices=st.lists(st.integers(max_value=-1, min_value=-100000), min_size=1, max_size=10))
def test_total_price_rejects_negative_amounts(prices):
    prices_csv = ",".join(map(str, prices))
    with pytest.raises(ValueError):
        total_price(prices_csv)


@given(prices_csv=st.text().filter(lambda value: PRICES_PATTERN.fullmatch(value) is None))
def test_total_price_rejects_malformed_csv(prices_csv):
    with pytest.raises(ValueError):
        total_price(prices_csv)


@given(prices_csv=st.one_of(st.none(), st.integers(), st.lists(st.integers())))
def test_total_price_rejects_unexpected_types(prices_csv):
    with pytest.raises(TypeError):
        total_price(prices_csv)


@given(price=st.integers(min_value=10**309, max_value=10**350))
def test_total_price_rejects_values_too_large_to_calculate(price):
    with pytest.raises(ValueError):
        total_price(str(price))


@given(ratings=st.lists(st.integers(min_value=1, max_value=5), min_size=1, max_size=100))
def test_average_rating_for_valid_values(ratings):
    ratings_text = " ".join(map(str, ratings))
    assert average_rating(ratings_text) == round(sum(ratings) / len(ratings), 1)


@given(ratings=st.text().filter(lambda value: RATINGS_PATTERN.fullmatch(value) is None))
def test_average_rating_rejects_empty_or_malformed_values(ratings):
    with pytest.raises(ValueError):
        average_rating(ratings)


@given(ratings=st.one_of(st.none(), st.integers(), st.lists(st.integers())))
def test_average_rating_rejects_unexpected_types(ratings):
    with pytest.raises(TypeError):
        average_rating(ratings)


@given(rating=st.one_of(st.integers(max_value=0), st.integers(min_value=6, max_value=1000)))
def test_average_rating_rejects_values_outside_one_to_five(rating):
    with pytest.raises(ValueError):
        average_rating(str(rating))
