# Pagination Module

The `pagination` module provides standardized models for implementing and handling paginated results in APIs and data retrieval operations.

## Key Features

- **Generic Page Model**: Works with any data type
- **Metadata**: Includes essential pagination metadata
- **Convenience Properties**: Helper properties for pagination UI

## API Reference

::: spryx_core.pagination
    options:
      show_root_heading: false
      show_source: true

## Usage Examples

### Basic Usage

```python
from spryx_core import Page
from typing import List

# Sample data to paginate
all_items = ["item1", "item2", "item3", "item4", "item5", "item6", "item7"]

# Create a paginated response
page_size = 3
current_page = 2
start_idx = (current_page - 1) * page_size
end_idx = start_idx + page_size

page = Page(
    items=all_items[start_idx:end_idx],  # Items for this page
    page=current_page,                    # Current page number (1-based)
    page_size=page_size,                  # Items per page
    total=len(all_items)                  # Total items across all pages
)

print(f"Page {page.page} of {page.total_pages}")  # Page 2 of 3
print(f"Items: {page.items}")                     # Items: ['item4', 'item5', 'item6']
```

### Pagination Metadata

The `Page` model calculates helpful metadata properties:

```python
from spryx_core import Page

# Create a sample paginated response
page = Page(
    items=["item4", "item5", "item6"],
    page=2,
    page_size=3,
    total=10
)

# Access metadata
print(f"Current page: {page.page}")         # 2
print(f"Items per page: {page.page_size}")  # 3
print(f"Total items: {page.total}")         # 10
print(f"Total pages: {page.total_pages}")   # 4

# Navigation helpers
print(f"Has previous page: {page.has_previous}")  # True
print(f"Has next page: {page.has_next}")          # True
print(f"Previous page: {page.previous_page}")     # 1
print(f"Next page: {page.next_page}")             # 3
```

### With Different Data Types

The `Page` model is generic and can be used with any data type:

```python
from spryx_core import Page
from typing import Dict, List

# With dictionaries
users = [
    {"id": "1", "name": "Alice"},
    {"id": "2", "name": "Bob"}
]

user_page = Page(
    items=users,
    page=1,
    page_size=10,
    total=2
)

# With custom classes
class Product:
    def __init__(self, id: str, name: str):
        self.id = id
        self.name = name

products = [
    Product("p1", "Laptop"),
    Product("p2", "Phone")
]

product_page = Page(
    items=products,
    page=1,
    page_size=10,
    total=2
)
```

## Integration with API Frameworks

### FastAPI Example

```python
from fastapi import FastAPI, Query
from spryx_core import Page
from typing import List, Dict

app = FastAPI()

# Sample data
items = [{"id": f"item{i}", "value": f"Value {i}"} for i in range(1, 101)]

@app.get("/items", response_model=Page[Dict])
async def get_items(
    page: int = Query(1, ge=1),
    page_size: int = Query(10, ge=1, le=100)
):
    start_idx = (page - 1) * page_size
    end_idx = start_idx + page_size
    
    return Page(
        items=items[start_idx:end_idx],
        page=page,
        page_size=page_size,
        total=len(items)
    )
``` 