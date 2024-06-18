import unittest
import json
import pandas as pd
from io import StringIO
from unittest.mock import patch
from app import app, save_to_postgres, load_from_postgres, apply_color_map


class FlaskTestCase(unittest.TestCase):

    def setUp(self):
        # Set up the test client
        self.app = app.test_client()
        self.app.testing = True

        # Sample CSV data for testing
        csv_data = StringIO("""depth,col1,col2,col3
        9000.1,224.0,224.0,224.0
        9000.2,224.0,224.0,224.0
        9000.3,224.0,224.0,224.0
        9000.4,224.0,224.0,224.0
        9000.5,224.0,224.0,224.0""")
        self.sample_df = pd.read_csv(csv_data)

    @patch('app.psycopg2.connect')
    def test_save_to_postgres(self, mock_connect):
        # Mock the database connection
        mock_conn = mock_connect.return_value
        mock_cursor = mock_conn.cursor.return_value

        # Test saving data to PostgreSQL
        save_to_postgres(self.sample_df)

        # Ensure the cursor's execute method was called
        self.assertTrue(mock_cursor.execute.called,
                        "Cursor execute should be called")

        # Ensure the commit method was called
        self.assertTrue(mock_conn.commit.called,
                        "Connection commit should be called")

    @patch('app.psycopg2.connect')
    def test_load_from_postgres(self, mock_connect):
        # Mock the database connection
        mock_conn = mock_connect.return_value
        mock_cursor = mock_conn.cursor.return_value

        # Mock the pandas read_sql function
        with patch('app.pd.read_sql') as mock_read_sql:
            mock_read_sql.return_value = self.sample_df

            # Test loading data from PostgreSQL
            df = load_from_postgres(9000.1, 9000.5)
            self.assertFalse(df.empty, "Loaded DataFrame should not be empty")
            self.assertEqual(len(df), 5, "DataFrame should have 5 rows")

    def test_apply_color_map(self):
        # Test applying color map to the data
        color_mapped_img = apply_color_map(self.sample_df.iloc[:, 1:])
        self.assertEqual(
            color_mapped_img.shape[0], 5, "Image should have 5 rows")
        self.assertEqual(
            color_mapped_img.shape[1], 3, "Image should have 3 columns")
        self.assertEqual(
            color_mapped_img.shape[2], 4, "Image should have 4 channels (RGBA)")

    @patch('app.psycopg2.connect')
    @patch('app.pd.read_sql')
    def test_get_image_frame(self, mock_read_sql, mock_connect):
        # Mock the database interaction
        mock_read_sql.return_value = self.sample_df

        # Test the get_image_frame route with valid parameters
        response = self.app.get(
            '/get_image_frame?depth_min=9000.1&depth_max=9000.5')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.mimetype, 'image/png')

    def test_get_image_frame_invalid(self):
        # Test the get_image_frame route with invalid parameters
        response = self.app.get(
            '/get_image_frame?depth_min=10000&depth_max=10005')
        self.assertEqual(response.status_code, 404)
        data = json.loads(response.data)
        self.assertEqual(
            data['error'], "No data found for the given depth range")


if __name__ == '__main__':
    unittest.main()
