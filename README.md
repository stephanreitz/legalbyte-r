# LegalByte

LegalByte is a legal automation platform designed to reduce repetitive and
operational work in law firms through automation and data processing.

## Project Status

🚧 This project is under active development.

The project is being developed as a practical software engineering project,
with the goal of evolving a real legal automation product while applying
professional software engineering practices.

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

See [`domain.md`](docs/domain.md) for more details.

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
[`development-conventions.md`](docs/development-conventions.md) for development
conventions.

## Code Ownership

This repository contains an original implementation developed for educational
and portfolio purposes. It does not include proprietary source code,
confidential information, or client data.

## Documentation

Public project documentation is stored in [`docs/`](docs/):

- [`vision.md`](docs/vision.md) — Describes the product purpose, target
  audience, problem, value proposition, MVP, and long-term vision.
- [`domain.md`](docs/domain.md) — Defines the shared domain language, core
  concepts, and main business workflow.
- [`user-flows.md`](docs/user-flows.md) — Describes how users interact with the
  platform, from authentication to Request completion.
- [`backlog.md`](docs/backlog.md) — Lists delivered and planned product
  capabilities by version.
- [`development-conventions.md`](docs/development-conventions.md) — Records the
  coding, documentation, and testing conventions used by the project.
- [`ADR-001.md`](docs/ADR-001.md) — Records the architectural decision to center
  the domain on Requests.

The repository also includes [`AGENTS.md`](AGENTS.md), which defines the
engineering principles and instructions followed during development.

## Development

The project is being developed incrementally through Sprints.

Each Sprint introduces or applies software engineering practices while
delivering meaningful product functionality.

The current development plan is managed through the
[LegalByte GitHub Project](https://github.com/stephanreitz/legalbyte-r).
