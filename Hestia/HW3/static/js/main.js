async function fetchModelData() {
    try {
        const response = await fetch('/main/data');
        const data = await response.json();

        // console.log(data);
        return data;

    } catch (error) {
        console.error('Error fetching model data:', error);
    }
}

function createCPlot(dataPoints) {
    var margin = { top: 10, right: 30, bottom: 30, left: 60 },
        width = 460 - margin.left - margin.right,
        height = 400 - margin.top - margin.bottom;

    var svg = d3.select(".pe-ratio")
        .append("svg")
        .attr("width", width + margin.left + margin.right)
        .attr("height", height + margin.top + margin.bottom)
        .append("g")
        .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

    // Extract date and closeprice values from dataPoints
    var parsedData = dataPoints.map(d => ({ date: new Date(d.date), closeprice: d.closeprice }));

    var xScale = d3.scaleTime()
        .domain(d3.extent(parsedData, d => d.date))
        .range([0, width]);

    var yScale = d3.scaleLinear()
        .domain([0, d3.max(parsedData, d => d.closeprice)])
        .range([height, 0]);

    var line = d3.line()
        .x(d => xScale(d.date))
        .y(d => yScale(d.closeprice))
        .curve(d3.curveMonotoneX);

    svg.append("path")
        .datum(parsedData)
        .attr("fill", "none")
        .attr("stroke", "steelblue")
        .attr("stroke-width", 1.5)
        .attr("d", line);

    // Add X axis
    svg.append("g")
        .attr("transform", "translate(0," + height + ")")
        .call(d3.axisBottom(xScale));

    // Add Y axis
    svg.append("g")
        .call(d3.axisLeft(yScale));
}

function createOPlot(dataPoints) {
    var margin = { top: 10, right: 30, bottom: 30, left: 60 },
        width = 460 - margin.left - margin.right,
        height = 400 - margin.top - margin.bottom;

    var svg = d3.select(".dividend-growth")
        .append("svg")
        .attr("width", width + margin.left + margin.right)
        .attr("height", height + margin.top + margin.bottom)
        .append("g")
        .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

    // Extract date and closeprice values from dataPoints
    var parsedData = dataPoints.map(d => ({ date: new Date(d.date), openprice: d.openprice }));

    var xScale = d3.scaleTime()
        .domain(d3.extent(parsedData, d => d.date))
        .range([0, width]);

    var yScale = d3.scaleLinear()
        .domain([0, d3.max(parsedData, d => d.openprice)])
        .range([height, 0]);

    var line = d3.line()
        .x(d => xScale(d.date))
        .y(d => yScale(d.openprice))
        .curve(d3.curveMonotoneX);

    svg.append("path")
        .datum(parsedData)
        .attr("fill", "none")
        .attr("stroke", "steelblue")
        .attr("stroke-width", 1.5)
        .attr("d", line);

    // Add X axis
    svg.append("g")
        .attr("transform", "translate(0," + height + ")")
        .call(d3.axisBottom(xScale));

    // Add Y axis
    svg.append("g")
        .call(d3.axisLeft(yScale));
}

function createLPlot(dataPoints) {
    var margin = { top: 10, right: 30, bottom: 30, left: 60 },
        width = 460 - margin.left - margin.right,
        height = 400 - margin.top - margin.bottom;

    var svg = d3.select(".book-value-share")
        .append("svg")
        .attr("width", width + margin.left + margin.right)
        .attr("height", height + margin.top + margin.bottom)
        .append("g")
        .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

    // Extract date and closeprice values from dataPoints
    var parsedData = dataPoints.map(d => ({ date: new Date(d.date), low: d.low }));

    var xScale = d3.scaleTime()
        .domain(d3.extent(parsedData, d => d.date))
        .range([0, width]);

    var yScale = d3.scaleLinear()
        .domain([0, d3.max(parsedData, d => d.low)])
        .range([height, 0]);

    var line = d3.line()
        .x(d => xScale(d.date))
        .y(d => yScale(d.low))
        .curve(d3.curveMonotoneX);

    svg.append("path")
        .datum(parsedData)
        .attr("fill", "none")
        .attr("stroke", "steelblue")
        .attr("stroke-width", 1.5)
        .attr("d", line);

    // Add X axis
    svg.append("g")
        .attr("transform", "translate(0," + height + ")")
        .call(d3.axisBottom(xScale));

    // Add Y axis
    svg.append("g")
        .call(d3.axisLeft(yScale));
}

function createVPlot(dataPoints) {
    var margin = { top: 10, right: 30, bottom: 30, left: 60 },
        width = 460 - margin.left - margin.right,
        height = 400 - margin.top - margin.bottom;

    var svg = d3.select(".divident-percentage")
        .append("svg")
        .attr("width", width + margin.left + margin.right)
        .attr("height", height + margin.top + margin.bottom)
        .append("g")
        .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

    // Extract date and closeprice values from dataPoints
    var parsedData = dataPoints.map(d => ({ date: new Date(d.date), volume: d.volume }));

    var xScale = d3.scaleTime()
        .domain(d3.extent(parsedData, d => d.date))
        .range([0, width]);

    var yScale = d3.scaleLinear()
        .domain([0, d3.max(parsedData, d => d.volume)])
        .range([height, 0]);

    var line = d3.line()
        .x(d => xScale(d.date))
        .y(d => yScale(d.volume))
        .curve(d3.curveMonotoneX);

    svg.append("path")
        .datum(parsedData)
        .attr("fill", "none")
        .attr("stroke", "steelblue")
        .attr("stroke-width", 1.5)
        .attr("d", line);

    // Add X axis
    svg.append("g")
        .attr("transform", "translate(0," + height + ")")
        .call(d3.axisBottom(xScale));

    // Add Y axis
    svg.append("g")
        .call(d3.axisLeft(yScale));
}

function createHPlot(dataPoints) {
    var margin = { top: 10, right: 30, bottom: 30, left: 60 },
        width = 460 - margin.left - margin.right,
        height = 400 - margin.top - margin.bottom;

    var svg = d3.select(".book-value")
        .append("svg")
        .attr("width", width + margin.left + margin.right)
        .attr("height", height + margin.top + margin.bottom)
        .append("g")
        .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

    // Extract date and closeprice values from dataPoints
    var parsedData = dataPoints.map(d => ({ date: new Date(d.date), high: d.high }));

    var xScale = d3.scaleTime()
        .domain(d3.extent(parsedData, d => d.date))
        .range([0, width]);

    var yScale = d3.scaleLinear()
        .domain([0, d3.max(parsedData, d => d.high)])
        .range([height, 0]);

    var line = d3.line()
        .x(d => xScale(d.date))
        .y(d => yScale(d.high))
        .curve(d3.curveMonotoneX);

    svg.append("path")
        .datum(parsedData)
        .attr("fill", "none")
        .attr("stroke", "steelblue")
        .attr("stroke-width", 1.5)
        .attr("d", line);

    // Add X axis
    svg.append("g")
        .attr("transform", "translate(0," + height + ")")
        .call(d3.axisBottom(xScale));

    // Add Y axis
    svg.append("g")
        .call(d3.axisLeft(yScale));
}


document.addEventListener('DOMContentLoaded', function () {
  var frame3 = document.querySelector('.frame-3');
  var frame6 = document.querySelector('.frame-6');
  var frame7 = document.querySelector('.frame-7');

  // Add click event listener for frame-3
  frame3.addEventListener('click', function () {
    // Navigate to the next page when frame-3 is clicked
    window.location.href = '';
  });

  // Add click event listener for frame-6
  frame6.addEventListener('click', function () {
    // Navigate to the next page when frame-6 is clicked
    window.location.href = 'about';
  });

  frame7.addEventListener('click', function () {
    // Navigate to the next page when frame-7 is clicked
    window.location.href = 'help';
  });
  fetchModelData().then(dataPoints => {
        
        createOPlot(dataPoints);
        createCPlot(dataPoints);
        createLPlot(dataPoints);
        createVPlot(dataPoints);
        createHPlot(dataPoints);
    });
 




});