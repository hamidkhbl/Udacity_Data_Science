var year = [1990, 2015];
var arable_land = [0.33933, 0.3885];

var trace1 = {
    x:year,
    y:arable_land,
    mode:'lines',
    type:'scatter'
};

var data = [trace1];

Plotly.plot("plot1",data);
