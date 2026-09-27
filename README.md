# Mod Options Menu v1.0

Adds a native **MODS** tab beside GAME, SOCIAL and OPTIONS in the escape menu. Each mod that registers options gets its own category button (up to 8), and its options appear as native rows (up to 32 per mod): toggles, choices and sliders, with descriptions in the game's description box. Values are saved to `%LOCALAPPDATA%\CowboyBingus\Helldivers2\Logs\ModOptionsMenu.values`.

Changes work as on the OPTIONS tab: they take effect when you press **APPLY** (Tab on keyboard, or the button the hint shows). Leaving the tab or closing the menu with unapplied changes brings up the game's **UNAPPLIED CHANGES** prompt; confirming it discards them, and the next Back leaves.

[Shallow Water Diving v3.8](https://github.com/CowboyBingus/ShallowWaterDiving/releases/latest) adds its maximum dive depth slider here.

Install [the release ZIP](https://github.com/CowboyBingus/ModOptionsMenu/releases/latest) and [Bingus Shared Loader v18 or newer](https://github.com/CowboyBingus/BingusSharedLoader/releases/latest), plus the mods that use it. Enable and deploy, then restart the game. Keep the shared loader as the winning Wwise startup replacement. Mod Options Menu is a separate dependency and is not bundled in Vanilla Plus Megapack.

Steam build **25480438** only: the addon checks the game.dll and EXE hashes and every native entry point before touching the menu. With the escape menu closed it costs one small memory read per frame; with it open, two. Neither allocates. Measured in recorded play: about 0.006 ms per frame aboard the ship and 0.002 ms per frame in missions.

## For mod authors

```lua
-- HD2-Addon: mods/example/your_mod
local registered = false
local function step()
    local menu = rawget(_G, 'ModOptionsMenu')
    if registered or not menu or menu.api ~= 1 then return end
    registered = true -- The two addons may load in either order.
    menu.register_option('example.your_mod.hints', {type = 'toggle', label = 'Show Hints',
                                                    mod = 'Your Mod', default = true,
                                                    description = 'Shows button hints above the crosshair.'})
    menu.register_option('example.your_mod.mode', {type = 'choice', label = 'Fire Mode', mod = 'Your Mod',
                                                   choices = {'Single', 'Burst', 'Auto'}, default = 1})
    menu.register_option('example.your_mod.scale', {type = 'slider', label = 'Scale', mod = 'Your Mod',
                                                    min = 0.5, max = 2, step = 0.1, default = 1,
                                                    description = 'Size of the markers.'})
    menu.register_option('example.your_mod.count', {type = 'slider', label = 'Marker Count', mod = 'Your Mod',
                                                    min = 1, max = 10, default = 3}) -- whole numbers
    menu.on_change('example.your_mod.hints', function(value) --[[ apply value ]] end)
end
local previous_update = rawget(_G, 'update')
update = function(dt)
    step()
    if type(previous_update) == 'function' then return previous_update(dt) end
end
```

- `register_option(id, spec)` returns `true`, or `false` and a reason. `id` keys the saved value, so keep it stable. `spec.mod` names the category button (default: your addon's entry name); `spec.gap = true` adds space above the row; `spec.description` (plain text, up to 400 bytes) appears in the game's description box beside the rows while the option is selected. Options without one hide the box.
- Types:
  - `toggle`: value `true` or `false`; `default` is `false` unless given.
  - `choice`: `choices` lists 2–16 names; the value is the 1-based index (`default` 1 unless given). Choice words the game already has (ON, OFF, LOW, HIGH…) are shown translated.
  - `slider`: `min`, `max` and `step` (default 1), with `min < max` and `0 < step <= max - min`; the value is a number snapped to the step (`default` is `min` unless given). The row shows as many decimals as `step` needs (at most 3); a whole-number `step` and `min` give an integer slider.
- `get(id)` returns the applied value; `set(id, value)` changes it from code (replacing any unapplied edit of it) without calling callbacks; `on_change(id, fn)` calls `fn(value, id)` when the player applies a change. `ready()` reports whether the native menu integration is active.

## Build and test

Clone [Bingus Shared Loader](https://github.com/CowboyBingus/BingusSharedLoader) beside this repository (or set `BINGUS_SHARED_LOADER` to its path); the build uses its `scripts/archive.py` and `scripts/build_addon.py`.

- `python tests/run_game_lua.py --run tests/test_options_tab.lua` drives the tab against simulated game memory in the game's own `lua51.dll` (set `HD2_LUA51_DLL` for a nonstandard installation).
- `python -B scripts/build.py` builds `releases/Mod-Options-Menu-v1.0.zip` and the live test addon `build/Mod-Options-Test-Addon.zip` (six sample mods, logs to `ModOptionsTest.log`).

[Changes](CHANGELOG.md) · [Release notes](docs/RELEASE_NOTES.md) · [Validation](docs/VALIDATION.md)
