# Contributing to OnlyWorlds

Start with the [README](./README.md) and the [docs](https://onlyworlds.github.io).

## Ideas, questions and requests

- [Discussions](https://github.com/OnlyWorlds/OnlyWorlds/discussions) for ideas, schema questions and requests for new fields or types.
- The [Council](https://council.onlyworlds.com), where changes to the schema are proposed as motions and voted on.
- [Discord](https://discord.gg/twCjqvVBwb) to talk it through.
- [Issues](https://github.com/OnlyWorlds/OnlyWorlds/issues) for something wrong in the files.

Feedback from non-developers counts as much as code: which fields your world needs, which names are unclear, what doesn't fit.

## Changing the files

1. Fork the repository and create a branch.
2. Make your change in `schema/` or `types/`.
3. Open a pull request that says what the change is for.

A change tools must react to (a new field, a renamed one, a new type) goes through the Council as a motion first. Corrections to descriptions and typos can come straight as a pull request. Backwards-compatible changes are preferred.

## Layout

```
schema/   one YAML file per element type, plus base_properties.yaml and world.yaml
types/    suggested supertypes and subtypes per type
VERSION   the schema version
```

## Code of conduct

See [CODE_OF_CONDUCT.md](./CODE_OF_CONDUCT.md).
