# v1.1

- Translatable: the MODS tab's own texts follow the game's Text Language when a translation is installed (see TRANSLATING.md).
- For mod authors (api version 2): option texts may be functions that return the text in the current language.
- Text limits count characters instead of bytes, so Chinese, Korean or Cyrillic text gets the same room as English.
- Mod names and choices are upper-cased in every script the game's fonts carry.
- Measured in live play: 0.003 ms per frame, unchanged from v1.0.

# v1.0.1

- Artwork-only release: the addon is identical to v1.0 (same compiled resource).
- The release ZIP now includes the mod's square cover (`thumbnail.png`), which Arsenal and HD2MM show for it, and the README opens with the banner.

# v1.0

- Adds a native MODS tab to the escape menu, beside GAME, SOCIAL and OPTIONS. Each mod that registers options gets its own category button (up to 8) with native toggle, choice and slider rows (up to 32 per mod) and descriptions in the game's description box.
- Edits work like the game's own settings: APPLY (Tab) applies them, and confirming the UNAPPLIED CHANGES prompt on leaving discards them. Applied values are saved and restored in later sessions.
- Gives mod authors `ModOptionsMenu.register_option`, `get`, `set`, `on_change` and `ready` (api 1). Shallow Water Diving v3.8 uses it for its maximum dive depth slider.
- Checks the game.dll and EXE hashes and every native entry point for Steam build 25480438 before touching the menu; on any other build the tab is not added.
- One memory read per frame with the escape menu closed and two with it open, without allocating. Measured in recorded play: about 0.006 ms per frame aboard the ship and 0.002 ms per frame in missions.
- Requires Bingus Shared Loader v18 or newer.
