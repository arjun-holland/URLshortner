import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import URLForm from './components/URLForm';

function App() {
  return (
    <Router>
      <div className="app-container">
        <header className="app-header fade-in-down">
          <div className="logo-container">
            <div className="logo-icon">🔗</div>
            <h1>URL SHORTNER</h1>
          </div>
          <p className="subtitle">Fast, Secure & Scalable URL Shortener</p>
        </header>

        <main className="app-main">
          <Routes>
            <Route path="/" element={<URLForm />} />
          </Routes>
        </main>

        <footer className="app-footer">
          <p>&copy; {new Date().getFullYear()} URL SHORTNER. Built with React & Django.</p>
        </footer>
      </div>
    </Router>
  );
}

export default App;
