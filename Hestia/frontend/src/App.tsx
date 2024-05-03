import React from "react";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import Home from "./pages/Home/Home";
import Financials from "./pages/Financials/Financials";
import Main from "./pages/Main/Main";
import About from "./pages/About/About";
import Info from "./pages/Info/Info";
import Prediction from "./pages/Prediction/Prediction";
const App: React.FC = () => {
    return (
        <Router>
            <Routes>
                <Route path="/financial" element={<Financials />} />
                <Route path="/dividend" element={<Home />} />
                <Route path="/home" element={<Main />} />
                <Route path="/predict" element={<Prediction />} />
                <Route path="/info" element={<Info />} />
                <Route path="/about" element={<About />} />
            </Routes>
        </Router>
    );
};
export default App;
