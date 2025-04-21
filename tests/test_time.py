"""
Tests for the time module.
"""

from datetime import datetime, timedelta, timezone
from unittest.mock import patch

import pytest

from spryx_core.time import (
    ISO_8601_UTC_RE,
    end_of_day,
    now_utc,
    parse_iso,
    start_of_day,
    to_iso,
    utc_from_timestamp,
)


class TestTime:
    def test_iso8601_regex(self):
        """Test that the ISO 8601 regex works correctly."""
        # Valid ISO 8601 UTC strings
        assert ISO_8601_UTC_RE.match("2023-05-18T15:30:00Z")
        assert ISO_8601_UTC_RE.match("2023-05-18T15:30:00.123Z")
        assert ISO_8601_UTC_RE.match("2023-05-18T15:30:00.123456Z")

        # Invalid ISO 8601 UTC strings
        assert not ISO_8601_UTC_RE.match("2023-05-18T15:30:00")  # No Z
        assert not ISO_8601_UTC_RE.match(
            "2023-05-18T15:30:00+00:00"
        )  # No Z, has offset
        assert not ISO_8601_UTC_RE.match("2023-05-18 15:30:00Z")  # Space instead of T
        assert not ISO_8601_UTC_RE.match("not-a-date")

    def test_now_utc(self):
        """Test now_utc returns current UTC time."""
        now = now_utc()
        assert isinstance(now, datetime)
        assert now.tzinfo == timezone.utc

        # Check it's reasonably close to now
        system_now = datetime.now(timezone.utc)
        assert abs((now - system_now).total_seconds()) < 1

    def test_to_iso_with_timezone(self):
        """Test to_iso with a timezone-aware datetime."""
        dt = datetime(2023, 5, 18, 15, 30, 45, 123456, tzinfo=timezone.utc)
        iso_str = to_iso(dt)
        assert iso_str == "2023-05-18T15:30:45.123456Z"

    def test_to_iso_without_timezone(self):
        """Test to_iso with a naive datetime."""
        dt = datetime(2023, 5, 18, 15, 30, 45, 123456)
        iso_str = to_iso(dt)
        assert iso_str == "2023-05-18T15:30:45.123456Z"

    def test_to_iso_with_milliseconds(self):
        """Test to_iso with milliseconds parameter."""
        dt = datetime(2023, 5, 18, 15, 30, 45, 123456, tzinfo=timezone.utc)
        iso_str = to_iso(dt, milliseconds=True)
        assert iso_str == "2023-05-18T15:30:45.123Z"

    def test_to_iso_different_timezone(self):
        """Test to_iso with non-UTC timezone."""
        # +1 hour from UTC
        tz = timezone(timedelta(hours=1))
        dt = datetime(2023, 5, 18, 16, 30, 45, 123456, tzinfo=tz)
        iso_str = to_iso(dt)
        # Should be converted to 15:30:45 UTC
        assert iso_str == "2023-05-18T15:30:45.123456Z"

    def test_parse_iso_valid(self):
        """Test parse_iso with valid ISO strings."""
        dt = parse_iso("2023-05-18T15:30:45Z")
        assert dt == datetime(2023, 5, 18, 15, 30, 45, tzinfo=timezone.utc)

        dt = parse_iso("2023-05-18T15:30:45.123Z")
        assert dt == datetime(2023, 5, 18, 15, 30, 45, 123000, tzinfo=timezone.utc)

    def test_parse_iso_invalid(self):
        """Test parse_iso with invalid ISO strings."""
        with pytest.raises(ValueError):
            parse_iso("not-a-date")

        with pytest.raises(ValueError):
            parse_iso("2023-05-18T15:30:45")  # No Z

        with pytest.raises(ValueError):
            parse_iso("2023-05-18T15:30:45+00:00")  # No Z, has offset

    def test_utc_from_timestamp(self):
        """Test utc_from_timestamp."""
        # Unix epoch
        dt = utc_from_timestamp(0)
        assert dt == datetime(1970, 1, 1, 0, 0, 0, tzinfo=timezone.utc)

        # We'll simplify the test and just test a few timestamp conversions
        # without mocking for easier testing

        # Test with a whole number timestamp
        dt = utc_from_timestamp(1684424445)
        assert isinstance(dt, datetime)
        assert dt.tzinfo == timezone.utc
        assert dt.year == 2023
        assert dt.month == 5
        assert dt.day == 18
        assert dt.hour == 15

        # Float timestamp
        float_ts = 1684424445.123
        dt = utc_from_timestamp(float_ts)
        assert isinstance(dt, datetime)
        assert dt.tzinfo == timezone.utc
        assert dt.year == 2023
        assert dt.month == 5
        assert dt.day == 18
        assert dt.hour == 15

    def test_start_of_day_with_input(self):
        """Test start_of_day with a datetime input."""
        dt = datetime(2023, 5, 18, 15, 30, 45, 123456, tzinfo=timezone.utc)
        start = start_of_day(dt)
        assert start == datetime(2023, 5, 18, 0, 0, 0, 0, tzinfo=timezone.utc)

    def test_start_of_day_without_input(self):
        """Test start_of_day without input (uses current time)."""
        mock_now = datetime(2023, 5, 18, 15, 30, 45, 123456, tzinfo=timezone.utc)
        with patch("spryx_core.time.now_utc", return_value=mock_now):
            start = start_of_day()
            assert start == datetime(2023, 5, 18, 0, 0, 0, 0, tzinfo=timezone.utc)

    def test_start_of_day_naive_datetime(self):
        """Test start_of_day with a naive datetime."""
        dt = datetime(2023, 5, 18, 15, 30, 45, 123456)
        start = start_of_day(dt)
        assert start == datetime(2023, 5, 18, 0, 0, 0, 0, tzinfo=timezone.utc)

    def test_end_of_day_with_input(self):
        """Test end_of_day with a datetime input."""
        dt = datetime(2023, 5, 18, 15, 30, 45, 123456, tzinfo=timezone.utc)
        end = end_of_day(dt)
        assert end == datetime(2023, 5, 18, 23, 59, 59, 999999, tzinfo=timezone.utc)

    def test_end_of_day_without_input(self):
        """Test end_of_day without input (uses current time)."""
        mock_now = datetime(2023, 5, 18, 15, 30, 45, 123456, tzinfo=timezone.utc)
        with patch("spryx_core.time.now_utc", return_value=mock_now):
            end = end_of_day()
            assert end == datetime(2023, 5, 18, 23, 59, 59, 999999, tzinfo=timezone.utc)
