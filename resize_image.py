import pandas as pd

from app import save_to_postgres


def resize_image():
    # Load the original data
    file_path = 'img.csv'
    data = pd.read_csv(file_path)

    # Resize the image width to 150 columns
    # First column is depth, so we take first 151 columns
    resized_data = data.iloc[:, :151]

    # Save the resized data to PostgreSQL
    save_to_postgres(resized_data)


if __name__ == '__main__':
    resize_image()
