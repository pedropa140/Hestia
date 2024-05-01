import React, { useState, useEffect } from 'react';

type Ticker = {
  ticker: string;
  company: string;
};

const Companies: React.FC = () => {
  const [tickers, setTickers] = useState<Ticker[]>([]);

  useEffect(() => {
    const fetchTickers = async () => {
      try {
        const response = await fetch('/api/tickers/');
        console.log(response)
        if (!response.ok) {
          throw new Error('Failed to fetch data');
        }
        const data = await response.json();
        setTickers(data); // Assuming data is an array of Ticker objects
      } catch (error) {
        console.error('Error fetching data:', error);
      }
    };

    fetchTickers();
  }, []);

  return (
    <div>
      <h1>Companies</h1>
      <table>
        <thead>
          <tr>
            <th>Ticker</th>
            <th>Company</th>
          </tr>
        </thead>
        <tbody>
          {tickers.map((ticker) => (
            <tr key={ticker.ticker}>
              <td>{ticker.ticker}</td>
              <td>{ticker.company}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default Companies;
