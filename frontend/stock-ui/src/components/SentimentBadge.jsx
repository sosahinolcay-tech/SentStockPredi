export default function SentimentBadge({ score = 0 }) {
  // score expected between -1 and 1
  let bg = 'bg-gray-200 text-gray-800';
  if (score >= 0.5) bg = 'bg-green-200 text-green-800';
  else if (score > 0) bg = 'bg-lime-200 text-lime-800';
  else if (score < 0 && score >= -0.5) bg = 'bg-amber-200 text-amber-800';
  else if (score < -0.5) bg = 'bg-red-200 text-red-800';

  return (
    <span className={`px-3 py-1 rounded-full font-medium ${bg}`}>
      {score >= 0 ? '+' : ''}{(score*100).toFixed(0)}%
    </span>
  );
}
