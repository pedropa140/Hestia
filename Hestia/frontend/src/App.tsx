import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Home from './pages/Home/Home'; 
import Financials from './pages/Financials/Financials'; 

const App: React.FC = () => {
  return (
    <Router>
      <Routes>
        <Route path="/financial" element={<Financials />} /> 
        <Route path="/dividend" element={<Home />} /> 
      </Routes>
    </Router>
  );
};

export default App;
