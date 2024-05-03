import React, { useState, useEffect } from 'react';
import NavigationBar from '../../components/NavigationBar';
import './Home.css';
import Plotly from 'plotly.js-dist';
const HomePage = () => {
    const [ticker, setTicker] = useState('');
    useEffect(() => {
        console.log("hello")
    }, [ticker]);

    const handleInputChange = (event: React.ChangeEvent<HTMLInputElement>) => {
        setTicker(event.target.value.toUpperCase());
    };

    const handleSubmit = (event: React.MouseEvent<HTMLDivElement>) => {
        event.preventDefault();
        console.log('Ticker:', ticker);
        generatePriceGraphFromCSV(ticker);
        generateDividendYieldGraphFromCSV(ticker);
    };

    const fetchCSV = async (filename: string) => {
        console.log("Fetching")
        const response = await fetch(`/stockdata/div_info/${filename}.csv`);
        if (!response.ok) {
            throw new Error('Failed to fetch CSV file');
        }
        const csvText = await response.text();
        const csvData = csvText.split('\n').map(row => row.split(','));
        return csvData;
    };

    const generatePriceGraphFromCSV = async (filename: string) => {
        try {
          
            const csvData = await fetchCSV(filename);

       
            const headers = csvData[0];
            let data = csvData.slice(1);

            const dateIndex = headers.indexOf('start_date');
            const openIndex = headers.indexOf('start_open');
            const closeIndex = headers.indexOf('start_close');
            const highIndex = headers.indexOf('start_high');
            const lowIndex = headers.indexOf('start_low');
            const endIndex = headers.indexOf('end_date');

             data = data.filter(row =>
                row[dateIndex] !== '' &&
                row[openIndex] !== '' &&
                row[closeIndex] !== '' &&
                row[highIndex] !== '' &&
                row[lowIndex] !== '' &&
                row[endIndex] !== ''
            );


            const dates = data.map(row => row[dateIndex]);
            const openPrices = data.map(row => parseFloat(row[openIndex]));
            const closePrices = data.map(row => parseFloat(row[closeIndex]));
            const highPrices = data.map(row => parseFloat(row[highIndex]));
            const lowPrices = data.map(row => parseFloat(row[lowIndex]));

            const startDate = new Date(Math.min(...dates));

            const traces = [
                { x: dates, y: openPrices, name: 'Open', mode: 'lines', type: 'scatter' },
                { x: dates, y: closePrices, name: 'Close', mode: 'lines', type: 'scatter' },
                { x: dates, y: highPrices, name: 'High', mode: 'lines', type: 'scatter' },
                { x: dates, y: lowPrices, name: 'Low', mode: 'lines', type: 'scatter' }
            ];

            const layout = {
                title: 'Stock Prices Over Time',
                xaxis: { title: 'Date' },
                yaxis: { title: 'Price' }
            };

            Plotly.newPlot('graphContainer', traces, layout);
        } catch (error) {
            console.error('Error generating graph from CSV:', error);
        }
    };

    const generateDividendYieldGraphFromCSV = async (filename: string ) => {
        try {
            const csvData = await fetchCSV(filename);

            const headers = csvData[0];
            let data = csvData.slice(1);

            const dateIndex = headers.indexOf('start_date');
            const dividendYieldIndex = headers.indexOf('dividend_yield_ratio');

            // Filter out rows with missing values for dividend yield
            data = data.filter(row =>
                row[dateIndex] !== '' &&
                row[dividendYieldIndex] !== ''
            );

            const dates = data.map(row => row[dateIndex]);
            const dividendYield = data.map(row => parseFloat(row[dividendYieldIndex]));

            const trace = {
                x: dates,
                y: dividendYield,
                type: 'scatter',
                mode: 'lines',
                name: 'Dividend Yield Ratio'
            };

            const layout = {
                title: 'Dividend Yield Ratio Over Time',
                xaxis: { title: 'Date' },
                yaxis: { title: 'Dividend Yield Ratio' }
            };

            Plotly.newPlot('dividendYieldGraphContainer', [trace], layout);
        } catch (error) {
            console.error('Error generating dividend yield graph from CSV:', error);
        }
    };
    return (
        <div className="main">
            <NavigationBar />
            <div className="main-page-outline">
                <div className="header-text-box">
                    <p className="header-text">Company Price and Yield</p>
                </div>
                <div className="graph-frame">
                    <div className="input">
                        <div className="textbox">
                            <input type="text" className="text-field-data" placeholder="Enter a Ticker" value={ticker} onChange={handleInputChange}/>
                        </div>
                        <div className="submit-button" onClick={handleSubmit}>
                            <div className="submit">Submit</div>
                        </div>
                    </div>
                    <div className="text-box">
                        <p className="bold-text">{ticker.toUpperCase()}</p>
                    </div>
                </div>
                <div className="graph">
                    <div className="header">Price Graph</div>
                    <div className="content">
                        <div id="graphContainer" className="graph-container"></div>
                    </div>
                </div>
                <div className="graph">
                    <div className="header">Dividend Yeild Ratio</div>
                    <div className="content">
                        <div id="dividendYieldGraphContainer" className="graph-container"></div>
                    </div>
                </div>
              
            </div>
        </div>
    );
};

export default HomePage;
