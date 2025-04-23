"""
Tests for the pagination module.
"""

import pytest
from pydantic import ValidationError

from spryx_core.pagination import Page


class TestPagination:
    def test_page_model_basic(self):
        """Test the Page model with valid data."""
        # Create a page with sample data
        page = Page(items=["item1", "item2", "item3"], page=2, page_size=3, total=10)

        # Check fields
        assert page.items == ["item1", "item2", "item3"]
        assert page.page == 2
        assert page.page_size == 3
        assert page.total == 10

        # Check computed fields
        assert page.total_pages == 4  # 10 items with 3 per page = 4 pages
        assert page.has_previous is True
        assert page.has_next is True
        assert page.previous_page == 1
        assert page.next_page == 3

    def test_page_model_first_page(self):
        """Test the Page model for the first page."""
        page = Page(items=["item1", "item2", "item3"], page=1, page_size=3, total=10)

        assert page.has_previous is False
        assert page.has_next is True
        assert page.previous_page is None
        assert page.next_page == 2

    def test_page_model_last_page(self):
        """Test the Page model for the last page."""
        page = Page(items=["item8", "item9", "item10"], page=4, page_size=3, total=10)

        assert page.has_previous is True
        assert page.has_next is False
        assert page.previous_page == 3
        assert page.next_page is None

    def test_page_model_single_page(self):
        """Test the Page model with only one page."""
        page = Page(items=["item1", "item2"], page=1, page_size=5, total=2)

        assert page.total_pages == 1
        assert page.has_previous is False
        assert page.has_next is False
        assert page.previous_page is None
        assert page.next_page is None

    def test_page_model_empty(self):
        """Test the Page model with no items."""
        page = Page(items=[], page=1, page_size=10, total=0)

        assert page.total_pages == 0
        assert page.has_previous is False
        assert page.has_next is False
        assert page.previous_page is None
        assert page.next_page is None

    def test_page_model_validation(self):
        """Test validation of the Page model."""
        # Invalid page number (less than 1)
        with pytest.raises(ValidationError):
            Page(items=["item1"], page=0, page_size=10, total=1)  # Invalid

        # Invalid page_size (less than or equal to 0)
        with pytest.raises(ValidationError):
            Page(items=["item1"], page=1, page_size=0, total=1)  # Invalid

        # Invalid total (less than 0)
        with pytest.raises(ValidationError):
            Page(items=["item1"], page=1, page_size=10, total=-1)  # Invalid

    def test_page_model_with_different_types(self):
        """Test Page model with different types of items."""
        # Page with dictionary items
        dict_page = Page(
            items=[{"id": 1, "name": "item1"}, {"id": 2, "name": "item2"}],
            page=1,
            page_size=2,
            total=2,
        )
        assert len(dict_page.items) == 2
        assert dict_page.items[0]["name"] == "item1"

        # Page with integer items
        int_page = Page(items=[1, 2, 3], page=1, page_size=3, total=3)
        assert len(int_page.items) == 3
        assert int_page.items[0] == 1
