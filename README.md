## OnlyWorlds

An open-source data standard for worldbuilding.

OnlyWorlds provides a universal language and supporting infrastructure for describing fictional or historical worlds across tools, games, and applications.

### What This Repository Contains

- `/schema` - Core YAML definitions for 22 element categories and their fields. **This is the standard.** Everything else in the ecosystem is generated from it or validated against it.
- `/types` - Element type listings
- `onlyworlds_complete_schema.yaml` - the whole schema rolled into one file, for tools that prefer a single document

Typed clients are **not** kept here — they live with the tools that maintain them, generated from the schema above:

| Language | Where |
|---|---|
| TypeScript / JavaScript | [`@onlyworlds/sdk`](https://www.npmjs.com/package/@onlyworlds/sdk) |
| MCP (any AI assistant) | [`@onlyworlds/mcp-client`](https://www.npmjs.com/package/@onlyworlds/mcp-client), registry id `com.onlyworlds/mcp` |
| Anything else | Read the YAML - it is small, and the [API reference](https://onlyworlds.com/api/docs) documents the wire shapes |

### Quick Links

- **[Main Platform](https://onlyworlds.com)** - Create and manage accounts and worlds
- **[Documentation](https://onlyworlds.github.io)** - Full guides and specifications 
- **[API Reference](https://onlyworlds.com/api/docs)** - REST API documentation
- **[Discord](https://discord.gg/twCjqvVBwb)** - Community discussion
- **[Discussions](https://github.com/OnlyWorlds/OnlyWorlds/discussions)** - Feature requests and feedback
- **[Visual Explorer](https://ecosystem-explorer.onlyworlds.com)** - 3D representation of infrastructure and concepts

 ### For World Builders

Create a few account and your first world on [onlyworlds.com](https://onlyworlds.com), then see [what tools are available](https://onlyworlds.github.io/docs/tools/) to build and explore worlds.
 
Feedback is welcome from anyone using or interested in the standard:
- Schema requests or suggestions
- Missing features 
- Tool ideas

Submit via [Discord](https://discord.gg/twCjqvVBwb), [Discussions](https://github.com/OnlyWorlds/OnlyWorlds/discussions), or the [Text Tool](https://onlyworlds.com/text_tool/). 

### For Developers

#### Building OnlyWorlds-Compatible Tools

You can feed the [documentation](https://onlyworlds.github.io), [API reference](https://onlyworlds.com/api/docs), or [sdk](https://www.npmjs.com/package/@onlyworlds/sdk) into any code-assist AI to get started. [OnlyWorldsBot](https://chatgpt.com/g/g-dydgDFnOz-onlyworldbot) is tailored for OnlyWorlds development and support.

Integration libraries:
- **JavaScript/TypeScript**: `npm install @onlyworlds/sdk`
- **MCP Integration**: `npm install @onlyworlds/mcp-client`
- **Python**: Available on TestPyPI (PyPI release coming soon)

See [developer documentation](https://onlyworlds.github.io/docs/development/) for integration guides.

**Bug reports**: Use [GitHub Issues](https://github.com/OnlyWorlds/OnlyWorlds/issues) or create a [discussion post](https://github.com/OnlyWorlds/OnlyWorlds/discussions/categories/software)

### API Access

The [REST API](https://onlyworlds.com/api/docs) provides programmatic access to create, modify, and sync world data. It follows the OpenAPI 3 specification and uses `API-Key` and `API-Pin` header authentication.

The current API is **v2**, at `https://www.onlyworlds.com/api/v2/`. Link fields use bare schema names (`location`, `characters`) — the `_id`/`_ids` suffixes belong to the legacy v1 dialect, which is still served as a compatibility adapter at `/api/worldapi/`. List responses are paginated in a `{data, has_more, next_cursor}` envelope, and `GET /api/v2/changes/` is a per-world change feed for incremental sync.
 
### License

Open source with no commercial restrictions. Free to use, adapt, and distribute.


