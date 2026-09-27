# v1.0

- Adds a native MODS tab to the escape menu, beside GAME, SOCIAL and OPTIONS. Each mod that registers options gets its own category button (up to 8) with native toggle, choice and slider rows (up to 32 per mod) and descriptions in the game's description box.
- Edits work like the game's own settings: APPLY (Tab) applies them, and confirming the UNAPPLIED CHANGES prompt on leaving discards them. Applied values are saved and restored in later sessions.
- Gives mod authors `ModOptionsMenu.register_option`, `get`, `set`, `on_change` and `ready` (api 1). Shallow Water Diving v3.8 uses it for its maximum dive depth slider.
- Checks the game.dll and EXE hashes and every native entry point for Steam build 25480438 before touching the menu; on any other build the tab is not added.
- One memory read per frame with the escape menu closed and two with it open, without allocating. Measured in recorded play: about 0.006 ms per frame aboard the ship and 0.002 ms per frame in missions.
- Requires Bingus Shared Loader v18 or newer.
