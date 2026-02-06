import { useState } from "react";

function App() {
  const [category, setCategory] = useState("technology");
  const [news, setNews] = useState([]);

  const fetchNews = async () => {
    const res = await fetch(`http://localhost:8000/news?category=${category}`);
    const data = await res.json();
    setNews(data);
  };

  return (
    <div style={{ padding: "20px" }}>
      <h1>📰 GenZ NewsHub</h1>

      <select onChange={(e) => setCategory(e.target.value)}>
        <option value="technology">Technology</option>
        <option value="sports">Sports</option>
        <option value="business">Business</option>
        <option value="health">Health</option>
      </select>

      <button onClick={fetchNews}>Fetch News</button>

     {news.map((item, index) => (
  <div key={index} style={{ border: "1px solid #ccc", marginTop: "10px", padding: "10px" }}>
    <h3>{item.title}</h3>
    <pre>{item.summary}</pre>

    <p>
      <strong>Sentiment:</strong> {item.sentiment} <br />
      <strong>Credibility:</strong> {item.credibility}
    </p>

    <a href={item.url} target="_blank" rel="noreferrer">Read Full Article</a>
  </div>
))}
