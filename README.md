# Pikud Haoref Lightbulb Notifier

`pikud_haoref_bulb` is a small python application that monitors Pikud HaOref alerts for a configured city, driveing a smart bulb to change colour based on the current alert state.

## Why

I wanted a purely passive Shabbat-friendly alert indicator.  Rather then leaving on גל השקט, this can provide a non-intrusive, Shabbat friendly notifiation, one that provides only the desired information.

## How

This polls Pikud HaOref and changes a smart bulb's colour to reflect the current state.

| Colour | Meaning |
|--------|---------|
| 🔴 Red | Rockets |
| 🟡 Yellow | Early warning |
| 🟢 Green | Leave the mamad (all clear) |
| 🔵 Blue | No internet (request failed) |
| ⚪ White | Unknown / no data |

## Hardware

My setup is simple. I run the docker on a raspberry pi I already had kicking around the house. I have a wall pluggable light socket like the image below, and a Yeelight compatible smart bulb.

## Running

### Configuration

| Option | CLI flag | Env var | Default | Required |
|--------|----------|---------|---------|----------|
| City / zone | `--city` | `PIKUD_HAOREF_ZONE` | — | yes |
| Poll interval (seconds) | `--delay` | `CHECK_HOMEFRONT_DELAY` | 60 | no |
| Bulb IPs | `--bulb` | `BULB_IPs` | - | no |

CLI flags override environment variables.  Your city name *must* match the Hebrew name for the area, as used by פיקוד העורף.

### Via docker compose

Set your city, API polling delay (in seconds), build, and run

```sh

# monitor every 90 seconds
export PIKUD_HAOREF_ZONE="נתניה - מזרח"
export POLLING_SECONDS=90

# comma separated list of light bulbs
export BULB_IPS="192.168.1.111,192.168.1.222"
docker compose up --build -d --force-recreate --remove-orphans
```
