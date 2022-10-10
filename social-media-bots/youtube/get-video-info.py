from requests_html import HTMLSession
from bs4 import BeautifulSoup as bs
import re
import json

session = HTMLSession()


def get_video_info(url):
    response = session.get(url)
    response.html.render(timeout=60)
    soup = bs(response.html.html, "html.parser")
    result = {}
    result["title"] = soup.find("meta", itemprop="name")['content']
    result["views"] = soup.find("meta", itemprop="interactionCount")['content']
    result["description"] = soup.find(
        "meta", itemprop="description")['content']
    result["date_published"] = soup.find(
        "meta", itemprop="datePublished")['content']
    result["duration"] = soup.find("span", {"class": "ytp-time-duration"}).text
    result["tags"] = ', '.join([meta.attrs.get(
        "content") for meta in soup.find_all("meta", {"property": "og:video:tag"})])

    data = re.search(r"var ytInitialData = ({.*?});", soup.prettify()).group(1)
    data_json = json.loads(data)
    videoPrimaryInfoRenderer = data_json['contents']['twoColumnWatchNextResults'][
        'results']['results']['contents'][0]['videoPrimaryInfoRenderer']
    videoSecondaryInfoRenderer = data_json['contents']['twoColumnWatchNextResults'][
        'results']['results']['contents'][1]['videoSecondaryInfoRenderer']
    likes_label = videoPrimaryInfoRenderer['videoActions']['menuRenderer']['topLevelButtons'][0]['toggleButtonRenderer'][
        'defaultText']['accessibility']['accessibilityData']['label']  # "No likes" or "###,### likes"
    likes_str = likes_label.split(' ')[0].replace(',', '')
    result["likes"] = '0' if likes_str == 'No' else likes_str
    result['dislikes'] = 'UNKNOWN'
    channel_tag = soup.find("meta", itemprop="channelId")['content']
    channel_name = soup.find("span", itemprop="author").next.next['content']
    channel_url = f"https://www.youtube.com/{channel_tag}"
    channel_subscribers = videoSecondaryInfoRenderer['owner']['videoOwnerRenderer'][
        'subscriberCountText']['accessibility']['accessibilityData']['label']
    result['channel'] = {'name': channel_name,
                         'url': channel_url, 'subscribers': channel_subscribers}
    return result


def print_video_info(url):
    data = get_video_info(url)

    print(f"\nTitle: {data['title']}")
    print(f"Views: {data['views']}")
    print(f"Published at: {data['date_published']}")
    print(f"Video Duration: {data['duration']}")
    print(f"Video tags: {data['tags']}")
    print(f"Likes: {data['likes']}")
    print(f"Dislikes: {data['dislikes']}")
    print(f"\nDescription: {data['description']}")
    print(f"\nChannel Name: {data['channel']['name']}")
    print(f"Channel URL: {data['channel']['url']}")
    print(f"Channel Subscribers: {data['channel']['subscribers']}")


if __name__ == "__main__":
    url = input('Enter youtube video url:\t')
    if url == '':
        url = 'https://www.youtube.com/watch?v=46tWHb4JZo8'
    print_video_info(url)
