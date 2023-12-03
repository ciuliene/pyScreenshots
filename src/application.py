import pygetwindow as gw

class WindowGeometry:
    def __init__(self, x: int, y:int, width:int, height: int) -> None:
        self._x = x
        self._y = y
        self._width = width
        self._height = height
        pass

    @property
    def x(self) -> int:
        return self._x
    
    @property
    def y(self) -> int:
        return self._y
    
    @property
    def width(self) -> int:
        return self._width
    
    @property
    def height(self) -> int:
        return self._height
    
    def __str__(self) -> str:
        return f'WindowGeometry(x={self.x}, y={self.y}, width={self.width}, height={self.height})'

def get_all_windows() -> list[str]:
    return gw.getAllTitles()

def get_window_geometry(app_name: str) -> WindowGeometry:
    windows = [app for app in gw.getAllTitles() if app_name.lower() in app.lower()]

    if len(windows) == 0:
        raise Exception(f'{app_name} window not found')

    quicktime = windows[0]

    geometry = gw.getWindowGeometry(quicktime)

    return WindowGeometry(int(geometry[0]), int(geometry[1]), int(geometry[2]), int(geometry[3]))

            