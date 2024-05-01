import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { API_URL } from './constants';
import _ from 'lodash'; // Import lodash

type Ticker = {
  ticker: string;
  company: string;
};

const Companies: React.FC = () => {
  const [tickers, setTickers] = useState<Ticker[]>([]);
  const [currentPage, setCurrentPage] = useState<number>(1);
  const [searchTerm, setSearchTerm] = useState<string>(''); // State for search term
  const itemsPerPage = 10;

  useEffect(() => {
    const fetchTickers = async () => {
      try {
        const response = await axios.get(API_URL + '/api/tickers/');
        setTickers(response.data); // Assuming data is an array of Ticker objects
      } catch (error) {
        console.error('Error fetching data:', error);
      }
    };

    fetchTickers();
  }, []);

  const totalPages = Math.ceil(tickers.length / itemsPerPage);

  const handleNextPage = () => {
    if (currentPage < totalPages) {
      setCurrentPage((prevPage) => prevPage + 1);
    }
  };

  const handlePrevPage = () => {
    if (currentPage > 1) {
      setCurrentPage((prevPage) => prevPage - 1);
    }
  };

  const startIndex = (currentPage - 1) * itemsPerPage;
  const visibleTickers = tickers
    .filter((ticker) =>
      // Filter by similarity to search term using lodash
      _.includes(_.toLower(ticker.ticker), _.toLower(searchTerm)) ||
      _.includes(_.toLower(ticker.company), _.toLower(searchTerm))
    )
    .slice(startIndex, startIndex + itemsPerPage);

  return (
    <div>
      <h1>Companies</h1>
      <div>
        <input
          type="text"
          placeholder="Search by ticker or company"
          value={searchTerm}
          onChange={(e) => setSearchTerm(e.target.value)}
        />
      </div>
      <table>
        <thead>
          <tr>
            <th>Ticker</th>
            <th>Company</th>
          </tr>
        </thead>
        <tbody>
          {visibleTickers.map((ticker) => (
            <tr key={ticker.ticker} onClick={}>
              <td>{ticker.ticker}</td>
              <td>{ticker.company}</td>
            </tr>
          ))}
        </tbody>
      </table>
      <div>
        <button onClick={handlePrevPage} disabled={currentPage === 1}>
          Previous
        </button>
        <button onClick={handleNextPage} disabled={currentPage === totalPages}>
          Next
        </button>
      </div>
    </div>
  );
};

export default Companies;
