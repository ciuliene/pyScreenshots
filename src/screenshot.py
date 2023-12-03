import pyautogui
import os

def get_screenshot(x: int, y: int, width: int, height: int, destination: str = None, name: str = None, expected_width: int = None, expected_height: int = None) -> str:
    screenshot = pyautogui.screenshot(region=(x, y, width, height))

    w_ratio = ((expected_width if expected_width is not None else width) / width)
    h_ratio = ((expected_height if expected_height is not None else height) / height)

    if w_ratio == 1 and not h_ratio == 1:
        w_ratio = h_ratio
    elif h_ratio == 1 and not w_ratio == 1:
        h_ratio = w_ratio

    r_width = int(width * w_ratio)
    r_height = int(height * h_ratio)
    screenshot = screenshot.resize([r_width, r_height])
    if destination is None:
        destination = 'screenshots'
    
    if not os.path.exists(destination):
        os.makedirs(destination)

    if name is None:
        name = 'screenshot'

    i = 0
    while True:
        i += 1
        file_name = f'{name}_{r_width}x{r_height}_{i}.png'
        if not os.path.exists(f'{destination}/{file_name}'):
            break

    screenshot.save(f'{destination}/{file_name}')

    return f'{destination}/{file_name}'
