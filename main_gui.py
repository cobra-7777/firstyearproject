from machine import Pin, PWM
from gpio_lcd import GpioLcd
import time
import neopixel
import urandom
import utime
import text_to_docfile as ttd
import speech_to_text as stt
import gpt_api as gpt
import audio_recording as ar
import text_to_speech as tts


# Create the LCD object
lcd = GpioLcd(rs_pin=Pin(26),
              enable_pin=Pin(27),
              d4_pin=Pin(14),
              d5_pin=Pin(12),
              d6_pin=Pin(13),
              d7_pin=Pin(15),
              num_lines=2, num_columns=16)

# Initialize the buttons with pull-up resistors
up_button = Pin(4, Pin.IN, Pin.PULL_UP)
select_button = Pin(16, Pin.IN, Pin.PULL_UP)
down_button = Pin(17, Pin.IN, Pin.PULL_UP)

menu_items = ['Record', 'Ask', 'Saved REC', 'Settings']
settings_submenus = ['Volume', 'Brightness', 'Contrast', 'Connection']
current_selection = 0
settings_submenu_selection = 0
menu_top = 0  # Top of the displayed menu
in_settings_submenu = False
is_recording = False
is_listening = False
is_select_button_pressed = False

# Initialize the Neopixel LEDs
neopixel_pin = Pin(25, Pin.OUT)
neopixel_strip = neopixel.NeoPixel(neopixel_pin, 1)

# Add new Neopixel strip connected to pin 33
neopixel_strip_3 = neopixel.NeoPixel(Pin(33, Pin.OUT), 3)

# Initialize the speakers
left_speaker_pin = PWM(Pin(5), freq=440, duty=0)  # Left speaker
right_speaker_pin = PWM(Pin(18), freq=440, duty=0)  # Right speaker

def play_tone(frequency, duration):
    left_speaker_pin.freq(frequency)
    right_speaker_pin.freq(frequency)
    left_speaker_pin.duty(200)
    right_speaker_pin.duty(200)
    time.sleep(duration)
    left_speaker_pin.duty(0)
    right_speaker_pin.duty(0)

def display_menu():
    lcd.clear()
    if in_settings_submenu:
        # Display settings submenus
        for i in range(2):  # Only two items can be displayed at once
            item_index = settings_submenu_selection + i
            if item_index < len(settings_submenus):
                item = settings_submenus[item_index]
                if item_index == settings_submenu_selection:
                    # Highlight the current selection
                    lcd.move_to(0, i)
                    lcd.putstr("> " + item)
                else:
                    lcd.move_to(0, i)
                    lcd.putstr("  " + item)
    else:
        # Display main menu
        for i in range(2):  # Only two items can be displayed at once
            item_index = menu_top + i
            if item_index < len(menu_items):
                item = menu_items[item_index]
                if item_index == current_selection:
                    # Highlight the current selection
                    lcd.move_to(0, i)
                    lcd.putstr("> " + item)
                else:
                    lcd.move_to(0, i)
                    lcd.putstr("  " + item)
    # turn off the neopixels when entering the menu
    for i in range(neopixel_strip_3.n):
        neopixel_strip_3[i] = (0, 0, 0)

    neopixel_strip_3.write()
    left_speaker_pin.duty(0)  # Make sure to stop the sound
    right_speaker_pin.duty(0)  # Make sure to stop the sound

def toggle_recording():
    global is_recording
    is_recording = not is_recording
    if is_recording:
        lcd.clear()
        lcd.putstr("Recording...")
        neopixel_strip[0] = (255, 0, 0)  # Set Neopixel color to red
        neopixel_strip.write()
    else:
        lcd.clear()
        display_menu()
        neopixel_strip[0] = (0, 0, 0)  # Turn off Neopixel
        neopixel_strip.write()

def toggle_listening():
    global is_listening
    is_listening = not is_listening
    if is_listening:
        lcd.clear()
        lcd.putstr("Listening...")
        neopixel_strip[0] = (0, 255, 0)  # Set Neopixel color to green
        neopixel_strip.write()
    else:
        lcd.clear()
        display_menu()
        neopixel_strip[0] = (0, 0, 0)  # Turn off Neopixel
        neopixel_strip.write()

# Display welcome message
lcd.clear()
lcd.move_to(0, 0)
lcd.putstr("   Welcome :-)")
sound_frequency = 440  # set sound frequency

play_tone(sound_frequency, 1)  # Play sound for 1 second

for _ in range(3):  # pulses for approximately 3 seconds
    r, g, b = [urandom.randint(0, 255) for _ in range(3)]
    for i in range(0, 255, 5):
        for j in range(neopixel_strip_3.n):
            neopixel_strip_3[j] = (int(r * i / 255), int(g * i / 255), int(b * i / 255))
        neopixel_strip_3.write()
        time.sleep(0.01)
    for i in range(255, 0, -5):
        for j in range(neopixel_strip_3.n):
            neopixel_strip_3[j] = (int(r * i / 255), int(g * i / 255), int(b * i / 255))
        neopixel_strip_3.write()
        time.sleep(0.01)

display_menu()

while True:
    if not up_button.value():
        if in_settings_submenu:
            if settings_submenu_selection > 0:
                settings_submenu_selection -= 1
        elif current_selection > 0:
            current_selection -= 1
            if current_selection < menu_top:
                menu_top -= 1
        display_menu()
        time.sleep(0.2)

    if not down_button.value():
        if in_settings_submenu:
            if settings_submenu_selection < len(settings_submenus) - 1:
                settings_submenu_selection += 1
        elif current_selection < len(menu_items) - 1:
            current_selection += 1
            if current_selection >= menu_top + 2:
                menu_top += 1
        display_menu()
        time.sleep(0.2)

    if not select_button.value():
        select_button_press_time = utime.ticks_ms()
        while not select_button.value():
            pass  # Wait for select button to be released
        press_duration = utime.ticks_diff(utime.ticks_ms(), select_button_press_time)

        if press_duration > 2000:  # More than 2 seconds
            if in_settings_submenu:
                # Back to main menu
                in_settings_submenu = False
                settings_submenu_selection = 0
            else:
                # Go to settings submenu
                in_settings_submenu = True
            display_menu()

        else:  # Short press
            if in_settings_submenu:
                # Handle selection in settings submenu
                print(f'Settings submenu selected: {settings_submenus[settings_submenu_selection]}')
            else:
                # Handle selection in main menu
                if menu_items[current_selection] == 'Record':
                    toggle_recording()
                elif menu_items[current_selection] == 'Ask':
                    toggle_listening()
                elif menu_items[current_selection] == 'Saved REC':
                    lcd.clear()
                    lcd.putstr('Playing REC...')
                    play_tone(440, 1)
                    lcd.clear()
                    display_menu()
                elif menu_items[current_selection] == 'Settings':
                    in_settings_submenu = True
                    display_menu()

        time.sleep(0.2)