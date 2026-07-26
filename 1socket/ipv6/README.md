# IPv6 Address Guide

This guide explains how to find the IPv6 address on Linux, Windows, and macOS devices.

---

# What is an IPv6 Address?

An IPv6 address is the newer version of IP addressing used on networks and the Internet.

Example:

```text
2001:db8:85a3::8a2e:370:7334
```

Unlike IPv4, IPv6 uses 128 bits and is written in hexadecimal.

---

# Linux

## Method 1: Using ip Command

Show all network interfaces and IPv6 addresses:

```bash
ip -6 addr
```

Example Output:

```text
2: wlp7s0: <BROADCAST,MULTICAST,UP,LOWER_UP>
    inet6 2405:201:xxxx:xxxx::1234/64 scope global
    inet6 fe80::abcd:1234:5678:90ef/64 scope link
```

### Address Types

- Global IPv6 Address:

```text
2405:201:xxxx:xxxx::1234
```

- Link-Local IPv6 Address:

```text
fe80::abcd:1234:5678:90ef
```

---

## Method 2: Show Only IPv6 Addresses

```bash
ip -6 addr show
```

---

## Method 3: View IPv6 Routing Table

```bash
ip -6 route
```

Example:

```text
default via fe80::1 dev wlp7s0
```

---

# Windows

## Method 1: Command Prompt

Open Command Prompt and run:

```cmd
ipconfig
```

Example Output:

```text
Wireless LAN adapter Wi-Fi:

   IPv6 Address . . . . . . . . . . :
   2405:201:xxxx:xxxx::1234

   Link-local IPv6 Address . . . . :
   fe80::abcd:1234:5678:90ef%15
```

---

## Method 2: PowerShell

```powershell
Get-NetIPAddress -AddressFamily IPv6
```

Example Output:

```text
IPAddress         : 2405:201:xxxx:xxxx::1234
InterfaceAlias    : Wi-Fi
AddressFamily     : IPv6
```

---

## Method 3: Network Settings

1. Open **Settings**
2. Go to **Network & Internet**
3. Select your connection
4. Open **Hardware Properties**
5. View the IPv6 Address

---

# macOS

## Method 1: Terminal

Show IPv6 information:

```bash
ifconfig
```

Example Output:

```text
en0:
    inet6 fe80::abcd:1234:5678:90ef%en0 prefixlen 64
    inet6 2405:201:xxxx:xxxx::1234 prefixlen 64
```

---

## Method 2: Network Setup

```bash
networksetup -getinfo Wi-Fi
```

Example Output:

```text
IPv6: Automatic
IPv6 IP address: 2405:201:xxxx:xxxx::1234
```

---

## Method 3: System Settings

1. Open **System Settings**
2. Select **Network**
3. Choose the active connection
4. Click **Details**
5. View the IPv6 Address

---

# Find IPv6 Address of Another Device

## Linux

Use Neighbor Discovery:

```bash
ip -6 neigh
```

Example:

```text
fe80::1234:5678:abcd:ef01 dev wlp7s0 lladdr aa:bb:cc:dd:ee:ff
```

---

## Windows

```cmd
netsh interface ipv6 show neighbors
```

---

## macOS

```bash
ndp -a
```

Example:

```text
fe80::1234:5678:abcd:ef01
```

---

# Test IPv6 Connectivity

## Linux / macOS

```bash
ping6 google.com
```

or

```bash
ping -6 google.com
```

---

## Windows

```cmd
ping -6 google.com
```

---

# Check Public IPv6 Address

## Linux / macOS

```bash
curl -6 ifconfig.me
```

---

## Windows PowerShell

```powershell
curl.exe -6 ifconfig.me
```

---

# IPv6 Address Types

| Type | Prefix | Example |
|--------|--------|--------|
| Global Unicast | 2000::/3 | 2405:201:xxxx::1234 |
| Link-Local | fe80::/10 | fe80::abcd:1234 |
| Loopback | ::1 | ::1 |
| Multicast | ff00::/8 | ff02::1 |

---

# Quick Commands Summary

## Linux

```bash
ip -6 addr
ip -6 route
ip -6 neigh
```

## Windows

```cmd
ipconfig
netsh interface ipv6 show neighbors
```

```powershell
Get-NetIPAddress -AddressFamily IPv6
```

## macOS

```bash
ifconfig
ndp -a
networksetup -getinfo Wi-Fi
```

---

# Troubleshooting

## Verify IPv6 is Enabled

### Linux

```bash
cat /proc/sys/net/ipv6/conf/all/disable_ipv6
```

Output:

```text
0
```

means IPv6 is enabled.

---

### Windows

```cmd
netsh interface ipv6 show interfaces
```

---

### macOS

```bash
networksetup -getinfo Wi-Fi
```

---

# Example IPv6 Address

```text
2405:201:abcd:1234:5678:9abc:def0:1234
```

Compressed Form:

```text
2405:201:abcd:1234::1234
```

IPv6 addresses may appear in full or compressed format.
