"""Test Snap Package Template."""

import primeiro_template


def test_import() -> None:
    """Test that the package can be imported."""
    assert isinstance(primeiro_template.__name__, str)
