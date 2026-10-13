# AGENTS.md

## Project Overview

LegalByte is a legal automation platform for law firms.

Its purpose is to reduce the time spent on repetitive and operational legal tasks, allowing lawyers and interns to focus on activities that require legal analysis.

The platform is centered around **Requests**. A user creates a Request to have the platform solve a problem. The implementation used to fulfill the Request is an internal detail of the application.

## Domain

The main domain concepts are:

- `Office` — law firm that uses the platform.
- `User` — person authorized to use the platform.
- `Request` — user's request for the platform to perform an operation. It is the Aggregate Root.
- `Task` — unit of work required to fulfill a Request.
- `Automation` — mechanism used to execute a Task.
- `Input` — data provided by the user.
- `Output` — result produced by the platform.

A Request may generate one or many Tasks.

The domain is documented in `docs/domain.md`.

## Product Principles

Every new feature should automate or simplify a recurring activity in the legal workflow.

The platform should:

- Reduce operational work.
- Reduce human errors.
- Increase productivity.
- Standardize processes.
- Allow legal professionals to dedicate more time to intellectual activities.

## Engineering Principles

### Prefer the simplest solution

Always choose the simplest solution that fully satisfies the current requirements.

Do not introduce abstractions, design patterns, or new layers unless they solve an existing problem.

Avoid designing for hypothetical future requirements ("just in case").

Prefer modifying existing code over creating new infrastructure when reasonable.

Keep changes as small and localized as possible.

Follow the existing architecture unless explicitly instructed otherwise.

### Avoid overengineering

Before introducing any of the following, verify that there is a concrete need:

- New hooks, utilities, or helper functions.
- New reusable components.
- New abstractions or service layers.
- Additional configuration files.
- Generic solutions for a single use case.
- New dependencies.

If the solution adds significant complexity without solving an actual current problem, do not implement it.

### Decision rule

When multiple valid implementations exist, prefer the one that is:

- Simpler.
- Easier to understand.
- Easier to maintain.
- More consistent with the existing codebase.

Do not optimize for hypothetical future extensibility.

## Architecture

The architecture should evolve according to the actual needs of the project.

Do not introduce architectural layers, abstractions, or patterns before there is a concrete problem that justifies them.

Architectural decisions that have significant impact on the project should be documented using Architecture Decision Records (ADRs).

Current architectural decisions are documented in the project's ADR files.

## Testing

Testing is a project-wide engineering practice.

New functionality should be developed with automated tests whenever appropriate.

Tests should provide meaningful protection against regressions without introducing unnecessary complexity.

## Documentation

Documentation should describe decisions, behavior, and conventions that are relevant to the project.

Do not create documentation solely for the sake of documentation.

Keep documentation concise and update it when the documented behavior or decision changes.

Important project documentation includes:

- `docs/vision.md` — product vision.
- `docs/domain.md` — domain language and model.
- `docs/user-flows.md` — user flows.
- `docs/backlog.md` — product backlog.
- `docs/ADR-*.md` — architectural decisions.

## Development Approach

The project is developed incrementally.

Each Sprint should deliver meaningful progress toward the product while introducing or applying engineering practices that are relevant to the current stage of development.

Avoid implementing functionality or infrastructure before it is needed.

When requirements change, prefer updating the existing implementation and documentation rather than introducing parallel solutions.
