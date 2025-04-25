# API Reference

This section provides detailed documentation for all modules and functions in the Spryx Core library.

## Modules Overview

Spryx Core is organized into several modules, each focused on a specific functionality:

| Module | Description |
|--------|-------------|
| [`id`](id.md) | ID generation and validation utilities using ULID |
| [`time`](time.md) | Date and time utilities for working with UTC timestamps |
| [`pagination`](pagination.md) | Models for paginated responses in APIs |
| [`types`](types.md) | Core type definitions and type utilities |
| [`constants`](constants.md) | Library-wide constants |
| [`sentinels`](sentinels.md) | Sentinel value implementations |
| [`enums`](enums.md) | Enumerated values used throughout the library |
| [`errors`](errors.md) | Common error classes |
| [`security`](security.md) | Security utilities including permissions and token claims |

## Import Structure

The most commonly used utilities are available directly from the top-level package:

```python
from spryx_core import (
    # ID
    generate_entity_id, is_valid_ulid, cast_entity_id, EntityId,
    
    # Time
    now_utc, to_iso, parse_iso, start_of_day, end_of_day,
    
    # Pagination
    Page,
    
    # Security
    Permission, AppClaims, UserClaims, TokenClaims,
    
    # Sentinels
    NOT_GIVEN, NotGiven,
    
    # Types
    NotGivenOr, default_or_given, is_given,
    
    # Enums
    Environment, SortOrder
)
```

For less commonly used functions or more specialized use cases, you can import from the specific module:

```python
# For specialized time operations
from spryx_core.time import utc_from_timestamp

# For specific error classes
from spryx_core.errors import SpryxError

# For detailed security features
from spryx_core.security import BaseClaims
```

## API Stability

Spryx Core follows semantic versioning (SemVer):

- **Stable APIs**: All public functions, classes and constants exported from `__init__.py` are considered stable and will not have breaking changes in minor releases.
- **Experimental APIs**: Functions and classes that are only available from their specific modules may have breaking changes in minor releases.

APIs marked as experimental in the documentation may change in future versions. 