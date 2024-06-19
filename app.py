import io, os

from flask import Flask, request, jsonify, send_file
import pandas as pd
import matplotlib.pyplot as plt
import psycopg2

app = Flask(__name__)

# PostgreSQL configuration
DATABASE_URL = os.environ.get(
    'DATABASE_URL', 'postgresql://myuser:mypassword@localhost/images_data')

DEBUG = (os.environ.get('DEBUG', 'True').lower() == 'true')

def save_to_postgres(data):
    conn = psycopg2.connect(DATABASE_URL)
    cursor = conn.cursor()

    # Create insert query
    placeholders = ', '.join(['%s'] * len(data.columns))
    columns = ', '.join(data.columns)
    sql = f"INSERT INTO resized_images ({columns}) VALUES ({placeholders})"

    for _, row in data.iterrows():
        cursor.execute(sql, tuple(row))

    conn.commit()
    cursor.close()
    conn.close()


def load_from_postgres(depth_min, depth_max):
    conn = psycopg2.connect(DATABASE_URL)
    query = "SELECT * FROM resized_images WHERE depth BETWEEN %s AND %s"
    df = pd.read_sql(query, conn, params=(depth_min, depth_max))
    conn.close()
    return df


def apply_color_map(data, cmap='viridis'):
    norm = plt.Normalize(vmin=data.min().min(), vmax=data.max().max())
    colormap = plt.get_cmap(cmap)
    rgba_img = colormap(norm(data.values))
    return rgba_img


@app.route('/get_image_frame', methods=['GET'])
def get_image_frame():
    depth_min = float(request.args.get('depth_min'))
    depth_max = float(request.args.get('depth_max'))

    filtered_data = load_from_postgres(depth_min, depth_max)

    if filtered_data.empty:
        return jsonify({"error": "No data found for the given image depth range"}), 404

    image_data = filtered_data.iloc[:, 1:]  # Exclude the depth column
    color_mapped_img = apply_color_map(image_data)

    buf = io.BytesIO()
    plt.imsave(buf, color_mapped_img, format='png')
    buf.seek(0)

    return send_file(buf, mimetype='image/png')


if __name__ == '__main__':
    app.run(debug=DEBUG)
