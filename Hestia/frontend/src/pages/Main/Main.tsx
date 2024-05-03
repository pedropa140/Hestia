import React from 'react';
import './Main.css';
import NavigationBar from '../../components/NavigationBar';
import logo from '../../icons/HestiaMain.jpeg'; 

const Main = () => {
  return (
    <div>
      <NavigationBar />
      <div className="homepage">
        <div className="content">
          <h1>Welcome to Hestia</h1>
          <p className="accent">Hearth and Value</p>
        </div>
        <div className="image-container">
          <img src={logo} alt="Homepage" />
        </div>
      </div>
    </div>
  );
};

export default Main;
