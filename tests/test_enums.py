"""
Tests for the enums module.
"""

import pytest

from spryx_core.enums import Environment, SortOrder


class TestEnums:
    def test_sort_order_values(self):
        """Test SortOrder enum values."""
        assert SortOrder.ASC == "asc"
        assert SortOrder.DESC == "desc"

        # Test all enum values
        assert list(SortOrder) == [SortOrder.ASC, SortOrder.DESC]
        assert len(SortOrder) == 2

    def test_sort_order_string_comparison(self):
        """Test SortOrder string comparison."""
        assert SortOrder.ASC == "asc"
        assert "asc" == SortOrder.ASC
        assert SortOrder.DESC == "desc"
        assert "desc" == SortOrder.DESC

    def test_sort_order_from_string(self):
        """Test creating SortOrder from string."""
        assert SortOrder("asc") == SortOrder.ASC
        assert SortOrder("desc") == SortOrder.DESC

    def test_sort_order_invalid_string(self):
        """Test creating SortOrder from invalid string."""
        with pytest.raises(ValueError):
            SortOrder("invalid")

    def test_environment_values(self):
        """Test Environment enum values."""
        assert Environment.DEV == "dev"
        assert Environment.STAGING == "staging"
        assert Environment.PRODUCTION == "production"

        # Test all enum values
        assert list(Environment) == [
            Environment.DEV,
            Environment.STAGING,
            Environment.PRODUCTION,
        ]
        assert len(Environment) == 3

    def test_environment_string_comparison(self):
        """Test Environment string comparison."""
        assert Environment.DEV == "dev"
        assert "dev" == Environment.DEV
        assert Environment.STAGING == "staging"
        assert "staging" == Environment.STAGING
        assert Environment.PRODUCTION == "production"
        assert "production" == Environment.PRODUCTION

    def test_environment_from_string(self):
        """Test creating Environment from string."""
        assert Environment("dev") == Environment.DEV
        assert Environment("staging") == Environment.STAGING
        assert Environment("production") == Environment.PRODUCTION

    def test_environment_invalid_string(self):
        """Test creating Environment from invalid string."""
        with pytest.raises(ValueError):
            Environment("invalid")
