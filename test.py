import requests
from isodate import parse_duration

def search():
    api_Key = 'AIzaSyBGjV4JOrmoq7waymn6_6zyqY_NUYjLYPQ'
    query = input("Enter Youtube Query:")
    search_url = 'https://www.googleapis.com/youtube/v3/search'
    video_url = 'https://www.googleapis.com/youtube/v3/videos'

    videos = []

    search_params = {
        'key' : api_Key,
        'q' : query,
        'part' : 'snippet',
        'maxResults' : 1,
        'type' : 'video'
    }

    r = requests.get(search_url, params=search_params)
    for i in r:
        print(i);
    quit
    results = r.json()['items']

    video_ids = []
    for result in results:
        video_ids.append(result['id']['videoId'])

    video_params = {
        'key' : api_Key,
        'id' : ','.join(video_ids),
        'part' : 'snippet,contentDetails',
        'maxResults' : 1
    }

    r = requests.get(video_url, params=video_params)
    results = r.json()['items']
    for result in results:
        video_data = {
            # 'id' : result['id'],
            'url' : f'https://www.youtube.com/watch?v={ result["id"] }',
            'thumbnail' : result['snippet']['thumbnails']['high']['url'],
            'duration' : int(parse_duration(result['contentDetails']['duration']).total_seconds() // 60),
            'title' : result['snippet']['title'],
        }
        videos.append(video_data)
    return(videos);
print(search());