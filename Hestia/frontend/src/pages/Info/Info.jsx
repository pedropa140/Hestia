import React from 'react';
import './Info.css';
import NavigationBar from '../../components/NavigationBar';
import logo from '../../icons/Hestia2.jpeg'; 

const Info = () => {
  return (
    <div>
      <NavigationBar />
      <div className="homepage">
        <div className="content">
          <h1>Infromation about Hestia</h1>
          <p className="accent">In ancient Greek religion and mythology, Hestia (/ˈhɛstiə, ˈhɛstʃə/; Greek: Ἑστία, meaning "hearth" or "fireside") is the virgin goddess of the hearth and the home. In myth, she is the firstborn child of the Titans Cronus and Rhea, and one of the Twelve Olympians.[1]

According to ancient Greek tradition, Hestia, along with four of her five siblings, was devoured by her own father Cronus as an infant due to his fear of being overthrown by one of his offspring, and was only freed when her youngest brother Zeus forced their father to disgorge the children he had eaten. Cronus and the rest of the Titans were cast down, and Hestia then became one of the Olympian gods, the new rulers of the cosmos, alongside her brothers and sisters. After the establishment of the new order and in spite of her status, Hestia withdraws from prominence in mythology, with few and sparse appearances in tales. Like Athena and Artemis, Hestia elected never to marry and remain an eternal virgin goddess instead, forever tending to the hearth of Olympus (becoming the first Vestal Virgin).

Despite her limited mythology, Hestia remained a very important goddess in ancient Greek society. Greek custom required that as the goddess of sacrificial fire, Hestia should receive the first offering at every sacrifice in the household. In the public domain, the hearth of the prytaneum functioned as her official sanctuary. Whenever a new colony was established, a flame from Hestia's public hearth in the mother city would be carried to the new settlement. The goddess Vesta is her Roman equivalent.</p>
        </div>
        <div className="image-container">
          <img src={logo} alt="Homepage" />
        </div>
      </div>
    </div>
  );
};

export default Info;
