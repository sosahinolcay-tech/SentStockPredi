import Plot from 'react-plotly.js';
import Plotly from 'plotly.js-basic-dist';

export default function StockChart({ history = [], forecast = [] }) {
  const traceHistory = {
    x: history.map(d => d.date),
    y: history.map(d => d.price),
    type: 'scatter',
    mode: 'lines',
    name: 'Actual',
    line: { color: '#007aff', width: 3 }
  };

  const traceForecast = {
    x: forecast.map(d => d.date),
    y: forecast.map(d => d.price),
    type: 'scatter',
    mode: 'lines',
    name: 'Forecast',
    line: { dash: 'dot', color: '#34c759', width: 3 }
  };

  return (
    <div className="w-full h-96">
      <Plot
        data={[traceHistory, traceForecast]}
        layout={{
          autosize: true,
          margin: { t: 30, r: 20, l: 40, b: 40 },
          legend: { orientation: 'h', font: { family: 'SF Pro Display, -apple-system, BlinkMacSystemFont, Segoe UI, Roboto, Helvetica Neue, Arial, sans-serif', size: 14 } },
          font: { family: 'SF Pro Display, -apple-system, BlinkMacSystemFont, Segoe UI, Roboto, Helvetica Neue, Arial, sans-serif', size: 16 },
          plot_bgcolor: 'rgba(255,255,255,0.95)',
          paper_bgcolor: 'rgba(255,255,255,0.95)',
          xaxis: { showgrid: false, zeroline: false },
          yaxis: { showgrid: true, gridcolor: '#e5e5ea', zeroline: false },
        }}
        style={{ width: '100%', height: '100%' }}
        useResizeHandler
        plotly={Plotly}
      />
    </div>
  );
}
