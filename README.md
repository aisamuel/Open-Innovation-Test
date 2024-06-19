```markdown
# Image Resize Application with PostgreSQL

This project demonstrates how to set up and run the Flask image resize application with PostgreSQL as the database locally.

## Project Structure

```
Open-Innovation-Test/
├── app.py
├── resize_image.py
├── test_app.py
├── img.csv
├── Profile
├── requirements.txt
├── .gitignore
└── README.md

```

## Prerequisites

- Python 3.8 or later
- PostgreSQL
- Git

## Getting Started

### 1. Clone the Repository

Clone the repository to your local machine:

```bash
git clone https://github.com/aisamuel/Open-Innovation-Test
cd Open-Innovation-Test
```

### 2. Set Up the Virtual Environment

Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### 3. Install Dependencies

Install the required Python packages:

```bash
pip install -r requirements.txt
```

### 4. Set Up PostgreSQL

1. **Create a Database and User**:
    - Open the PostgreSQL command line or pgAdmin and create a new database and user.

    ```sql
    CREATE DATABASE image_data;
    CREATE USER myuser WITH ENCRYPTED PASSWORD 'mypassword';
    GRANT ALL PRIVILEGES ON DATABASE image_data TO myuser;
    ```

2. **Create the Table**:
    - Use the following SQL commands to create the table:

    ```sql
    CREATE TABLE resized_images (
        id SERIAL PRIMARY KEY,
        depth FLOAT,
        col1 FLOAT,
        col2 FLOAT,
        col3 FLOAT,
        col4 FLOAT,
        col5 FLOAT,
        col6 FLOAT,
        col7 FLOAT,
        col8 FLOAT,
        col9 FLOAT,
        col10 FLOAT,
        col11 FLOAT,
        col12 FLOAT,
        col13 FLOAT,
        col14 FLOAT,
        col15 FLOAT,
        col16 FLOAT,
        col17 FLOAT,
        col18 FLOAT,
        col19 FLOAT,
        col20 FLOAT,
        col21 FLOAT,
        col22 FLOAT,
        col23 FLOAT,
        col24 FLOAT,
        col25 FLOAT,
        col26 FLOAT,
        col27 FLOAT,
        col28 FLOAT,
        col29 FLOAT,
        col30 FLOAT,
        col31 FLOAT,
        col32 FLOAT,
        col33 FLOAT,
        col34 FLOAT,
        col35 FLOAT,
        col36 FLOAT,
        col37 FLOAT,
        col38 FLOAT,
        col39 FLOAT,
        col40 FLOAT,
        col41 FLOAT,
        col42 FLOAT,
        col43 FLOAT,
        col44 FLOAT,
        col45 FLOAT,
        col46 FLOAT,
        col47 FLOAT,
        col48 FLOAT,
        col49 FLOAT,
        col50 FLOAT,
        col51 FLOAT,
        col52 FLOAT,
        col53 FLOAT,
        col54 FLOAT,
        col55 FLOAT,
        col56 FLOAT,
        col57 FLOAT,
        col58 FLOAT,
        col59 FLOAT,
        col60 FLOAT,
        col61 FLOAT,
        col62 FLOAT,
        col63 FLOAT,
        col64 FLOAT,
        col65 FLOAT,
        col66 FLOAT,
        col67 FLOAT,
        col68 FLOAT,
        col69 FLOAT,
        col70 FLOAT,
        col71 FLOAT,
        col72 FLOAT,
        col73 FLOAT,
        col74 FLOAT,
        col75 FLOAT,
        col76 FLOAT,
        col77 FLOAT,
        col78 FLOAT,
        col79 FLOAT,
        col80 FLOAT,
        col81 FLOAT,
        col82 FLOAT,
        col83 FLOAT,
        col84 FLOAT,
        col85 FLOAT,
        col86 FLOAT,
        col87 FLOAT,
        col88 FLOAT,
        col89 FLOAT,
        col90 FLOAT,
        col91 FLOAT,
        col92 FLOAT,
        col93 FLOAT,
        col94 FLOAT,
        col95 FLOAT,
        col96 FLOAT,
        col97 FLOAT,
        col98 FLOAT,
        col99 FLOAT,
        col100 FLOAT,
        col101 FLOAT,
        col102 FLOAT,
        col103 FLOAT,
        col104 FLOAT,
        col105 FLOAT,
        col106 FLOAT,
        col107 FLOAT,
        col108 FLOAT,
        col109 FLOAT,
        col110 FLOAT,
        col111 FLOAT,
        col112 FLOAT,
        col113 FLOAT,
        col114 FLOAT,
        col115 FLOAT,
        col116 FLOAT,
        col117 FLOAT,
        col118 FLOAT,
        col119 FLOAT,
        col120 FLOAT,
        col121 FLOAT,
        col122 FLOAT,
        col123 FLOAT,
        col124 FLOAT,
        col125 FLOAT,
        col126 FLOAT,
        col127 FLOAT,
        col128 FLOAT,
        col129 FLOAT,
        col130 FLOAT,
        col131 FLOAT,
        col132 FLOAT,
        col133 FLOAT,
        col134 FLOAT,
        col135 FLOAT,
        col136 FLOAT,
        col137 FLOAT,
        col138 FLOAT,
        col139 FLOAT,
        col140 FLOAT,
        col141 FLOAT,
        col142 FLOAT,
        col143 FLOAT,
        col144 FLOAT,
        col145 FLOAT,
        col146 FLOAT,
        col147 FLOAT,
        col148 FLOAT,
        col149 FLOAT,
        col150 FLOAT
    );
    ```

### 5. Configure Environment Variables

Set the `DATABASE_URL` environment variable in your local environment:

```bash
export DATABASE_URL='postgresql://myuser:mypassword@localhost/image_data'
```   

## Example SQL Query for Creating the Table

```sql
CREATE TABLE resized_images (
    id SERIAL PRIMARY KEY,
    depth FLOAT,
    col1 FLOAT,
    col2 FLOAT,
    col3 FLOAT,
    col4 FLOAT,
    col5 FLOAT,
    col6 FLOAT,
    col7 FLOAT,
    col8 FLOAT,
    col9 FLOAT,
    col10 FLOAT,
    col11 FLOAT,
    col12 FLOAT,
    col13 FLOAT,
    col14 FLOAT,
    col15 FLOAT,
    col16 FLOAT,
    col17 FLOAT,
    col18 FLOAT,
    col19 FLOAT,
    col20 FLOAT,
    col21 FLOAT,
    col22 FLOAT,
    col23 FLOAT,
    col24 FLOAT,
    col25 FLOAT,
    col26 FLOAT,
    col27 FLOAT,
    col28 FLOAT,
    col29 FLOAT,
    col30 FLOAT,
    col31 FLOAT,
    col32 FLOAT,
    col33 FLOAT,
    col34 FLOAT,
    col35 FLOAT,
    col36 FLOAT,
    col37 FLOAT,
    col38 FLOAT,
    col39 FLOAT,
    col40 FLOAT,
    col41 FLOAT,
    col42 FLOAT,
    col43 FLOAT,
    col44 FLOAT,
    col45 FLOAT,
    col46 FLOAT,
    col47 FLOAT,
    col48 FLOAT,
    col49 FLOAT,
    col50 FLOAT,
    col51 FLOAT,
    col52 FLOAT,
    col53 FLOAT,
    col54 FLOAT,
    col55 FLOAT,
    col56 FLOAT,
    col57 FLOAT,
    col58 FLOAT,
    col59 FLOAT,
    col60 FLOAT,
    col61 FLOAT,
    col62 FLOAT,
    col63 FLOAT,
    col64 FLOAT,
    col65 FLOAT,
    col66 FLOAT,
    col67 FLOAT,
    col68 FLOAT,
    col69 FLOAT,
    col70 FLOAT,
    col71 FLOAT,
    col72 FLOAT,
    col73 FLOAT,
    col74 FLOAT,
    col75 FLOAT,
    col76 FLOAT,
    col77 FLOAT,
    col78 FLOAT,
    col79 FLOAT,
    col80 FLOAT,
    col81 FLOAT,
    col82 FLOAT,
    col83 FLOAT,
    col84 FLOAT,
    col85 FLOAT,
    col86 FLOAT,
    col87 FLOAT,
    col88 FLOAT,
    col89 FLOAT,
    col90 FLOAT,
    col91 FLOAT,
    col92 FLOAT,
    col93 FLOAT,
    col94 FLOAT,
    col95 FLOAT,
    col96 FLOAT,
    col97 FLOAT,
    col98 FLOAT,
    col99 FLOAT,
    col100 FLOAT,
    col101 FLOAT,
    col102 FLOAT,
    col103 FLOAT,
    col104 FLOAT,
    col105 FLOAT,
    col106 FLOAT,
    col107 FLOAT,
    col108 FLOAT,
    col109 FLOAT,
    col110 FLOAT,
    col111 FLOAT,
    col112 FLOAT,
    col113 FLOAT,
    col114 FLOAT,
    col115 FLOAT,
    col116 FLOAT,
    col117 FLOAT,
    col118 FLOAT,
    col119 FLOAT,
    col120 FLOAT,
    col121 FLOAT,
    col122 FLOAT,
    col123 FLOAT,
    col124 FLOAT,
    col125 FLOAT,
    col126 FLOAT,
    col127 FLOAT,
    col128 FLOAT,
    col129 FLOAT,
    col130 FLOAT,
    col131 FLOAT,
    col132 FLOAT,
    col133 FLOAT,
    col134 FLOAT,
    col135 FLOAT,
    col136 FLOAT,
    col137 FLOAT,
    col138 FLOAT,
    col139 FLOAT,
    col140 FLOAT,
    col141 FLOAT,
    col142 FLOAT,
    col143 FLOAT,
    col144 FLOAT,
    col145 FLOAT,
    col146 FLOAT,
    col147 FLOAT,
    col148 FLOAT,
    col149 FLOAT,
    col150 FLOAT
);
```

### 6. Run the Resize Image Script

Run the resize image file to populate the database:

```bash
python resize_image.py
```

### 7. Run the Test Script

Run the test script:

```bash
python test_app.py
```

### 8. Run the Application Locally

Run the Flask application:

```bash
python app.py
```

The application should now be running at `http://127.0.0.1:5000/`.

### 9. Run the Application Remotely

The application is also hosted remotely;

The application is running at `https://image-viewer-samuel65-8ca14a06.koyeb.app/get_image_frame?depth_min=9000.1&depth_max=9000.19`.


