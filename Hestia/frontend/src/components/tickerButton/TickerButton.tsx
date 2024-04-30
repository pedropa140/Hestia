import React from "react";
import { ticker } from "../../types/ticker";
import "./TickerButton.css";
function TickerButton({ ticker, index }: { ticker: ticker; index: number }) {
    return (
        <tr className={"Ticker-Button" + (index % 2 === 0 ? "" : " odd")}>
            <th>{ticker.ticker}</th>
            <th>{ticker.company}</th>
        </tr>
    );
}

export default TickerButton;
