# Emulating games on the PockeCHIP


## Install mednafen emulator:

`sudo apt-get install mednafen libsdl2-dev`


## Further setting:

Within the PocketCHIP run the emulator so it creates the config file for further editing

`mednafen`

Go to the directory `/home/chip/.mednafen/` and look for a file named like `mednafen.cfg`

Change the following lines on the file:

| Original line | Changed line |
| ------------- | ------------ |
| video.driver opengl | video.driver sdl |
|sound.device default | sound.device sexyal-literal-default |
|| gba.xscalefs 2.000000 |
|| gba.yscalefs 2.000000 |
|| gba.stretch full|
|| gba.yres 272 |
|| gba.xres 480 |
|| gb.stretch aspect|
|| gb.xres 480 |
|| gb.xscalefs 2.000000 |
|| gb.yres 272 |
|| gb.yscalefs 2.000000 |
|| snes.stretch full|
|| snes.xres 480|
|| snes.xscalefs 2.000000 |
|| snes.yres 272|
|| snes.yscalefs 2.000000 |
|| nes.stretch aspect|
|| nes.xres 480 |
|| nes.xscalefs 2.000000 |
|| nes.yres 272 |
|| nes.yscalefs 2.000000|

To run any game just type: `mednafen -fs 1 /path/to/rom`

## Creating a "GUI" for the emulator.

If you desire to have a "GUI" create a `.sh` file with the content of `medGUI.sh` file that is it within this repository folder.

Install needed packages:

`sudo apt-get install zenity`

After this, give execution permissions to the file by typing `chmod +x medGui.sh`

**NOTES:** 
  
  * Take into account that in the file `medGUI.sh` there is a route pointing to `/home/chip/roms` folder, if you have the roms in other location, go and edit the file so it is pointing to the right directory.
  
  * You can place this file in the Desktop so you'll have a quick access to it.
  
  * `alt+shift+1` should show a window to configure the controller.
