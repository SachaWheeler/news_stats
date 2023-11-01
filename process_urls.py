import feedparser
import numpy as np

# List of RSS feed URLs
rss_feed_urls = [
    'https://example.com/rss-feed-1.xml',
    'https://example.com/rss-feed-2.xml',
    # Add more RSS feed URLs as needed
]

# Function to fetch and parse RSS feeds
def fetch_and_parse_feeds(feed_urls):
    parsed_feeds = []
    for feed_url in feed_urls:
        feed = feedparser.parse(feed_url)
        parsed_feeds.append(feed)
    return parsed_feeds

# Function to process RSS feed data using NumPy
def process_feeds_with_numpy(parsed_feeds):
    # Example: Extract and store the number of entries in each feed
    num_entries = [len(feed.entries) for feed in parsed_feeds]
    # Convert the list to a NumPy array for further processing
    num_entries_array = np.array(num_entries)

    # You can perform various NumPy operations on the data, e.g., calculate statistics
    mean_entries = np.mean(num_entries_array)
    max_entries = np.max(num_entries_array)
    min_entries = np.min(num_entries_array)

    return num_entries_array, mean_entries, max_entries, min_entries

# Fetch and parse RSS feeds
parsed_feeds = fetch_and_parse_feeds(rss_feed_urls)

# Process the parsed RSS feed data using NumPy
num_entries_array, mean_entries, max_entries, min_entries = process_feeds_with_numpy(parsed_feeds)

# Print the results
print(f"Number of entries in each feed: {num_entries_array}")
print(f"Mean number of entries: {mean_entries}")
print(f"Maximum number of entries: {max_entries}")
print(f"Minimum number of entries: {min_entries}")

