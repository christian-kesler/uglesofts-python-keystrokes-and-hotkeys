from pynput import keyboard
from pynput.keyboard import Controller, Key
import time

print("Hello.  I am your personal keystrokes and hotkeys assistant.  Below is a list of commands I currently support.")
print("0 + e + f | email_footer")
print("0 + m + f | email_footer")
print("0 + g + w | google_workspace")

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


def google_workspace():
	print("function <google_workspace> called")

	c.release('0')
	c.release('g')
	c.release('w')

	c.press(Key.backspace)
	c.release(Key.backspace)
	c.press(Key.backspace)
	c.release(Key.backspace)
	c.press(Key.backspace)
	c.release(Key.backspace)
	time.sleep(.1)

	c.press(Key.cmd_l)
	c.release(Key.cmd_l)
	time.sleep(1)
	c.type("google chrome")
	time.sleep(1)
	c.press(Key.enter)
	c.release(Key.enter)
	time.sleep(1)

	c.type("https://music.youtube.com/playlist?list=RDCLAK5uy_kb7EBi6y3GrtJri4_ZH56Ms786DFEimbM")
	c.press(Key.enter)
	c.release(Key.enter)
	time.sleep(8)

	c.press(Key.tab)
	c.release(Key.tab)
	time.sleep(1)

	c.press(Key.enter)
	c.release(Key.enter)
	time.sleep(4)

	c.press(Key.ctrl)
	c.press("t")
	c.release(Key.ctrl)
	c.release("t")
	time.sleep(1)

	c.type("https://drive.google.com")
	c.press(Key.enter)
	c.release(Key.enter)
	time.sleep(1)

	c.press(Key.ctrl)
	c.press("t")
	c.release(Key.ctrl)
	c.release("t")
	time.sleep(1)

	c.type("https://calendar.google.com")
	c.press(Key.enter)
	c.release(Key.enter)
	time.sleep(1)

	c.press(Key.ctrl)
	c.press("t")
	c.release(Key.ctrl)
	c.release("t")
	time.sleep(1)

	c.type("https://mail.google.com")
	c.press(Key.enter)
	c.release(Key.enter)
	time.sleep(1)

	print("function <google_workspace> completed")


with keyboard.GlobalHotKeys(
	{
		'0+e+f': email_footer,
		'0+m+f': email_footer,
		'0+g+w': google_workspace
	}
) as h:
	h.join()