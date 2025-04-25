# Enums Module

The `enums` module provides standardized enumeration types used throughout Spryx projects. These enums create a type-safe way to represent fixed sets of values and common patterns.

## Key Features

- **Type Safety**: Proper enumeration types for compile-time checking
- **String Serialization**: Easy serialization to and from strings
- **Common Patterns**: Standard enums for environment and sorting

## API Reference

::: spryx_core.enums
    options:
      show_root_heading: false
      show_source: true

## Usage Examples

### Environment Enum

The `Environment` enum represents application environments (development, testing, production):

```python
from spryx_core import Environment
import os

# Check current environment
current_env = Environment.current()
print(f"Current environment: {current_env}")

# Environment-specific behavior
if current_env == Environment.PRODUCTION:
    # Production-specific configuration
    database_url = "production-db.example.com"
elif current_env == Environment.STAGING:
    # Staging-specific configuration
    database_url = "staging-db.example.com"
else:
    # Development/testing configuration
    database_url = "localhost"

# Setting environment
os.environ["ENVIRONMENT"] = "staging"
current_env = Environment.current()
print(f"Updated environment: {current_env}")  # Environment.STAGING
```

### SortOrder Enum

The `SortOrder` enum provides standardized values for sort direction (ascending or descending):

```python
from spryx_core import SortOrder

# Function that accepts sort order
def fetch_sorted_users(sort_field="name", sort_order=SortOrder.ASCENDING):
    # Generate SQL or query based on sort order
    direction = "ASC" if sort_order == SortOrder.ASCENDING else "DESC"
    query = f"SELECT * FROM users ORDER BY {sort_field} {direction}"
    print(f"Executing query: {query}")
    
    # Return sorted users
    return []

# Usage examples
users = fetch_sorted_users()                              # Default ascending
users = fetch_sorted_users(sort_order=SortOrder.DESCENDING)  # Explicit descending
```

### Converting Between Strings and Enums

```python
from spryx_core import Environment, SortOrder

# String to Enum
env_str = "production"
env = Environment(env_str)
print(env)  # Environment.PRODUCTION
print(env == Environment.PRODUCTION)  # True

# Enum to String
sort_order = SortOrder.DESCENDING
sort_str = sort_order.value
print(sort_str)  # "desc"
```

### Using Enums in APIs

When using these enums in API parameters or responses:

```python
from fastapi import FastAPI, Query
from spryx_core import SortOrder
from enum import Enum
from typing import List, Dict

app = FastAPI()

@app.get("/users")
async def get_users(
    sort_field: str = "created_at",
    sort_order: SortOrder = SortOrder.DESCENDING
):
    # Use the enum directly in your API handler
    direction = "ASC" if sort_order == SortOrder.ASCENDING else "DESC"
    # ... rest of implementation
    return {"users": [], "sort_field": sort_field, "sort_order": sort_order.value}
```

## Best Practices

1. **Use Enums for Fixed Sets**: When a variable can only take a limited set of values, use an enum instead of strings or integers.

2. **Type Checking**: Leverage Python's type checking to catch errors at compile time with enum types.

3. **String Conversion**: When working with external systems or APIs, use the enum's `value` property to convert to strings.

4. **Default Values**: Provide sensible defaults for enum parameters (like `SortOrder.ASCENDING` for sorting). 