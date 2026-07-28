## OnlyWorlds

An open-source data standard for worldbuilding.

OnlyWorlds provides a universal language and supporting infrastructure for describing fictional or historical worlds across tools, games, and applications. 

### What This Repository Contains

- `/schema` — Core YAML definitions for the 22 element categories and their fields. **This is the standard.** Everything else in the ecosystem is generated from it or validated against it.
- `/types` — Element type listings
- `onlyworlds_complete_schema.yaml` — the whole schema rolled into one file, for tools that prefer a single document

Typed clients are **not** kept here, they live with the tools that maintain them, generated from the schema above:

| Language                | Where                                                                                                          |
|-------------------------|----------------------------------------------------------------------------------------------------------------|
| TypeScript / JavaScript | [`@onlyworlds/sdk`](https://www.npmjs.com/package/@onlyworlds/sdk) — v4, ESM-only, v2-native                   |
| AI assistants (MCP)     | Hosted server at `https://www.onlyworlds.com/mcp` (streamable HTTP), registry id `com.onlyworlds/mcp`          |
| Anything else           | Read the YAML — it is small — and see the [API reference](https://onlyworlds.com/api/docs) for the wire shapes |

### Quick Links

- **[Main Platform](https://onlyworlds.com)** — accounts, worlds, keys
- **[Tools](https://onlyworlds.com/tools)** — what exists and what it does
- **[Documentation](https://onlyworlds.github.io)** — full guides and specifications
- **[API Reference](https://onlyworlds.com/api/docs)** — REST API documentation
- **[Feedback](https://onlyworlds.com/feedback)** — requests, bugs, anything at all
- **[Discord](https://discord.gg/twCjqvVBwb)** — community discussion
- **[Discussions](https://github.com/OnlyWorlds/OnlyWorlds/discussions)** — feature requests and design talk

### For World Builders

**[Atlas](https://atlas.onlyworlds.com)** is the main way in: a free, local-first app where the folder on your disk *is* the world: plain JSON files you can read, back up, and keep, with no account required to start. There is also an [Obsidian plugin](https://onlyworlds.com/tools) if your notes already live there, and a [browser editor](https://onlyworlds.com) on the platform itself.

See [all tools](https://onlyworlds.com/tools) for the rest, including converters that bring worlds in from other applications.

Feedback is welcome from anyone using or interested in the standard: schema requests, missing features, tool ideas. Send it via [onlyworlds.com/feedback](https://onlyworlds.com/feedback), [Discord](https://discord.gg/twCjqvVBwb), or [Discussions](https://github.com/OnlyWorlds/OnlyWorlds/discussions).

### For Developers

#### Building OnlyWorlds-Compatible Tools

The schema in this repository is everything you need to model a world. The [API](https://onlyworlds.com/api/docs) serves it, and worlds are equally readable as plain files on disk, so a tool can work against either without an account.

You can feed the [documentation](https://onlyworlds.github.io), the [API reference](https://onlyworlds.com/api/docs), or the [SDK](https://www.npmjs.com/package/@onlyworlds/sdk) into any code-assist AI to get started. Several tools in the ecosystem were built that way.

- **JavaScript / TypeScript**: `npm install @onlyworlds/sdk`
- **AI assistants**: connect to the hosted MCP server at `https://www.onlyworlds.com/mcp`, use the [claude code toolkit](https://github.com/OnlyWorlds/toolkit) for local harnesses, or use the SDK for typed API access and project context.
- **Python**: a client package is published under `onlyworlds`

See the [developer guides](https://onlyworlds.github.io/docs/development/) and [onlyworlds.com/develop](https://onlyworlds.com/develop) for integration walkthroughs.

**Bug reports**: [GitHub Issues](https://github.com/OnlyWorlds/OnlyWorlds/issues), a [discussion post](https://github.com/OnlyWorlds/OnlyWorlds/discussions/categories/software), or [onlyworlds.com/feedback](https://onlyworlds.com/feedback).

### API Access

The [REST API](https://onlyworlds.com/api/docs) provides programmatic access to create, modify, and sync world data. It follows the OpenAPI 3 specification and uses `API-Key` and `API-Pin` header authentication.

The current API is **v2**, at `https://www.onlyworlds.com/api/v2/`. Link fields use bare schema names (`location`, `characters`). The `_id`/`_ids` suffixes belong to the legacy v1 dialect, still served as a compatibility adapter at `/api/worldapi/`. List responses are paginated in a `{data, has_more, next_cursor}` envelope, and `GET /api/v2/changes/` is a per-world change feed for incremental sync.

### License

Open source with no commercial restrictions. Free to use, adapt, and distribute.
