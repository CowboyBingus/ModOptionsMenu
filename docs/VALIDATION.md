Supports Helldivers 2 Steam build 25480438 / EXE 1.8.46015.0.

Offline: `tests/test_options_tab.lua` runs in the game's own lua51.dll against
simulated game memory. It covers the tab and category labels, page builds and
restoration of the native rows, the layout and description pass, APPLY and the
UNAPPLIED CHANGES prompt (answered before or after the addon's update, with the
game's cleared confirm key), saved values, 16-byte aligned native buffers, the
per-frame read budgets with zero garbage, and the slider Shallow Water Diving
registers.

In game (recorded play): the MODS tab with two registering mods, toggles and a
slider, descriptions, APPLY (Tab), discarding through the UNAPPLIED CHANGES
prompt, and saved values across restarts. Controller navigation is not yet
verified in game.
