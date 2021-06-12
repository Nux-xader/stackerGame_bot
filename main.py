import pyautogui, time

script = """# https://github.com/nux-xader
import pyautogui, time
def main():
	num = 0
	while True:
		num+=1
		time.sleep(1.6)
		print(str(pyautogui.position())+' [1.6 s] >>'+str(num)+' ['+str(time.time())+']')
		pyautogui.click(xx, yy)
main()
"""

def preperate():
	try:
		while True:
			position = str(pyautogui.position()).replace('Point(x=', '').replace(' y=', '').replace(')', '').split(',')
			print(pyautogui.position())
	except KeyboardInterrupt:
		open('main.py', 'w').write(script.replace('xx', position[0]).replace('yy', position[1]))
		print('Run script again')
		exit()


input('please enter, and move your cursor at target\nthen press ctrl+c')
preperate()