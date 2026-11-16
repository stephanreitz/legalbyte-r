# User Flows

This document describes LegalByte's main user flows.

It serves as a reference for interface, API, and business rule development.

---

## Flow 1 — Login

### Goal

Allow an authenticated user to access the automations available on the
platform.

### Flow

1. The user enters an email address and password.
2. The user selects **Log in**.
3. Valid credentials lead to the Dashboard.
4. Invalid credentials produce an error message.
5. Both fields are required.

---

## Flow 2 — Dashboard

### Goal

Present all automations available to the user. Availability may vary by user.

### Flow

1. After login, the user is directed to the LegalByte Dashboard.
2. The Dashboard displays a greeting and the tools available to that user.
3. Each automation is represented by a name, short description, and icon.
4. The user selects an automation.
5. The platform opens the page for that automation.

---

## Flow 3 — Submit a Request

### Goal

Submit a Request through a LegalByte tool.

### Flow

1. The user selects a tool from the Dashboard.
2. The platform opens a page containing:
   - The tool name and purpose.
   - A description of the expected result.
   - Instructions for using the tool.
   - Required inputs and tool-specific options.
   - A field for uploading one or more files.
   - A button for submitting the Request.
3. The user follows the instructions, selects the options, and uploads the
   required files.
4. Before processing, the platform validates:
   - Required fields and options.
   - Required files and file count limits.
   - Supported file formats and tool-specific file requirements.
   - Parameter validity and compatibility.
   - The user's permission to use the tool.
5. Valid data starts the Request. Invalid data produces clear validation
   errors and prevents processing.
6. The platform creates and processes the Request.
7. The Request may trigger one or more Automations of the same type.
8. When processing finishes, the platform presents the result.
9. The user downloads the generated file, usually a spreadsheet.

---

## Flow 4 — Track and Complete a Request

### Goal

Allow the user to track Request processing, inspect each Task result, and
obtain the final Request result.

### Flow

1. After input validation, the platform directs the user to the Request
   tracking page.
2. The page lists all related Tasks and their current statuses.
3. Task statuses are updated as processing progresses.
4. Each successful Task records and displays its result.
5. Each failed Task displays the reason for its failure.
6. After all Tasks finish, the platform consolidates the Request result.
7. The platform generates a report listing successful Tasks, failed Tasks, and
   failure reasons.
8. The user downloads the generated report, usually a spreadsheet.

### Note

Result content may vary by tool. Regardless of the tool, every Request must
identify what was processed, what succeeded, what failed, and why it failed.

---

## Flow 5 — Logout

1. The user selects **Log out**.
2. The platform ends the session.
3. The user returns to the login page.

---

## Standard automation flow

Every automation follows the same interaction pattern:

```text
Input
  ↓
Configuration
  ↓
Execution
  ↓
Result
```

This flow must remain consistent to provide a uniform user experience.

---

## MVP

The MVP provides one automation:

- Irrelevant Publication Filtering

Other automations will be added incrementally and will reuse the same
navigation flow.
