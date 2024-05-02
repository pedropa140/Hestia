import axios from "axios";
import React, { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import { API_URL } from "../../constants";

interface data {
    ticker: string;
    company_name: string;
    start_date: string;
    end_date: string;
    book_value: number;
    book_to_share: number;
    earnings_per_share: number;
    debt_ratio: number;
    current_ratio: number;
    dividend_yield: number;
    start_open: number;
    start_high: number;
    end_open: number;
    end_close: number;
    end_high: number;
}
import "./Ticker.css";
function Ticker() {
    const { tickername } = useParams();

    const [Data, setData] = useState<data[]>([]);

    useEffect(() => {
        return () => {};
    }, [Data]);
    async function getCharts() {}
    async function getTicker() {
        let data = await axios.get(API_URL + "api/ticker-data/" + tickername);
    }

    return (
        <div className="row justify-content-center align-content-center full-page">
            <div className="col-xl-10 col-xxl-9">
                <div className="card shadow">
                    <div className="card-header d-flex flex-wrap justify-content-center align-items-center justify-content-sm-between gap-3">
                        <h5 className="display-6 text-nowrap text-capitalize mb-0">{tickername}</h5>
                        <div className="input-group input-group-sm w-auto">
                            {/* <input
                                className="form-control form-control-sm"
                                type="text"
                                placeholder="Search by ticker or company"
                                value={searchTerm}
                                onChange={(e) => setSearchTerm(e.target.value)}
                            /> */}
                        </div>
                    </div>
                    <div className="card-body">
                        <div className="table-responsive">
                            <table className="table table-striped table-hover">
                                {/* <thead>
                                    <tr>
                                        <th>Ticker</th>
                                        <th>Company Name</th>
                                    </tr>
                                </thead> */}
                                <tbody>
                                    <tr>
                                        <td>
                                            <img className="chart-img" src={API_URL + `/api/ticker/` + tickername + "/chart/book_to_share"}></img>
                                            <div className="text-center">Book to Share</div>
                                        </td>
                                        <td>
                                            <img className="chart-img" src={API_URL + `/api/ticker/` + tickername + "/chart/current_ratio"}></img>
                                            <div className="text-center">Current Ratio</div>
                                        </td>
                                        <td>
                                            <img className="chart-img" src={API_URL + `/api/ticker/` + tickername + "/chart/debt_ratio"}></img>
                                            <div className="text-center">Debt Ratio</div>
                                        </td>
                                    </tr>
                                    <tr>
                                        <td>
                                            <img className="chart-img" src={API_URL + `/api/ticker/` + tickername + "/chart/dividend_yield"}></img>
                                            <div className="text-center">Dividend Yield</div>
                                        </td>
                                        <td>
                                            <img
                                                className="chart-img"
                                                src={API_URL + `/api/ticker/` + tickername + "/chart/earnings_per_share"}
                                            ></img>
                                            <div className="text-center">Earnings Per Share</div>
                                        </td>
                                        <td>
                                            <img className="chart-img" src={API_URL + `/api/ticker/` + tickername + "/chart/stock_prices"}></img>
                                            <div className="text-center">Stock Price</div>
                                        </td>
                                    </tr>
                                    {/* <tr>
                                        <td>
                                            <img className="chart-img" src={API_URL + `/api/ticker/` + tickername + "/chart/book_to_share"}></img>
                                            <div className="text-center">Book to Share</div>
                                        </td>
                                        <td>
                                            <img className="chart-img" src={API_URL + `/api/ticker/` + tickername + "/chart/current_ratio"}></img>
                                            <div className="text-center">Current Ratio</div>
                                        </td>
                                        <td>
                                            <img className="chart-img" src={API_URL + `/api/ticker/` + tickername + "/chart/debt_ratio"}></img>
                                            <div className="text-center">Debt Ratio</div>
                                        </td>
                                    </tr>
                                    <tr>
                                        <td>
                                            <img className="chart-img" src={API_URL + `/api/ticker/` + tickername + "/chart/dividend_yield"}></img>
                                            <div className="text-center">Dividend Yield</div>
                                        </td>
                                        <td>
                                            <img
                                                className="chart-img"
                                                src={API_URL + `/api/ticker/` + tickername + "/chart/earnings_per_share"}
                                            ></img>
                                            <div className="text-center">Earnings Per Share</div>
                                        </td>
                                        <td>
                                            <img className="chart-img" src={API_URL + `/api/ticker/` + tickername + "/chart/stock_prices"}></img>
                                            <div className="text-center">Stock Price</div>
                                        </td> 
                                    </tr> */}
                                </tbody>
                            </table>
                        </div>
                    </div>
                    <div className="card-footer">
                        {/* <nav>
                            <ul className="pagination pagination-sm mb-0 justify-content-center">
                                <li className="page-item">
                                    <a className="page-link" aria-label="Previous" href="#" onClick={handlePrevPage}>
                                        <span aria-hidden="true">«</span>
                                    </a>
                                </li>
                                <li className="page-item">
                                    <a className="page-link" href="#">
                                        1
                                    </a>
                                </li>
                                <li className="page-item">
                                    <a className="page-link" href="#">
                                        2
                                    </a>
                                </li>
                                <li className="page-item">
                                    <a className="page-link" href="#">
                                        3
                                    </a>
                                </li>
                                <li className="page-item">
                                    <a className="page-link" aria-label="Next" href="#" onClick={handleNextPage}>
                                        <span aria-hidden="true">»</span>
                                    </a>
                                </li>
                            </ul>
                        </nav> */}
                    </div>
                </div>
            </div>
        </div>
    );
}

export default Ticker;
