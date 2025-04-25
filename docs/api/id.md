# ID Module

The `id` module provides utilities for generating and validating entity IDs. It primarily uses ULID (Universally Unique Lexicographically Sortable Identifier) as the format for IDs, with fallback to UUID4 if the ULID library is not available.

## Key Features

- **ULID Generation**: Creates sortable, unique identifiers
- **Type Safety**: Provides the `EntityId` type for improved type checking
- **Validation**: Tools to validate ID format

## API Reference

::: spryx_core.id
    options:
      show_root_heading: false
      show_source: true

## Usage Examples

### Basic ID Generation

```python
from spryx_core import generate_entity_id

# Generate a new unique ID
entity_id = generate_entity_id()
print(entity_id)  # Example: 01HNJG7VWTZA0CGTJ9T7WG9CPB
```

### Validation

```python
from spryx_core import is_valid_ulid

# Check if an ID is in valid ULID format
valid_id = "01HNJG7VWTZA0CGTJ9T7WG9CPB"
invalid_id = "not-a-valid-id"

print(is_valid_ulid(valid_id))    # True
print(is_valid_ulid(invalid_id))  # False
```

### Type Safety

```python
from spryx_core import EntityId, cast_entity_id
from typing import Dict

# Use EntityId as a type hint
def get_user(user_id: EntityId) -> Dict:
    # Function implementation...
    return {"id": user_id, "name": "Test User"}

# Cast a string to EntityId type
user_id = cast_entity_id("01HNJG7VWTZA0CGTJ9T7WG9CPB")
user = get_user(user_id)
```

## ULID vs UUID

ULIDs offer several advantages over UUIDs:

1. **Sortability**: ULIDs are lexicographically sortable, meaning they can be sorted as strings
2. **Time-based**: The first part of a ULID encodes the creation timestamp
3. **Human readability**: ULIDs use Crockford's base32 encoding for improved readability
4. **Compact representation**: 26 characters vs 36 for UUID

If the `ulid` package is not installed, the library will automatically fall back to generating UUID4 strings instead. 