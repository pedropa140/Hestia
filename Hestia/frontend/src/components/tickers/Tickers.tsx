import React, { useEffect, useState } from "react";
import { ticker } from "../../types/ticker";
import TickerButton from "../tickerButton/TickerButton";
import "./Tickers.css";
function Tickers() {
    const [Tickers, setTickers] = useState([] as ticker[]);
    const [FiltererTickers, SetFilteredTickers] = useState([] as ticker[]);
    const itemsPerTable = 10;
    const [Index, setIndex] = useState(0);

    useEffect(() => {
        setTickers([
            { ticker: "A", company: "THE A COMPANY" },
            { ticker: "A", company: "THE A COMPANY" },
            { ticker: "A", company: "THE A COMPANY" },
            { ticker: "A", company: "THE A COMPANY" },
            { ticker: "A", company: "THE A COMPANY" },
            { ticker: "A", company: "THE A COMPANY" },
            { ticker: "A", company: "THE A COMPANY" },
            { ticker: "A", company: "THE A COMPANY" },
            { ticker: "A", company: "THE A COMPANY" },
            { ticker: "A", company: "THE A COMPANY" },
            { ticker: "A", company: "THE A COMPANY" },
            { ticker: "A", company: "THE A COMPANY" },
            { ticker: "A", company: "THE A COMPANY" },
            { ticker: "A", company: "THE A COMPANY" },
            { ticker: "A", company: "THE A COMPANY" },
            { ticker: "A", company: "THE A COMPANY" },
            { ticker: "A", company: "THE A COMPANY" },
            { ticker: "A", company: "THE A COMPANY" },
            { ticker: "A", company: "THE A COMPANY" },
            { ticker: "A", company: "THE A COMPANY" },
            { ticker: "A", company: "THE A COMPANY" },
            { ticker: "A", company: "THE A COMPANY" },
            { ticker: "A", company: "THE A COMPANY" },
            { ticker: "A", company: "THE A COMPANY" },
            { ticker: "A", company: "THE A COMPANY" },
            { ticker: "A", company: "THE A COMPANY" },
            { ticker: "A", company: "THE A COMPANY" },
            { ticker: "A", company: "THE A COMPANY" },
            { ticker: "A", company: "THE A COMPANY" },
        ]);

        return () => {};
    }, []);
    useEffect(() => {
        const end = (Index + 1) * itemsPerTable;
        const start = end - itemsPerTable;
        SetFilteredTickers([...Tickers].splice(start, itemsPerTable));
        return () => {};
    }, [Index, Tickers]);
    async function next() {
        const nextPage = Index + 1;
        const end = itemsPerTable * nextPage;
        if (end > Tickers.length) {
            if (end - 10 > Tickers.length) {
                return;
            }
            setIndex(end);
        }
        setIndex(Index + 1);
    }
    async function prevPage() {
        const nextPage = Index - 1;
        if (nextPage < 0) {
            return;
        }
        setIndex(nextPage);
    }
    return (
        <div>
            <div>Search Bar</div>
            <div className="table-container">
                <table className="ticker-table">
                    <tr>
                        <th>Ticker</th>
                        <th>Company</th>
                    </tr>
                    {FiltererTickers.map((ticker, i) => (
                        <TickerButton ticker={ticker} index={i} />
                    ))}
                </table>
                <div className="ticker-table-menu">
                    <span onClick={() => prevPage()}>←</span>
                    <div>{Index}</div>
                    <span onClick={() => next()}>→</span>
                </div>
            </div>
        </div>
    );
}

export default Tickers;
