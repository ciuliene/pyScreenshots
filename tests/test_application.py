from unittest import TestCase, main
from unittest.mock import patch
from src.application import *
import pygetwindow

@patch.object(pygetwindow, 'getAllTitles')
class TestApplication(TestCase):
    def test_getting_all_windows_returns_a_list(self, mock_get_all_titles):
        # Arrange
        mock_get_all_titles.return_value = ['window1', 'window2']

        # Act
        result = get_all_windows()

        # Assert
        self.assertEqual(result, ['window1', 'window2'])
        
    @patch.object(pygetwindow, 'getWindowGeometry')
    def test_getting_window_geometry_returns_a_window_geometry_object(self, mock_geometry, mock_get_all_titles):
        # Arrange
        mock_get_all_titles.return_value = ['window1', 'window2']
        mock_geometry.return_value = [10, 20, 30, 40]

        # Act
        result = get_window_geometry('window1')

        # Assert
        self.assertIsInstance(result, WindowGeometry)
        self.assertEqual(result.x, 10)
        self.assertEqual(result.y, 20)
        self.assertEqual(result.width, 30)
        self.assertEqual(result.height, 40)
        self.assertEqual(str(result), 'WindowGeometry(x=10, y=20, width=30, height=40)')

    def test_getting_window_geometry_raises_exception_when_window_not_found(self, mock_get_all_titles):
        # Arrange
        mock_get_all_titles.return_value = ['window1', 'window2']

        # Act
        with self.assertRaises(Exception) as context:
            get_window_geometry('window3')

        # Assert
        self.assertEqual(str(context.exception), 'window3 window not found')

if __name__ == '__main__':
    main()