from pynput import keyboard
from pynput.keyboard import Controller, Key
import time

print("keystrokes file ready for execution")

c = Controller()

def email_footer():
	print("email footer function called")

	c.release('0')
	c.release('e')
	c.release('m')
	c.release('f')

	c.press(Key.backspace)
	c.release(Key.backspace)
	c.press(Key.backspace)
	c.release(Key.backspace)
	c.press(Key.backspace)
	c.release(Key.backspace)
	time.sleep(.1)

	c.type('Respectfully,')
	time.sleep(.1)
	c.press(Key.enter)
	c.release(Key.enter)
	time.sleep(.1)
	c.type('Christian Kesler')
	time.sleep(.1)

	print("email footer function completed")



with keyboard.GlobalHotKeys(
	{
		'0+e+f': email_footer,
		'0+m+f': email_footer
	}
) as h:
	h.join()