import pyautogui, time
time.sleep(5)
pyautogui.click()
distance = 800
while distance > 0:
    pyautogui.dragRel(distance, 0, duration=1)
    distance = distance - 50
    pyautogui.dragRel(0, distance, duration=2)
    pyautogui.dragRel(-distance, 0, duration=1)
    distance = distance - 50
    pyautogui.dragRel(0, -distance, duration=2)
