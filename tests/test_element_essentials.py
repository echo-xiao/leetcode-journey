from lc_review.element_essentials import ESSENTIALS, EXPLICIT_FRAMEWORK, FAMILIES, SLOTS

# CARDS lived in lc_review.elements, which existed only to render the docs/
# sheet that Notion replaced. ESSENTIALS is the definition now, so the three
# tables are checked against each other instead.


def test_slots_and_families_cover_the_same_techniques():
    assert set(SLOTS) == set(ESSENTIALS)
    assert set(FAMILIES) == set(ESSENTIALS)


def test_each_slot_labels_exactly_one_question():
    for name, questions in ESSENTIALS.items():
        assert len(SLOTS[name]) == len(questions), (
            f"{name}: {len(SLOTS[name])} slots for {len(questions)} questions"
        )


def test_every_family_is_one_of_the_three():
    allowed = {"递归系", "循环系", "洞察系", "递归系 / 循环系"}
    for name, family in FAMILIES.items():
        assert family in allowed, f"{name}: unexpected family {family!r}"


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


def test_explicit_framework_cards_are_real_technique_names():
    for name in EXPLICIT_FRAMEWORK:
        assert name in ESSENTIALS


def test_every_card_now_has_a_checklist():
    # Superseded assertion: 堆, 栈与队列 and 数学技巧 used to be intentionally
    # empty because their source articles are index pages. echo asked for them
    # to be filled in from what the technique actually forces you to decide, so
    # an empty tuple is now a gap rather than an honest refusal.
    empty = [name for name, items in ESSENTIALS.items() if items == ()]
    assert not empty, f"cards with no checklist: {empty}"
