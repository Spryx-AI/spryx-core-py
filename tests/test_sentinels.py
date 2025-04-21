"""
Tests for the sentinels module.
"""

import pickle


from spryx_core.sentinels import NotGiven, _SentinelBase


class TestSentinels:
    def test_sentinel_name(self):
        """Test that sentinels have the correct name."""
        sentinel = _SentinelBase("TestSentinel")
        assert str(sentinel) == "TestSentinel"
        assert repr(sentinel) == "TestSentinel"

    def test_sentinel_bool(self):
        """Test that sentinels always evaluate to False."""
        sentinel = _SentinelBase("TestSentinel")
        assert bool(sentinel) is False
        assert not sentinel

    def test_sentinel_equality(self):
        """Test sentinel equality."""
        sentinel1 = _SentinelBase("TestSentinel")
        sentinel2 = _SentinelBase("TestSentinel")
        sentinel3 = _SentinelBase("OtherSentinel")

        # Different instances with same name are not equal by identity
        assert sentinel1 is not sentinel2
        # Different instances with different names are not equal
        assert sentinel1 != sentinel3

    def test_not_given_singleton(self):
        """Test that NotGiven is a singleton instance."""
        assert NotGiven is NotGiven
        assert NotGiven._name == "NotGiven"
        assert str(NotGiven) == "NotGiven"
        assert bool(NotGiven) is False

    def test_sentinel_pickling(self):
        """Test that sentinels can be pickled and unpickled."""
        sentinel = _SentinelBase("TestSentinel")
        pickled = pickle.dumps(sentinel)
        unpickled = pickle.loads(pickled)

        assert unpickled._name == "TestSentinel"
        assert str(unpickled) == "TestSentinel"
        assert bool(unpickled) is False

    def test_not_given_pickling(self):
        """Test that NotGiven can be pickled and unpickled."""
        pickled = pickle.dumps(NotGiven)
        unpickled = pickle.loads(pickled)

        assert unpickled._name == "NotGiven"
        assert str(unpickled) == "NotGiven"
        assert bool(unpickled) is False
