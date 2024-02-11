/* Copyright 2020 Josef Adamcik
 * Modification for VIA support and RGB underglow by Jens Bonk-Wiltfang
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 2 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 */

#pragma once

/* By default left side is selected as master, 
see https://docs.qmk.fm/#/feature_split_keyboard?id=setting-handedness
for more options. */

#if defined(KEYBOARD_seismos)
// Add RGB underglow and top facing lighting
#    define WS2812_DI_PIN D3
#    define SERIAL_USART_FULL_DUPLEX
#    define SIDE_LEFT
#    if defined(SIDE_LEFT)
        #    define SERIAL_USART_TX_PIN F4
        #    define SERIAL_USART_RX_PIN F5
#    else
        #    define SERIAL_USART_TX_PIN F5
        #    define SERIAL_USART_RX_PIN F4
#    endif
// If your microcontroller supports it, you can detect the pin swap instead:
#    define SERIAL_USART_PIN_SWAP

#define BOOTMAGIC_LITE_ROW 0
#define BOOTMAGIC_LITE_COLUMN 0

//   Shift register for columns
#    define SHIFT_CS_PIN B6
#    define SHIFT_MOSI_PIN B2
#    define SHIFT_SCLK_PIN B1
#    define RGBLED_NUM 80
#    define RGBLED_SPLIT \
        { 40, 40 }
#    define EE_HANDS
#endif
