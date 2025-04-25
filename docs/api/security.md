# Security Module

The `security` module provides utilities for implementing security features in Spryx applications, including permission handling, token claims validation, and related functionality.

## Key Features

- **Permission Management**: Typed permission enums with consistent format
- **Token Claims**: Pydantic models for validating JWT claims
- **Type Safety**: Strong typing for security-related components

## API Reference

### Permissions

::: spryx_core.security.permissions
    options:
      show_root_heading: false
      show_source: true

### Claims

::: spryx_core.security.claims
    options:
      show_root_heading: false
      show_source: true

## Usage Examples

### Working with Permissions

The `Permission` enum defines standardized permission strings:

```python
from spryx_core import Permission

# Check if user has specific permissions
def check_user_permissions(user_permissions, required_permissions):
    return all(perm in user_permissions for perm in required_permissions)

# Using with typed permissions
user_permissions = [Permission.READ_USERS, Permission.READ_ORDERS]
can_manage_users = check_user_permissions(user_permissions, [Permission.READ_USERS, Permission.WRITE_USERS])
```

### Validating Token Claims

The claims models provide type-safe validation for JWT tokens:

```python
from spryx_core import TokenClaims
import jwt
from datetime import datetime, timedelta, UTC

# Example JWT payload
payload = {
    "iss": "spryx-auth",
    "sub": "user123",
    "aud": "my-app",
    "iat": datetime.now(UTC),
    "exp": datetime.now(UTC) + timedelta(hours=1),
    "token_type": "user",
    "permissions": ["users:read", "orders:read"]
}

# Encode token (in a real app, this would be done by the auth server)
secret = "your-secret-key"
token = jwt.encode(payload, secret, algorithm="HS256")

# Decode and validate token
def validate_token(token):
    try:
        # Decode token
        decoded = jwt.decode(token, secret, algorithms=["HS256"])
        
        # Validate and cast to appropriate type
        claims = TokenClaims.model_validate(decoded)
        
        # The claims object will be either UserClaims or AppClaims
        # based on the token_type discriminator
        return claims
    except Exception as e:
        print(f"Token validation failed: {e}")
        return None

# Use the validated claims
claims = validate_token(token)
if claims and hasattr(claims, "permissions"):
    # It's a UserClaims object
    user_permissions = claims.permissions
    print(f"User has permissions: {user_permissions}")
```

## Difference Between UserClaims and AppClaims

Spryx supports two types of tokens:

1. **User Tokens** (`UserClaims`): Issued to human users and contain user-specific permissions.
2. **App Tokens** (`AppClaims`): Issued to machine clients/applications and contain scopes rather than permissions.

The `TokenClaims` type uses discriminated unions to automatically cast to the correct type based on the `token_type` field. 