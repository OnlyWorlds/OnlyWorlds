# Security

Report a vulnerability through GitHub's
[private vulnerability reporting](https://github.com/OnlyWorlds/OnlyWorlds/security/advisories/new), not a public issue.
Only the maintainers see it. Skeld, the AI maintainer (see the README), reads it, and the OnlyWorlds founder answers for
the fix.

This repository holds the standard: YAML files that describe types and fields. What counts here is a definition that
would lead every conforming tool to mishandle data (a field whose declared shape lets a crafted value through, a link
rule that leaks across worlds), and anything in the repository's workflows. This address is also the contact named by
`www.onlyworlds.com/.well-known/security.txt`: a problem in onlyworlds.com itself, or in a tool that speaks the standard,
is taken here and passed on to its maintainer.

Supported: the newest version of the standard.
