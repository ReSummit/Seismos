print("Starting")

import board

from kmk.kmk_keyboard import KMKKeyboard
from kb import KMKCust
from kmk.keys import KC

from kmk.handlers.sequences import simple_key_sequence

from kmk.extensions.RGB import RGB
from kmk.extensions.rgb import AnimationModes
from kmk.extensions.media_keys import MediaKeys

from kmk.modules.layers import Layers

# I2C Pins
SCL=board.SCL
SDA=board.SDA

keyboard = KMKCust()
layers = Layers()
media_handler = MediaKeys()

keyboard.modules.append(Layers())
keyboard.extensions.append(MediaKeys())
 
# Key aliases
xxxxx = KC.NO
_______ = KC.TRNS

# Macro definitions
RAISE = KC.MO(1)
LOWER = KC.MO(2)
CTRA = KC.CTRL(KC.A)
CTRZ = KC.CTRL(KC.Z)
CTRX = KC.CTRL(KC.X)
CTRC = KC.CTRL(KC.C)
CTRV = KC.CTRL(KC.V)
VIMQA = simple_key_sequence((KC.COLN, KC.Q, KC.A, KC.ENT))
VIMRE = simple_key_sequence((KC.COLN, KC.PERC, KC.S, KC.PIPE, KC.PIPE, KC.PIPE, KC.G))

keyboard.keymap = [
    [
        KC.ESC,     KC.N1,      KC.N2,      KC.N3,      KC.N4,  KC.N5,      KC.D,                       KC.A,              KC.N6,      KC.N7,      KC.N8,      KC.N9,      KC.N0,      KC.BSPC,
        KC.GRV,     KC.Q,       KC.W,       KC.E,       KC.R,   KC.T,       KC.F,                       KC.B,              KC.Y,       KC.U,       KC.I,       KC.O,       KC.P,       KC.BSLS,
        KC.TAB,     KC.A,       KC.S,       KC.D,       KC.F,   KC.G,       KC.D,                       KC.C,              KC.H,       KC.J,       KC.K,       KC.L,       KC.SCLN,    KC.QUOT,
        KC.LSFT,    KC.Z,       KC.X,       KC.C,       KC.V,   KC.B,       KC.F,                       KC.D,              KC.N,       KC.M,       KC.COMM,    KC.DOT,     KC.SLSH,    KC.ENTER,
        KC.LCTL,    KC.LGUI,    KC.LALT,    KC.APP,     LOWER,  KC.SPC,     KC.AUDIO_MUTE,              KC.AUDIO_MUTE,     KC.SPC,     RAISE,      KC.LEFT,    KC.DOWN,    KC.UP,      KC.RGHT,

        # Encoders
        KC.AUDIO_VOL_UP,      #Left side clockwise
        KC.AUDIO_VOL_DOWN,    #Left side counterclockwise
        KC.AUDIO_VOL_UP,  #Right side clockwise
        KC.AUDIO_VOL_DOWN,  #Right side counterclockwise
    ],
    [
        _______,   KC.F1,   KC.F2,   KC.F3,   KC.F4,   KC.F5, _______,          _______,   KC.F6,   KC.F7,   KC.F8,   KC.F9,  KC.F10,   KC.DEL,
        _______,  KC.F11,  KC.F12, _______, _______, _______, _______,          _______, _______, _______, _______, _______, _______,  KC.PSCR,
        _______, _______, _______, _______, _______, _______, _______,          _______, _______, _______, _______, _______, _______,  _______,
        _______, _______, _______, _______, _______, _______, _______,          _______, _______, _______, _______, _______, _______,  _______,
        _______, _______, _______, _______, _______, _______, _______,          _______, _______, _______, _______, _______, _______,  _______,

        # Encoders
        KC.AUDIO_VOL_UP,      #Left side clockwise
        KC.AUDIO_VOL_DOWN,    #Left side counterclockwise
        KC.AUDIO_VOL_UP,  #Right side clockwise
        KC.AUDIO_VOL_DOWN,  #Right side counterclockwise
    ],
    [
        _______, _______, _______, _______,  _______,  _______, _______,          _______, _______, _______,  _______,  _______,  _______, _______,
        _______,   VIMQA, _______, _______,    VIMRE,  _______, _______,          _______, _______, _______,  _______,  _______,  _______, _______,
        _______, _______, _______, KC.LPRN,  KC.LBRC,  KC.MINS, _______,          _______,  KC.EQL, KC.RBRC,  KC.RPRN,  _______,  _______, _______,
        _______,    CTRZ,    CTRX,    CTRC,     CTRV,  _______, _______,          _______, _______, _______,  _______,  _______,  _______, _______,
        _______, _______, _______, _______,  _______,  _______, _______,          _______, _______, _______,  KC.HOME,  KC.PGDN,  KC.PGUP,  KC.END,

        # Encoders
        KC.AUDIO_VOL_UP,      #Left side clockwise
        KC.AUDIO_VOL_DOWN,    #Left side counterclockwise
        KC.AUDIO_VOL_UP,  #Right side clockwise
        KC.AUDIO_VOL_DOWN,  #Right side counterclockwise
    ],
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