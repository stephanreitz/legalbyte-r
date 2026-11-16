# Domain

This document defines LegalByte's domain language and model.

Code, documentation, and business rules must use the same terms. This document
must be updated whenever a feature introduces a new business concept.

---

## Overview

LegalByte is a legal automation platform for law firms.

Its goal is to reduce time spent on repetitive operational tasks so that
lawyers and interns can focus on work that requires legal analysis.

The model is centered on Requests. Users do not interact directly with
automations. They ask the platform to solve a problem, while the implementation
used to fulfill that request remains an internal application detail.

---

## Principles

Every new feature must:

- Automate or simplify a recurring activity in a legal workflow.
- Reduce operational time and human error.
- Produce a clear and useful result for the user.
- Remain independent from other automations whenever possible.

---

## Conceptual model

```text
Office
  ↓
Users
  ↓
Requests
  ↓
Tasks
  ↓
Automations
  ↓
Output
```

---

## Glossary

### Office

A platform customer. It groups its users and their requests.

Example: Law Firm A.

### User

A person authorized to use the platform. A User belongs to one Office and
creates Requests.

Initial roles:

- Lawyer
- Intern

Other roles, such as Administrator and Manager, may be introduced later.

### Request

A user's intent. Every relevant interaction starts with a Request.

Examples include filtering a spreadsheet, filing a batch of cases, searching
documents, and generating a report.

A Request is the domain Aggregate Root. It stores parameters and inputs, tracks
processing, consolidates results, and presents the overall status to the user.

Request statuses:

- Pending
- Processing
- Completed
- Partially completed
- Failed

### Task

A unit of work required to fulfill a Request. A Request may generate one,
dozens, or hundreds of Tasks.

Each Task has its own lifecycle and status. Logs belong to Tasks and describe
what was executed, what failed, and why.

### Automation

A mechanism capable of executing a Task. It is not the center of the domain,
but one of the mechanisms used to fulfill a Request.

Examples include Irrelevant Publication Filtering, Automated Court Filings,
Spreadsheet Analysis, and Intelligent Document Search.

New mechanisms may be introduced without changing the system's central concept.

### Input

Data provided by the user, such as files (XLSX, CSV, PDF, or DOCX) and
parameters entered through the interface.

### Output

The result produced by the platform, such as a spreadsheet, PDF, report,
message, or compressed file.

### Publication

A concept specific to the Irrelevant Publication Filtering automation. Each
Publication is a record from the spreadsheet submitted by the user, classified
as relevant or irrelevant according to the automation rules.

---

## Main workflow

```text
Office
  ↓
User
  ↓
Creates a Request
  ↓
Provides Input
  ↓
The Request generates one or more Tasks
  ↓
Automations execute the Tasks
  ↓
The Request consolidates the Output
  ↓
The user downloads the result
```

---

## Out of scope

LegalByte does not replace a law firm's management system (CRM/ERP).

It is a complementary automation platform that may integrate with existing
systems in the future.
