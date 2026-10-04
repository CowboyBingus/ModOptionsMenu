# v1.2

- More than 8 mods with options fit the MODS tab: the category buttons show 7 mods at a time, and the 8th button turns the page (up to 16 pages, 112 mods). A 9th mod's options used to be registered but never shown.
- Values are saved through a temp file, and the previous file is kept as `ModOptionsMenu.values.bak` for when the values file is missing or unreadable. A crash or a full disk during a save no longer loses every mod's settings.
- A failed save keeps the values, is logged once and is tried again 10 seconds later instead of every frame.
- The values file is written only when a value changed, and a save still due is written when the game shuts down.
- A saved NaN or infinite slider value always loads as the option's default; an infinity used to load as the slider's minimum or maximum.
- A MODS row whose slider the game or another mod sets to NaN or an infinity, or whose choice is past the option's choices, is set back to its value instead of becoming an edit that APPLY passes on.
- Every Windows function the addon calls is declared under a private name, so another mod's declarations of the same functions can no longer change the prototypes it calls.
- The update runs on Bingus Shared Runtime's guard, like the family's other mods: an error in an update below MOM pauses it until 60 frames run cleanly, handing an open MODS tab back to the game.
- After 8 errors in one burst the update stops for the session, handing an open MODS tab back to the game first; errors about a minute apart never add up, and the API keeps working.
- Each burst logs only its first error, pauses and resumes get a line each, and the status is in `BingusRuntime.statuses.ModOptionsMenu`.
- The update passes every argument and return value through to the update it wraps, not just the frame time.
- The game build check takes its module hashes from Bingus Shared Runtime's session cache, so each game file is hashed once per session for every mod.
- For mod authors (api `version` 3): a 113th mod's `register_option` returns `false` with the reason "all 112 mod categories are in use" instead of `true`.
- For mod authors: categories are keyed by the new `spec.mod_id` (a stable id such as 'author.mod'), or else by the registering addon and the first mod name it gave. A translated mod name no longer splits a mod into two categories, and two mods with the same name keep their own.
- For mod authors: `set()` no longer writes the MODS rows itself; the value counts at once and a shown row follows on the next frame, so a call while the menu closes cannot write into it.
- For mod authors: a slider's `min`, `max`, `step` and `default` must be finite numbers that fit a float, and `set()` refuses NaN and both infinities with "invalid value".
- For contributors: the build runs every test in a LuaJIT and in the game's lua51.dll before it packages anything.
- Measured in live play: 0.004 ms per frame in missions and 0.007 on the ship.

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
