import React from "react";
import Navbar from "../../components/navbar/Navbar";
import "./Home.css";
import Tickers from "../../components/tickers/Tickers";
function Home() {
    return (
        <div className="home-app">
            <Navbar />
            <Tickers />
        </div>
    );
}

export default Home;
