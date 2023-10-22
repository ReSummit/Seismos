# Seismos

An evolution of the Zebra keyboard, but can be used for everyday typing. Switch between ortholinear for macro keypads and staggered for typing on the go.

Since this design utilizes daughter boards, you can even choose to move the columns around with a different rail system from the example one provided (stable case design coming soon).

Allows for an interchangeable configuration between 4 and 5 row keys per column. With both halves of the keyboard, you can have a maximum of 68 keys (+2 encoder switches).

## Pictures / Example Column Shifts:
<div style="display: flex; justify-content: center;">
    <figure>
        <img src="pics/ortho.jpg" style="width: 100%; margin-right: 10px;">
    </figure>
    <figure>
        <img src="pics/staggered.jpg" style="width: 49%; margin-left: 10px;">
    </figure>
    <figure>
        <img src="pics/questionable.jpg" style="width: 49%; margin-right: 10px;">
    </figure>
</div>

# PCB Library Structure

NOTE: If you check the PCB for DRC errors, most of them will come from either the keyboard_reversible.pretty footprint or the switch footprints inherited from the MiRage keyboard. Since both have been used before, they can be ignored.

## Libraries
All PCBs in the `pcbs` folder refer to the footprint and symbol libraries found in `libs/Seismos-libs` as well as `libs/keyboard_reversible.pretty`.

Wait, keyboard_reversible.pretty isn't in the git clone? You need to run git submodule initialization and update with this command:
```bash
git submodule update --init --recursive
```

After this, you should not get errors on missing libraries.

## Current State of PCBs
**UPDATE** (2023_10_220): New layouts for Core PCBs allow for 5 rows. There are now column and thumb cluster layouts for 4 and 5 keys (however, thumb cluster can only have 4 max). Please check the BOM again to verify as you now need 10 position JST SH connectors. 9 position JST SH connectors are now deprecated.

For this release, there are PCBs for 4 and 5 columns. Currently, the left, right, and columns are made with a maximum size of 7x5 keys per side. Something to know is that due to routing efficiency, the column order is reversed for the right side; however, row number remains the same from top to bottom.

## PCB Design Thoughts
Theoretically, since JST SH connectors are pretty small, we can possibly a maximum of 12 pins, which means that you can get at most ~7 rows per column... if the microcontroller has that many pins!
(NOTE: A suggestion to reduce pin count is to wire the 1x4 keys as a 2x2 key setup to save pins; however, this results in a 2x2n keyboard layout, which will likely be a pain... Still interesting though to point out.)

# Important notes for building keyboard

For the JST SH cables, note that the male to male connector tips should face the same side. An example one is shown below (note it is a 9 pin JST SH cale, but should be the same for 10 pin JST cables).
<div style="display: flex; justify-content: center;">
    <figure>
        <img src="pics/JST_SH9_Cable.jpg" style="width: 25%; margin-right: 10px;">
        <figcaption>Example of JST SH cable with male-to-male connectors facing the same side.</figcaption>
    </figure>
</div>

# BOM
## Required
* JST SH individual wires and connectors (preferrably 10cm long). Aliexpress has these with different colors like cable mods.
    * NOTE: For these links, they come from the same seller. Contact the seller after placing a temporary order to reduce shipping costs before paying!
    * Wires: https://www.aliexpress.us/item/3256802676433370.html (choose colors, **10 cm**, and **double head**)
        * For 5 rows, 10 cm is typically enough; you may be surprised at how far the columns can go with this. However, if you plan on changing the case design, you may need 15 cm if your columns need to go farther.
    * Connectors: https://www.aliexpress.us/item/3256802084257935.html (choose **10 pin** and **SMD Horizontal**)
* Parts that can be found from Typeractive.xyz:
    * EVQPUC02K reset button
    * SSSS811101 (alternatively on Aliexpress, MSK-12C01 or SW-12C01N-GY18)
    * 110 mAH battery
* nice!nano (or Arduino Pro Micro compatible footprint)
* 1N4148W Diodes
* M3 assorted length screws (specific screw lengths to be added later)
* MX / Choc PCB Sockets (1511 for MX or 1350 for Chocs)

## Optional
* SK6812MINI-E for RGB
    * 6x per column from center of keyboard + 4 for thumb
        * Example: left and right sides require 80 total for all columns. If you only need 5 columns, then you need 68.
* nice!view (or OLED, but won't be aligned to nice!nano)
* Low profile socket pin headers for socketed microcontrollers (or similar)
* Rotary encoder EC11 (similar to Sofle)
* PJ320A headphone jacks 
    * **NOTE**: Due to me wanting to allow for wireless or wired setups, **the current PCB design will not charge the other keyboard side**. This is because VCC is disconnected to avoid blowing up the charging circuit of the nice!nano. If you need it, you may need to modify the PCB and schematic to allow for this.

# Case
Curious to see what it looks like? Behold, OnShape link that contains questionable features that are unlabelled... will get around to it but need a working prototype first!  
**WARNING: Case made but has not been test fitted with PCB! It is also using an older version of the PCB and only have 4 rows.**  
<p align="center">
    <p>Onshape Document (click on picture):</p>
    <a href="https://cad.onshape.com/documents/f7367bff9cd2cc9be8d2436b/w/1f753fadbcf1b9049e256121/e/c4b472236e977df85b7d8a49">
        <img src="pics/onshape.png" alt="OnShape" width="50%">
    </a>
</p>


# References

Seismos uses elements found from multiple places for footprints, symbols, and even the idea.

The idea for this keyboard was inspired from the [Zebra keyboard](https://github.com/nezumee/zebra). It uses jumper cables but looks to be mainly for having a physical means to determine the layout.

For footprints, they are derived from multiple places:
* [SnapEDA](https://snapeda.com) for initial 9 position JST SH footprints and models.
* [EasyEDA](https://easyeda.com) for the power switch, reset button, and 10 position JST SH footprints as well as some models.
* [Corne](https://github.com/foostan/crkbd) repository for the SK6812MINI-E footprint.
    * Fork from [petejohanson](https://github.com/petejohanson/crkbd/tree/board/corne-ultralight) for guide on nice!view pin connections.
* [Sofle](https://github.com/josefadamcik/SofleKeyboard) keyboard for rotary encoder and headphone jack footprints.
    * [Hayden Hu's PJ320A model](https://grabcad.com/library/pj320a-pj320d-3-5mm-jack-10) was used to show the headphone jack on the 3D viewer.
    * [Dmitry Levin's EC11 encoder models](https://grabcad.com/library/11mm-metal-shaft-rotary-encoders-tht-vertical-w-push-on-switch-1) was used to show the encoder on the 3D viewer.
* [keyboard_reversible.pretty](https://github.com/50an6xy06r6n/keyboard_reversible.pretty) for easy reverse footprints made for the Pro Micro.
* [Zack Freedman's MiRage Keyboard](https://github.com/ZackFreedman/MiRage) for Choc / MX footprints with modifications to include SK6812MINI-E within the footprint.
    * [Dennis Lee's Kailh 1350 socket model](https://grabcad.com/library/kailh-1350-socket-20) was used to show the switch socket on the 3D viewer.


In the libs folder, there may be other files regarding other footprints such as the EVQPUC02K. This was found on EasyEDA on early attempts to extract the footprints.
There is also the MSK-12C02 switch. This was found from [mzst's blog](https://mzstblog.blogspot.com/2016/01/msk-12c02-smd-slider-switch-spdt-eagle.html) website, which was a good reference for the switch, but I ended up using the symbol and combined with the other footprint found from EasyEDA. Archived here as well bvecause it is nice to have a backup of it.
