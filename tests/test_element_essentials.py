from lc_review.element_essentials import ESSENTIALS, EXPLICIT_FRAMEWORK
from lc_review.elements import CARDS

CARD_NAMES = {card.name for card in CARDS}


def test_every_essentials_key_is_a_real_card_name():
    for name in ESSENTIALS:
        assert name in CARD_NAMES, f"{name!r} is not a card in CARDS"


def test_every_card_has_an_essentials_entry():
    for card in CARDS:
        assert card.name in ESSENTIALS, f"{card.name} has no ESSENTIALS entry"


def test_no_entry_has_more_than_four_items():
    for name, items in ESSENTIALS.items():
        assert len(items) <= 4, f"{name} has {len(items)} items"


def test_every_item_is_a_short_question():
    for name, items in ESSENTIALS.items():
        for item in items:
            assert item.endswith("？"), f"{name}: {item!r} does not end with ？"
            assert len(item) <= 60, f"{name}: {item!r} is too long for a table cell"


def test_explicit_framework_cards_are_real_card_names():
    for name in EXPLICIT_FRAMEWORK:
        assert name in CARD_NAMES


def test_at_least_one_card_has_no_meaningful_checklist():
    # An honest gap: some source articles are index pages or grab-bags with
    # no unifying checklist, and should not have a fabricated one.
    empty = [name for name, items in ESSENTIALS.items() if items == ()]
    assert empty, "expected at least one card with an intentionally empty tuple"
