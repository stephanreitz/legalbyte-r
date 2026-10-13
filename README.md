# LegalByte Resurrection

LegalByte is a legal automation platform designed to reduce repetitive and
operational work in law firms through automation and data processing.

## Project Status

🚧 This project is under active development.

The project is being rebuilt from scratch as a practical software engineering
project, with the goal of evolving a real legal automation product while
applying professional software engineering practices.

## Purpose

LegalByte aims to reduce the effort and human errors involved in repetitive
legal tasks, helping lawyers and interns spend more time on activities that
require legal analysis.

## MVP

The initial MVP will provide:

- User authentication.
- Dashboard with the tools available to each user.
- Request-based workflow.
- Publication filtering automation.
- File upload and processing.
- Result generation and download.
- Task-level processing status and error reporting.

## Domain

The platform is centered around **Requests**.

A user creates a Request to have the platform solve a problem. A Request may
generate one or multiple Tasks, which may be fulfilled through Automations.

The implementation used to fulfill a Request is an internal detail of the
application.

See [`domain.md`](domain.md) for more details.

## Planned Stack

The project will initially use:

- Python
- Django
- Django REST Framework
- PostgreSQL
- JWT authentication
- Docker
- AWS
- GitHub Actions
- pytest

The stack will evolve according to the actual needs of the project.

## Engineering Principles

The project follows a simple principle:

> Build the simplest solution that fully satisfies the current requirements.

The project intentionally avoids premature abstractions, unnecessary
infrastructure, and overengineering.

Testing, architecture, documentation, Docker, AWS, and CI/CD will be
introduced incrementally as the project evolves.

See [`AGENTS.md`](AGENTS.md) for the project's engineering principles and
[`development-conventions.md`](development-conventions.md) for development
conventions.

## Documentation

- [`vision.md`](vision.md) — Product vision.
- [`domain.md`](domain.md) — Domain language and model.
- [`user-flows.md`](user-flows.md) — User flows.
- [`backlog.md`](backlog.md) — Product backlog.
- [`AGENTS.md`](AGENTS.md) — Engineering principles and project instructions.
- [`development-conventions.md`](development-conventions.md) — Development conventions.
- [`ADR-001.md`](ADR-001.md) — Architectural decision records.

## Development

The project is being developed incrementally through Sprints.

Each Sprint introduces or applies software engineering practices while
delivering meaningful product functionality.

The current development plan is managed through the
[LegalByte Resurrection GitHub Project](https://github.com/stephanreitz/legalbyte-r).
