export default function HeadlinesTable({ items = [] }) {
  return (
    <div className="overflow-auto max-h-48">
      <table className="min-w-full text-base font-normal" style={{fontFamily:'-apple-system,BlinkMacSystemFont,Segoe UI,Roboto,Helvetica Neue,Arial,sans-serif'}}>
        <thead>
          <tr className="text-left text-xs text-gray-400 border-b">
            <th className="pb-2 font-medium">When</th>
            <th className="pb-2 font-medium">Headline</th>
            <th className="pb-2 font-medium">Sentiment</th>
          </tr>
        </thead>
        <tbody>
          {items.map((it, idx) => (
            <tr key={idx} className="border-t hover:bg-gray-100 transition-colors">
              <td className="py-2 align-top text-gray-500 whitespace-nowrap">{it.when || ''}</td>
              <td className="py-2 text-gray-900">{it.title}</td>
              <td className="py-2 align-top text-gray-500">{it.sentiment?.toFixed ? it.sentiment.toFixed(2) : ''}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}
