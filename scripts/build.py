"""Build the Mod Options Menu addon and its live test addon.

Needs a Bingus Shared Loader checkout beside this repository (or its path in
BINGUS_SHARED_LOADER) for scripts/archive.py and scripts/build_addon.py.
"""

from __future__ import annotations

import json
import os
from pathlib import Path
import struct
import sys
import uuid
import zipfile


LOADER = Path(os.environ.get("BINGUS_SHARED_LOADER",
                             Path(__file__).resolve().parents[2] / "BingusSharedLoader"))
sys.path.insert(0, str(LOADER / "scripts"))
from archive import ARCHIVE, make_archive, resource_hash  # noqa: E402
from build_addon import entry_source  # noqa: E402


HERE = Path(__file__).resolve().parents[1]
VERSION = "1.0"
LUA_NAME = "mods/cowboybingus/mod_options_menu"
GUID = "95ef276a-6287-465f-ac5b-8512d2227b74"
TEST_NAME = "mods/cowboybingus/mod_options_test"
TEST_GUID = "71e42ee6-c64d-4f97-8249-97e4840bf8e5"
DESCRIPTION = ("Adds a native MODS tab beside Game, Social and Options: each installed mod gets its "
               "own category with native toggles, choices and sliders. Requires Bingus Shared Loader v18+.")


def package(output: Path, name: str, source: Path, guid: str, title: str, description: str,
            extra: dict[str, bytes]) -> Path:
    body = entry_source(name, source.read_bytes())
    lua = struct.pack("<II", len(body), 2) + body
    option = {"Name": title, "Description": description, "Include": ["Addon"]}
    manifest = {"Version": 1, "Guid": str(uuid.UUID(guid)), "Name": title,
                "Description": description, "Options": [option]}
    if "thumbnail.png" in extra:
        manifest["IconPath"] = option["Image"] = "thumbnail.png"
    files = dict(extra)
    files.update({
        "manifest.json": (json.dumps(manifest, indent=2) + "\n").encode(),
        "Addon/" + ARCHIVE: make_archive({resource_hash(name): lua}),
        "Addon/" + ARCHIVE + ".stream": b"",
        "Addon/" + ARCHIVE + ".gpu_resources": b"",
    })
    output.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(output, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        for path, payload in sorted(files.items()):
            info = zipfile.ZipInfo(path, date_time=(1980, 1, 1, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            archive.writestr(info, payload)
    return output


def build(output: Path) -> Path:
    return package(output, LUA_NAME, HERE / "src" / "mod_options_menu.lua", GUID,
                   "Mod Options Menu v" + VERSION, DESCRIPTION,
                   {"INSTALL.txt": (HERE / "INSTALL.txt").read_bytes()})


def build_test(output: Path) -> Path:
    return package(output, TEST_NAME, HERE / "tests" / "live" / "options_test.lua", TEST_GUID,
                   "Mod Options Test Addon", "Registers sample options for six test mods and logs "
                   "changes to ModOptionsTest.log. Requires Mod Options Menu.", {})


if __name__ == "__main__":
    print(build(HERE / "releases" / f"Mod-Options-Menu-v{VERSION}.zip"))
    print(build_test(HERE / "build" / "Mod-Options-Test-Addon.zip"))
