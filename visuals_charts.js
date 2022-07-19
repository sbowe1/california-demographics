// require("https://cdn.jsdelivr.net/npm/chart.js");
// import Chart from 'chart.js';
// const Chart = require('chart.js');

const data4 = {
    datasets: [{
      label: 'Scatter Dataset',
      data: [{
        x: -10,
        y: 0
      }, {
        x: 0,
        y: 10
      }, {
        x: 10,
        y: 5
      }, {
        x: 0.5,
        y: 5.5
      }],
      backgroundColor: 'rgb(255, 99, 132)'
    }],
  };
  
  const config4 = {
    type: 'scatter',
    data: data4,
    options: {
      scales: {
        x: {
          type: 'linear',
          position: 'bottom'
        }
      }
    }
  };
  
  const myChart4 = new Chart(
    document.getElementById('myChart4'),
    config4
  );