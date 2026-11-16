# Development Conventions

## Language

- Code must always be written in English.
- Technical documentation must always be written in English.
- The frontend will initially use Portuguese.
- The frontend may be changed to English in the future.

## Documentation

Documentation should follow the principles defined in `../AGENTS.md`.

Documentation is not required for every piece of code. Add documentation when it provides meaningful context, explains non-obvious behavior, or records an important decision.

Python docstrings should use the **Google Style** format.

## Testing

The project will use **pytest** for automated testing.

Tests will be kept separate from production code in a dedicated `tests/` directory.

The initial test structure will be organized by **feature**, keeping the complexity proportional to the current needs of the project.

### TDD commit cycle

Each behavior must be developed and recorded in two commits:

1. **Red commit**
   - Write only the next test.
   - Run the focused test.
   - Confirm that it fails for the expected reason.
   - Commit the failing test with a `test:` message.

2. **Green commit**
   - Write the smallest implementation that satisfies the test.
   - Run the focused test and then the full test suite.
   - Commit the implementation with a `feat:` or `fix:` message.

Do not mix unrelated changes into either commit. Red commits are preserved in this educational repository to make the TDD progression visible. In a shared production repository, they may be squashed before merging so the main branch remains green.

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
