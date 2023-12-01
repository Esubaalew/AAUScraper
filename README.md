# AAU Website Content Fetcher

A Python module for fetching `news` and `announcements` from the Addis Ababa University (AAU) website.

## Overview

This module provides a function, `fetch_content`, which takes a URL as input and retrieves content information from the AAU website. It is designed to extract details such as titles, links, sample text, image links, and dates posted from the website's `news and announcements`. 

### Usage

Passing URL `http://www.aau.edu.et/` or `http://www.aau.edu.et/page/{anyinteger}` loads the news, while passing URL `http://www.aau.edu.et/blog/category/announcements/` or `http://www.aau.edu.et/blog/category/announcements/page/{anyinteger}` loads announcements.


```python
from fetch import fetch_content

# Example usage
url = "http://www.aau.edu.et/" 
# you can change the url to ~/page{integer} 
# url = "http://www.aau.edu.et/page/2" for example
content_info_list = fetch_content(url)

for content_info in content_info_list:
    print(f"Title: {content_info['title']}")
    print(f"Link: {content_info['link']}")
    print(f"Sample Text: {content_info['sample_text']}")
    print(f"Image Link: {content_info['image_link']}")
    print(f"Date Posted: {content_info['date_posted']}")
    print("\n" + "="*50 + "\n")
```
## Function Signature

```python
def fetch_content(url: str) -> List[Dict[str, str]]:
    """
    Fetch content information from the AAU website.

    Args:
        url (str): The URL of the website to fetch content from.

    Returns:
        List[Dict[str, str]]: A list of dictionaries representing content information.

    Raises:
        Any exceptions encountered during the HTTP request or parsing.
    """
```
## Other Example
```python
announcements_url = "http://www.aau.edu.et/blog/category/announcements/"
# you can change the url to ~/page{integer} 
# announcements_url = "http://www.aau.edu.et/blog/category/announcements/" for example
announcements_info_list = fetch_content(announcements_url)

for content_info in announcements_info_list:
    print(f"Title: {content_info['title']}")
    print(f"Link: {content_info['link']}")
    print(f"Sample Text: {content_info['sample_text']}")
    print(f"Image Link: {content_info['image_link']}")
    print(f"Date Posted: {content_info['date_posted']}")
    print("\n" + "="*50 + "\n")
```

## Disclaimer

This code is provided for educational and non-commercial purposes only. It is meant to serve as a learning resource and demonstration.
