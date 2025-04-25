# Errors Module

The `errors` module provides standardized error classes for use throughout Spryx projects. It establishes a consistent pattern for error reporting, serialization, and handling.

## Key Features

- **Standardized Error Structure**: Consistent error format across the codebase
- **Type Safety**: Generic typing for error codes
- **Serialization**: Easy conversion to dictionary format for API responses

## API Reference

::: spryx_core.errors
    options:
      show_root_heading: false
      show_source: true

## Usage Examples

### Basic Error Handling

The main error class is `SpryxError`, which can be used with enum-based error codes:

```python
from enum import StrEnum
from spryx_core.errors import SpryxError

# Define domain-specific error codes
class UserError(StrEnum):
    NOT_FOUND = "user_not_found"
    ALREADY_EXISTS = "user_already_exists"
    INVALID_DATA = "user_invalid_data"

# Raise a properly structured error
def get_user(user_id: str):
    # If user not found in database
    if not user_exists(user_id):
        raise SpryxError(
            code=UserError.NOT_FOUND,
            message=f"User with ID {user_id} not found",
            details={"user_id": user_id}
        )
    
    # Continue with function logic...
    return {"id": user_id, "name": "Test User"}

# Example helper function
def user_exists(user_id: str) -> bool:
    return False  # Mock implementation
```

### Error Serialization

The `SpryxError` class provides built-in serialization to dictionaries, which is useful for API responses:

```python
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from spryx_core.errors import SpryxError

app = FastAPI()

@app.exception_handler(SpryxError)
async def spryx_error_handler(request: Request, exc: SpryxError):
    # Convert the error to a dictionary format
    error_dict = exc.to_dict()
    
    # Return a JSON response with the error details
    return JSONResponse(
        status_code=400,
        content=error_dict
    )

# The response will look like:
# {
#     "error": "user_not_found",
#     "message": "User with ID 123 not found",
#     "details": {"user_id": "123"}
# }
```

### Specialized Error Classes

You can create domain-specific error classes by inheriting from `SpryxError`:

```python
from spryx_core.errors import SpryxError
from enum import StrEnum

class PaymentErrorCode(StrEnum):
    INSUFFICIENT_FUNDS = "insufficient_funds"
    PAYMENT_FAILED = "payment_failed"
    INVALID_CARD = "invalid_card"

class PaymentError(SpryxError[PaymentErrorCode]):
    """Specialized error class for payment-related errors."""
    pass

# Usage
def process_payment(amount: float, card_token: str):
    if amount <= 0:
        raise PaymentError(
            code=PaymentErrorCode.INVALID_CARD,
            message="Payment amount must be positive",
            details={"amount": amount}
        )
    # Process payment...
```

## Best Practices

1. **Use Enum Codes**: Always use enum values for error codes to maintain consistency and type safety.

2. **Detailed Messages**: Include helpful, specific error messages that explain what went wrong.

3. **Structured Details**: Add context in the `details` dictionary to help diagnose issues.

4. **Domain-Specific Errors**: Create specialized error classes for different domains in your application. 