# fetch.py
"""
A module for fetching content data from the AAU website.

This module provides a function, fetch_content, which takes a URL as input and retrieves content information from the AAU website.

Usage:
    content_info_list = fetch_content(url)

Args:
    url (str): The URL of the website to fetch content from.

Returns:
    List[Dict[str, str]]: A list of dictionaries, where each dictionary represents content information with the following keys:
        - 'title': The title of the content.
        - 'link': The link to the content.
        - 'sample_text': A sample text or description of the content.
        - 'image_link': The link to the image associated with the content.
        - 'date_posted': The date when the content was posted.
        For announcements, the title is prefixed with 'Announcement'.

Example:
    announcements_url = "http://www.aau.edu.et/blog/category/announcements/"
    announcements_info_list = fetch_content(announcements_url)

    for content_info in announcements_info_list:
        print(f"Title: {content_info['title']}")
        print(f"Link: {content_info['link']}")
        print(f"Sample Text: {content_info['sample_text']}")
        print(f"Image Link: {content_info['image_link']}")
        print(f"Date Posted: {content_info['date_posted']}")
        print("\n" + "="*50 + "\n")
"""

from urllib.request import urlopen
from bs4 import BeautifulSoup
from typing import List, Dict


def fetch_content(url: str) -> List[Dict[str, str]]:
    """
    Fetch content information from the AAU website.

    Args:
        url (str): The URL of the website to fetch content from.

    Returns:
        List[Dict[str, str]]: A list of dictionaries representing content information.

    Raises:
        Any exceptions encountered during the HTTP request or parsing.

    Example:
        announcements_url = "http://www.aau.edu.et/blog/category/announcements/"
        announcements_info_list = fetch_content(announcements_url)

        for content_info in announcements_info_list:
            print(f"Title: {content_info['title']}")
            print(f"Link: {content_info['link']}")
            print(f"Sample Text: {content_info['sample_text']}")
            print(f"Image Link: {content_info['image_link']}")
            print(f"Date Posted: {content_info['date_posted']}")
            print("\n" + "="*50 + "\n")
    """
    html = urlopen(url).read().decode('utf-8')
    soup = BeautifulSoup(html, 'html.parser')

    content_items = soup.find_all('div', class_='post-wrap')

    content_info_list = []

    for index, content_item in enumerate(content_items, start=1):
        title = content_item.find('h2', class_='title').find('a').text.strip()
        link = content_item.find('h2', class_='title').find('a')['href']
        sample_text = content_item.find('div', class_='entry').find('p').text.strip()
        image_link = content_item.find('div', class_='entry').find('img')['src']
        date_posted = content_item.find('span', class_='meta_date').text.strip()

        # Check if the link is an announcements link
        if "category/announcements" in link:
            title = f"Announcement {index}: {title}"

        content_info = {
            'title': title,
            'link': link,
            'sample_text': sample_text,
            'image_link': image_link,
            'date_posted': date_posted
        }

        content_info_list.append(content_info)

    return content_info_list
