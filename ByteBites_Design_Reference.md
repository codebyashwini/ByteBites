# ByteBites Reference File

## About This Project
You are building the backend logic for a campus food ordering app called ByteBites
using Python classes and simple algorithms.

## Project Scope
Do not add authentication logic, a database layer, or any features not described 
in the spec.

## Behavioral Instructions

### Code Style & Structure
- Follow the class structure defined in the UML diagram exactly; do not introduce additional classes without justification.
- Use clear, descriptive names for attributes and methods (e.g., `total_price` not `tp`).
- Keep methods focused on a single responsibility; if a method grows beyond ~15 lines, consider breaking it into helpers.
- Add docstrings only when the method's purpose is non-obvious; prefer self-documenting code with clear names.

### Scope & Features
- Implement only what is specified in the requirements. Do not add "nice-to-have" features or prepare for hypothetical future extensions.
- Avoid adding authentication, database persistence, or file I/O unless explicitly required.
- Do not over-engineer data structures; use built-in Python types (list, dict, tuple) unless there's a clear reason for a custom class.

### Algorithm & Complexity
- Prefer simple, readable algorithms over clever optimizations. This is a learning project, not a performance-critical system.
- Use clear variable names and intermediate steps that show intent, rather than compact or condensed logic.
- For list operations, use built-in methods and comprehensions; avoid hand-rolled loops when not necessary.

### Error Handling & Validation
- Validate input only at system boundaries (user input, API parameters). Trust internal code to pass valid data.
- Raise clear `ValueError` or `TypeError` exceptions with descriptive messages when validation fails.
- Do not add try/except blocks speculatively; add them only if the calling code cannot prevent an error.

### Testing & Verification
- Write methods that are easy to test; avoid tight coupling or side effects that make unit testing difficult.
- Assume tests will be written separately; design public methods to be assertion-friendly.
- Return values that are easy to verify, not complex nested structures that require unpacking.

### Documentation & Comments
- Code comments are for *why*, not *what*—the code itself should show what it does. Comment only non-obvious intent or constraints.
- Keep behavioral notes (e.g., "prices are in cents to avoid float precision issues") in relevant docstrings.
- Do not add planning or architectural comments; those belong in a design doc or PR description.

### When in Doubt
- Consult the spec and UML diagram as the source of truth.
- Choose explicit and simple over implicit and clever.
- Bias toward readable code that a teammate can understand in seconds, not minimal code that requires study.
