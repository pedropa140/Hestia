import React from 'react';
import './About.css';
import NavigationBar from '../../components/NavigationBar';
import logo from '../../icons/HestiaMain.jpeg'; 

const About = () => {
  return (
    <div>
      <NavigationBar />
      <div className="homepage">
        <div className="content">
          <h1>Hestia</h1>
          <p className="accent">As technology advances, more individuals have the opportunity to participate in retail investing. Similar to any other purchase, there is an inherent value associated with an investment. The purpose of this service is to highlight, explain and potentially forecast patterns in how factors such as book value, earnings, dividend yield, and profit-to-earnings ratios influence stock prices. The primary objective is to provide investors with access to company financial information and enable them to observe its impact on stock prices. While acknowledging that the concept of value is subjective, and a company's worth is influenced by various factors, this service aims to establish a foundational framework that investors can use to evaluate stocks. The ultimate goal of any investment is growth, and this service will specifically concentrate on the analysis of companies that offer dividends. The intention is to empower users with the capability to invest for both value and long-term growth. </p>
        </div>
        <div className="image-container">
          <img src={logo} alt="Homepage" />
        </div>
      </div>
    </div>
  );
};

export default About;
