import pygetwindow as gw

class WindowGeometry:
    def __init__(self, x: int, y: int, width: int, height: int, app_name: str = None) -> None:
        if not WindowGeometry.is_valid_window(x, y, width, height):  # pragma: no cover
            raise Exception('Provided parameters cannot be negative or zero')
        self._x = x
        self._y = y
        self._width = width
        self._height = height
        self._app_name = app_name
        pass

    def is_valid_window(x: int, y: int, width: int, height: int) -> bool:
        return x >= 0 and y >= 0 and width >= 1 and height >= 1

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
        return f'x={str(self.x).ljust(10)}y={str(self.y).ljust(10)}width={str(self.width).ljust(10)}height={str(self.height).ljust(10)}{"app_name=" + self._app_name if self._app_name is not None else ""}'


def get_all_windows(with_geometry: bool = False) -> list[str]:
    windows = [window for window in gw.getAllTitles(
    ) if WindowGeometry.is_valid_window(*gw.getWindowGeometry(window))]

    if with_geometry:
        windows = [
            f"{WindowGeometry(*gw.getWindowGeometry(window), app_name=window)}" for window in windows]

    return sorted(windows)


def get_window_geometry(app_name: str | None, index: int | None) -> WindowGeometry:
    if app_name is None and index is None:
        raise Exception(
            'Please specify the name or the index of the application to take a screenshot of')

    selected_window = None
    windows = get_all_windows()

    if index is not None:
        if index >= len(windows) or index < 0:
            raise Exception(
                f'Index {index} is out of range. Max index is {len(windows) - 1}')

        selected_window = windows[index]
    else:
        windows = [app for app in windows if app_name.lower()
                   in app.lower()]

        if len(windows) == 0:
            raise Exception(f'"{app_name}" window not found')

        if len(windows) > 1:
            print_items(windows)
            index = input("Select the window index: ")
            selected_window = windows[int(index)]
        else:
            selected_window = windows[0]

    print(f'Found {selected_window} window')

    geometry = gw.getWindowGeometry(selected_window)
    return WindowGeometry(int(geometry[0]), int(geometry[1]), int(geometry[2]), int(geometry[3]), selected_window)


def print_items(items) -> None:
    [print(f"\t{i}) {item}") for i, item in enumerate(sorted(items))]
