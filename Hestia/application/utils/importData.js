const fs = require('fs');

async function getStockData(symbol) {
  const apiKey = '1023s0ZC9ogHepq151jtapaFSdNV9mi4'; // Replace with your API key

  try {
    const response = await fetch(`https://api.polygon.io/v2/aggs/ticker/${symbol}/range/1/day/2023-01-01/2023-02-01?adjusted=true&sort=asc&limit=31&apiKey=${apiKey}`);
    const data = await response.json();
    console.log(data);
    const jsonString = JSON.stringify(data, null, 2);
    fs.writeFileSync("./utils/data.json", jsonString);
    console.log(jsonString)
    return data;
  } catch (error) {
    console.error('Error fetching stock data:', error);
  }
}

let dataPromise = getStockData('EGLE');
