# OnlyWorlds

OnlyWorlds is an open-source framework for creating, storing, and exchanging structured world data across tools and applications.  

Use cases include:
- Narrative writing and world organization
- Tabletop roleplaying and campaign planning
- Game integration and simulation
- Map-based tools
- History and educational models

This repository contains the base **schema definitions**, defined in YAML and automatically converted into other programming languages to support further development.

The schema is under active development and intended as a collaborative foundation: contributions, reimaginings, and extensions are strongly encouraged.
 
- Full documenation & available tools: **[onlyworlds.github.io](https://onlyworlds.github.io)**
- Account & world management: **[onlyworlds.com](https://onlyworlds.com)**

## Repository & Contribution

This repository is the central reference for the OnlyWorlds schema. It includes:
- Core definitions: YAML schemas for all world element categories and fields (see `/schema`)
- Automated exports to other formats/languages (see `/languages`)
- A discussion section for organized feedback
 
### For Developers

Developers can contribute by building or integrating tools that use the schema. This may include editors, viewers, generators, converters, games, or any other applications that operate with (parts of) world data.

Key resources:
- The `/schema` directory (YAML-based schema definitions)
- The `/languages` directory (ready conversions of the YAML schema)
- The [OnlyWorlds OpenAPI](https://onlyworlds.com/api/docs) for transferring worlds

Schema updates and structural proposals can be proposed and discussed through GitHub pull requests, [Discord](https://discord.gg/twCjqvVBwb), or the [Discussions section](https://github.com/OnlyWorlds/OnlyWorlds/discussions).

### For Developers-to-be

If you have ideas or wishes but little or no experience, 2025 is a great year to get building. You can feed this website, together with the [OpenAPI page](https://onlyworlds.com/api/docs), into any code-assist AI of choice to get started. 

[OnlyWorldBot](https://chatgpt.com/g/g-dydgDFnOz-onlyworldbot) is freely available and tailored to helping you develop for the OnlyWorlds framework.

### For Creators and Non-Technical Users

Feedback is welcome from anyone using or interested in the format. This may include:
- Requests for new or changed element categories or fields 
- Notes on missing features or mismatches with your worldbuilding needs
- Tool ideas or UI-related concerns

Feedback can be submitted via:
- [GitHub Discussions](https://github.com/OnlyWorlds/OnlyWorlds/discussions)
- [OnlyWorlds Discord](https://discord.gg/twCjqvVBwb)
- [Parse Tool](https://onlyworlds.com/parse_tool/)

## OpenAPI & API Access

The [OnlyWorlds API](https://onlyworlds.com/api/docs) provides world-level access to create, modify, and sync world data across applications. It follows the OpenAPI 3 specification and supports authentication via a system of world-specific API keys and user PINs. 

## License

This project is licensed under a permissive open-source license. The schema and data model are free to use, adapt, and distribute. There are no commercial restrictions or ecosystem lock-in.

## More Resources

- [Main site](https://onlyworlds.com)
- [Documentation & Tool Directory](https://onlyworlds.github.io)
- [API Reference](https://onlyworlds.com/api/docs)
- [GitHub Discussions](https://github.com/OnlyWorlds/OnlyWorlds/discussions)
- [Discord Server](https://discord.gg/twCjqvVBwb)
