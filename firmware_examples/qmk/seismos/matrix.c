#include "quantum.h"

/***
 * Matrix code for shift register column output
 * 
 * You need to set 3 pins for column output: 
 * SHIFT_CS_PIN, SHIFT_MOSI_PIN, and SHIFT_SCLK_PIN
*/

static const pin_t row_pins[MATRIX_ROWS] = MATRIX_ROW_PINS;

# if (!defined(SHIFT_CS_PIN) || !defined(SHIFT_MOSI_PIN) || !defined(SHIFT_SCLK_PIN))
# error "You must define SHIFT_CS_PIN, SHIFT_MOSI_PIN, and SHIFT_SCLK_PIN"
# endif

int col_order[] = { 5, 4, 3, 2, 1, 0, 6 };

void pulsePin(uint8_t pin) {
    writePinHigh(pin);
    matrix_io_delay();
    writePinLow(pin);
}

void scan_reset_reg(uint8_t empty) {
    // Sets register latch to 01000000

    // Shift 1 into 2nd slot of shift register
    matrix_io_delay();
    writePinHigh(SHIFT_MOSI_PIN);
    matrix_io_delay();
    pulsePin(SHIFT_SCLK_PIN);
    writePinLow(SHIFT_MOSI_PIN);
    matrix_io_delay();
    pulsePin(SHIFT_SCLK_PIN);

    // Latch the current column (this is CS)
    matrix_io_delay();
    pulsePin(SHIFT_CS_PIN);
}

void matrix_init_custom(void) {
    // Set the pins as output
    writePinLow(SHIFT_CS_PIN);
    setPinOutput(SHIFT_CS_PIN);

    writePinLow(SHIFT_MOSI_PIN);
    setPinOutput(SHIFT_MOSI_PIN);

    writePinLow(SHIFT_SCLK_PIN);
    setPinOutput(SHIFT_SCLK_PIN);

    // Clear shift register
    for (uint8_t r = 0; r < 8; ++r) {
        matrix_io_delay();
        pulsePin(SHIFT_SCLK_PIN);
    }

    // Latch the current column (this is CS)
    matrix_io_delay();
    pulsePin(SHIFT_CS_PIN);
}

bool matrix_scan_custom(matrix_row_t current_matrix[]) {
    bool matrix_has_changed = false;

    // Clear shift register
    writePinLow(SHIFT_MOSI_PIN);
    for (uint8_t r = 0; r < 8; ++r) {
        matrix_io_delay();
        pulsePin(SHIFT_SCLK_PIN);
    }
    matrix_io_delay();
    pulsePin(SHIFT_CS_PIN);

    scan_reset_reg(0);

    // Loop per row
    for (uint8_t row = 0; row < MATRIX_ROWS; row++) {
        // Read the current row
        matrix_row_t new_row = 0;

        // Cycle through each column
        for (uint8_t col = 0; col <= MATRIX_COLS; col++) {
            matrix_io_delay();
            new_row |= readPin(row_pins[row]) ? (1 << col_order[col]) : 0;

            // Continue to shift to next column
            matrix_io_delay();
            pulsePin(SHIFT_SCLK_PIN);
            matrix_io_delay();
            pulsePin(SHIFT_CS_PIN);
        }
        scan_reset_reg(0);

        // Check if the current row has changed
        if (current_matrix[row] != new_row) {
            matrix_has_changed = true;
            current_matrix[row] = new_row;
            // uprintf("KL: row: %2u, new_row: 0x%04X, xMATRIX_COLS: %2u\n", row, new_row, MATRIX_COLS);
        }
    }

    return matrix_has_changed;
}