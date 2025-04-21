"""
Tests for the package initialization.
"""


import spryx_core


class TestInit:
    def test_package_exports(self):
        """Test that the package exports all expected attributes."""
        # Constants
        assert hasattr(spryx_core, "NOT_GIVEN")

        # Enums
        assert hasattr(spryx_core, "Environment")
        assert hasattr(spryx_core, "SortOrder")

        # ID
        assert hasattr(spryx_core, "EntityId")
        assert hasattr(spryx_core, "cast_entity_id")
        assert hasattr(spryx_core, "generate_entity_id")
        assert hasattr(spryx_core, "is_valid_ulid")

        # Sentinels
        assert hasattr(spryx_core, "NotGiven")

        # Time
        assert hasattr(spryx_core, "end_of_day")
        assert hasattr(spryx_core, "now_utc")
        assert hasattr(spryx_core, "parse_iso")
        assert hasattr(spryx_core, "start_of_day")
        assert hasattr(spryx_core, "to_iso")
        assert hasattr(spryx_core, "utc_from_timestamp")

        # Types
        assert hasattr(spryx_core, "NotGivenOr")
        assert hasattr(spryx_core, "default_or_given")
        assert hasattr(spryx_core, "is_given")

    def test_imports_usage(self):
        """Test that imported items can be used directly."""
        # Test a few representative imports
        assert spryx_core.NOT_GIVEN is spryx_core.NotGiven

        # Create a simple entity ID and check it
        entity_id = spryx_core.generate_entity_id()
        assert isinstance(entity_id, str)
        assert spryx_core.is_valid_ulid(entity_id)

        # Test SortOrder enum
        assert spryx_core.SortOrder.ASC == "asc"

        # Test is_given function
        assert spryx_core.is_given("test") is True
        assert spryx_core.is_given(spryx_core.NOT_GIVEN) is False
