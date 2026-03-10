import React, { useState } from 'react';
import axios from 'axios';
import { Link } from 'react-router-dom';
import { Link as LinkIcon, Copy, ExternalLink, CheckCircle } from 'lucide-react';

const API_BASE_URL = 'http://127.0.0.1:8000';

const URLForm = () => {
  const [longUrl, setLongUrl] = useState('');
  const [shortenedData, setShortenedData] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');
  const [copied, setCopied] = useState(false);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setError('');
    setShortenedData(null);
    setCopied(false);

    try {
      const response = await axios.post(`${API_BASE_URL}/api/shorten`, {
        long_url: longUrl
      });
      setShortenedData({
        shortCode: response.data.short_code,
        shortUrl: `${API_BASE_URL}${response.data.short_url}`
      });
    } catch (err) {
      setError(err.response?.data?.error || 'Failed to shorten URL. Please try again.');
    } finally {
      setLoading(false);
    }
  };

  const copyToClipboard = () => {
    if (shortenedData) {
      navigator.clipboard.writeText(shortenedData.shortUrl);
      setCopied(true);
      setTimeout(() => setCopied(false), 2000);
    }
  };

  return (
    <div className="card form-container">
      <div className="card-header">
        <div className="icon-wrapper">
          <LinkIcon size={24} className="icon-gradient" />
        </div>
        <h2>Shorten Your Link</h2>
        <p>Create a short and memorable link to share.</p>
      </div>

      <form onSubmit={handleSubmit} className="url-form">
        <div className="input-group">
          <input
            type="url"
            value={longUrl}
            onChange={(e) => setLongUrl(e.target.value)}
            placeholder="Paste your long URL here... e.g., https://example.com/very/long/path"
            required
            className="url-input"
          />
          <button type="submit" className="submit-btn" disabled={loading}>
            {loading ? <span className="loader"></span> : 'Shorten'}
          </button>
        </div>
        {error && <div className="error-message">{error}</div>}
      </form>

      {shortenedData && (
        <div className="result-container fade-in">
          <div className="result-header">
            <h3>Your Short URL is Ready!</h3>
          </div>
          <div className="result-box">
            <a href={shortenedData.shortUrl} target="_blank" rel="noopener noreferrer" className="short-url">
              {shortenedData.shortUrl}
            </a>
            <div className="result-actions">
              <button 
                onClick={copyToClipboard} 
                className={`action-btn ${copied ? 'copied' : ''}`}
                title="Copy to clipboard"
              >
                {copied ? <CheckCircle size={18} /> : <Copy size={18} />}
              </button>
              <a 
                href={shortenedData.shortUrl} 
                target="_blank" 
                rel="noopener noreferrer"
                className="action-btn"
                title="Open link"
              >
                <ExternalLink size={18} />
              </a>
            </div>
          </div>
        </div>
      )}
    </div>
  );
};

export default URLForm;
