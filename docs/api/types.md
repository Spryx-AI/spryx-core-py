# Types Module

The `types` module provides core type definitions and utilities used throughout the Spryx Core library. It focuses on improving type safety and providing tools for working with special types like sentinel values.

## Key Features

- **Type Definitions**: Common type aliases and generics
- **Type Utilities**: Helper functions for type operations
- **Sentinel Value Handling**: Utilities for working with the `NotGiven` sentinel

## API Reference

::: spryx_core.types
    options:
      show_root_heading: false
      show_source: true

## Usage Examples

### Working with NotGiven Type

The `NotGivenOr` type represents a value that can either be the sentinel `NOT_GIVEN` or a value of type `T`:

```python
from spryx_core import NOT_GIVEN, NotGivenOr
from typing import Dict, List

# Function that accepts optional parameters
def search_users(
    name: NotGivenOr[str] = NOT_GIVEN,
    age: NotGivenOr[int] = NOT_GIVEN,
    tags: NotGivenOr[List[str]] = NOT_GIVEN
) -> List[Dict]:
    # Build search criteria
    criteria = {}
    
    if name is not NOT_GIVEN:
        criteria["name"] = name
        
    if age is not NOT_GIVEN:
        criteria["age"] = age
        
    if tags is not NOT_GIVEN:
        criteria["tags"] = tags
    
    # Use criteria for search...
    return []  # Return search results
```

### Checking if a Value Was Given

The `is_given` utility function checks if a value is not the `NOT_GIVEN` sentinel:

```python
from spryx_core import NOT_GIVEN, is_given

# Example function with optional parameters
def update_profile(
    name=NOT_GIVEN,
    email=NOT_GIVEN,
    age=NOT_GIVEN
):
    updates = {}
    
    if is_given(name):
        updates["name"] = name
        
    if is_given(email):
        updates["email"] = email
        
    if is_given(age):
        updates["age"] = age
        
    return updates

# Different use cases
update_profile(name="John")                # {"name": "John"}
update_profile(email="john@example.com")   # {"email": "john@example.com"}
update_profile()                           # {}
```

### Default Values

Use `default_or_given` to provide a default value when a parameter wasn't provided:

```python
from spryx_core import NOT_GIVEN, default_or_given

def process_data(data, options=NOT_GIVEN):
    # Use default options if none were provided
    effective_options = default_or_given(options, {"timeout": 30, "retry": True})
    
    # Now use effective_options...
    print(f"Using options: {effective_options}")

# Different use cases
process_data("some_data")                          # Uses default options
process_data("some_data", {"timeout": 60})         # Uses provided options
```

## Best Practices

1. **Use NotGivenOr for Optional Parameters**: Instead of using `Optional[T]` with `None` as the default, consider using `NotGivenOr[T]` with `NOT_GIVEN` as the default for parameters where you need to distinguish between "parameter not provided" and "parameter explicitly set to None".

2. **Type Annotation**: Always include proper type annotations to leverage static type checking tools.

3. **Consistent Patterns**: Use the same pattern throughout your codebase for handling optional parameters. 