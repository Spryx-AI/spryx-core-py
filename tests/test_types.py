"""
Tests for the types module.
"""


from spryx_core.constants import NOT_GIVEN
from spryx_core.sentinels import NotGiven
from spryx_core.types import NotGivenOr, default_or_given, is_given


class TestTypes:
    def test_is_given_with_regular_values(self):
        """Test is_given with regular values."""
        assert is_given("hello") is True
        assert is_given(123) is True
        assert is_given(0) is True
        assert is_given("") is True
        assert is_given(False) is True
        assert is_given(None) is True
        assert is_given([]) is True
        assert is_given({}) is True

    def test_is_given_with_not_given(self):
        """Test is_given with NotGiven."""
        assert is_given(NotGiven) is False
        assert is_given(NOT_GIVEN) is False

    def test_default_or_given_with_given_values(self):
        """Test default_or_given with given values."""
        assert default_or_given("hello", "default") == "hello"
        assert default_or_given(123, 456) == 123
        assert default_or_given(0, 456) == 0
        assert default_or_given("", "default") == ""
        assert default_or_given(False, True) is False
        assert default_or_given(None, "default") is None
        assert default_or_given([], [1, 2, 3]) == []
        assert default_or_given({}, {"a": 1}) == {}

    def test_default_or_given_with_not_given(self):
        """Test default_or_given with NotGiven."""
        assert default_or_given(NotGiven, "default") == "default"
        assert default_or_given(NOT_GIVEN, 123) == 123
        assert default_or_given(NOT_GIVEN, None) is None

    def test_default_or_given_without_default(self):
        """Test default_or_given without specifying a default."""
        assert default_or_given("hello") == "hello"
        assert default_or_given(NotGiven) is None
        assert default_or_given(NOT_GIVEN) is None

    def test_not_given_or_type(self):
        """Test NotGivenOr type annotations."""

        def func(x: NotGivenOr[str]) -> str:
            if is_given(x):
                return x
            return "default"

        assert func("hello") == "hello"
        assert func(NotGiven) == "default"
        assert func(NOT_GIVEN) == "default"
