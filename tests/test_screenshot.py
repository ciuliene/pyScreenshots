from unittest import TestCase
from unittest.mock import patch, MagicMock
from src.screenshot import *

class MockScrenshot():
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self._count_resizes = 0
        self._resizes_arguments = []
        self._count_saves = 0

    def get_resizes_count(self):
        return self._count_resizes
    
    def get_resizes_arguments(self):
        return self._resizes_arguments

    def get_saves_count(self):
        return self._count_resizes
     
    def resize(self, size):
        self.width = size[0]
        self.height = size[1]
        self._count_resizes += 1
        self._resizes_arguments.append(size)
        return self
    
    def save(self, destination):
        self._count_saves += 1
        pass

@patch('os.makedirs', return_value=True)
@patch('os.path.exists', return_value=False)
class TestScreenshot(TestCase):
    @patch.object(pyautogui, 'screenshot')
    def test_getting_a_screenshot_returns_expected_screenshot_without_resize(self, mock_screenshot, *_):
        # Arrange
        screenshot = MockScrenshot(100, 100)
        mock_screenshot.return_value = screenshot
        destination = 'dest'
        name = 'name'
        expected = f'{destination}/{name}_100x100_1.png'

        # Act
        result = get_screenshot(0, 0, 100, 100, destination, name)

        # Assert
        self.assertEqual(result, expected)
        self.assertEqual(1, screenshot.get_resizes_count())
        self.assertEqual(1, len(screenshot.get_resizes_arguments()))
        self.assertEqual([100, 100], screenshot.get_resizes_arguments()[0])
        self.assertEqual(1, screenshot.get_saves_count())

    @patch.object(pyautogui, 'screenshot')
    def test_getting_a_screenshot_returns_expected_screenshot_with_expected_width_resize(self, mock_screenshot, *_):
        # Arrange
        screenshot = MockScrenshot(100, 100)
        mock_screenshot.return_value = screenshot
        destination = 'screenshots'
        name = 'name'
        expected = f'{destination}/{name}_200x300_1.png'

        # # Act
        result = get_screenshot(0, 0, 100, 150, None, name, 200)

        # Assert
        self.assertEqual(result, expected)
        self.assertEqual(1, screenshot.get_resizes_count())
        self.assertEqual(1, len(screenshot.get_resizes_arguments()))
        self.assertEqual([200, 300], screenshot.get_resizes_arguments()[0])
        self.assertEqual(1, screenshot.get_saves_count())

    @patch.object(pyautogui, 'screenshot')
    def test_getting_a_screenshot_returns_expected_screenshot_with_expected_height_resize(self, mock_screenshot, *_):
        # Arrange
        screenshot = MockScrenshot(100, 100)
        mock_screenshot.return_value = screenshot
        destination = 'dest'
        name = 'screenshot'
        expected = f'{destination}/{name}_133x200_1.png'

        # # Act
        result = get_screenshot(0, 0, 100, 150, destination, None, None, 200)

        # Assert
        self.assertEqual(result, expected)
        self.assertEqual(1, screenshot.get_resizes_count())
        self.assertEqual(1, len(screenshot.get_resizes_arguments()))
        self.assertEqual([133, 200], screenshot.get_resizes_arguments()[0])
        self.assertEqual(1, screenshot.get_saves_count())