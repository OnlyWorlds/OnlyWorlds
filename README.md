# OnlyWorlds

OnlyWorlds is an open-source worldbuilding framework for creating, storing, and exchanging structured world data across tools and applications.

This repository contains the **schema definitions** used to describe world elements. The schemas are defined in YAML and automatically converted into multiple programming languages to support a growing tool ecosystem.

The schema is under active development and subject to change based on community input.

## Overview

OnlyWorlds provides a shared structure for digital worlds. The goal is to enable creators to build interoperable, portable, and reusable world data, regardless of genre or application.

It is used across domains such as:
- Narrative writing and world bibles
- Tabletop roleplaying tools
- Game engines and map editors
- Historical simulations and educational applications

For more information and an overview of current tools, visit:  
**[https://onlyworlds.github.io](https://onlyworlds.github.io)**

This repository is the central reference for the OnlyWorlds schema. It includes:
- YAML schemas for all world element categories (see `/schema`)
- Automated exports to other formats/languages (see `/languages`)
- A discussion section for organized feedback

This repository defines the shared data layer. Tools that use it may live in other repos or be independently developed.

## Contribution

OnlyWorlds is an open standard. Contributions are highly encouraged from both technical and non-technical participants. The current schema is a first draft, created to provide a practical starting point. It is not final or authoritative, adn the goal is for this structure to grow through open discussion and shared work. Contributions, critiques, and reimaginings are highly encouraged.

### For Developers

Developers can contribute by building or integrating tools that use the schema. This may include editors, viewers, generators, converters, games, or any other applications that operate with (parts of) world data.

Key resources:
- The `/schema` directory (YAML-based schema definitions)
- The `/languages` directory (ready conversions of the YAML schema)
- The [OnlyWorlds API](https://onlyworlds.com/api/docs) for transferring worlds 

Schema updates and structural proposals can be discussed and proposed through GitHub pull requests, [Discord](https://discord.gg/twCjqvVBwb),  or the [Discussions section](https://github.com/OnlyWorlds/OnlyWorlds/discussions).

### For Creators and Non-Technical Users

Feedback is welcome (necessary!) from anyone using or exploring the format. This includes:
- Requests for new or changed element categories or fields 
- Notes on missing features or mismatches with your worldbuilding needs
- Tool ideas or UI-related concerns

Feedback can be submitted via:
- [GitHub Discussions](https://github.com/OnlyWorlds/OnlyWorlds/discussions)
- [OnlyWorlds Discord](https://discord.gg/twCjqvVBwb)
- [Parse Tool](https://onlyworlds.com/parse_tool/)

## OpenAPI & API Access

The [OnlyWorlds API](https://onlyworlds.com/api/docs) provides world-level access to create, modify, and sync world data across applications. It follows the OpenAPI 3 specification and supports authentication via world-specific API keys and user PINs. 

## License

This project is licensed under a permissive open-source license. The schema and data model are free to use, adapt, and distribute. There are no commercial restrictions or ecosystem lock-in.

See `LICENSE` for details.

## Related Resources

- [Main site](https://onlyworlds.com)
- [Documentation & Tool Directory](https://onlyworlds.github.io)
- [API Reference](https://onlyworlds.com/api/docs)
- [GitHub Discussions](https://github.com/OnlyWorlds/OnlyWorlds/discussions)
- [Discord Server](https://discord.gg/twCjqvVBwb)
