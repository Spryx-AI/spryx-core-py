"""
Tests for the ID module.
"""

import re
import uuid
from unittest.mock import patch


from spryx_core.id import EntityId, cast_entity_id, generate_entity_id, is_valid_ulid


class TestId:
    def test_entity_id_type(self):
        """Test that EntityId is a proper NewType."""
        id_value = "01H2XGMTVZ1QW1F4KJJNVD0YJR"
        entity_id = EntityId(id_value)
        assert isinstance(entity_id, str)
        assert entity_id == id_value

    def test_generate_entity_id_with_ulid(self):
        """Test entity ID generation with ULID."""
        entity_id = generate_entity_id()
        assert isinstance(entity_id, str)
        # ULID is 26 chars in Crockford base32
        assert len(entity_id) == 26
        assert re.match(r"^[0-9A-HJKMNP-TV-Z]{26}$", entity_id)

    @patch("spryx_core.id._has_ulid", False)
    def test_generate_entity_id_with_uuid_fallback(self):
        """Test entity ID generation with UUID fallback."""
        mock_uuid = "12345678-1234-5678-1234-567812345678"
        with patch("uuid.uuid4", return_value=uuid.UUID(mock_uuid)):
            entity_id = generate_entity_id()
            assert isinstance(entity_id, str)
            assert entity_id == mock_uuid

    def test_is_valid_ulid(self):
        """Test ULID validation."""
        # Valid ULID
        assert is_valid_ulid("01H2XGMTVZ1QW1F4KJJNVD0YJR") is True

        # Invalid ULIDs
        assert is_valid_ulid("not-a-ulid") is False
        assert is_valid_ulid("") is False
        assert is_valid_ulid("01H2XGMTVZ1QW1F4KJJNVD0YJ") is False  # Too short
        assert is_valid_ulid("01H2XGMTVZ1QW1F4KJJNVD0YJRX") is False  # Too long
        assert is_valid_ulid("01H2XGMTVZ1QW1F4KJJNVD0YJ$") is False  # Invalid char
        assert is_valid_ulid("01h2xgmtvz1qw1f4kjjnvd0yjr") is False  # Lowercase

    def test_cast_entity_id(self):
        """Test casting a string to EntityId."""
        id_value = "01H2XGMTVZ1QW1F4KJJNVD0YJR"
        entity_id = cast_entity_id(id_value)
        assert isinstance(entity_id, str)
        assert entity_id == id_value
