# Bluetooth Address (MAC Address) Guide

A Bluetooth address (also called a **Bluetooth MAC Address** or **BD Address**) is a unique identifier assigned to a Bluetooth device.

Example:

```text
DC:41:A9:FB:7A:C4
```

---

# Linux

## Method 1: Using bluetoothctl

Run:

```bash
bluetoothctl list
```

Example Output:

```text
Controller DC:41:A9:FB:7A:C4 user-laptop [default]
```

Bluetooth Address:

```text
DC:41:A9:FB:7A:C4
```

---

## Method 2: Using hciconfig

Run:

```bash
hciconfig
```

Example Output:

```text
hci0: Type: Primary
    BD Address: DC:41:A9:FB:7A:C4
```

The value after **BD Address** is the Bluetooth MAC Address.

---

## Method 3: View Nearby Devices

List discovered devices:

```bash
bluetoothctl devices
```

Or scan for devices:

```bash
hcitool scan
```

Example Output:

```text
Scanning ...
AA:BB:CC:DD:EE:FF Phone
11:22:33:44:55:66 Headphones
```

---

# Windows

## Method 1: Using Settings

1. Open **Settings**
2. Go to **Bluetooth & devices**
3. Select the Bluetooth device
4. Open **Properties** or **More device information**
5. View the Bluetooth Address

---

## Method 2: Using PowerShell

Open PowerShell and run:

```powershell
Get-PnpDevice | findstr Bluetooth
```

You can also view network adapters:

```powershell
Get-NetAdapter
```

---

## Method 3: Using Device Manager

1. Press `Win + X`
2. Open **Device Manager**
3. Expand **Bluetooth**
4. Right-click your Bluetooth adapter
5. Select **Properties**
6. Open the **Details** tab
7. Look for **Bluetooth Device Address**

---

# macOS

## Method 1: System Information

1. Click the **Apple Menu**
2. Select **About This Mac**
3. Click **System Report**
4. Select **Bluetooth**

The Bluetooth controller information will be displayed, including the address.

---

## Method 2: Terminal

Run:

```bash
system_profiler SPBluetoothDataType
```

Example Output:

```text
Address: DC-41-A9-FB-7A-C4
```

---

# Ubuntu Quick Commands

Show Bluetooth Controller:

```bash
bluetoothctl list
```

Show Detailed Bluetooth Information:

```bash
hciconfig
```

List Discovered Devices:

```bash
bluetoothctl devices
```

---

# Example Bluetooth Address

```text
DC:41:A9:FB:7A:C4
```

Format:

```text
XX:XX:XX:XX:XX:XX
```

- 6 bytes (48 bits)
- Written in hexadecimal
- Unique to each Bluetooth adapter

---

# Troubleshooting

## Bluetooth Not Found

Check Bluetooth service status:

```bash
systemctl status bluetooth
```

Start Bluetooth service:

```bash
sudo systemctl start bluetooth
```

Enable Bluetooth at boot:

```bash
sudo systemctl enable bluetooth
```

---

## Check Bluetooth Hardware

```bash
lsusb | grep -i bluetooth
```

or

```bash
lspci | grep -i bluetooth
```

---

## Verify Bluetooth Controller

```bash
bluetoothctl list
```

If no controller appears, verify drivers and hardware support.
