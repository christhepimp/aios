# AIOS

**The operating system is the model. The kernel is the body.**

AIOS is a project to build an AI-native OS: not a chat widget on Android, and not a fantasy kernel rewrite on day one. The OS *is* an agent. It sees what you are doing, plans, runs tools, and slowly takes over userland while Linux stays the hardware layer.

You cannot replace Linux from inside an Android emulator in one shot. Android *is* Linux plus a userspace stack (init, zygote, ART, binder). Real OS work is staged:

1. Root a lab emulator so we own userspace.
2. Run an AI supervisor as PID-adjacent control (init replacement later).
3. Swap services one by one: launcher, settings, package manager, shell.
4. Keep the Linux kernel until we have a reason and a team to write a new one.

That last step is years of work. This repo starts at steps 1–3.

## Repo layout

```
aios/
  docs/           architecture and lab notes
  supervisor/     the AI control plane (Python prototype)
  init-hooks/     how we attach without forking the kernel yet
  lab/            rooted emulator recipes
```

## Lab: rooted Android emulators (research, 2025–2026)

Use these as disposable labs. Do not treat a consumer game emulator as a production kernel tree.

| Path | What you get | Notes |
| --- | --- | --- |
| Android Studio AVD + [rootAVD](https://github.com/newbit1/rootAVD) + Magisk | Official images, `adb`, Magisk modules | Best default lab |
| [MagiskOnEmulator](https://github.com/shakalaca/MagiskOnEmulator) | Patch official emulator ramdisk | API 22–30 / S, not a full kernel fork |
| [Genymotion + Magisk](https://support.genymotion.com/hc/en-us/articles/8957952431389-How-to-install-Magisk-on-Genymotion) | Fast x86/ARM VMs, vendor Magisk zips | Official Magisk notes by Android version |
| Nox / LDPlayer / MuMu with writable system + Kitsune/Magisk | Easy root toggle | Fine for userspace experiments, not kernel source |

What root actually gives you: `su`, writable overlay, ability to replace `/system` binaries, Magisk modules, and a shell as uid 0. It does **not** give you a clean Linux source tree you can swap for a new kernel. Kernel work is a separate tree (AOSP kernel, mainline Linux), built on the host, flashed as a boot image.

## What “the OS is AI” means here

- **Perception:** screenshots, logcat, accessibility tree, notifications.
- **Policy:** a local or remote model that outputs structured actions.
- **Actuation:** `adb`, `su`, intents, overlay UI, later a custom launcher and init.
- **Memory:** session + long-term store of user goals and device state.
- **Safety:** confirm destructive actions; never auto-wipe or auto-root a real phone from this repo.

See `docs/ARCHITECTURE.md` and `supervisor/README.md`.

## Status

Prototype control plane and docs only. No custom kernel. No claim that Linux has been replaced.
