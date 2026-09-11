# Supervisor

The supervisor is the first piece of “OS as AI.” It runs on the host in this prototype and drives the rooted emulator over adb.

```
python supervisor/aios_supervisor.py --dry-run
```

It does not replace Linux. It is the control plane we will later move on-device.
