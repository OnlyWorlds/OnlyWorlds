# OnlyWorlds

An open standard for worldbuilding data: 22 element types, their fields, and the links between them, defined in YAML.

A world in this shape can be read and written by any tool that speaks it: a desktop app, an Obsidian vault, a game engine, an AI assistant. Every element needs only a name; every other field is optional.

## What is here

- `schema/`: one YAML file per element type, plus `base_properties.yaml` (the fields every element has) and `world.yaml` (the world itself). This is the standard.
- `types/`: suggested supertypes and subtypes for each element type.
- `VERSION`: the schema version.

The 22 types: Character, Creature, Species, Family, Collective, Institution, Location, Object, Construct, Ability, Trait, Title, Language, Law, Event, Narrative, Phenomenon, Relation, Map, Pin, Marker, Zone.

In world data, keys are lowercase (`id`, `name`, `image_url`), a single link holds one element's UUID, and a multi-link holds a list of UUIDs.

## Making a world

[Atlas](https://atlas.onlyworlds.com) is the main workspace. A world is a folder of plain files on your own machine, and no account is needed to start. An account on [onlyworlds.com](https://www.onlyworlds.com) hosts worlds online, with sharing and API access. Other tools, including an Obsidian plugin and converters from other apps, are listed at [onlyworlds.com/tools](https://www.onlyworlds.com/tools).

## Building a tool

Get the schema from [schema-dist](https://github.com/OnlyWorlds/schema-dist): it packages this repo for tools, with a reference decoder, so you don't have to parse the YAML yourself.

| | |
|---|---|
| TypeScript | `npm install @onlyworlds/sdk` ([sdk](https://github.com/OnlyWorlds/sdk)) |
| Python | [python-sdk](https://github.com/OnlyWorlds/python-sdk) (pre-release) |
| Unity / C# | [unity-sdk](https://github.com/OnlyWorlds/unity-sdk) |
| AI assistants | the MCP server at `https://www.onlyworlds.com/mcp` |
| Claude Code | the [toolkit](https://github.com/OnlyWorlds/toolkit) plugin |

Using Godot, Unreal or another engine without an SDK: see [Games](https://onlyworlds.github.io/docs/development/games) in the docs.

The REST API is at `https://www.onlyworlds.com/api/v2/`, with an interactive reference at [/api/docs](https://www.onlyworlds.com/api/docs). Keys are per world, sent as `API-Key` and `API-Pin` headers. The developer docs are at [onlyworlds.github.io](https://onlyworlds.github.io).

## Changing the standard

The schema changes through the [Council](https://council.onlyworlds.com): motions, votes and precedents. Schema requests and questions are welcome there, in [Discussions](https://github.com/OnlyWorlds/OnlyWorlds/discussions), or at [onlyworlds.com/feedback](https://www.onlyworlds.com/feedback). Bugs go to [Issues](https://github.com/OnlyWorlds/OnlyWorlds/issues).

## Links

[onlyworlds.com](https://www.onlyworlds.com) · [Docs](https://onlyworlds.github.io) · [API reference](https://www.onlyworlds.com/api/docs) · [Tools](https://www.onlyworlds.com/tools) · [Discord](https://discord.gg/twCjqvVBwb) · [Feedback](https://www.onlyworlds.com/feedback)

## Licence

MIT. See [LICENSE](LICENSE).
