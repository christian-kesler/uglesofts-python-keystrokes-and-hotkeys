from pynput import keyboard
from pynput.keyboard import Controller, Key
import time
from plyer import notification
import string
from random import randrange

print("Hello.  I am your personal keystrokes and hotkeys assistant.  Below is a list of commands I currently support.")
print("0 + e + f | email_footer")
print("0 + m + f | email_footer")
print("0 + g + w | google_workspace")
print("0 + g + p | generate_password")

def notif_end(function_name):
	notification.notify(
		title = "Keystrokes Program",
		message = "The " + function_name + " function has been completed.",
		app_icon = "robot.ico",
		timeout = 1
	)

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

	notif_end("email_footer")

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

	notif_end("google_workspace")

	print("function <google_workspace> completed")


def generate_password():
	print("function <generate_password> called")

	password_raw = ""
	password_shuffled = ""

	digits = "0123456789"

	characters = string.ascii_lowercase + string.ascii_uppercase + string.punctuation + digits

	password_raw = string.ascii_lowercase[randrange(len(string.ascii_lowercase))] + string.ascii_uppercase[randrange(len(string.ascii_uppercase))] + string.punctuation[randrange(len(string.punctuation))]	+ digits[randrange(len(digits))]

	for x in range(12):
		password_raw = password_raw + characters[randrange(len(characters))]

	for x in range(len(password_raw)):
		index = randrange(len(password_raw))

		password_shuffled = password_shuffled + password_raw[index]
		password_raw = password_raw[0:index] + password_raw[(index+1):]

	bar = ""
	for x in range(32):
		bar = bar + "="

	print(bar)
	print(password_shuffled)
	print(bar)

	notif_end("generate_password")

	print("function <generate_password> completed")


with keyboard.GlobalHotKeys(
	{
		'0+e+f': email_footer,
		'0+m+f': email_footer,
		'0+g+w': google_workspace,
		'0+g+p': generate_password
	}
) as h:
	h.join()