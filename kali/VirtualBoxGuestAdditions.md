From the virtual machine menu, click Devices -> “Insert Guest Additions CD Image”.

Navigate to the directory and execute the VBoxLinuxAdditions.run script to install the Guest Additions:

```
cd /mnt/cdrom
sudo sh ./VBoxLinuxAdditions.run --nox11
```

The --nox11 option tells the installer not to spawn an xterm window.

Once the virtual machine is booted, log into it and verify that the installation was successful and the kernel module is loaded using the lsmod command:

`lsmod | grep vboxguest`
