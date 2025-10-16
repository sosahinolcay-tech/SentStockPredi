import axios from "axios";

const BASE = import.meta.env.VITE_API_URL || "http://127.0.0.1:5000";

export async function getPrediction(ticker) {
  const res = await axios.get(`${BASE}/predict?ticker=${encodeURIComponent(ticker)}`);
  return res.data;
}

export default { getPrediction };
