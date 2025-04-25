# Release Notes

This page documents the release history of Spryx Core.

## Upcoming

_Features that are planned for future releases._

- Improved error handling and custom exceptions
- Support for more date/time formats and operations
- Enhanced pagination features

## 0.1.0 (Initial Release)

_Release date: YYYY-MM-DD_

### Added

- Initial implementation of core utilities:
  - EntityId generation using ULID/UUID
  - Time utilities for UTC handling and ISO-8601 formatting
  - Pagination model for API responses
  - Type definitions and sentinel values
  - Basic error classes
  - Permission handling utilities
- Documentation using MkDocs
- Test suite with pytest

### Dependencies

- Python 3.8+
- Optional: ulid-py (for ULID support)
- Optional: pydantic (for pagination model) 