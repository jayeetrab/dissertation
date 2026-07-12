import React, { useState } from 'react'
import HallucinationTag from './HallucinationTag.jsx'

/**
 * ScorePanel — scoring controls for one system output (baseline or rag).
 *
 * Props:
 *   system         {string}   'baseline' | 'rag'
 *   resultId       {string}   UUID of the parent TaskResult
 *   output         {string}   The text output to be scored
 *   existingScore  {object?}  Pre-populated scores (if already scored)
 *   onSaved        {fn}       Called after a successful save
 *   apiBase        {string}   e.g. 'http://localhost:8000'
 */
export default function ScorePanel({ system, resultId, output, existingScore, onSaved, apiBase }) {
  const [accuracy,     setAccuracy]     = useState(existingScore?.accuracy || 0)
  const [completeness, setCompleteness] = useState(existingScore?.completeness || 0)
  const [usefulness,   setUsefulness]   = useState(existingScore?.planning_usefulness || 0)
  const [grounding,    setGrounding]    = useState(existingScore?.grounding || 0)

  const [hallucPresent, setHallucPresent] = useState(existingScore?.hallucination_present || false)
  const [hallucType,    setHallucType]    = useState(existingScore?.hallucination_type || 'none')
  const [hallucDetail,  setHallucDetail]  = useState(existingScore?.hallucination_detail || '')
  const [notes,         setNotes]         = useState(existingScore?.scorer_notes || '')

  const [saving, setSaving] = useState(false)
  const [saved,  setSaved]  = useState(false)
  const [error,  setError]  = useState(null)

  const color = system === 'baseline' ? 'var(--amber)' : 'var(--green)'
  const title = system === 'baseline' ? 'Baseline LLM' : 'RAG System'

  // ── Score radio helper ──────────────────────────────────────
  const ScoreRadio = ({ id, value, onChange, max = 5 }) => (
    <div className="score-group">
      {Array.from({ length: max }, (_, i) => i + 1).map(n => (
        <div key={n} className="score-option">
          <input
            type="radio"
            id={`${id}-${n}`}
            name={id}
            value={n}
            checked={value === n}
            onChange={() => onChange(n)}
          />
          <label htmlFor={`${id}-${n}`}>{n}</label>
        </div>
      ))}
    </div>
  )

  // ── Save handler ────────────────────────────────────────────
  const handleSave = async () => {
    if (!accuracy || !completeness || !usefulness) {
      setError('Please fill in Accuracy, Completeness and Usefulness scores before saving.')
      return
    }
    setError(null)
    setSaving(true)

    try {
      const res = await fetch(`${apiBase}/score/${resultId}`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          result_id:             resultId,
          system,
          accuracy,
          completeness,
          planning_usefulness:   usefulness,
          grounding,
          hallucination_present: hallucPresent,
          hallucination_type:    hallucType,
          hallucination_detail:  hallucDetail,
          scorer_notes:          notes,
        }),
      })

      if (!res.ok) {
        const msg = await res.text()
        throw new Error(msg)
      }

      setSaved(true)
      onSaved?.()
      setTimeout(() => setSaved(false), 2500)
    } catch (e) {
      setError(`Save failed: ${e.message}`)
    } finally {
      setSaving(false)
    }
  }

  // ── Render ──────────────────────────────────────────────────
  return (
    <div style={{
      background: 'var(--bg3)',
      border: `1px solid ${color}33`,
      borderTop: `3px solid ${color}`,
      borderRadius: 'var(--radius)',
      padding: '18px',
    }}>
      <h3 style={{ color, marginBottom: '14px', fontSize: '14px' }}>
        {title} — Score this output
      </h3>

      {/* Output preview */}
      <div className="output-box" style={{ marginBottom: '18px', maxHeight: '190px', fontSize: '12px' }}>
        {output || 'No output generated'}
      </div>

      {/* 2-column score grid */}
      <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '16px', marginBottom: '16px' }}>
        <div>
          <div className="label">Accuracy (1–5)</div>
          <div style={{ fontSize: '11px', color: 'var(--text3)', marginBottom: '8px' }}>
            1 = completely wrong · 5 = fully accurate per source docs
          </div>
          <ScoreRadio id={`${resultId}-${system}-acc`} value={accuracy} onChange={setAccuracy} />
        </div>

        <div>
          <div className="label">Completeness (1–5)</div>
          <div style={{ fontSize: '11px', color: 'var(--text3)', marginBottom: '8px' }}>
            1 = missing most elements · 5 = addresses all parts
          </div>
          <ScoreRadio id={`${resultId}-${system}-comp`} value={completeness} onChange={setCompleteness} />
        </div>

        <div>
          <div className="label">Planning Usefulness (1–5)</div>
          <div style={{ fontSize: '11px', color: 'var(--text3)', marginBottom: '8px' }}>
            1 = useless to a planner · 5 = immediately useful in practice
          </div>
          <ScoreRadio id={`${resultId}-${system}-use`} value={usefulness} onChange={setUsefulness} />
        </div>

        <div>
          <div className="label">Source Grounding (0–2)</div>
          <div style={{ fontSize: '11px', color: 'var(--text3)', marginBottom: '8px' }}>
            0 = no source · 1 = vague ref · 2 = specific paragraph cited
          </div>
          <ScoreRadio id={`${resultId}-${system}-grnd`} value={grounding} onChange={setGrounding} max={2} />
        </div>
      </div>

      <hr />

      {/* Hallucination */}
      <div style={{ margin: '14px 0' }}>
        <HallucinationTag
          present={hallucPresent}
          type={hallucType}
          detail={hallucDetail}
          onPresentChange={(v) => {
            setHallucPresent(v)
            if (!v) setHallucType('none')
          }}
          onTypeChange={setHallucType}
          onDetailChange={setHallucDetail}
        />
      </div>

      {/* Scorer notes */}
      <div style={{ marginBottom: '14px' }}>
        <div className="label">Scorer Notes (optional)</div>
        <textarea
          value={notes}
          onChange={e => setNotes(e.target.value)}
          placeholder="Any observations — e.g. 'Cited NPPF 2023 not 2024', 'Excellent grounding but incomplete'"
          style={{ minHeight: '58px' }}
        />
      </div>

      {/* Error */}
      {error && (
        <div style={{
          color: 'var(--red)', background: 'rgba(224,82,82,0.08)',
          border: '1px solid rgba(224,82,82,0.25)',
          borderRadius: 'var(--radius-sm)', padding: '8px 12px',
          fontSize: '12px', marginBottom: '10px',
        }}>
          {error}
        </div>
      )}

      {/* Save button */}
      <button
        className={`btn ${saved ? 'btn-secondary' : 'btn-primary'}`}
        onClick={handleSave}
        disabled={saving}
      >
        {saving
          ? <><div className="spinner" style={{ width: '13px', height: '13px' }} /> Saving…</>
          : saved
            ? '✓ Saved'
            : 'Save Score'
        }
      </button>
    </div>
  )
}
