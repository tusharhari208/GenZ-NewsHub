import { useState } from "react";

function App() {
  const [category, setCategory] = useState("technology");
  const [news, setNews] = useState([]);

  const API_URL = "https://genz-newshub.onrender.com";

  const fetchNews = async () => {
    const res = await fetch(`${API_URL}/news?category=${category}`);
    const data = await res.json();
    setNews(data);
  };

  return (
    <div style={{ padding: "20px" }}>
      <h1>GenZ NewsHub</h1>

      <select onChange={(e) => setCategory(e.target.value)}>
        <option value="technology">Technology</option>
        <option value="sports">Sports</option>
        <option value="business">Business</option>
      </select>

      <button onClick={fetchNews} style={{ marginLeft: "10px" }}>
        Fetch News
      </button>

      {news.map((item, index) => (
        <div key={index}>
          <h3>{item.title}</h3>
          <p>{item.summary}</p>
          <a href={item.url} target="_blank" rel="noreferrer">
            Read Full Article
          </a>
        </div>
      ))}
    </div>
  );
}

export default App;
