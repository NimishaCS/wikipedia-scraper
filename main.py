from scraper import WikipediaScraper


def main():
    topic = input("Enter the Wikipedia topic to scrape: ")

    # Generate the filename automatically
    default_filename = WikipediaScraper.generate_filename_from_topic(topic)
    print(f"Generated output file name: {default_filename}")

    scraper = WikipediaScraper(topic)

    try:
        print("Fetching page...")
        scraper.fetch_page()

        print("Extracting content...")
        scraper.save_to_file(default_filename)

        print("Process completed successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
