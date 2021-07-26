from join_function import join


def test_join_use_case() -> None:
    assert join([1, 2, 3], ", ") == "1, 2, 3"


def test_join_edge_case_single_item() -> None:
    assert join([1], ", ") == "1"


def test_join_edge_empty_delimiter() -> None:
    assert join([1, 2, 3], "") == "123"
