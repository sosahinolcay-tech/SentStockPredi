import React from 'react'

export default function LoadingSpinner({ size = 44 }) {
  const style = {
    width: size,
    height: size,
  }

  return (
    <div className="spinner" style={style} aria-hidden="true">
      <svg viewBox="0 0 50 50" className="spinner-svg">
        <circle className="spinner-track" cx="25" cy="25" r="20" fill="none" strokeWidth="4" />
        <path className="spinner-head" d="M25 5 a20 20 0 0 1 0 40" fill="none" strokeWidth="4" strokeLinecap="round" />
      </svg>
    </div>
  )
}
