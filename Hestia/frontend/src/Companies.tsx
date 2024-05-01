import React, { useState, useEffect } from 'react';
import axios from 'axios'; // Import Axios

import { API_URL } from './constants';

type Ticker = {
    ticker: string;
    company: string;
};

const Companies: React.FC = () => {
  const [tickers, setTickers] = useState<Ticker[]>([]);

  useEffect(() => {
    const fetchTickers = async () => {
      try {
        const response = await axios.get(API_URL + '/api/tickers/'); // Use Axios.get() for GET requests
        console.log(response);
        setTickers(response.data); // Assuming data is an array of Ticker objects (Axios automatically parses JSON)
      } catch (error) {
        console.error('Error fetching data:', error);
      }
    };

    fetchTickers();
  }, []); // Empty dependency array for componentDidMount effect

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
