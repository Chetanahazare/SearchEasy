import React, { useState } from 'react';
import './App.css';

const App = () => {
  const [query, setQuery] = useState('');
  const [results, setResults] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const handleSearch = async () => {
    setLoading(true);
    setError(null);
    try {
      const response = await fetch(`http://127.0.0.1:5000/search?query=${query}`);
      if (!response.ok) throw new Error('Network response was not ok');
      const data = await response.json();
      setResults(data);
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="container">
      <h1>Search for Resources</h1>
      <input
        type="text"
        value={query}
        onChange={(e) => setQuery(e.target.value)}
        placeholder="Enter your search query"
      />
      <button onClick={handleSearch}>Search</button>

      {loading && <p>Loading...</p>}
      {error && <p className="error">{error}</p>}
      
      {results && (
        <div>
          <h2>YouTube Videos</h2>
          <ul>
            {results.YouTube.map((video, index) => (
              <li key={index}>
                <a href={video.link} target="_blank" rel="noopener noreferrer">{video.title}</a>
              </li>
            ))}
          </ul>
          
          <h2>Articles/Blogs</h2>
          <ul>
            {results['Articles/Blogs'].map((article, index) => (
              <li key={index}>
                <a href={article.link} target="_blank" rel="noopener noreferrer">{article.title}</a>
              </li>
            ))}
          </ul>
          
          <h2>Academic Papers</h2>
          <ul>
            {results['Academic Papers'].map((paper, index) => (
              <li key={index}>
                <a href={paper.link} target="_blank" rel="noopener noreferrer">{paper.title}</a>
              </li>
            ))}
          </ul>
        </div>
      )}
    </div>
  );
};

export default App;




