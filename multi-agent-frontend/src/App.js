import React, { useState } from 'react';

function App() {
  const [goal, setGoal] = useState('');
  const [result, setResult] = useState('');
  const [loading, setLoading] = useState(false);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setResult('');

    try {
      const response = await fetch('http://127.0.0.1:5000/run-agent', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ goal }),
      });
      const data = await response.json();
      if (response.ok) {
        setResult(JSON.stringify(data, null, 2));
      } else {
        setResult(data.error || 'Error occurred');
      }
    } catch (error) {
      setResult('Failed to connect to backend');
    }
    setLoading(false);
  };

  return (
    <div style={{ padding: 20 }}>
      <h1>Multi-Agent AI System</h1>
      <form onSubmit={handleSubmit}>
        <textarea
          rows={4}
          cols={50}
          value={goal}
          onChange={(e) => setGoal(e.target.value)}
          placeholder="Enter your goal here"
          required
        />
        <br />
        <button type="submit" disabled={loading}>
          {loading ? 'Processing...' : 'Run Agents'}
        </button>
      </form>

      {result && (
        <div style={{ marginTop: 20, whiteSpace: 'pre-wrap' }}>
          <h3>Result:</h3>
          <pre>{result}</pre>
        </div>
      )}
    </div>
  );
}

export default App;
