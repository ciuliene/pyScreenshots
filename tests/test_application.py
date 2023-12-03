from unittest import TestCase, main
from unittest.mock import patch
from src.application import *
import pygetwindow


@patch('builtins.print')
@patch.object(pygetwindow, 'getAllTitles')
class TestApplication(TestCase):
    @patch.object(pygetwindow, 'getWindowGeometry')
    def test_getting_all_windows_returns_a_list(self, mock_geometry, mock_get_all_titles, *_):
        # Arrange
        mock_get_all_titles.return_value = ['window1', 'window2']
        mock_geometry.return_value = [10, 20, 30, 40]

        # Act
        result = get_all_windows()

        # Assert
        self.assertEqual(result, ['window1', 'window2'])

    @patch.object(pygetwindow, 'getWindowGeometry')
    def test_getting_all_windows_returns_a_list_of_positive_geometries(self, mock_geometry, mock_get_all_titles, *_):
        # Arrange
        mock_get_all_titles.return_value = [
            'window1', 'window2', 'window3', 'window4', 'window5']
        mock_geometry.side_effect = [
            [10, 20, 30, 40], [-1, 0, 1, 1], [0, -1, 1, 1], [0, 0, 0, 1], [0, 0, 1, 0]]

        # Act
        result = get_all_windows()

        # Assert
        self.assertEqual(result, ['window1'])

    @patch.object(pygetwindow, 'getWindowGeometry')
    def test_getting_all_windows_returns_a_list_with_geometries_when_specified(self, mock_geometry, mock_get_all_titles, *_):
        # Arrange
        mock_get_all_titles.return_value = [
            'window1', 'window2', 'window3', 'window4', 'window5']
        mock_geometry.side_effect = [
            [10, 20, 30, 40], [-1, 0, 1, 1], [0, -1, 1, 1], [0, 0, 0, 1], [0, 0, 1, 0], [10, 20, 30, 40]]

        # Act
        result = get_all_windows(True)

        # Assert
        self.assertEqual(result, [
                         'x=10        y=20        width=30        height=40        app_name=window1'])

    def test_getting_window_geometry_raises_exception_when_no_window_specified(self, mock_get_all_titles, *_):
        # Arrange
        mock_get_all_titles.return_value = ['window1', 'window2']

        # Act
        with self.assertRaises(Exception) as context:
            get_window_geometry(None, None)

        # Assert
        self.assertEqual(str(context.exception),
                         'Please specify the name or the index of the application to take a screenshot of')

    @patch.object(pygetwindow, 'getWindowGeometry')
    def test_getting_window_geometry_returns_a_window_geometry_object(self, mock_geometry, mock_get_all_titles, *_):
        # Arrange
        mock_get_all_titles.return_value = ['window1', 'window2']
        mock_geometry.return_value = [10, 20, 30, 40]

        # Act
        result = get_window_geometry('window1', None)

        # Assert
        self.assertIsInstance(result, WindowGeometry)
        self.assertEqual(result.x, 10)
        self.assertEqual(result.y, 20)
        self.assertEqual(result.width, 30)
        self.assertEqual(result.height, 40)
        self.assertEqual(
            str(result), 'x=10        y=20        width=30        height=40        app_name=window1')

    @patch('builtins.input')
    @patch.object(pygetwindow, 'getWindowGeometry')
    def test_getting_window_geometry_returns_a_window_geometry_object_from_user_selection(self, mock_geometry, mock_input, mock_get_all_titles, *_):
        # Arrange
        mock_get_all_titles.return_value = [
            'window1', 'window2', 'window1 (1)']
        mock_geometry.return_value = [10, 20, 30, 40]
        mock_input.return_value = 1

        # Act
        result = get_window_geometry('window1', None)

        # Assert
        self.assertIsInstance(result, WindowGeometry)
        self.assertEqual(result.x, 10)
        self.assertEqual(result.y, 20)
        self.assertEqual(result.width, 30)
        self.assertEqual(result.height, 40)
        self.assertEqual(
            str(result), 'x=10        y=20        width=30        height=40        app_name=window1 (1)')

    @patch.object(pygetwindow, 'getWindowGeometry')
    def test_getting_window_geometry_by_index_returns_a_window_geometry_object(self, mock_geometry, mock_get_all_titles, *_):
        # Arrange
        mock_get_all_titles.return_value = ['window1', 'window2']
        mock_geometry.return_value = [10, 20, 30, 40]

        # Act
        result = get_window_geometry(None, 1)

        # Assert
        self.assertIsInstance(result, WindowGeometry)
        self.assertEqual(result.x, 10)
        self.assertEqual(result.y, 20)
        self.assertEqual(result.width, 30)
        self.assertEqual(result.height, 40)
        self.assertEqual(
            str(result), 'x=10        y=20        width=30        height=40        app_name=window2')

    @patch.object(pygetwindow, 'getWindowGeometry')
    def test_getting_window_geometry_raises_exception_when_index_out_of_range(self, mock_geometry, mock_get_all_titles, *_):
        # Arrange
        mock_get_all_titles.return_value = ['window1', 'window2']
        mock_geometry.return_value = [10, 20, 30, 40]

        # Act
        with self.assertRaises(Exception) as context:
            get_window_geometry(None, 2)

        # Assert
        self.assertEqual(str(context.exception),
                         'Index 2 is out of range. Max index is 1')

    @patch.object(pygetwindow, 'getWindowGeometry')
    def test_getting_window_geometry_raises_exception_when_window_not_found(self, mock_geometry, mock_get_all_titles, *_):
        # Arrange
        mock_get_all_titles.return_value = ['window1', 'window2']
        mock_geometry.return_value = [10, 20, 30, 40]

        # Act
        with self.assertRaises(Exception) as context:
            get_window_geometry('window3', None)

        # Assert
        self.assertEqual(str(context.exception), '"window3" window not found')

if __name__ == '__main__':
    main()