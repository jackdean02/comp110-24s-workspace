"""Test my garden functions."""

__author__ = "730385160"
from garden_helpers import add_by_kind
from garden_helpers import add_by_date
from garden_helpers import lookup_by_kind_and_date

def test_add_by_kind_edge() -> None:
    """Tests if you can add a plant by kind with an empty dictionary."""
    by_kind: dict = {}
    add_by_kind(by_kind, "flower", "rose")
    assert by_kind["flower"] == ["rose"]


def test_add_by_kind_use() -> None:
    """Tests functionality for new plant kind."""
    by_kind: dict = {"flower": ["rose", "daisy"]}
    add_by_kind(by_kind, "grain", "wheat")
    assert by_kind == {"flower": ["rose", "daisy"], "grain": ["wheat"]}


def test_add_by_date_use() -> None:
    """Tests functionality for new month."""
    garden_by_date: dict = {"February": ["lily"], "May": ["rose"]}
    add_by_date(garden_by_date, "June", "poppy")
    assert garden_by_date == {"February": ["lily"], "May": ["rose"], "June": ["poppy"]}


def test_add_by_date_edge() -> None:
    """Tests if you can add a plant by date with an empty dictionary."""
    garden_by_date: dict = {}
    add_by_date(garden_by_date, "December", "Christmas Tree")
    assert garden_by_date["December"] == ["Christmas Tree"]


def test_lookup_by_kind_and_date_use() -> None:
    """Tests functionality of looking up plant by kind and date."""
    by_kind: dict[str, list[str]] = {"flower": ["marigold"], "vegetable": ["peas"]}
    by_date: dict[str, list[str]] = {"April": ["marigold"], "August": ["peas"]}
    lookup_by_kind_and_date(by_kind, by_date, "vegetable", "August")
    assert by_date["August"] == ["peas"]


def test_lookup_by_kind_and_date_edge() -> None:
    """Tests functionality for edge case."""
    by_kind: dict[str, list[str]] = {"flower": ["marigold"], "vegetable": ["peas"]}
    by_date: dict[str, list[str]] = {"April": ["marigold"], "August": ["peas"]}
    lookup_by_kind_and_date(by_kind, by_date, "flower", "April")
    assert by_kind["flower"] == ["marigold"]
