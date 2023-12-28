import board
from kmk.kmk_keyboard import KMKKeyboard as _KMKKeyboard
from kmk.scanners import DiodeOrientation
from kmk.modules.split import Split, SplitType
from kmk.scanners.keypad import MatrixScanner
from kmk.scanners.encoder import RotaryioEncoder
from kmk.extensions.rgb import AnimationModes

led_positions = [
    30, 24, 18, 12, 6,  0,
    31, 25, 19, 13, 7,  1,
    32, 26, 20, 14, 8,  2,
    33, 27, 21, 15, 9,  3,
    34, 28, 22, 16, 10, 4,
    35, 29, 23, 17, 11, 5,  36, 37, 38, 39
]
led_positions_half = [
    30, 24, 18, 12, 6,  0,
    31, 25, 19, 13, 7,  1,
    32, 26, 20, 14, 8,  2,
    33, 27, 21, 15, 9,  3,
    34, 28, 22, 16, 10, 4,
    35, 29, 23, 17, 11, 5,  36, 37, 38, 39
]

rgb_data = [
    [0, 0, 255], [0, 191, 255], [0, 255, 128], [63, 255, 0], [254, 255, 0], [251, 64, 0],
    [0, 0, 255], [0, 191, 255], [0, 255, 128], [63, 255, 0], [254, 255, 0], [251, 64, 0],
    [0, 0, 255], [0, 191, 255], [0, 255, 128], [63, 255, 0], [254, 255, 0], [251, 64, 0],
    [0, 0, 255], [0, 191, 255], [0, 255, 128], [63, 255, 0], [254, 255, 0], [251, 64, 0],
    [0, 0, 255], [0, 191, 255], [0, 255, 128], [63, 255, 0], [254, 255, 0], [251, 64, 0], [247, 0, 122], [188, 0, 249], [188, 0, 249], [247, 0, 122],
]
rgb_data_half = [
    [0, 0, 255], [0, 191, 255], [0, 255, 128], [63, 255, 0], [254, 255, 0], [251, 64, 0],
    [0, 0, 255], [0, 191, 255], [0, 255, 128], [63, 255, 0], [254, 255, 0], [251, 64, 0],
    [0, 0, 255], [0, 191, 255], [0, 255, 128], [63, 255, 0], [254, 255, 0], [251, 64, 0],
    [0, 0, 255], [0, 191, 255], [0, 255, 128], [63, 255, 0], [254, 255, 0], [251, 64, 0],
    [0, 0, 255], [0, 191, 255], [0, 255, 128], [63, 255, 0], [254, 255, 0], [251, 64, 0], [247, 0, 122], [188, 0, 249], [188, 0, 249], [247, 0, 122],
]

# Creates a tuple containing both LED position and RGB data
pos_rgb_half = [(x, y) for x, y in zip(led_positions_half, rgb_data_half)]

class KMKCust(_KMKKeyboard):
    def __init__(
        self,
        use_oled=False,
        rgb_type="basic_rgb",
    ):
        # create and register the scanner(s)
        self.matrix = [
            MatrixScanner(
                # required arguments:
                column_pins=self.col_pins,
                row_pins=self.row_pins,
                # optional arguments with defaults:
                columns_to_anodes=self.diode_orientation,
                interval=0.01,  # Debounce time in floating point seconds
                max_events=64,
            ),
            RotaryioEncoder(
                pin_a=self.encoder_a,
                pin_b=self.encoder_b,
                divisor=2,
            ),
        ]

        # Split code:
        split = Split(
            split_flip=True,  # If both halves are the same, but flipped, set this True
            split_side=None,  # Sets if this is to SplitSide.LEFT or SplitSide.RIGHT, or use EE hands
            split_type=SplitType.UART,  # Defaults to UART
            uart_interval=20,  # Sets the uarts delay. Lower numbers draw more power
            data_pin=self.SCL,  # The primary data pin to talk to the secondary device with
            data_pin2=self.SDA,  # Second uart pin to allow 2 way communication
            use_pio=True,  # Use RP2040 PIO implementation of UART. Required if you want to use other pins than RX/TX
        )
        self.modules.append(split)

        self.setup_oled(use_oled)

    col_pins = (board.GP21, board.GP23, board.GP20, board.GP22, board.GP26, board.GP27, board.GP9)
    row_pins = (board.GP4, board.GP5, board.GP6, board.GP7, board.GP8)
    diode_orientation = DiodeOrientation.COL2ROW
    encoder_a = board.GP28
    encoder_b = board.GP29
    SCL=board.SCL
    SDA=board.SDA
    rgb_pixel_pin = board.GP0

    # NOQA
    # flake8: noqa
    # fmt: off
    coord_mapping = [
         0,  1,  2,  3,  4,  5,  6,     43, 42, 41, 40, 39, 38, 37,
         7,  8,  9, 10, 11, 12, 13,     50, 49, 48, 47, 46, 45, 44,
        14, 15, 16, 17, 18, 19, 20,     57, 56, 55, 54, 53, 52, 51,
        21, 22, 23, 24, 25, 26, 27,     64, 63, 62, 61, 60, 59, 58,
        28, 29, 30, 31, 32, 33, 34,     71, 70, 69, 68, 67, 66, 65,

        35, 36,
        72, 73,
    ]
    # fmt: on

    # OLED Code:
    def setup_oled(self, use_oled):
        if use_oled == True:
            from kmk.extensions.peg_oled_Display import (
                Oled,
                OledDisplayMode,
                OledReactionType,
                OledData,
            )

            # --8<-- [start:oled]
            oled_ext = Oled(
                OledData(
                    corner_one={
                        0: OledReactionType.STATIC,
                        1: ["Layer"],
                    },
                    corner_two={
                        0: OledReactionType.LAYER,
                        1: ["0", "1", "2"],
                    },
                    corner_three={
                        0: OledReactionType.LAYER,
                        1: ["BASE", "RAISE", "LOWER"],
                    },
                    corner_four={
                        0: OledReactionType.LAYER,
                        1: ["qwerty", "nums", "sym"],
                    },
                ),
                toDisplay=OledDisplayMode.TXT,
                flip=True,
                # oHeight=64,
            )
            # --8<-- [end:oled]
            self.extensions.append(oled_ext)

    # Setup for peg_rgb or basic_rgb:
    def setup_rgb(self, rgb_type):
        if rgb_type == "peg_rgb":

            self.brightness_limit = 0.2
            # Exctract and trim the position data from the pos_rgb tuple according to a KLOR variant:
            self.led_key_pos = pos_rgb
            # Return the number of items in the exctracted and trimmed data from above:
            self.num_pixels = len(self.led_key_pos)
            # Pass the specific [R, G, B] data for a KLOR variant via 'led_display' into peg_rgb():
            self.peg_rgb(pos_rgb)

        if rgb_type == "basic_rgb":
            # In basic RGB implementation you only pass the LED count per side not the total of both sides:
            half_pos = len(pos_rgb_half)
            # Pass the number of LEDs of one keyboard half via 'half_pos' into basic_rgb():
            self.basic_rgb(pixels=(half_pos))

    # Basic RGB code:
    def basic_rgb(self, pixels):
        from kmk.extensions.RGB import RGB

        # --8<-- [start:rgb]
        rgb = RGB(
            pixel_pin=board.GP0,
            num_pixels=40,
            val_default=50,
            hue_step=5,
            sat_step=5,
            val_step=5,
            animation_speed=5,
            animation_mode=AnimationModes.SWIRL,
            reverse_animation=False,
            refresh_rate=60,
        )
        # --8<-- [end:rgb]
        self.extensions.append(rgb)

    # PEG_RGB code (per key RGB):
    def peg_rgb(self, led_display):
        from kmk.extensions.peg_rgb_matrix import Rgb_matrix, Rgb_matrix_data

        rgb_ext = Rgb_matrix(
            ledDisplay=led_display,
            split=True,
            rightSide=False,
            disable_auto_write=True,
        )
        self.extensions.append(rgb_ext)