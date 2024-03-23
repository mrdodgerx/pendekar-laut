# Pendekar Laut Comic Scraper

This Python script scrapes image URLs from a website hosting episodes of the Hong Kong comic book series "Pendekar Laut" and downloads the images into folders based on the episode URLs.

## Installation

1. Clone this repository:
    ~~~
    git clone 
    ~~~

2. Install the required Python packages:

    ```
    pip install -r requirements.txt
    ```

## Usage

1. Modify the `MAIN_URL` variable in the script to the URL of the main page of the "Pendekar Laut" comic website.

2. Run the script:

    ~~~
    python pendekar_laut_scraper.py
    ~~~

The script will fetch all episodes from the main page, find the "Read more" link for each episode, download the images from that link, and save them into folders named after each episode.

## Dependencies

- [requests](https://pypi.org/project/requests/): For making HTTP requests to fetch webpage content.
- [Beautiful Soup](https://pypi.org/project/beautifulsoup4/): For parsing HTML content.
- [fake_headers](https://pypi.org/project/fake-headers/): For generating fake user-agent headers to avoid bot detection.
- [urllib](https://docs.python.org/3/library/urllib.html): For parsing URLs.

## Synopsis

"Pendekar Laut" (translated as "Sea Warrior" in English) is a popular Hong Kong comic book series written and illustrated by an anonymous author. The story revolves around the adventures of Pai Cheung Lang, the titular character who is a skilled martial artist and sailor. Set in a fictional world inspired by Chinese martial arts and nautical themes, Pai Cheung Lang embarks on various quests and battles against formidable adversaries while seeking justice and protecting the innocent.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
