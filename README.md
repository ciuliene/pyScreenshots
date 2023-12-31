# PyScreenshots

[![Test](https://github.com/ciuliene/pyScreenshots/actions/workflows/app_test.yml/badge.svg)](https://github.com/ciuliene/pyScreenshots/actions/workflows/app_test.yml) [![codecov](https://codecov.io/gh/ciuliene/pyScreenshots/graph/badge.svg?token=177KCQUNLD)](https://codecov.io/gh/ciuliene/pyScreenshots)

This script allows you to take screenshots of your active applications and save them in a folder.

## Operating systems

The scripts has been tested on macOS only. I cannot guarantee that it will work on other operating systems.

## Requirements

- Python 3.6+

Install the required packages ([virtual environment](https://docs.python.org/3/library/venv.html) is recommended):

```bash
pip install -r requirements.txt
```

## Usage

### Arguments:

Take a screenshot of an application. Available options:

| Flag | Type | Description | Required | Default | Errors |
| --- | --- | --- | --- | --- | --- |
| -l, --list | bool | Get the list of active applications | ⃝ | - | - |
| -la, --list-all | bool | Get the list of active applications with geometries | ⃝ | - | - |
| If `--list` is not provided: |
| -n, --name | str | Application name | ◉ | None | Whether application is not open |
| -i, --index | int | Application index | ◉ | None | Whether index is out of range |
| -d, --destination | str | Destination folder | ⃝ | 'screenshots' (subfolder in current folder) | None |
| -ew, --expected-width | int | Expected width of the screenshot | ⃝ | Current width | Whether negative or zero |
| -eh, --expected-height | int | Expected height of the screenshot | ⃝ | Current height | Wheter negative or zero |
| -r, --repeat | int | Number of screenshots to take | ⃝ | 1 | None |

### Examples:

Get the list of active applications (the name is used with the `-n` argument, the index is used with the `-i` argument):

```bash
python main.py -l
```

Get the list of active applications with geometries (the name is used with the `-n` argument, the index is used with the `-i` argument)::

```bash
python main.py -la
```

Take a screenshot of the application (selected by index) and save it in the "screenshots" folder:

```bash
python main.py -i <app_index>
```

Take a screenshot of the provided application name (if it is active) and save it in the "screenshots" folder:

```bash
python main.py -n <app_name>
```

Take 5 screenshots of the provided application name (if it is active) and save them in the "/Users/screenshots" folder (will be created if it does not exist). To take the next one press `Enter`

```bash
python main.py -n <app_name> -d "/Users/screenshots" -r 5
```

Take a screenshot of the provided application name (if it is active) and save it in the "screenshots" folder. The width of the screenshot will be 1920px (height will be adjusted to keep the aspect ratio)

```bash
python main.py -n <app_name> -ew 1920
```

Take a screenshot of the provided application name (if it is active) and save it in the "screenshots" folder. The size of the screenshot will be 1920x1080 pixels.

```bash
python main.py -n <app_name> -ew 1920 -eh 1080
```