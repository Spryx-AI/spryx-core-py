# Sentinels Module

The `sentinels` module implements the sentinel pattern for representing special values in Python. Sentinels are unique objects used to signify special conditions, particularly useful for distinguishing between "not provided" and "explicitly set to None" in function parameters.

## Key Features

- **Unique Sentinels**: Guaranteed unique singleton objects
- **Type Safety**: Properly typed for static analysis
- **String Representation**: Clear debugging information

## API Reference

::: spryx_core.sentinels
    options:
      show_root_heading: false
      show_source: true

## Usage Examples

### Basic Usage

```python
from spryx_core import NOT_GIVEN

# Function with optional parameters using the sentinel pattern
def update_user(user_id, name=NOT_GIVEN, email=NOT_GIVEN, active=NOT_GIVEN):
    updates = {}
    
    if name is not NOT_GIVEN:
        updates["name"] = name
        
    if email is not NOT_GIVEN:
        updates["email"] = email
        
    if active is not NOT_GIVEN:
        updates["active"] = active
    
    # Apply updates to user with user_id
    print(f"Updating user {user_id} with {updates}")
    return updates

# Different usage scenarios
update_user("user123", name="John")                           # Updates only name
update_user("user123", email="john@example.com")              # Updates only email
update_user("user123", active=False)                          # Updates only active status
update_user("user123", name="John", email="john@example.com") # Updates name and email
update_user("user123")                                        # No updates

# Now we can explicitly set None, which is different from not providing a value
update_user("user123", name=None)  # Explicitly setting name to None
```

### The NotGiven Class

The `NotGiven` class is the sentinel's type, with `NOT_GIVEN` being the singleton instance:

```python
from spryx_core import NOT_GIVEN, NotGiven

# Check type
print(isinstance(NOT_GIVEN, NotGiven))  # True

# String representation
print(str(NOT_GIVEN))  # "<not given>"
print(repr(NOT_GIVEN))  # "NOT_GIVEN"
```

### Comparing Sentinels

Sentinel values have identity-based equality, meaning they only equal themselves:

```python
from spryx_core import NOT_GIVEN

# Identity comparison
print(NOT_GIVEN is NOT_GIVEN)  # True

# Equality comparison
print(NOT_GIVEN == NOT_GIVEN)  # True
print(NOT_GIVEN == None)       # False
print(NOT_GIVEN == "")         # False
print(NOT_GIVEN == 0)          # False
```

## Best Practices

1. **Use with Optional Parameters**: Use sentinels for optional parameters when you need to distinguish between "not provided" and "explicitly set to None".

2. **Type Annotations**: For proper type checking, use `NotGivenOr[T]` from the `types` module as the type annotation:

   ```python
   from spryx_core import NOT_GIVEN, NotGivenOr
   
   def update_profile(name: NotGivenOr[str] = NOT_GIVEN):
       pass
   ```

3. **Consistent Pattern**: Use the same pattern throughout your codebase for handling optional parameters to maintain consistency. 