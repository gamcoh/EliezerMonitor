from pynput import keyboard
import sqlite3

keys_pressed: list = ['begin']

def insert_keys() -> None:
	conn = sqlite3.connect('database/eliezermonitor.db')
	print('-' * 100)
	print('Saving in db')
	with conn:
		for key in keys_pressed:
			conn.execute('''insert into keys(date, key) values(CURRENT_TIMESTAMP, ?)''', [ str(key) ])


def on_press(key) -> None:
	# stop listener
	if key == keyboard.Key.ctrl and keys_pressed[-1] == keyboard.Key.esc:
		print('*' * 100)
		print('closed')
		return False

	if len(keys_pressed) >= 1_000:
		insert_keys()
		keys_pressed.clear()
	keys_pressed.append(key)


with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
