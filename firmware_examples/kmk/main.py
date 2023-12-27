print("Starting")

import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation

from kmk.extensions.RGB import RGB
from kmk.extensions.rgb import AnimationModes
from kmk.extensions.media_keys import MediaKeys

from kmk.modules.layers import Layers
from kmk.modules.encoder import EncoderHandler
from kmk.modules.split import Split, SplitSide

# I2C Pins
SCL=board.SCL
SDA=board.SDA

keyboard = KMKKeyboard()
layers = Layers()
split = Split(data_pin=SCL,
              data_pin2=SDA,
              use_pio=True
              )
encoder_handler = EncoderHandler()
media_handler = MediaKeys()
keyboard.modules = [layers, encoder_handler, split]

keyboard.debug_enabled = True

#keyboard.col_pins = (board.GP27, board.GP26, board.GP22, board.GP20, board.GP23, board.GP21, board.GP9)
keyboard.col_pins = (board.GP21, board.GP23, board.GP20, board.GP22, board.GP26, board.GP27, board.GP9)
keyboard.row_pins = (board.GP4, board.GP5, board.GP6, board.GP7, board.GP8)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

# Encoder
encoder_handler.pins = (
    # regular direction encoder and a button
    (board.GP29, board.GP28, None, True) # encoder #1 
)
encoder_handler.map = [ (( KC.A, KC.B ),), ]

# if split.split_side == SplitSide.LEFT:
#     keyboard.keymap = [
#         [
#             KC.ESC,     KC.N1,      KC.N2,      KC.N3,      KC.N4,  KC.N5,      KC.NO,        
#             KC.GRV,     KC.Q,       KC.W,       KC.E,       KC.R,   KC.T,       KC.NO,        
#             KC.TAB,     KC.A,       KC.S,       KC.D,       KC.F,   KC.G,       KC.NO,        
#             KC.LSFT,    KC.Z,       KC.X,       KC.C,       KC.V,   KC.B,       KC.NO,        
#             KC.LCTL,    KC.LGUI,    KC.LALT,    KC.APP,     KC.NO,  KC.SPC,     KC.AUDIO_MUTE,
#         ]
#     ]
# else:
#     keyboard.keymap = [
#         [
#             KC.NO,              KC.N6,      KC.N7,      KC.N8,      KC.N9,       KC.N0,      KC.BSPC,
#             KC.NO,              KC.Y,       KC.U,       KC.I,       KC.O,       KC.P,       KC.BSLS,
#             KC.NO,              KC.H,       KC.J,       KC.K,       KC.L,       KC.SCLN,    KC.QUOT,
#             KC.NO,              KC.N,       KC.M,       KC.COMM,    KC.DOT,     KC.SLSH,    KC.ENTER,
#             KC.AUDIO_MUTE,      KC.SPC,     KC.NO,      KC.LEFT,    KC.DOWN,    KC.UP,      KC.RGHT,
#         ]
#     ]
 
keyboard.keymap = [
    [
        KC.ESC,     KC.N1,      KC.N2,      KC.N3,      KC.N4,  KC.N5,      KC.D,               KC.K,              KC.N6,      KC.N7,      KC.N8,      KC.N9,       KC.N0,      KC.BSPC,
        KC.GRV,     KC.Q,       KC.W,       KC.E,       KC.R,   KC.T,       KC.F,               KC.J,              KC.Y,       KC.U,       KC.I,       KC.O,       KC.P,       KC.BSLS,
        KC.TAB,     KC.A,       KC.S,       KC.D,       KC.F,   KC.G,       KC.D,               KC.K,              KC.H,       KC.J,       KC.K,       KC.L,       KC.SCLN,    KC.QUOT,
        KC.LSFT,    KC.Z,       KC.X,       KC.C,       KC.V,   KC.B,       KC.F,               KC.J,              KC.N,       KC.M,       KC.COMM,    KC.DOT,     KC.SLSH,    KC.ENTER,
        KC.LCTL,    KC.LGUI,    KC.LALT,    KC.APP,     KC.NO,  KC.SPC,     KC.AUDIO_MUTE,      KC.AUDIO_MUTE,      KC.SPC,     KC.NO,      KC.LEFT,    KC.DOWN,    KC.UP,      KC.RGHT,
    ]
]

rgb = RGB(
            pixel_pin=board.GP0,
            num_pixels=40,
            val_default=10,
            hue_step=5,
            sat_step=5,
            val_step=5,
            animation_speed=5,
            animation_mode=AnimationModes.SWIRL,
            reverse_animation=False,
            refresh_rate=60,
)

keyboard.extensions.append(rgb)
keyboard.extensions.append(media_handler)

if __name__ == '__main__':
    keyboard.go()