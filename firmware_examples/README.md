# Firmware files for Seismos
If you are finished with your PCB, congratulations! The PCBs are quite a challenge to do; I would know doing the PCBs twice at the moment...

**NOTE**: As of now, since the shift register was introduced in v2.0.0, only QMK has it configured. I will get to KMK and ZMK later but for now, they serve as an okay example for the column and keycode layout.

At this point, you can now flash your firmware to your Seismos. Here, you can find two firmware files for Seismos:
* KMK
    * KMK requires the normal setup for installing into your microcontroller. If you have chosen to use RGB, you will also need to import the neopixel library from adafruit into the `lib` folder. If you don't need this, remove the RGB sections from `main.py`. After that, you should be good to go with a basic layout.
* ZMK
    * ZMK requires a compilation of the firmware. Here, files are provided for a nice!nano v2 with a nice!view display. Follow the initialization steps to setup ZMK. Then copy the folder inside the zmk folder into `app/boards/shields`. You can then compile with the following code. If you have a zmk-config folder, use the flag `-DZMK_CONFIG="<zmk-config folder>"`:
```bash
west build --pristine -d build/seismosL -b nice_nano_v2 -- -DSHIELD="seismos_left nice_view_adapter nice_view"
cp build/seismosL/zephyr/zmk.uf2 ./seismosL.uf2

west build --pristine -d build/seismosR -b nice_nano_v2 -- -DSHIELD="seismos_right nice_view_adapter nice_view"
cp build/seismosR/zephyr/zmk.uf2 ./seismosR.uf2
```
    * Unfortunately, I haven't gotten to compile this for the RP2040. If you happen to get that working, do a pull request and I can take a look.
* QMK
    * QMK firmware uses some code from Sofle's QMK codebase, especially the oled (untested)
    * The current QMK firmware uploaded uses RP2040 conversion for the RP2040 board I have. If you have a pro micro, you can disable this conversion in the `rules.mk` file.