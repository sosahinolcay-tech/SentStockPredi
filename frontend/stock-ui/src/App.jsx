import { useEffect, useState } from 'react'
import { getPrediction } from './api'
import StockChart from './components/StockChart'
import SentimentBadge from './components/SentimentBadge'
import HeadlinesTable from './components/HeadlinesTable'

function App() {
  const [ticker, setTicker] = useState('AAPL')
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState(null)
  const [forecast, setForecast] = useState([])
  const [history, setHistory] = useState([])
  const [sentiment, setSentiment] = useState(0)
  const [headlines, setHeadlines] = useState([])

  async function fetchFor(t) {
    setLoading(true)
    setError(null)
    try {
      const data = await getPrediction(t)
      setForecast(data.forecast || [])
      setHistory(data.history || [])
      setSentiment(typeof data.sentiment === 'number' ? data.sentiment : 0)
      setHeadlines(data.headlines || [])
    } catch (err) {
      setError(err.message || String(err))
    } finally {
      setLoading(false)
    }
  }

  useEffect(() => {
    fetchFor(ticker)
  }, [])

  return (
    <div className="min-h-screen bg-gradient-to-br from-gray-100 to-gray-300 pb-12" style={{fontFamily:'-apple-system,BlinkMacSystemFont,Segoe UI,Roboto,Helvetica Neue,Arial,sans-serif'}}>
      <div className="max-w-5xl mx-auto px-6">
        <header className="flex flex-col sm:flex-row items-center justify-between py-10 mb-10">
          <h1 className="text-4xl font-bold tracking-tight text-gray-900 drop-shadow-sm mb-4 sm:mb-0" style={{letterSpacing:'-0.02em'}}>SentStockPredi</h1>
          <div className="flex items-center gap-3 mt-4 sm:mt-0">
            <input
              className="border border-gray-300 bg-white/95 px-5 py-3 rounded-2xl shadow focus:outline-none focus:ring-2 focus:ring-blue-400 text-lg transition-all duration-150 placeholder-gray-400 font-medium"
              value={ticker}
              onChange={e => setTicker(e.target.value.toUpperCase())}
              aria-label="Ticker"
              placeholder="AAPL"
              style={{fontFamily:'-apple-system,BlinkMacSystemFont,Segoe UI,Roboto,Helvetica Neue,Arial,sans-serif', fontSize:'1.1rem', fontWeight:500}}
            />
            <button
              className="bg-blue-500 hover:bg-blue-600 text-white px-7 py-3 rounded-2xl shadow-md transition-all duration-150 font-semibold text-lg focus:outline-none focus:ring-2 focus:ring-blue-400"
              onClick={() => fetchFor(ticker)}
              style={{fontFamily:'-apple-system,BlinkMacSystemFont,Segoe UI,Roboto,Helvetica Neue,Arial,sans-serif', fontSize:'1.1rem', fontWeight:600}}
            >
              Fetch
            </button>
          </div>
        </header>

        {loading && <div className="mb-4 text-center text-gray-500 animate-pulse">Loading data…</div>}
        {error && <div className="text-red-600 mb-4 text-center">{error}</div>}

        <section className="grid grid-cols-1 lg:grid-cols-3 gap-10 mb-10">
          <div className="lg:col-span-2 bg-white/90 rounded-3xl shadow-xl p-8 backdrop-blur border border-gray-100">
            <StockChart history={history} forecast={forecast} />
          </div>
          <aside className="bg-white/90 rounded-3xl shadow-xl p-8 space-y-8 backdrop-blur border border-gray-100">
            <div>
              <h3 className="text-lg font-semibold text-gray-500 mb-3">Sentiment</h3>
              <div className="flex items-center gap-4">
                <SentimentBadge score={sentiment} />
                <div className="text-lg text-gray-600">Score</div>
              </div>
            </div>

            <div>
              <h3 className="text-lg font-semibold text-gray-500 mb-3">Recent headlines</h3>
              <HeadlinesTable items={headlines} />
            </div>
          </aside>
        </section>

  <footer className="text-xs text-gray-400 text-center mt-10">Tip: enter a ticker (e.g., MSFT) and press Fetch.</footer>
      </div>
    </div>
  )
}

export default App
