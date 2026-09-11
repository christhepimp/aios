# Architecture

```
+---------------------------------------------+
|  AI Supervisor  (goals, plan, tools, memory) |
+---------------------------------------------+
|  Policy / skills  (structured JSON actions)  |
+---------------------------------------------+
|  Userspace we own: shell, launcher, services |
+---------------------------------------------+
|  Android framework (ART, binder, zygote)     |
+---------------------------------------------+
|  Linux kernel  (drivers, process, mm, fs)    |
+---------------------------------------------+
|  Emulator / hardware                         |
+---------------------------------------------+
```

Replace from the top down. The kernel is last because every driver, scheduler, and filesystem lives there. An AI process is not a kernel.

## Phases

### Phase 0 — Lab
Rooted AVD or Genymotion. `adb shell su`. Snapshot the VM after every working change.

### Phase 1 — Supervisor
Host or on-device Python/Go agent. Sees logcat + screenshot. Emits actions: tap, type, run, install, explain.

### Phase 2 — Skin
Custom launcher and system UI that talk only to the supervisor. User never opens a dumb settings app unless the agent sends them there.

### Phase 3 — Init
A small `aios-init` that Magisk or a custom ramdisk starts after kernel init. It supervises zygote instead of the stock init scripts doing everything.

### Phase 4 — Kernel (later, separate repo)
Only if we need different scheduling, isolation, or capability model. Fork AOSP common kernel. Do not “edit Linux from inside the emulator.” Build on the host. Flash `boot.img`.

## Non-goals

- Shipping a from-scratch kernel this week
- Rooting other people’s phones
- Pretending a chatbot is an OS
