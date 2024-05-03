import React from 'react';
import './NavigationBar.css'; 

import Container from 'react-bootstrap/Container';
import Nav from 'react-bootstrap/Nav';
import Navbar from 'react-bootstrap/Navbar';
import logo from '../icons/Hestia.jpeg'; 

function NavigationBar() {
  return (
    <Navbar expand="lg" className="custom-navbar bg-body-tertiary">
      <Container fluid>
        <Navbar.Brand href="/home">
          <img
            src={logo} // Image source
            alt="Hestia Logo" // Alternate text for accessibility
            width="30" // Adjust width as needed
            height="30" // Adjust height as needed
            className="d-inline-block align-top" // Bootstrap class to align image
          />
        </Navbar.Brand>
        <Navbar.Toggle aria-controls="navbarScroll" />
        <Navbar.Collapse id="navbarScroll">
          <Nav
            className="custom-nav me-auto my-2 my-lg-0"
            style={{ maxHeight: '100px' }}
            navbarScroll
          >
            <Nav.Link href="/home">Home</Nav.Link>
            <Nav.Link href="/dividend">Dividend and Price</Nav.Link>
            <Nav.Link href="/financial">Company Finacials</Nav.Link>
            <Nav.Link href="/predict">Prediction</Nav.Link>
            <Nav.Link href="/about">About</Nav.Link>
            <Nav.Link href="/info">Info</Nav.Link>
          </Nav>
        </Navbar.Collapse>
      </Container>
    </Navbar>
  );
}

export default NavigationBar;