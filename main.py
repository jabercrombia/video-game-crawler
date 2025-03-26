import os
import psycopg2
import requests
from dotenv import load_dotenv
from icrawler.builtin import GoogleImageCrawler

# Load environment variables from the .env file
load_dotenv()

# Get database connection details from the environment variables
host = os.getenv('PG_HOST')
port = os.getenv('PG_PORT')
dbname = os.getenv('PG_DATABASE')
user = os.getenv('PG_USER')
password = os.getenv('PG_PASSWORD')
# Connect to PostgreSQL database
def get_keywords_from_db():
    # Your database connection setup
    conn = psycopg2.connect(
        dbname=dbname, 
        user=user, 
        password=password, 
        host=host, 
        port=port,
    )
    cursor = conn.cursor()

    # Query to get the list of genres, platforms, or whatever you want to use for image search
    cursor.execute("SELECT id,name FROM vgsales LIMIT 4")
    rows = cursor.fetchall()

    # Extract keywords (genre) and ids from query results
    keywords_with_ids = [{'id': row[0], 'keyword': row[1]} for row in rows]  # Assuming id is in the first column and genre in the second
    cursor.close()
    conn.close()

    return keywords_with_ids
# Function to download a single image for a given keyword and store it in a folder named after the id
def download_image(id, keyword, directory='images'):
    # Ensure the folder exists for the ID (to save the image in a unique folder named after the ID)
    id_dir = os.path.join(directory, str(id))
    os.makedirs(id_dir, exist_ok=True)

    # Initialize the GoogleImageCrawler with a unique folder for each ID
    crawler = GoogleImageCrawler(storage={'root_dir': id_dir})

    # Start crawling and download one image for the keyword
    crawler.crawl(
        keyword='box art' + keyword,  # Search term (from the database)
        max_num=1,  # Only download 1 image
        filters={
            'size': 'medium',  # Filter images by size (small, medium, large)
            'type': 'photo'  # Filter image type (photo, clipart, etc.)
        }
    )


# Main loop to download images for each keyword
def main():
    # Get the list of keywords with their ids (genres, platforms, etc.)
    keywords_with_ids = get_keywords_from_db()

    # Loop through the keywords and download one image per query result
    for item in keywords_with_ids:
        keyword = item['keyword']
        keyword_id = item['id']
        print(f"Downloading image for keyword: {keyword} with ID: {keyword_id}")
        download_image(keyword_id, keyword)


if __name__ == "__main__":
    main()