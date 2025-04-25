# Spryx Core

**Core utilities and types for Spryx projects**

[![PyPI version](https://img.shields.io/pypi/v/spryx-core.svg)](https://pypi.org/project/spryx-core/)
[![Python versions](https://img.shields.io/pypi/pyversions/spryx-core.svg)](https://pypi.org/project/spryx-core/)

## Overview

Spryx Core is a Python library that provides common utilities and type definitions used across Spryx projects, including:

- ID generation and validation using ULIDs
- Time manipulation and formatting utilities
- Pagination models for API responses
- Type definitions and sentinel values
- Common error classes
- Permission handling utilities

## Installation

```bash
pip install spryx-core
```

## Quick Usage

```python
from spryx_core import generate_entity_id, now_utc, to_iso, Page

# Generate unique IDs
entity_id = generate_entity_id()
print(entity_id)  # Example: 01HNJG7VWTZA0CGTJ9T7WG9CPB

# Work with UTC timestamps
current_time = now_utc()
iso_timestamp = to_iso(current_time)
print(iso_timestamp)  # Example: 2023-12-01T14:32:15.123456Z

# Create paginated responses
page = Page(
    items=["item1", "item2"],
    page=1,
    page_size=10,
    total=25
)
print(f"Current page: {page.page}, Total pages: {page.total_pages}")
```

## Features

- **Type Safety**: Strong typing support with proper annotations
- **Performance**: Optimized for speed and minimal resource usage
- **Flexibility**: Utilities that adapt to different project requirements
- **Zero External Dependencies**: Core library has no third-party dependencies (except for optional ULID support)

Check out the [Getting Started](getting-started.md) guide for detailed usage examples. 