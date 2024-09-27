# from flask import Flask, request, jsonify
# from flask_cors import CORS # type: ignore
# from googleapiclient.discovery import build
# import requests
# import xml.etree.ElementTree as ET

# app = Flask(__name__)
# CORS(app) 

# # Function to get YouTube videos
# def get_youtube_videos(query):
#     youtube = build('youtube', 'v3', developerKey='AIzaSyBM359dirKWkhccQ6ChnovBS3lMqLnqTUw')  # Your YouTube API key
#     request = youtube.search().list(
#         part='snippet',
#         q=query,
#         type='video',
#         order='viewCount',
#         maxResults=5
#     )
#     response = request.execute()
    
#     videos = []
#     for item in response['items']:
#         video_id = item['id']['videoId']
#         title = item['snippet']['title']
#         link = f"https://www.youtube.com/watch?v={video_id}"
#         videos.append({"title": title, "link": link})
#     return videos

# # Function to get articles and blogs using Google Custom Search API
# def get_articles_blogs(query):
#     api_key = 'AIzaSyDjw87UQoFT-kvcaZjkXSa_peN4AKnWGWc'  # Your Google API key
#     search_engine_id = 'e25f93441b5d24540'  # Your Custom Search Engine ID
#     url = f"https://www.googleapis.com/customsearch/v1?q={query}&key={api_key}&cx={search_engine_id}"
    
#     response = requests.get(url)
#     data = response.json()
    
#     articles = []
#     for item in data.get('items', []):
#         title = item['title']
#         link = item['link']
#         articles.append({"title": title, "link": link})
#     return articles

# # Function to get academic papers from arXiv API
# def get_academic_papers(query):
#     url = f'http://export.arxiv.org/api/query?search_query=all:{query}&start=0&max_results=5'
#     response = requests.get(url)
    
#     papers = []
    
#     if response.status_code == 200:
#         # Parse the XML response
#         root = ET.fromstring(response.content)
#         for entry in root.findall('{http://www.w3.org/2005/Atom}entry'):
#             title = entry.find('{http://www.w3.org/2005/Atom}title').text
#             link = entry.find('{http://www.w3.org/2005/Atom}id').text
#             papers.append({"title": title, "link": link})
#     else:
#         print(f"Error: {response.status_code}")
    
#     return papers

# # Search endpoint
# @app.route('/search', methods=['GET'])
# def search():
#     query = request.args.get('query')
    
#     youtube_videos = get_youtube_videos(query)
#     articles_blogs = get_articles_blogs(query)
#     academic_papers = get_academic_papers(query)

#     combined_results = {
#         "YouTube": youtube_videos,
#         "Articles/Blogs": articles_blogs,
#         "Academic Papers": academic_papers
#     }

#     return jsonify(combined_results)

# if __name__ == '__main__':
#     app.run(debug=True)

from flask import Flask, request, jsonify
from flask_cors import CORS
from googleapiclient.discovery import build
import requests
import xml.etree.ElementTree as ET

app = Flask(__name__)
CORS(app)

# Function to get YouTube videos
def get_youtube_videos(query):
    youtube = build('youtube', 'v3', developerKey='AIzaSyBM359dirKWkhccQ6ChnovBS3lMqLnqTUw')  # Your YouTube API key
    request = youtube.search().list(
        part='snippet',
        q=query,
        type='video',
        order='viewCount',
        maxResults=5
    )
    response = request.execute()
    
    videos = []
    for item in response['items']:
        video_id = item['id']['videoId']
        title = item['snippet']['title']
        link = f"https://www.youtube.com/watch?v={video_id}"
        videos.append({"title": title, "link": link})
    return videos

# Function to get articles and blogs using Google Custom Search API
def get_articles_blogs(query):
    api_key = 'AIzaSyDjw87UQoFT-kvcaZjkXSa_peN4AKnWGWc'  # Your Google API key
    search_engine_id = 'e25f93441b5d24540'  # Your Custom Search Engine ID
    url = f"https://www.googleapis.com/customsearch/v1?q={query}&key={api_key}&cx={search_engine_id}"
    
    response = requests.get(url)
    data = response.json()
    
    articles = []
    for item in data.get('items', []):
        title = item['title']
        link = item['link']
        articles.append({"title": title, "link": link})
    return articles

# Function to get academic papers from arXiv API
def get_academic_papers(query):
    url = f'http://export.arxiv.org/api/query?search_query=all:{query}&start=0&max_results=5'
    response = requests.get(url)
    
    papers = []
    
    if response.status_code == 200:
        # Parse the XML response
        root = ET.fromstring(response.content)
        for entry in root.findall('{http://www.w3.org/2005/Atom}entry'):
            title = entry.find('{http://www.w3.org/2005/Atom}title').text
            link = entry.find('{http://www.w3.org/2005/Atom}id').text
            papers.append({"title": title, "link": link})
    else:
        print(f"Error: {response.status_code}")
    
    return papers

# Search endpoint
@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('query')
    
    try:
        youtube_videos = get_youtube_videos(query)
        articles_blogs = get_articles_blogs(query)
        academic_papers = get_academic_papers(query)

        combined_results = {
            "YouTube": youtube_videos,
            "Articles/Blogs": articles_blogs,
            "Academic Papers": academic_papers
        }

        return jsonify(combined_results)

    except Exception as e:
        # Return an error response if there's an issue (like quota exceeded)
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)
