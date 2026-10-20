# Changelog

What changed in the OnlyWorlds standard, newest first. The version is in [`VERSION`](VERSION); the files for each version are in [`schema/`](schema/). A change that tools must react to goes through the Council as a motion; editorial fixes (descriptions, typos, constraints that never matched their intent) are made directly and listed here.

Tools usually read the standard through [schema-dist](https://github.com/OnlyWorlds/schema-dist), whose releases say which version of the standard each one carries.

## 00.32.01 (2026-10-20)

Editorial: a description sharpened, no field changed.

- **Event**: `characters` now reads "Characters who know about the event: they were present, aware of it, or involved in it", where it read "Key characters relevant to the event". A Character only mentioned in an event (discussed, not there) is linked from a Narrative's `characters` or named in the text instead, so a tool that shows a Character what it knows can trust this field. Narrative's `characters` stays as it was: the people a story is about.

## 00.32.00 (2026-10-10)

- **World**: `created_at`, `updated_at` and `public_read` join the definition. Every reader already saw them on the wire. `api_key`, `user` and `version` leave the definition: they were leftovers from v1 that describe a platform, not a world. Nothing for a tool to react to, because the v2 API never served the removed keys and the added ones are optional.
- **Id** (2026-10-12, editorial): the description now matches what the platform does. An id is a UUID: new ids are minted as uuidv7, and ids minted earlier as uuidv4 stay valid.

## 00.31.00 (2026-10-09)

- **World**: `length_unit`, `mass_unit` and `distance_unit` say which units the world's numbers are in.

## 00.30.02 (2026-10-08)

- Only a name and an id are required on an element. The world comes from the key, not from the element.
- **Pin, Marker**: their required lists are gone. A pin without a map is a real pattern in apps, and the API never enforced them.
- Descriptions corrected: Location's `rival` and `partner` read singular (they are single links), Pin's `element` describes the link instead of platform storage, and Marker's `order` says what happens without it. Relation's duplicate `events` declaration is removed.

## 00.30.01 (2026-07-29)

Editorial: nothing was added, removed or retyped.

- `maximum: 0` was removed from 26 fields. It was meant as "no maximum", but in JSON Schema it means "may not exceed zero". Leaving it out already means unbounded.
- `minimum: 0` was added where a field had a ceiling and no floor: Character's six personality scores, Relation's `intensity` and Species' `aggression`. Trait's modifiers keep their negative range on purpose.
- Ability's `potency` gained `minimum: 0` (it already had a maximum of 100).
- Construct's `relations` and Event's `languages` had their descriptions nested inside `items`, where readers could not see them; they were moved up onto the field.
- Five description typos were fixed (the docs site had already corrected them by hand).

## Earlier

- **2025-12-09**: the **Zone** type, and an `order` field on Marker. Both were added while the version still read 00.30.00.
- **00.30.00 (2025-07-09)** and before: see the [commit history](https://github.com/OnlyWorlds/OnlyWorlds/commits/main).
