# POC Assignment - Search and Content Aggregator

This project is a search-based content aggregator using Flask for the backend and React for the frontend. It retrieves YouTube videos, articles/blogs, and academic papers based on a user's search query.

# First
![Output Image](https://github.com/Chetanahazare/SearchEasy/blob/main/public/images/Screenshot%202024-09-27%20134211.png?raw=true)

# First

![Output Image](https://github.com/Chetanahazare/SearchEasy/blob/main/public/images/Screenshot%202024-09-27%20134211.png?raw=true)

# First
![Output Image](https://github.com/Chetanahazare/SearchEasy/blob/main/public/images/Screenshot%202024-09-27%20134211.png?raw=true)

# First

![Output Image](https://github.com/Chetanahazare/SearchEasy/blob/main/public/images/Screenshot%202024-09-27%20134211.png?raw=true)


## Available Scripts

In the project directory, you can run:

### `npm start` (Frontend)

Runs the frontend React app in the development mode.  
Open [http://localhost:3000](http://localhost:3000) to view it in your browser.  

The page will reload if you make edits.  
You will also see any lint errors in the console.

### `python app.py` (Backend)

Runs the Flask backend server.  
Open [http://127.0.0.1:5000/search?query=<your_query>](http://127.0.0.1:5000/search?query=example) to check the backend response.

Make sure Flask is installed, and run the following command in the terminal to start the backend:

```bash
python app.py
```

The backend will listen for requests on `http://127.0.0.1:5000/`.

## API Endpoints

### `GET /search`

The `/search` endpoint accepts a query parameter and retrieves data from three sources:
- **YouTube Videos**: Uses YouTube Data API to fetch videos related to the query.
- **Articles/Blogs**: Uses Google Custom Search API to get related articles or blog posts.
- **Academic Papers**: Fetches academic papers from the arXiv API.

### Example Request

```bash
http://127.0.0.1:5000/search?query=ai
```

### Example Response

```json
{
  "YouTube": [
    {
      "title": "Understanding AI",
      "link": "https://www.youtube.com/watch?v=abcd1234"
    }
  ],
  "Articles/Blogs": [
    {
      "title": "What is Artificial Intelligence?",
      "link": "https://www.example.com/ai-article"
    }
  ],
  "Academic Papers": [
    {
      "title": "Advancements in AI Research",
      "link": "https://arxiv.org/abs/abcd1234"
    }
  ]
}
```

## Project Structure

The project consists of two parts:

1. **Backend (Flask)**: Manages API requests and fetches data from YouTube, Google Custom Search, and arXiv APIs.
   - **app.py**: Main Flask app that handles the `/search` endpoint.

2. **Frontend (React)**: The user interface for querying the backend and displaying search results.
   - **App.js**: React component that handles user input and renders the results.

## Installation and Setup

### Backend (Flask)

1. Install the required Python packages using `pip`:
   
   ```bash
   pip install flask flask-cors google-api-python-client requests
   ```

2. Set up API keys in `app.py`:
   - YouTube API Key: Replace `'YOUR_YOUTUBE_API_KEY'` in `get_youtube_videos()` function.
   - Google Custom Search API Key and Engine ID: Replace `'YOUR_GOOGLE_API_KEY'` and `'YOUR_SEARCH_ENGINE_ID'` in `get_articles_blogs()` function.

3. Run the Flask server:

   ```bash
   python app.py
   ```

### Frontend (React)

1. Install the required dependencies:

   ```bash
   npm install
   ```

2. Start the React development server:

   ```bash
   npm start
   ```

3. Ensure the Flask backend is running so the frontend can fetch data from the `/search` endpoint.

## Features

- **YouTube Video Search**: Fetches the most viewed videos related to the query.
- **Article and Blog Search**: Fetches articles or blog posts related to the query.
- **Academic Paper Search**: Retrieves academic papers from arXiv.
- **Cross-Origin Requests**: CORS is enabled to allow communication between the frontend and backend.
- **Error Handling**: Displays appropriate messages in case of network issues or search errors.

## Learn More

To learn more about Flask, React, and the APIs used in this project, refer to the following documentation:

- [Flask Documentation](https://flask.palletsprojects.com/en/latest/)
- [React Documentation](https://reactjs.org/)
- [YouTube Data API](https://developers.google.com/youtube/v3)
- [Google Custom Search API](https://developers.google.com/custom-search/v1/overview)
- [arXiv API](https://arxiv.org/help/api)
