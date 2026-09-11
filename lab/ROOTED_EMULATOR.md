# Rooted emulator lab

Recommended path: **Android Studio AVD + rootAVD + Magisk**.

## Why this path

- Official system images
- Real `adb`
- Magisk is the standard way to persist root without pretending you rewrote Linux

## Steps (host)

1. Install Android Studio and create an AVD (API 30+ Google APIs image is a good start; Play images are harder).
2. Clone rootAVD and follow its list/root commands for your API level.
3. Cold boot the AVD. Open Magisk. Complete setup. Reboot.
4. Confirm:

```
adb shell su -c id
# uid=0(root) gid=0(root)
```

## Alternatives

- MagiskOnEmulator: patch `ramdisk.img`, copy it back, cold boot.
- Genymotion: use their rebuilt Magisk zips for the matching ABI and Android version.
- Nox / LDPlayer / MuMu: enable writable system disk, then Kitsune/Magisk. Use only for userspace tests.

## What to do after root

- Snapshot the AVD.
- Push `supervisor/` scripts.
- Do not delete `/system/bin/init`.
- Do not flash random kernels from forums.
