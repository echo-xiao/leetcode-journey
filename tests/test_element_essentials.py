from lc_review.element_essentials import ESSENTIALS, EXPLICIT_FRAMEWORK
from lc_review.elements import CARDS

CARD_NAMES = {card.name for card in CARDS}


def test_every_essentials_key_is_a_real_card_name():
    for name in ESSENTIALS:
        assert name in CARD_NAMES, f"{name!r} is not a card in CARDS"


def test_every_card_has_an_essentials_entry():
    for card in CARDS:
        assert card.name in ESSENTIALS, f"{card.name} has no ESSENTIALS entry"


def test_no_entry_is_long_enough_to_stop_being_a_checklist():
    # Was <= 4. Dynamic programming legitimately needs five (状态/选择/dp 定义/
    # base case/遍历顺序), so the cap moved rather than the card being trimmed
    # to fit an arbitrary number.
    for name, items in ESSENTIALS.items():
        assert len(items) <= 6, f"{name} has {len(items)} items"


def test_every_item_is_a_short_question():
    for name, items in ESSENTIALS.items():
        for item in items:
            assert item.endswith("？"), f"{name}: {item!r} does not end with ？"
            assert len(item) <= 60, f"{name}: {item!r} is too long for a table cell"


def test_explicit_framework_cards_are_real_card_names():
    for name in EXPLICIT_FRAMEWORK:
        assert name in CARD_NAMES


def test_every_card_now_has_a_checklist():
    # Superseded assertion: 堆, 栈与队列 and 数学技巧 used to be intentionally
    # empty because their source articles are index pages. echo asked for them
    # to be filled in from what the technique actually forces you to decide, so
    # an empty tuple is now a gap rather than an honest refusal.
    empty = [name for name, items in ESSENTIALS.items() if items == ()]
    assert not empty, f"cards with no checklist: {empty}"
