
# Image Crawler

This project is an image crawler that searches for images based on specific keywords, stores them in an image directory, and uses PostgreSQL to manage the data.

## Features

- Crawl images using keywords from a PostgreSQL database.
- Automatically download the first image result for each keyword.
- Store images in an organized directory, using the keyword (or ID) as the folder name.
- Easy integration with Python and PostgreSQL for scalable solutions.

## Prerequisites

- Python 3.7 or higher
- PostgreSQL Database
- `icrawler` for image crawling
- `psycopg2` for connecting to PostgreSQL
- `dotenv` for managing environment variables

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/jabercrombia/video-game-crawler.git
   cd image-crawler
   ```

2. Set up a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Set up the environment variables by creating a `.env` file in the root of the project. Example:

   ```env
   DB_HOST=your_database_host
   DB_NAME=your_database_name
   DB_USER=your_database_user
   DB_PASSWORD=your_database_password
   ```

## Usage

1. Update the database connection settings in your `.env` file.
2. Run the script to begin crawling images:

   ```bash
   python crawler.py
   ```

The script will connect to your PostgreSQL database, query the necessary keywords or IDs, and crawl for the images.

The images will be stored in a directory structure like this:

```
/images
    /<ID>
        /image.jpg
```

### Example

If your query returns an ID of `123` with a keyword of `playstation`, the images will be saved in the following directory:

```
/images/123/image.jpg
```

## Database Schema

The database should have a table with at least the following columns:

- `id` (INT, Primary Key)
- `keyword` (VARCHAR)
- `image_url` (VARCHAR, optional, stores the URL of the downloaded image)

Example schema:

```sql
CREATE TABLE images (
    id SERIAL PRIMARY KEY,
    keyword VARCHAR(255) NOT NULL,
    image_url VARCHAR(255)
);
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
