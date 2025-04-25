# Permissions Module

The `permissions` module provides utilities for defining and working with permission strings in Spryx applications. It helps enforce consistent permission naming and improves type safety when dealing with access control.

## Key Features

- **Standardized Format**: Consistent permission string format
- **Type Safety**: Enum-based permission definitions for compile-time checking
- **Extensibility**: Easy to extend for domain-specific permissions

## API Reference

::: spryx_core.permissions
    options:
      show_root_heading: false
      show_source: true

## Usage Examples

### Basic Usage

The `Permission` enum defines standard permission strings:

```python
from spryx_core.permissions import Permission

# Check if a user has a specific permission
def has_permission(user, permission):
    return permission in user.permissions

# Usage with strongly-typed permissions
user_can_read = has_permission(current_user, Permission.READ_USERS)
user_can_write = has_permission(current_user, Permission.WRITE_USERS)
```

### In Authorization Middleware

Using the permissions enum in an authorization middleware:

```python
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from spryx_core.permissions import Permission
from typing import List

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# A dependency that checks for required permissions
def requires_permissions(required_permissions: List[Permission]):
    def dependency(token: str = Depends(oauth2_scheme)):
        # Decode token and get user permissions
        user_permissions = get_user_permissions(token)
        
        # Check if the user has all required permissions
        missing_permissions = [
            p for p in required_permissions 
            if p not in user_permissions
        ]
        
        if missing_permissions:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail=f"Missing required permissions: {missing_permissions}"
            )
        
        return True
    
    return dependency

# Example usage in an API endpoint
@app.get(
    "/users", 
    dependencies=[Depends(requires_permissions([Permission.READ_USERS]))]
)
def get_users():
    # Only accessible if user has READ_USERS permission
    return {"users": [...]}

# Mock implementation
def get_user_permissions(token: str) -> List[Permission]:
    # In a real implementation, this would decode the token
    # and retrieve the user's permissions
    return [Permission.READ_USERS]
```

### Extending with Custom Permissions

You can extend the base `Permission` enum for domain-specific permissions:

```python
from enum import StrEnum, unique
from spryx_core.permissions import Permission as BasePermission

@unique
class ProductPermission(StrEnum):
    READ_PRODUCTS = "products:read"
    WRITE_PRODUCTS = "products:write"
    DELETE_PRODUCTS = "products:delete"

# Combined permissions
ALL_PERMISSIONS = list(BasePermission) + list(ProductPermission)
```

## Best Practices

1. **Consistent Format**: Follow the `resource:action` format for permission strings.

2. **Group by Resource**: Organize permissions by resource type (users, orders, etc.).

3. **Granular Control**: Define specific read/write permissions rather than general admin permissions.

4. **Permission Checking**: Create helper functions to check permissions consistently across your application. 