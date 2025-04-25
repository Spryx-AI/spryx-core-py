# Contributing

Thank you for your interest in contributing to Spryx Core! This document provides guidelines and instructions for contributing to the project.

## Development Setup

### Prerequisites

- Python 3.8+
- Poetry (recommended for dependency management)
- Git

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/ppcantidio/spryx-core-py.git
   cd spryx-core-py
   ```

2. Install dependencies with Poetry:
   ```bash
   poetry install
   ```

   Or with pip:
   ```bash
   pip install -e ".[dev]"
   ```

3. Install pre-commit hooks:
   ```bash
   pre-commit install
   ```

## Development Workflow

### Running Tests

```bash
# Run all tests
pytest

# Run tests with coverage
pytest --cov=spryx_core

# Run a specific test file
pytest tests/test_id.py
```

### Code Style

We use Black, isort, flake8, and mypy for code formatting and linting:

```bash
# Run Black formatter
black spryx_core tests

# Run isort
isort spryx_core tests

# Run flake8
flake8 spryx_core tests

# Run mypy
mypy spryx_core
```

Pre-commit hooks will automatically check these when you commit changes.

## Pull Request Process

1. Create a new branch for your feature or bugfix:
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. Make your changes and write tests for your code.

3. Run the test suite to make sure everything passes:
   ```bash
   pytest
   ```

4. Commit your changes using semantic commit messages:
   ```
   feat(module): add new feature
   fix(module): fix bug
   docs(module): update documentation
   ```

5. Push your branch to GitHub:
   ```bash
   git push origin feature/your-feature-name
   ```

6. Create a pull request against the `main` branch.

## Documentation

When contributing, please update the documentation accordingly:

1. Update docstrings in the code using Google style docstrings
2. Update or add Markdown files in the `docs/` directory for any new features
3. Build and preview documentation locally:
   ```bash
   mkdocs serve
   ```

## Release Process

Spryx Core follows semantic versioning (SemVer):

- MAJOR version for incompatible API changes
- MINOR version for new functionality in a backward compatible manner
- PATCH version for backward compatible bug fixes

## Code of Conduct

Please be respectful and inclusive in your interactions with the project and its community. We strive to make this a welcoming environment for everyone. 