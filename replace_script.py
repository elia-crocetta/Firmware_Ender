#!/usr/bin/env python3
# Script per sostituire parametri per la mia stampante.
# Per buildare, utilizzare STM32F103RE_creality(512K)
import fileinput
import sys

# Mapping delle sostituzioni
replacements = {
    "//#define BLTOUCH": "#define BLTOUCH",
    "//#define SHOW_PROGRESS_PERCENT": "#define SHOW_PROGRESS_PERCENT",
    "//#define NOZZLE_PARK_FEATURE": "#define NOZZLE_PARK_FEATURE",
    "//#define ADVANCED_PAUSE_FEATURE": "#define ADVANCED_PAUSE_FEATURE",
    "//#define PARK_HEAD_ON_PAUSE": "#define PARK_HEAD_ON_PAUSE",
    "//#define SHOW_CUSTOM_BOOTSCREEN": "#define SHOW_CUSTOM_BOOTSCREEN",
    "//#define CUSTOM_STATUS_SCREEN_IMAGE": "#define CUSTOM_STATUS_SCREEN_IMAGE",
    "//#define POWER_LOSS_RECOVERY": "#define POWER_LOSS_RECOVERY",
    "#define PLR_ENABLED_DEFAULT   false": "#define PLR_ENABLED_DEFAULT   true",
    "//#define POWER_LOSS_ZRAISE": "#define POWER_LOSS_ZRAISE",
    "//#define POWER_LOSS_PURGE_LEN": "#define POWER_LOSS_PURGE_LEN",
    "//#define AUTO_BED_LEVELING_BILINEAR": "#define AUTO_BED_LEVELING_BILINEAR",
    "#define AUTO_BED_LEVELING_UBL": "//#define AUTO_BED_LEVELING_UBL",
    "//#define Z_SAFE_HOMING": "#define Z_SAFE_HOMING",
    "#define Z_MIN_PROBE_USES_Z_MIN_ENDSTOP_PIN": "//#define Z_MIN_PROBE_USES_Z_MIN_ENDSTOP_PIN",
    "//#define USE_PROBE_FOR_Z_HOMING": "#define USE_PROBE_FOR_Z_HOMING",
    "//#define Z_MIN_PROBE_PIN -1": "#define Z_MIN_PROBE_PIN PB1",
    "//#define BABYSTEP_ZPROBE_OFFSET": "#define BABYSTEP_ZPROBE_OFFSET",
    "//#define LCD_BED_LEVELING": "#define LCD_BED_LEVELING",
    "//#define LCD_BED_TRAMMING": "#define LCD_BED_TRAMMING",
    "#define MIN_SOFTWARE_ENDSTOP_Z": "//#define MIN_SOFTWARE_ENDSTOP_Z",
    "#define NOZZLE_TO_PROBE_OFFSET { 10, 10, 0 }": "#define NOZZLE_TO_PROBE_OFFSET { -42, -10, 0 }",
    "//#define BLTOUCH_DELAY 500": "#define BLTOUCH_DELAY 500",
    "//#define FILAMENT_RUNOUT_SENSOR": "#define FILAMENT_RUNOUT_SENSOR",
    "#define FILAMENT_CHANGE_UNLOAD_LENGTH      100": "#define FILAMENT_CHANGE_UNLOAD_LENGTH      150",
    "#define FILAMENT_CHANGE_FAST_LOAD_LENGTH     0": "#define FILAMENT_CHANGE_FAST_LOAD_LENGTH    50",
    "#define NOZZLE_TO_PROBE_OFFSET { 10, 10, 0 }": "#define NOZZLE_TO_PROBE_OFFSET { -42, -10, -10 }",
    "#define MIN_SOFTWARE_ENDSTOP_Z": "//#define MIN_SOFTWARE_ENDSTOP_Z",
    "//#define EXTRAPOLATE_BEYOND_GRID": "#define EXTRAPOLATE_BEYOND_GRID",
    "#define ARC_SUPPORT": "//#define ARC_SUPPORT",
    "//#define PROBE_OFFSET_WIZARD": "#define PROBE_OFFSET_WIZARD"
}

files = ["Marlin/Configuration.h", "Marlin/Configuration_adv.h"]

for line in fileinput.input(files, inplace=True):
    stripped = line.strip()
    if stripped in replacements:
        print(replacements[stripped])
    else:
        print(line, end="")
