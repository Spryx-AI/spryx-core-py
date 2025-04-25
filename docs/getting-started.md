# Getting Started

This guide will help you get started with the Spryx Core library, explaining its main features and providing practical examples.

## Installation

Install the package using pip:

```bash
pip install spryx-core
```

For development or optional features, you might want to include extra dependencies:

```bash
# For ULID support (recommended for ID generation)
pip install "spryx-core[ulid]"
```

## Core Features

### Entity ID Generation

Spryx Core provides a standardized way to generate and validate entity IDs using ULIDs (Universally Unique Lexicographically Sortable Identifier):

```python
from spryx_core import generate_entity_id, is_valid_ulid, cast_entity_id

# Generate a new ID
new_id = generate_entity_id()  # Returns a ULID as a string
print(new_id)  # Example: 01HNJG7VWTZA0CGTJ9T7WG9CPB

# Validate if a string is a valid ULID
is_valid = is_valid_ulid(new_id)  # Returns True for valid ULIDs

# Cast a string to EntityId type
typed_id = cast_entity_id(new_id)  # Type checking for EntityId
```

### Time and Date Utilities

Working with dates and times in UTC is simplified with these utilities:

```python
from spryx_core import now_utc, to_iso, parse_iso, start_of_day, end_of_day

# Get current UTC time
current_time = now_utc()

# Format as ISO 8601 string
iso_string = to_iso(current_time)
print(iso_string)  # Example: 2023-12-01T14:32:15.123456Z

# Parse ISO 8601 string
parsed_time = parse_iso("2023-12-01T14:32:15Z")

# Get start and end of day
day_start = start_of_day(current_time)  # 00:00:00.000000
day_end = end_of_day(current_time)      # 23:59:59.999999
```

### Pagination

For APIs that return paginated results, use the `Page` model:

```python
from spryx_core import Page

# Create a paginated response
page = Page(
    items=["item1", "item2", "item3"],  # The actual data for the current page
    page=1,                             # Current page number (1-based)
    page_size=10,                       # Items per page
    total=25                            # Total items across all pages
)

# Access pagination metadata
print(f"Current page: {page.page}")
print(f"Total pages: {page.total_pages}")
print(f"Has next page: {page.has_next}")
print(f"Next page number: {page.next_page}")
```

### Sentinel Values

Use sentinel values to represent special cases more explicitly than using `None`:

```python
from spryx_core import NOT_GIVEN, is_given, default_or_given

# Function with optional parameter using NOT_GIVEN sentinel
def update_user(name=NOT_GIVEN, email=NOT_GIVEN):
    updates = {}
    
    if is_given(name):
        updates["name"] = name
        
    if is_given(email):
        updates["email"] = email
        
    return updates

# Different from passing None - clearly indicates the parameter wasn't provided
result1 = update_user(name="John")        # {"name": "John"}
result2 = update_user(email="j@test.com") # {"email": "j@test.com"}
result3 = update_user()                   # {}

# Set a default value if the parameter wasn't given
value = default_or_given(NOT_GIVEN, "default_value")  # Returns "default_value"
```

### Security Utilities

Spryx Core provides security-related utilities for permission handling and JWT token validation:

```python
from spryx_core import Permission, UserClaims, TokenClaims
from datetime import datetime, timedelta, UTC
import json

# Working with permissions
def check_user_access(user_permissions, required_permission):
    return required_permission in user_permissions

user_permissions = [Permission.READ_USERS, Permission.READ_ORDERS]
can_read_users = check_user_access(user_permissions, Permission.READ_USERS)  # True
can_write_users = check_user_access(user_permissions, Permission.WRITE_USERS)  # False

# Working with JWT claims
# Example JWT payload
claims_data = {
    "iss": "spryx-auth",
    "sub": "user123",
    "aud": "my-app",
    "iat": datetime.now(UTC),
    "exp": datetime.now(UTC) + timedelta(hours=1),
    "token_type": "user",
    "permissions": ["users:read", "orders:read"]
}

# Convert datetime to string for this example (JWT libraries would handle this)
serializable_data = {
    **claims_data,
    "iat": claims_data["iat"].isoformat(),
    "exp": claims_data["exp"].isoformat()
}
json_data = json.dumps(serializable_data)

# In a real app, you would decode JWT and then:
parsed_data = json.loads(json_data)
# Convert back string dates to datetime for validation
parsed_data["iat"] = datetime.fromisoformat(parsed_data["iat"])
parsed_data["exp"] = datetime.fromisoformat(parsed_data["exp"])

# Validate claims
try:
    # This automatically discriminates between UserClaims and AppClaims
    token_claims = TokenClaims.model_validate(parsed_data)
    # Access user-specific fields
    if hasattr(token_claims, "permissions"):
        print(f"User permissions: {token_claims.permissions}")
except Exception as e:
    print(f"Invalid token: {e}")
```

### Environment Enums

Control environment-specific behavior:

```python
from spryx_core import Environment

# Check current environment
if Environment.current() == Environment.PRODUCTION:
    # Production-specific behavior
    pass
elif Environment.current() == Environment.DEVELOPMENT:
    # Development-specific behavior
    pass
```

## Next Steps

Explore the [API Reference](api/index.md) for detailed documentation of all modules and functions. 