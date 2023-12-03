from src.application import get_window_geometry, get_all_windows
from src.screenshot import get_screenshot
from argparse import ArgumentParser
import os

def get_arguments() -> ArgumentParser: # pragma: no cover
    wh_message = 'Expected {0}. If not specified, use the current {0}'

    parser = ArgumentParser()
    parser.add_argument('-l', '--list', dest="list", action='store_true', help='List all active windows')
    parser.add_argument('-la', '--list-all', dest="list_all", action='store_true',
                        help='List all active windows with their geometries')
    parser.add_argument('-n', '--name', dest="name", type=str, help='Name of the application to take a screenshot of')
    parser.add_argument('-i', '--index', dest="index", type=int,
                        help='Index of the application to take a screenshot of', default=None)
    parser.add_argument('-d', '--destination', dest="destination", type=str, help='Destination folder', default='screenshots')
    parser.add_argument('-ew', '--expected-width', dest="expected_width", type=int, help=wh_message.format('width'), default=None)
    parser.add_argument('-eh', '--expected-height', dest="expected_height", type=int, help=wh_message.format('height'), default=None)
    parser.add_argument('-r', '--repeat', dest="repeat", type=int, help="How many screenshots to take. Go ahead by pressing 'enter' key", default=1)

    options = parser.parse_args()

    if options.list or options.list_all:
        return options

    if options.name is None and options.index is None:
        parser.error(
            'Please specify the name or the index of the application to take a screenshot of')

    if (options.expected_width is not None and options.expected_width < 1) or (options.expected_height is not None and options.expected_height < 1):
        parser.error('Provided parameters cannot be negative or zero')

    return options

if __name__ == '__main__': # pragma: no cover
    try:
        options = get_arguments()
        if options.list or options.list_all:
            [print(f"\t{i}) {window}")
             for i, window in enumerate(sorted(get_all_windows(options.list_all)))]
            exit()

        index = options.repeat if options.repeat > 0 else 1

        while index > 0:
            if index < options.repeat:
                input("Press 'enter' to take the next screenshot...")

            geometry = get_window_geometry(options.name, options.index)
            screenshot_path = get_screenshot(
                geometry.x,
                geometry.y,
                geometry.width,
                geometry.height,
                destination=options.destination,
                name=options.name,
                expected_width=options.expected_width,
                expected_height=options.expected_height)

            index -= 1

            print(
                f"\033[92mScreenshot taken successfully:\033[0m\n{os.path.abspath(screenshot_path)}")
    except Exception as e:
        print(f"\033[91m{e}\033[0m")
        exit(1)


