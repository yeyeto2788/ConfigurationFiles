# **`99-calibration.conf`**

  **Description:** Calibration config file for PocketCHIP TouchScreen

## First install the `xinput-calibrator`

  `sudo apt-get install xinput-calibrator`

## Create the file or modify the existing one:

  Locate the file in `/usr/share/X11/xorg.conf.d/` and create or modify the file `99-calibration.conf` so it have the configuration as in this repository folder.
  
  To do so, type: `sudo nano /usr/share/X11/xorg.conf.d/99-calibration.conf` 

## Reboot the PocketCHIP

  `sudo shutdown -h now`
  
___
