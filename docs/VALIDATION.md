Supports Helldivers 2 Steam build 25480438 / EXE 1.8.46015.0.

Offline: `tests/test_options_tab.lua` runs in the game's own lua51.dll against
simulated game memory. It covers the tab and category labels, page builds and
restoration of the native rows, the layout and description pass, APPLY and the
UNAPPLIED CHANGES prompt (answered before or after the addon's update, with the
game's cleared confirm key), saved values, 16-byte aligned native buffers, the
per-frame read budgets with zero garbage, set() writing rows only after the
step has checked the view, the update on Bingus Shared Runtime's guard (own
error bursts, a pause on an error below with the view handed back and rebuilt
after 60 clean frames, stops, shutdown), the slider Shallow Water
Diving registers, and the pages for more than 8 mods (7 mods per page, the page
control's row, page turns that relabel only the buttons, edits and discards
across pages, 112 mods at most). `tests/test_categories.lua` covers which mods
get a category and category identity (mod_id, or addon and first name, through
a language change); `tests/test_values.lua` the values file (unchanged values
not written, temp file and backup, interrupted and failed saves, retries);
`tests/test_ffi_names.lua` Windows SDK declarations of the addon's functions made
before or after it loads, and the build check through the runtime's shared
module hashes; `tests/test_slider_numbers.lua` NaN and infinite slider
numbers at registration, in set() and in the values file, interpreted and
compiled (the MODS rows' own case is in test_options_tab.lua);
`tests/test_hostile.lua` the addon in a hostile shared state (Bingus Shared
Runtime's hostile_vm.lua): every Windows name it and its runtime use declared
first with wrong prototypes, and a failing update below it. All run in the
workspace LuaJIT and the game's lua51.dll, and scripts/build.py runs every one
in both before it builds.

In game (recorded play): the MODS tab with two registering mods, toggles and a
slider, descriptions, APPLY (Tab), discarding through the UNAPPLIED CHANGES
prompt, and saved values across restarts. Controller navigation is not yet
verified in game. The changes after v1.1 (the mod limit and category
identity, set() timing, the values file's backup, error bursts, private Windows
names, NaN and infinite slider numbers, pages past 8 mods, the runtime's guard
and module hashes) are verified offline only. For the pages, play must check: the 8th button's PAGE 1 OF n text; its one
row and description; turning it with the mouse, keyboard and controller
(buttons relabel, no APPLY hint, no flicker, focus stays on the row); whether
hidden buttons on a short last page leave a gap above the page button; that
controller navigation skips them; and that leaving and reopening MODS shows the
last page and leaves OPTIONS as it was.
