# NIEM Standard

This folder should contain the [NIEM-Releases](https://github.com/NIEM/NIEM-Releases) repository pinned to tag `6.0`.

Run the helper script below from the repository root to clone the submodule:

```sh
bash scripts/setup_niem_releases.sh
```

The script executes the equivalent of:

```sh
git submodule add https://github.com/NIEM/NIEM-Releases openpermit/standards/niem/NIEM-Releases
cd openpermit/standards/niem/NIEM-Releases
git checkout tags/6.0
```

Make sure the submodule exists before running the schema build script.
