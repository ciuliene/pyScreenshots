# PyScreenshots

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
| If `--list` is not provided: |
| -n, --name | str | Application name | ◉ | None | Whether application is not open |
| -d, --destination | str | Destination folder | ⃝ | 'screenshots' (subfolder in current folder) | None |
| -ew, --expected-width | int | Expected width of the screenshot | ⃝ | Current width | Whether negative or zero |
| -eh, --expected-height | int | Expected height of the screenshot | ⃝ | Current height | Wheter negative or zero |
| -r, --repeat | int | Number of screenshots to take | ⃝ | 1 | None |

### Examples:

Get the list of active applications (names are used with the `-n` argument):

```bash
python main.py -l
```

Take a screenshot of the provided application name (if it is active) and save it in the "screenshots" folder:

```bash
python main.py -n <app_name>
```

Take 5 screenshots of QuickTime application (if it is active) and save them in the "/Users/screenshots" folder (will be created if it does not exist). To take the next one press `Enter`

```bash
python main.py -n <app_name> -d "/Users/screenshots" -r 5
```

Take a screenshot of QuickTime application (if it is active) and save it in the "screenshots" folder. The width of the screenshot will be 1920px (height will be adjusted to keep the aspect ratio)

```bash
python main.py -n <app_name> -ew 1920
```

Take a screenshot of QuickTime application (if it is active) and save it in the "screenshots" folder. The size of the screenshot will be 1920x1080 pixels.

```bash
python main.py -n <app_name> -ew 1920 -eh 1080
```