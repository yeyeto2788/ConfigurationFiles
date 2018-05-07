# How to properly process the board cutout

**1. Import Geometry**

Open Other.gbr

**2. Generate Isolation Geometry**

Generate Geometry (Having selected the board cutout gerber), this will generate the file `Other.gbr_iso`

**3. Select only the exterior geometry**

`ext Other.gbr_iso` this command will generate the file `Other.gbr_iso_exteriors`

**4. Create the path and cutout for the board.**

`geocutout Other.gbr_iso_exteriors -dia 2.0 -gapsize 0.5 -gaps lr`

These are the options for the `-gaps` parameter `(8|4|tb|lr|2tb|2lr)>]`

