import React, { useState, useEffect } from "react";
import NavigationBar from "../../components/NavigationBar";
import "./Financials.css";
// @ts-ignore
import Plotly from "plotly.js-dist";
const Financials = () => {
    const [ticker, setTicker] = useState("");

    useEffect(() => {
        console.log("hello");
    }, [ticker]);

    const handleInputChange = (event: React.ChangeEvent<HTMLInputElement>) => {
        setTicker(event.target.value.toUpperCase());
    };

    const handleSubmit = (event: React.MouseEvent<HTMLDivElement>) => {
        event.preventDefault();
        console.log("Ticker:", ticker);
        generatePriceGraphFromCSV(ticker);
        generateBVGraphFromCSV(ticker);
        generateEPSGraphFromCSV(ticker);
        generateCRGraphFromCSV(ticker);
        generateDRGraphFromCSV(ticker);
    };

    const fetchCSV = async (filename: string) => {
        console.log("Fetching");
        const response = await fetch(`/stockdata/div_info/${filename}.csv`);
        if (!response.ok) {
            throw new Error("Failed to fetch CSV file");
        }
        const csvText = await response.text();
        const csvData = csvText.split("\n").map((row) => row.split(","));
        return csvData;
    };

    const generatePriceGraphFromCSV = async (filename: string) => {
        try {
            const csvData = await fetchCSV(filename);

            const headers = csvData[0];
            let data = csvData.slice(1);

            const dateIndex = headers.indexOf("start_date");
            const openIndex = headers.indexOf("start_open");
            const closeIndex = headers.indexOf("start_close");
            const highIndex = headers.indexOf("start_high");
            const lowIndex = headers.indexOf("start_low");
            const endIndex = headers.indexOf("end_date");

            data = data.filter(
                (row) =>
                    row[dateIndex] !== "" &&
                    row[openIndex] !== "" &&
                    row[closeIndex] !== "" &&
                    row[highIndex] !== "" &&
                    row[lowIndex] !== "" &&
                    row[endIndex] !== ""
            );

            const dates = data.map((row) => row[dateIndex]);
            const openPrices = data.map((row) => parseFloat(row[openIndex]));
            const closePrices = data.map((row) => parseFloat(row[closeIndex]));
            const highPrices = data.map((row) => parseFloat(row[highIndex]));
            const lowPrices = data.map((row) => parseFloat(row[lowIndex]));

            // const startDate = new Date(Math.min(...(dates as any)));

            const traces = [
                { x: dates, y: openPrices, name: "Open", mode: "lines", type: "scatter" },
                { x: dates, y: closePrices, name: "Close", mode: "lines", type: "scatter" },
                { x: dates, y: highPrices, name: "High", mode: "lines", type: "scatter" },
                { x: dates, y: lowPrices, name: "Low", mode: "lines", type: "scatter" },
            ];

            const layout = {
                title: "Stock Prices Over Time",
                xaxis: { title: "Date" },
                yaxis: { title: "Price" },
            };

            Plotly.newPlot("graphContainer", traces, layout);
        } catch (error) {
            console.error("Error generating graph from CSV:", error);
        }
    };

    const generateBVGraphFromCSV = async (filename: string) => {
        try {
            const csvData = await fetchCSV(filename);

            const headers = csvData[0];
            let data = csvData.slice(1);

            const dateIndex = headers.indexOf("start_date");
            const bookValueIndex = headers.indexOf("book_value");

            // Filter out rows with missing values for dividend yield
            data = data.filter((row) => row[dateIndex] !== "" && row[bookValueIndex] !== "");

            const dates = data.map((row) => row[dateIndex]);
            const bookValue = data.map((row) => parseFloat(row[bookValueIndex]));

            const trace = {
                x: dates,
                y: bookValue,
                type: "scatter",
                mode: "lines",
                name: "Book Value",
            };

            const layout = {
                title: "Book Value Over Time",
                xaxis: { title: "Date" },
                yaxis: { title: "Book Value" },
            };

            Plotly.newPlot("bookValueGraphContainer", [trace], layout);
        } catch (error) {
            console.error("Error generating dividend yield graph from CSV:", error);
        }
    };

    const generateEPSGraphFromCSV = async (filename: string) => {
        try {
            const csvData = await fetchCSV(filename);

            const headers = csvData[0];
            let data = csvData.slice(1);

            const dateIndex = headers.indexOf("start_date");
            const epsIndex = headers.indexOf("earnings_per_share");

            // Filter out rows with missing values for dividend yield
            data = data.filter((row) => row[dateIndex] !== "" && row[epsIndex] !== "");

            const dates = data.map((row) => row[dateIndex]);
            const eps = data.map((row) => parseFloat(row[epsIndex]));

            const trace = {
                x: dates,
                y: eps,
                type: "scatter",
                mode: "lines",
                name: "Earnings per Share",
            };

            const layout = {
                title: "Earnings Per Share Over Time",
                xaxis: { title: "Date" },
                yaxis: { title: "Earnings/Share (bps)" },
            };

            Plotly.newPlot("epsGraphContainer", [trace], layout);
        } catch (error) {
            console.error("Error generating dividend yield graph from CSV:", error);
        }
    };
    const generateCRGraphFromCSV = async (filename: string) => {
        try {
            const csvData = await fetchCSV(filename);

            const headers = csvData[0];
            let data = csvData.slice(1);

            const dateIndex = headers.indexOf("start_date");
            const crIndex = headers.indexOf("current_ratio");

            // Filter out rows with missing values for dividend yield
            data = data.filter((row) => row[dateIndex] !== "" && row[crIndex] !== "");

            const dates = data.map((row) => row[dateIndex]);
            const cr = data.map((row) => parseFloat(row[crIndex]));

            const trace = {
                x: dates,
                y: cr,
                type: "scatter",
                mode: "lines",
                name: "Current Ratio",
            };

            const layout = {
                title: "Current Rator Over Time",
                xaxis: { title: "Date" },
                yaxis: { title: "Current Ratio" },
            };

            Plotly.newPlot("crGraphContainer", [trace], layout);
        } catch (error) {
            console.error("Error generating dividend yield graph from CSV:", error);
        }
    };

    const generateDRGraphFromCSV = async (filename: string) => {
        try {
            const csvData = await fetchCSV(filename);

            const headers = csvData[0];
            let data = csvData.slice(1);

            const dateIndex = headers.indexOf("start_date");
            const drIndex = headers.indexOf("debt_ratio");

            // Filter out rows with missing values for dividend yield
            data = data.filter((row) => row[dateIndex] !== "" && row[drIndex] !== "");

            const dates = data.map((row) => row[dateIndex]);
            const dr = data.map((row) => parseFloat(row[drIndex]));

            const trace = {
                x: dates,
                y: dr,
                type: "scatter",
                mode: "lines",
                name: "Debt Ratio",
            };

            const layout = {
                title: "Debt Ratio",
                xaxis: { title: "Date" },
                yaxis: { title: "Debt Ratio" },
            };

            Plotly.newPlot("drGraphContainer", [trace], layout);
        } catch (error) {
            console.error("Error generating dividend yield graph from CSV:", error);
        }
    };
    return (
        <div className="main">
            <NavigationBar />
            <div className="main-page-outline">
                <div className="header-text-box">
                    <p className="header-text">Company Fiscal Measurements</p>
                </div>
                <div className="graph-frame">
                    <div className="input">
                        <div className="textbox">
                            <input type="text" className="text-field-data" placeholder="Enter a Ticker" value={ticker} onChange={handleInputChange} />
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
                    <div className="header">Price</div>
                    <div className="content">
                        <div id="graphContainer" className="graph-container"></div>
                    </div>
                </div>
                <div className="graph">
                    <div className="header">Book Value</div>
                    <div className="content">
                        <div id="bookValueGraphContainer" className="graph-container"></div>
                    </div>
                </div>
                <div className="graph">
                    <div className="header">Earnings per Share</div>
                    <div className="content">
                        <div id="epsGraphContainer" className="graph-container"></div>
                    </div>
                </div>
                <div className="graph">
                    <div className="header">Current Ratio</div>
                    <div className="content">
                        <div id="crGraphContainer" className="graph-container"></div>
                    </div>
                </div>
                <div className="graph">
                    <div className="header">Debt Ratio</div>
                    <div className="content">
                        <div id="drGraphContainer" className="graph-container"></div>
                    </div>
                </div>
            </div>
        </div>
    );
};

export default Financials;
