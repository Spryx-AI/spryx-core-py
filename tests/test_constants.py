"""
Tests for the constants module.
"""

import pytest

from spryx_core.constants import NOT_GIVEN
from spryx_core.sentinels import NotGiven


class TestConstants:
    def test_not_given_constant(self):
        """Test that NOT_GIVEN is a NotGiven instance."""
        assert NOT_GIVEN is not None
        assert NOT_GIVEN._name == "NotGiven"
        assert str(NOT_GIVEN) == "NotGiven"
        assert bool(NOT_GIVEN) is False

    def test_not_given_is_singleton(self):
        """Test that NOT_GIVEN is a singleton instance."""
        # NOT_GIVEN should be the same instance as NotGiven class
        assert NOT_GIVEN is NotGiven

    def test_not_given_behavior(self):
        """Test NOT_GIVEN behavior in conditionals."""
        # Should be falsey
        if NOT_GIVEN:
            pytest.fail("NOT_GIVEN should be falsey")

        # Should be usable in if/else
        value = "default" if NOT_GIVEN else "value"
        assert value == "value"

        # Testing as a default parameter
        def func(param=NOT_GIVEN):
            return "default" if param is NOT_GIVEN else param

        assert func() == "default"
        assert func("value") == "value"
        assert func(None) is None
