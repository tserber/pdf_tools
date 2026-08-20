# AGENTS.md

## Coding philosophy: lazy senior developer

Adapted from [ponytail](https://github.com/DietrichGebert/ponytail)'s decision ladder.
The best code is the code never written — before implementing anything, ask in order:

1. **Is it necessary?** Apply YAGNI — don't build for hypothetical future needs.
2. **Already exists here?** Reuse existing helpers/patterns before writing new ones.
3. **Built into stdlib?** Prefer the standard library over a new dependency.
4. **Native platform feature?** Use what Docker/Postgres/Terraform/etc. already offer natively.
5. **Dependency already installed?** Use it before adding another one.
6. **Can it be one line?** Maximize brevity where that doesn't hurt clarity.
7. **Only then:** write the minimal working solution.

Deletion over addition. Boring over clever. Fewest files possible.

This applies *after* fully understanding the problem — it's not a shortcut around
comprehension. Never be lazy about: understanding the problem completely, input
validation at trust boundaries, error handling that prevents data loss, security,
or anything explicitly requested.

Non-trivial logic gets one runnable check behind it (a test, or a minimal
assert-based demo) — no need for more than that. If a deliberate shortcut is
taken, leave a `ponytail:` comment noting the limitation and the upgrade path.
