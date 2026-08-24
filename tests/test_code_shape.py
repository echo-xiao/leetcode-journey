from lc_review import code_shape

SUM_LOOP = """
def f(x):
    total = 0
    for i in x:
        total += i
    return total
"""

SUM_LOOP_RENAMED = """
def g(nums):
    s = 0
    for n in nums:
        s += n
    return s
"""

SUM_BUILTIN = """
def f(x):
    return sum(x)
"""


def test_renaming_everything_does_not_change_the_shape():
    # The whole point of the AST route: the owner asked for "big structural
    # change", and a variable rename is not one.
    assert code_shape.shape_of(SUM_LOOP) == code_shape.shape_of(SUM_LOOP_RENAMED)


def test_a_different_implementation_changes_the_shape():
    assert code_shape.shape_of(SUM_LOOP) != code_shape.shape_of(SUM_BUILTIN)


def test_whitespace_and_blank_lines_do_not_change_the_shape():
    spaced = "def f(x):\n\n    total = 0   \n\n    for i in x:\n        total += i\n    return total\n"
    assert code_shape.shape_of(SUM_LOOP) == code_shape.shape_of(spaced)


def test_docstrings_and_comments_do_not_change_the_shape():
    documented = '''
def f(x):
    """Add everything up."""
    # running total
    total = 0
    for i in x:
        total += i
    return total
'''
    assert code_shape.shape_of(SUM_LOOP) == code_shape.shape_of(documented)


def test_type_annotations_do_not_change_the_shape():
    annotated = """
def f(x: list[int]) -> int:
    total: int = 0
    for i in x:
        total += i
    return total
"""
    assert code_shape.shape_of(SUM_LOOP) == code_shape.shape_of(annotated)


def test_changing_a_comparison_does_change_the_shape():
    # Not a false positive. Flipping <= to < is a logic change, and the owner
    # wants those picked up.
    a = "def f(a, b):\n    return a <= b\n"
    b = "def f(a, b):\n    return a < b\n"
    assert code_shape.shape_of(a) != code_shape.shape_of(b)


def test_argument_order_is_not_lost_to_renaming():
    # Alpha-renaming must stay faithful: numbering by first appearance is what
    # keeps these two apart, and it is the property "same shape means same
    # meaning" rests on.
    a = "def f(a, b):\n    return a - b\n"
    b = "def f(a, b):\n    return b - a\n"
    assert code_shape.shape_of(a) != code_shape.shape_of(b)


def test_unparseable_code_falls_back_to_normalised_text():
    # Java, C++, or a Python file LeetCode returned truncated. It must still
    # produce a stable answer rather than raise.
    java = "class Solution { public int trap(int[] h) { return 0; } }"
    assert code_shape.shape_of(java) == code_shape.shape_of(java + "\n\n")
    assert code_shape.shape_of(java) != code_shape.shape_of(java.replace("0", "1"))


def test_has_new_shape_is_false_when_remote_is_already_covered():
    assert not code_shape.has_new_shape([SUM_LOOP_RENAMED], [SUM_LOOP])


def test_has_new_shape_is_true_when_remote_brings_something_unseen():
    assert code_shape.has_new_shape([SUM_LOOP, SUM_BUILTIN], [SUM_LOOP])


def test_has_new_shape_is_false_when_local_has_more_than_remote():
    # Local can legitimately hold versions LeetCode no longer lists. That is
    # not a reason to redownload.
    assert not code_shape.has_new_shape([SUM_LOOP], [SUM_LOOP, SUM_BUILTIN])
