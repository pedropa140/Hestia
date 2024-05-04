import React, { useEffect, useState } from "react";
import "./Prediction.css";
import NavigationBar from "../../components/NavigationBar";
// import logo from "../../icons/HestiaMain.jpeg";
const Prediction = () => {
    const models = [
        { name: "Mega Cap", value: "Mega-cap-best_svm_model.pkl" },
        { name: "Micro Cap", value: "Micro-cap-best_svm_model.pkl" },
        { name: "Mid Cap", value: "Mid-cap-best_svm_model.pkl" },
        { name: "Small Cap", value: "Small-cap-best_svm_model.pkl" },
        { name: "Large Cap", value: "Large-cap-best_svm_model.pkl" },
    ];

    const [Model, setModel] = useState("");
    const [ticker, setTicker] = useState("");
    const [Result, setResult] = useState("Please enter a ticker!");
    const [resultText, setResultText] = useState("");
    const [resultClass, setResultClass] = useState("");
    useEffect(() => {}, [ticker]);
    const fetchCSV = async (tickername: string) => {
        console.log("Fetching");
        const response = await fetch(`/stockdata/div_info/${tickername}.csv`);
        if (!response.ok) {
            throw new Error("Failed to fetch CSV file");
        }
        const csvText = await response.text();
        const csvData = csvText.split("\n").map((row) => row.split(","));
        return csvData;
    };
    const handleInputChange = (event: React.ChangeEvent<HTMLInputElement>) => {
        setTicker(event.target.value.toUpperCase());
    };
    async function updatePrediction() {
        const csvData = await fetchCSV(ticker);

        const headers = csvData[0];
        let data = csvData.slice(1);

        console.log(data[1]);
        let d = [data[1][4],data[1][5],data[1][6],data[1][7],data[1][8], data[1][9],data[1][1]]
        console.log(d)
       const response = await fetch(`http://localhost:5000/model`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json", // Specify that you're sending JSON data
            },
            body: JSON.stringify(d), // Convert the array to JSON string
        });
        const body = await response.json();
        let pred = body.prediction
        if (pred === 1) {
            setResultText(`${ticker} Is a Strong Buy`);
            setResultClass("green"); // Set the class for green color
        } else if (pred === 0) {
            setResultText(`${ticker} Is a Strong Hold`);
            setResultClass("blue"); // Set the class for blue color
        } else if (pred === -1) {
            setResultText(`${ticker} Is a Strong Sell`);
            setResultClass("red"); // Set the class for red color
        } else {
            setResultText("Unknown");
            setResultClass(""); // Set no specific class
        }
    }
    const handleSubmit = (event: React.MouseEvent<HTMLDivElement>) => {
        event.preventDefault();
        console.log("Ticker:", ticker);
        updatePrediction();
    };

    const getResultColor = (result) => {
    switch (result) {
        case '1':
            return 'green';
        case '-1':
            return 'red';
        case '0':
            return 'blue';
        default:
            return 'black'; // default color if result is not -1, 0, or 1
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
                <div className="main-body" style={{ textAlign: 'center' }}>
                    <div className={`main-body-text ${resultClass}`} style={{ fontSize: '54px', textAlign: 'center' }}>{resultText}</div>
                </div>
            </div>
        </div>
    );
};

export default Prediction;
