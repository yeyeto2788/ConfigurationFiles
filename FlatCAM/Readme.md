# FlatCAM related information to process PCBs


## How to process some basic files:
### Processing the top/bottom layer.
```
python FlatCAM.py --shellfile=/path/to/file
open_gerber mygerber.gbr -outname pcb
isolate pcb -tooldia 0.04 -passes 3 -overlap 0.05 -combine 1 -outname pcb_iso
cncjob pcb_iso -z_cut -0.1 -z_move 1.0 -feedrate 128.0 -tooldia 0.2 -outname pcb_iso_cnc
write_gcode pcb_iso_cnc pcb.gcode
export_gcode pcb.gcode
```

### Processing the drill holes.
```
python FlatCAM.py --shellfile=/path/to/file
open_excellon drill.drl -outname drl
drillcncjob drl -drillz -1.6 -travelz 0.5 -feedrate 16.0 -spindlespeed 1000 -outname drl_cnc
write_gcode drl_cnc drl.gcode
```

### Processing the PCB cutout.
```
python FlatCAM.py --shellfile=/path/to/file
open_gerber cutgerber.gbr -outname cuts
isolate cuts -dia 1.0 -passes 1 -overlap 0.0 -combine 1 -outname cuts_iso
ext cuts_iso -outname cuts_iso_exterior
delete cuts_iso
geocutout cuts_iso_exterior -dia 2.0 -gapsize 1.0 -gaps 4 
cncjob cuts_iso_exterior -z_cut -1.6 -z_move 0.5 -feedrate 16.0 -tooldia 1.0 -spindlespeed 1000 -multidepth true -depthperpass 1.6 -outname pcb_cuts_cnc
write_gcode pcb_cuts_cnc cuts.gcode
```


### Steps on the process the PCB cutout

**1. Import Geometry**

Open `cutgerber.gbr` file.

Command: `open_gerber cutgerber.gbr -outname cuts`

**2. Generate Isolation Geometry**

Generate Geometry (Having selected the board cutout gerber), this will generate the file `cuts_iso`

Command: `isolate cuts -dia 1.0 -passes 1 -overlap 0.0 -combine 1 -outname cuts_iso`

**3. Generate the exterior geometry**

Generate the exterior geometry for the cutout and it will be named `cuts_iso_exterior`

Command: `ext cuts_iso -outname cuts_iso_exterior` 

**4. Create the path and cutout for the board.**

It is needed to create the 

Command: `geocutout cuts_iso_exterior -dia 2.0 -gapsize 1.0 -gaps 4`

These are the options for the `-gaps` parameter `(8|4|tb|lr|2tb|2lr)>]`



## `defaults.json` file.
In this file there is a configuration that can be imported into the FlatCAM software. (**I haven't test this yet!**)

## TODO:

* Offset for the boards.
```
offset pcb -12 198
offset cuts -12 198
offset drl -12 198
```
* Slow start GCODE.

```
G00 Z4
G00 X0 Y0
S0
M03
S200
G4 P2
S400
G4 P2
S600
G4 P2
```
