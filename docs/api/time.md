# Time Module

The `time` module provides utilities for working with dates and times in UTC, including ISO-8601 formatting, parsing, and common time operations.

## Key Features

- **UTC Focus**: All functions work exclusively with UTC timezone
- **ISO-8601 Formatting**: Standardized timestamp formatting
- **Common Operations**: Useful time manipulation functions
- **Type Safety**: Proper typing for all functions

## API Reference

::: spryx_core.time
    options:
      show_root_heading: false
      show_source: true

## Usage Examples

### Current UTC Time

```python
from spryx_core import now_utc

# Get current UTC time
current_time = now_utc()
print(current_time)  # Example: 2023-12-01 14:32:15.123456+00:00
```

### ISO-8601 Formatting

```python
from spryx_core import now_utc, to_iso

# Format current time as ISO-8601
current_time = now_utc()
iso_format = to_iso(current_time)
print(iso_format)  # Example: 2023-12-01T14:32:15.123456Z

# Format with millisecond precision
iso_ms = to_iso(current_time, milliseconds=True)
print(iso_ms)  # Example: 2023-12-01T14:32:15.123Z
```

### Parsing ISO-8601 Timestamps

```python
from spryx_core import parse_iso

# Parse ISO-8601 string to datetime
dt = parse_iso("2023-12-01T14:32:15Z")
print(dt)  # 2023-12-01 14:32:15+00:00
```

### Day Boundaries

```python
from spryx_core import start_of_day, end_of_day, now_utc

today = now_utc()

# Get midnight (00:00:00.000000)
day_start = start_of_day(today)
print(day_start)  # Example: 2023-12-01 00:00:00+00:00

# Get last moment of day (23:59:59.999999)
day_end = end_of_day(today)
print(day_end)  # Example: 2023-12-01 23:59:59.999999+00:00

# Date range for "today"
print(f"Today spans from {day_start} to {day_end}")
```

### Converting Timestamps

```python
from spryx_core.time import utc_from_timestamp

# Convert UNIX timestamp to UTC datetime
unix_timestamp = 1701443535  # Seconds since epoch
dt = utc_from_timestamp(unix_timestamp)
print(dt)  # Example: 2023-12-01 14:32:15+00:00
```

## Best Practices

1. **Always Use UTC**: For any timestamp storage or processing, use UTC timezone.
2. **Store in ISO Format**: When storing timestamps as strings, use ISO-8601 format.
3. **Consistent Format**: Use the `to_iso()` function to ensure consistent formatting. 