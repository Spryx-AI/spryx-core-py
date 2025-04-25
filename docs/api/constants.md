# Constants Module

The `constants` module provides package-wide constant values used across spryx-core. These constants serve as singleton instances and standard values to maintain consistency throughout the codebase.

## Key Features

- **Singleton Sentinels**: Shared instances of sentinel objects
- **Global Access**: Centralized location for commonly used constants

## API Reference

::: spryx_core.constants
    options:
      show_root_heading: false
      show_source: true

## Usage Examples

### NOT_GIVEN Sentinel

The most important constant is the `NOT_GIVEN` sentinel, which is a singleton instance of the `NotGiven` class:

```python
from spryx_core import NOT_GIVEN

# Using NOT_GIVEN as a default parameter value
def update_user(name=NOT_GIVEN, email=NOT_GIVEN):
    updates = {}
    
    if name is not NOT_GIVEN:
        updates["name"] = name
        
    if email is not NOT_GIVEN:
        updates["email"] = email
        
    return updates

# Usage
update_user(name="John")        # {"name": "John"}
update_user(email="j@test.com") # {"email": "j@test.com"}
update_user()                   # {}
```

## Best Practices

1. **Import from Top Level**: For commonly used constants like `NOT_GIVEN`, import directly from the top-level package:

   ```python
   from spryx_core import NOT_GIVEN
   ```

2. **Identity Comparison**: When comparing against sentinel values, use the `is` operator for identity comparison:

   ```python
   if value is NOT_GIVEN:
       # Handle not given case
   ```

3. **Consistency**: Use the constants consistently throughout your codebase to maintain predictable behavior. 