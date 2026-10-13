# Development Conventions

## Language

- Code must always be written in English.
- Technical documentation must always be written in English.
- The frontend will initially use Portuguese.
- The frontend may be changed to English in the future.

## Documentation

Documentation should follow the principles defined in `AGENTS.md`.

Documentation is not required for every piece of code. Add documentation when it provides meaningful context, explains non-obvious behavior, or records an important decision.

Python docstrings should use the **Google Style** format.

## Testing

The project will use **pytest** for automated testing.

Tests will be kept separate from production code in a dedicated `tests/` directory.

The initial test structure will be organized by **feature**, keeping the complexity proportional to the current needs of the project.

Example:

```text
project/
├── app/
│   ├── users/
│   └── requests/
│
└── tests/
    ├── users/
    │   └── test_authentication.py
    └── requests/
        └── test_creation.py└── ...
```
