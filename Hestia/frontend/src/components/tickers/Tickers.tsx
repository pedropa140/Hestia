import React, { useEffect, useState } from "react";
import { ticker } from "../../types/ticker";
import TickerButton from "../tickerButton/TickerButton";
import "./Tickers.css";
function Tickers() {
    const [Tickers, setTickers] = useState([] as ticker[]);
    const [FiltererTickers, SetFilteredTickers] = useState([] as ticker[]);
    useEffect(() => {
        setTickers([
            { name: "A", company: "THE A COMPANY" },
            { name: "A", company: "THE A COMPANY" },
            { name: "A", company: "THE A COMPANY" },
            { name: "A", company: "THE A COMPANY" },
            { name: "A", company: "THE A COMPANY" },
            { name: "A", company: "THE A COMPANY" },
            { name: "A", company: "THE A COMPANY" },
            { name: "A", company: "THE A COMPANY" },
            { name: "A", company: "THE A COMPANY" },
            { name: "A", company: "THE A COMPANY" },
            { name: "A", company: "THE A COMPANY" },
        ]);

        return () => {};
    }, []);

    return (
        <div>
            <div>Search Bar</div>
            <table className="ticker-table">
                <tr>
                    <th>Ticker</th>
                    <th>Company</th>
                </tr>
                {Tickers.map((ticker, i) => (
                    <TickerButton ticker={ticker} index={i} />
                ))}
            </table>
        </div>
    );
}

export default Tickers;
