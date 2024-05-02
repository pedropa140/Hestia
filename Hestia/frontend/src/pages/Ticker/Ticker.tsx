import React, { useEffect } from "react";
import { useParams } from "react-router-dom";

function Ticker() {
    const { tickername } = useParams();

    useEffect(() => {
        return () => {};
    }, []);

    async function getTicker() {}

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
                            {/* <table className="table table-striped table-hover">
                                <thead>
                                    <tr>
                                        <th>Ticker</th>
                                        <th>Company Name</th>
                                    </tr>
                                </thead>
                                <tbody>
                                    {visibleTickers.map((ticker) => (
                                        <tr key={ticker.ticker}>
                                            <td>{ticker.ticker}</td>
                                            <td>{ticker.company}</td>
                                        </tr>
                                    ))}
                                </tbody>
                            </table> */}
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
