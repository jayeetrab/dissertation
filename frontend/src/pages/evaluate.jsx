import React, { useEffect, useState } from 'react'
import { motion, AnimatePresence } from 'framer-motion'
import { ChevronLeft, ChevronRight } from 'lucide-react'
import { API } from '../app.jsx'

const CATEGORY_LABELS = {
  policy_compliance:         'Policy Compliance',
  evidence_synthesis:        'Evidence Synthesis',
  site_appraisal:            'Site Appraisal',
  stakeholder_communication: 'Stakeholder Communication',
  strategic_analysis:        'Strategic Analysis',
}

const HALLUCINATION_TYPES = [
  { value: 'none',                label: 'None detected' },
  { value: 'fabricated_clause',   label: 'Fabricated clause (invented policy paragraph)' },
  { value: 'outdated_policy',     label: 'Outdated policy (pre-2024 NPPF rules applied)' },
  { value: 'spatial_misattribution', label: 'Spatial misattribution (wrong geographic policy)' },
  { value: 'confident_ambiguity', label: 'Confident ambiguity (definitive answer where policy is vague)' },
]

function ScoreRadio({ name, value, onChange, max = 5 }) {
  return (
    <div style={{ display: 'flex', gap: '4px' }}>
      {Array.from({ length: max }, (_, i) => i + 1).map(n => (
        <label 
          key={n} 
          style={{
            position: 'relative',
            display: 'flex', alignItems: 'center', justifyContent: 'center',
            width: '36px', height: '36px', borderRadius: '4px',
            background: value === n ? 'var(--accent)' : 'var(--bg2)',
            color: value === n ? '#000' : 'var(--text-secondary)',
            border: `1px solid ${value === n ? 'var(--accent)' : 'var(--border2)'}`,
            cursor: 'pointer', fontWeight: 500, fontSize: '14px',
            transition: 'all 0.15s ease',
          }}
          onMouseEnter={e => { if (value !== n) { e.currentTarget.style.borderColor = 'var(--text-primary)'; e.currentTarget.style.color = 'var(--text-primary)' } }}
          onMouseLeave={e => { if (value !== n) { e.currentTarget.style.borderColor = 'var(--border2)'; e.currentTarget.style.color = 'var(--text-secondary)' } }}
        >
          <input
            type="radio" id={`${name}-${n}`} name={name}
            value={n} checked={value === n}
            onChange={() => onChange(n)}
            style={{ position: 'absolute', opacity: 0, width: 0, height: 0 }}
          />
          {n}
        </label>
      ))}
    </div>
  )
}

function ScoreForm({ resultId, taskId, system, output, existingScore, onSaved, delay = 0 }) {
  const [accuracy, setAccuracy] = useState(existingScore?.accuracy || 0)
  const [completeness, setCompleteness] = useState(existingScore?.completeness || 0)
  const [usefulness, setUsefulness] = useState(existingScore?.planning_usefulness || 0)
  const [grounding, setGrounding] = useState(existingScore?.grounding || 0)
  const [hallucPresent, setHallucPresent] = useState(existingScore?.hallucination_present || false)
  const [hallucType, setHallucType] = useState(existingScore?.hallucination_type || 'none')
  const [hallucDetail, setHallucDetail] = useState(existingScore?.hallucination_detail || '')
  const [notes, setNotes] = useState(existingScore?.scorer_notes || '')

  useEffect(() => {
    setAccuracy(existingScore?.accuracy || 0)
    setCompleteness(existingScore?.completeness || 0)
    setUsefulness(existingScore?.planning_usefulness || 0)
    setGrounding(existingScore?.grounding || 0)
    setHallucPresent(existingScore?.hallucination_present || false)
    setHallucType(existingScore?.hallucination_type || 'none')
    setHallucDetail(existingScore?.hallucination_detail || '')
    setNotes(existingScore?.scorer_notes || '')
  }, [resultId, existingScore])

  const [saving, setSaving] = useState(false)
  const [saved, setSaved]   = useState(false)

  const title = system === 'baseline' ? 'Baseline LLM Output' : 'RAG System Output'

  const save = async () => {
    if (!accuracy || !completeness || !usefulness) {
      alert('Please fill in all 1-5 scores before saving.')
      return
    }
    setSaving(true)
    try {
      await fetch(`${API}/score/${taskId}`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          result_id:           resultId,
          system,
          accuracy,
          completeness,
          planning_usefulness: usefulness,
          grounding,
          hallucination_present: hallucPresent,
          hallucination_type:  hallucType,
          hallucination_detail: hallucDetail,
          scorer_notes:        notes,
        })
      })
      setSaved(true)
      onSaved()
      setTimeout(() => setSaved(false), 2000)
    } finally {
      setSaving(false)
    }
  }

  return (
    <motion.div 
      initial={{ opacity: 0, y: 15 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ delay, duration: 0.6, ease: [0.16, 1, 0.3, 1] }}
      className="card"
      style={{
        display: 'flex', flexDirection: 'column'
      }}
    >
      <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', marginBottom: '16px' }}>
        <h3 style={{ color: 'var(--text-primary)', fontSize: '14px', fontWeight: 600 }}>{title}</h3>
      </div>

      {/* Output preview */}
      <div className="output-box" style={{ marginBottom: '24px', maxHeight: '300px' }}>
        {output || <span style={{ color: 'var(--text-tertiary)' }}>No output generated for this system.</span>}
      </div>

      <div style={{ fontSize: '11px', fontWeight: 600, color: 'var(--text-tertiary)', textTransform: 'uppercase', letterSpacing: '0.05em', marginBottom: '16px', borderBottom: '1px solid var(--border)', paddingBottom: '8px' }}>
        Evaluation Rubric
      </div>

      <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '24px', marginBottom: '24px' }}>
        {/* Accuracy */}
        <div>
          <div className="label">Accuracy (1–5)</div>
          <div style={{ fontSize: '11px', color: 'var(--text-tertiary)', marginBottom: '8px' }}>
            1 = wrong · 5 = accurate
          </div>
          <ScoreRadio name={`${resultId}-${system}-acc`} value={accuracy} onChange={setAccuracy} />
        </div>

        {/* Completeness */}
        <div>
          <div className="label">Completeness (1–5)</div>
          <div style={{ fontSize: '11px', color: 'var(--text-tertiary)', marginBottom: '8px' }}>
            1 = missing elements · 5 = complete
          </div>
          <ScoreRadio name={`${resultId}-${system}-comp`} value={completeness} onChange={setCompleteness} />
        </div>

        {/* Usefulness */}
        <div>
          <div className="label">Planning Usefulness (1–5)</div>
          <div style={{ fontSize: '11px', color: 'var(--text-tertiary)', marginBottom: '8px' }}>
            1 = useless · 5 = highly useful
          </div>
          <ScoreRadio name={`${resultId}-${system}-use`} value={usefulness} onChange={setUsefulness} />
        </div>

        {/* Grounding (0-2) */}
        <div>
          <div className="label">Source Grounding (0–2)</div>
          <div style={{ fontSize: '11px', color: 'var(--text-tertiary)', marginBottom: '8px' }}>
            0 = none · 2 = specific citation
          </div>
          <ScoreRadio name={`${resultId}-${system}-grnd`} value={grounding} onChange={setGrounding} max={2} />
        </div>
      </div>

      {/* Hallucination */}
      <div style={{ marginTop: '16px', background: hallucPresent ? 'rgba(239, 68, 68, 0.05)' : 'transparent', padding: hallucPresent ? '16px' : '0', borderRadius: 'var(--radius-sm)', border: hallucPresent ? '1px solid rgba(239, 68, 68, 0.2)' : '1px solid transparent', transition: 'all 0.2s' }}>
        <div style={{ display: 'flex', alignItems: 'center', gap: '12px', marginBottom: '16px' }}>
          <input 
            type="checkbox" 
            checked={hallucPresent} 
            onChange={(e) => {
              setHallucPresent(e.target.checked)
              if (!e.target.checked) setHallucType('none')
            }}
            id={`halluc-${system}-${resultId}`}
            style={{ width: '16px', height: '16px', accentColor: 'var(--red)' }}
          />
          <label htmlFor={`halluc-${system}-${resultId}`} style={{ fontSize: '13px', fontWeight: 500, color: hallucPresent ? 'var(--red)' : 'var(--text-primary)', cursor: 'pointer' }}>
            Flag output for hallucination
          </label>
        </div>

        <AnimatePresence>
          {hallucPresent && (
            <motion.div 
              initial={{ opacity: 0, height: 0 }}
              animate={{ opacity: 1, height: 'auto' }}
              exit={{ opacity: 0, height: 0 }}
              transition={{ duration: 0.3, ease: [0.16, 1, 0.3, 1] }}
              style={{ overflow: 'hidden' }}
            >
              <div style={{ display: 'flex', flexDirection: 'column', gap: '16px', paddingTop: '8px', borderTop: '1px solid rgba(239, 68, 68, 0.2)' }}>
                <div>
                  <div className="label" style={{ color: 'var(--red)' }}>Hallucination Type</div>
                  <select 
                    value={hallucType} 
                    onChange={e => setHallucType(e.target.value)}
                    style={{ borderColor: 'rgba(239, 68, 68, 0.3)' }}
                  >
                    {HALLUCINATION_TYPES.filter(h => h.value !== 'none').map(h => (
                      <option key={h.value} value={h.value}>{h.label}</option>
                    ))}
                  </select>
                </div>
                <div>
                  <div className="label" style={{ color: 'var(--red)' }}>Details / Exact Quote</div>
                  <textarea
                    value={hallucDetail}
                    onChange={e => setHallucDetail(e.target.value)}
                    placeholder="Provide exact quote or details..."
                    style={{ minHeight: '60px', borderColor: 'rgba(239, 68, 68, 0.3)' }}
                  />
                </div>
              </div>
            </motion.div>
          )}
        </AnimatePresence>
      </div>

      {/* Notes */}
      <div style={{ marginTop: '24px' }}>
        <div className="label">Scorer Notes (optional)</div>
        <textarea
          value={notes}
          onChange={e => setNotes(e.target.value)}
          placeholder="Any additional observations..."
          style={{ minHeight: '60px' }}
        />
      </div>

      <button
        className="btn btn-primary"
        onClick={save}
        disabled={saving}
        style={{ marginTop: '24px', alignSelf: 'flex-start' }}
      >
        {saving ? 'Saving...' : saved ? '✓ Saved Successfully' : 'Save Evaluation'}
      </button>
    </motion.div>
  )
}

export default function Evaluate() {
  const [results, setResults]   = useState([])
  const [current,  setCurrent]  = useState(0)
  const [catFilter, setCatFilter] = useState('all')
  const [loading, setLoading]   = useState(true)

  const loadResults = () => {
    fetch(`${API}/results`).then(r => r.json()).then(data => {
      setResults(data.filter(r => r.baseline_output || r.rag_output))
      setLoading(false)
    })
  }

  useEffect(() => { loadResults() }, [])

  const filtered = catFilter === 'all'
    ? results
    : results.filter(r => r.category === catFilter)

  const result = filtered[current]

  if (loading) return (
    <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center', height: '60vh', gap: '16px', color: 'var(--text-secondary)' }}>
      <div className="spinner" /> 
      <div style={{ fontWeight: 500 }}>Loading Evaluations...</div>
    </div>
  )

  if (results.length === 0) return (
    <motion.div initial={{ opacity: 0 }} animate={{ opacity: 1 }} className="card" style={{ textAlign: 'center', padding: '60px', maxWidth: '600px', margin: '40px auto' }}>
      <h2 style={{ fontSize: '18px', marginBottom: '8px' }}>No results to evaluate yet</h2>
      <p style={{ color: 'var(--text-secondary)', fontSize: '13px' }}>
        Run some tasks first on the Run Experiment page before starting the evaluation process.
      </p>
    </motion.div>
  )

  const scored = results.filter(r => r.baseline_scores && r.rag_scores).length

  return (
    <motion.div 
      initial={{ opacity: 0, y: 10 }} 
      animate={{ opacity: 1, y: 0 }} 
      transition={{ duration: 0.4, ease: [0.16, 1, 0.3, 1] }}
    >
      <div style={{ display: 'flex', alignItems: 'center', gap: '16px', marginBottom: '32px' }}>
        <div>
          <h1 style={{ fontSize: '24px' }}>Evaluate Outputs</h1>
          <p style={{ color: 'var(--text-secondary)', fontSize: '14px', marginTop: '4px' }}>
            Manually assess model outputs against the grading rubric.
          </p>
        </div>
        <div style={{ marginLeft: 'auto', display: 'flex', gap: '16px', alignItems: 'center' }}>
          <div style={{ fontSize: '13px', fontWeight: 500, color: 'var(--text-primary)', background: 'var(--bg2)', padding: '6px 12px', borderRadius: '4px', border: '1px solid var(--border)' }}>
            {scored} / {results.length} fully scored
          </div>
          <select 
            value={catFilter} 
            onChange={e => { setCatFilter(e.target.value); setCurrent(0) }}
            style={{ width: 'auto', padding: '6px 12px' }}
          >
            <option value="all">All Categories</option>
            {Object.entries(CATEGORY_LABELS).map(([k, v]) => (
              <option key={k} value={k}>{v}</option>
            ))}
          </select>
        </div>
      </div>

      {/* Task selector */}
      <div className="card" style={{ marginBottom: '24px', padding: '16px 24px', display: 'flex', flexDirection: 'column', gap: '16px' }}>
        <div style={{ display: 'flex', flexWrap: 'wrap', gap: '6px', alignItems: 'center' }}>
          <span className="label" style={{ margin: 0, marginRight: '8px', color: 'var(--text-primary)' }}>Task Selection</span>
          {filtered.map((r, i) => {
            const fullyScored = r.baseline_scores && r.rag_scores
            return (
              <button
                key={r.result_id}
                onClick={() => setCurrent(i)}
                style={{
                  padding: '4px 8px', borderRadius: '4px',
                  border: '1px solid',
                  borderColor: i === current ? 'var(--accent)' : fullyScored ? 'rgba(16, 185, 129, 0.3)' : 'var(--border2)',
                  background: i === current ? 'var(--accent)' : fullyScored ? 'rgba(16, 185, 129, 0.1)' : 'var(--bg2)',
                  color: i === current ? '#000' : fullyScored ? 'var(--green)' : 'var(--text-primary)',
                  cursor: 'pointer', fontSize: '12px', fontFamily: 'var(--font-mono)', fontWeight: 500,
                  transition: 'all 0.15s ease'
                }}
              >
                {r.task_id}
              </button>
            )
          })}
        </div>
        
        <div style={{ display: 'flex', gap: '12px', alignItems: 'center', borderTop: '1px solid var(--border)', paddingTop: '16px' }}>
          <button className="btn btn-secondary btn-sm" onClick={() => setCurrent(Math.max(0, current - 1))} disabled={current === 0}>
            <ChevronLeft size={16} /> Prev
          </button>
          <span style={{ fontSize: '13px', fontWeight: 500, color: 'var(--text-primary)' }}>
            {current + 1} of {filtered.length}
          </span>
          <button className="btn btn-secondary btn-sm" onClick={() => setCurrent(Math.min(filtered.length - 1, current + 1))} disabled={current === filtered.length - 1}>
            Next <ChevronRight size={16} />
          </button>
        </div>
      </div>

      <AnimatePresence mode="wait">
        {result && (
          <motion.div 
            key={result.task_id}
            initial={{ opacity: 0, x: 20 }}
            animate={{ opacity: 1, x: 0 }}
            exit={{ opacity: 0, x: -20 }}
            transition={{ duration: 0.4, ease: [0.16, 1, 0.3, 1] }}
          >
            {/* Task Details */}
            <div className="card" style={{ marginBottom: '24px', background: 'var(--bg2)', borderLeft: '3px solid var(--accent)' }}>
              <div style={{ display: 'flex', gap: '8px', marginBottom: '12px' }}>
                <span className="badge badge-gray">{result.task_id}</span>
                <span className="badge badge-gray">{CATEGORY_LABELS[result.category]}</span>
              </div>
              <p style={{ fontSize: '14px', lineHeight: '1.6', color: 'var(--text-primary)', fontWeight: 500 }}>{result.task_text}</p>
            </div>

            {/* Score forms */}
            <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '24px' }}>
              <ScoreForm
                resultId={result.result_id}
                taskId={result.task_id}
                system="baseline"
                output={result.baseline_output}
                existingScore={result.baseline_scores}
                onSaved={loadResults}
                delay={0.1}
              />
              <ScoreForm
                resultId={result.result_id}
                taskId={result.task_id}
                system="rag"
                output={result.rag_output}
                existingScore={result.rag_scores}
                onSaved={loadResults}
                delay={0.2}
              />
            </div>
          </motion.div>
        )}
      </AnimatePresence>
    </motion.div>
  )
}