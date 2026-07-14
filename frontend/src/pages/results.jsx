import React, { useEffect, useState, useCallback } from 'react'
import { motion, AnimatePresence } from 'framer-motion'
import { Download, Zap, BarChart3, AlertCircle } from 'lucide-react'
import {
  ResponsiveContainer, BarChart, Bar, XAxis, YAxis, Tooltip, Legend,
  RadarChart, PolarGrid, PolarAngleAxis, Radar,
  ScatterChart, Scatter, CartesianGrid, Cell,
} from 'recharts'
import { API } from '../app.jsx'

const CATEGORY_LABELS = {
  policy_compliance:         'Policy Compliance',
  evidence_synthesis:        'Evidence Synthesis',
  site_appraisal:            'Site Appraisal',
  stakeholder_communication: 'Stakeholder Communication',
  strategic_analysis:        'Strategic Analysis',
}

// Apple-inspired colors for charts
const CATEGORY_COLORS = {
  policy_compliance:         '#0071E3',
  evidence_synthesis:        '#34C759',
  site_appraisal:            '#FF9500',
  stakeholder_communication: '#AF52DE',
  strategic_analysis:        '#5AC8FA',
}

const HALLUCINATION_LABELS = {
  fabricated_clause:      'Fabricated clause',
  outdated_policy:        'Outdated policy',
  spatial_misattribution: 'Spatial misattribution',
  confident_ambiguity:    'Confident ambiguity',
}

// ── Custom Recharts tooltip ───────────────────────────────────
function CustomTooltip({ active, payload, label }) {
  if (!active || !payload?.length) return null
  return (
    <div style={{
      background: 'rgba(255, 255, 255, 0.9)', 
      backdropFilter: 'blur(10px)',
      border: '1px solid var(--border)',
      borderRadius: 'var(--radius-sm)', 
      padding: '12px 16px',
      fontSize: '13px', color: 'var(--text-primary)',
      boxShadow: 'var(--shadow)'
    }}>
      <div style={{ fontWeight: '600', marginBottom: '8px', color: 'var(--text-secondary)' }}>{label}</div>
      {payload.map((p, i) => (
        <div key={i} style={{ display: 'flex', alignItems: 'center', gap: '8px', marginBottom: '4px' }}>
          <div style={{ width: '8px', height: '8px', borderRadius: '50%', background: p.color }} />
          <span style={{ color: 'var(--text-primary)' }}>{p.name}:</span>
          <strong style={{ marginLeft: 'auto' }}>{typeof p.value === 'number' ? p.value.toFixed(2) : p.value}</strong>
        </div>
      ))}
    </div>
  )
}

// ── Section heading ───────────────────────────────────────────
function Section({ title, children, delay = 0 }) {
  return (
    <motion.div 
      initial={{ opacity: 0 }}
      animate={{ opacity: 1 }}
      transition={{ delay, duration: 0.3 }}
      style={{ marginBottom: '48px' }}
    >
      <h2 style={{ marginBottom: '24px', fontSize: '20px', letterSpacing: '-0.01em' }}>{title}</h2>
      {children}
    </motion.div>
  )
}

// ── KPI tile ─────────────────────────────────────────────────
function KPI({ label, value, color, sub }) {
  return (
    <div className="card" style={{ borderTop: `4px solid ${color || 'var(--accent)'}`, display: 'flex', flexDirection: 'column' }}>
      <div className="label" style={{ marginBottom: '12px' }}>{label}</div>
      <div style={{ fontSize: '32px', fontFamily: 'var(--font-serif)', fontWeight: '600', color: color || 'var(--text-primary)', letterSpacing: '-0.02em', lineHeight: 1 }}>
        {value ?? '—'}
      </div>
      {sub && <div style={{ fontSize: '13px', color: 'var(--text-secondary)', marginTop: 'auto', paddingTop: '12px', fontWeight: 500 }}>{sub}</div>}
    </div>
  )
}

// ── Main component ────────────────────────────────────────────
export default function Results() {
  const [results, setResults] = useState([])
  const [loading, setLoading] = useState(true)
  const [exporting, setExporting] = useState(false)
  const [runningRagas, setRunningRagas] = useState(false)
  const [validation, setValidation] = useState(null)
  const [modelCmp, setModelCmp] = useState(null)
  const [toast, setToast] = useState(null)
  const [vsReady, setVsReady] = useState(true)

  useEffect(() => {
    fetch(`${API}/validation`).then(r => r.json()).then(setValidation).catch(() => {})
    fetch(`${API}/model-comparison`).then(r => r.json()).then(setModelCmp).catch(() => {})
    fetch(`${API}/health`).then(r => r.json()).then(h => setVsReady(!!h?.vectorstore?.ready)).catch(() => {})
  }, [])

  const showToast = (msg) => {
    setToast(msg)
    setTimeout(() => setToast(null), 3500)
  }

  const load = useCallback(() => {
    fetch(`${API}/results`)
      .then(r => r.json())
      .then(data => { setResults(data); setLoading(false) })
      .catch(() => setLoading(false))
  }, [])

  useEffect(() => { load() }, [load])

  // ── Export CSV ───────────────────────────────────────────────
  const handleExportCSV = async () => {
    setExporting(true)
    try {
      const res = await fetch(`${API}/export/csv`)
      if (!res.ok) throw new Error(await res.text())
      const blob = await res.blob()
      const url  = URL.createObjectURL(blob)
      const a    = document.createElement('a')
      const ts   = new Date().toISOString().slice(0,16).replace('T','_').replace(':','-')
      a.href     = url
      a.download = `planningrag_results_${ts}.csv`
      a.click()
      URL.revokeObjectURL(url)
      showToast('CSV downloaded ✓')
    } catch (e) {
      showToast(`Export failed: ${e.message}`)
    } finally {
      setExporting(false)
    }
  }

  // ── Export JSON ──────────────────────────────────────────────
  const handleExportJSON = async () => {
    try {
      const res  = await fetch(`${API}/export/json`)
      if (!res.ok) throw new Error(await res.text())
      const blob = await res.blob()
      const url  = URL.createObjectURL(blob)
      const a    = document.createElement('a')
      a.href     = url
      a.download = `planningrag_results_${new Date().toISOString().slice(0,10)}.json`
      a.click()
      URL.revokeObjectURL(url)
      showToast('JSON exported ✓')
    } catch (e) {
      showToast(`Export failed: ${e.message}`)
    }
  }

  // ── Run RAGAS ────────────────────────────────────────────────
  const handleRagas = async () => {
    setRunningRagas(true)
    showToast('Running RAGAS evaluation… (may take a few minutes)')
    try {
      const res  = await fetch(`${API}/evaluate/ragas`, { method: 'POST' })
      const data = await res.json()
      showToast(`RAGAS done — ${data.evaluated} results evaluated ✓`)
      load()
    } catch (e) {
      showToast(`RAGAS failed: ${e.message}`)
    } finally {
      setRunningRagas(false)
    }
  }

  // ── Derived data ─────────────────────────────────────────────
  const scored = results.filter(r => r.baseline_scores && r.rag_scores)

  const avgScore = (arr, field) => {
    const vals = arr.map(r => r[field]).filter(Boolean)
    return vals.length ? (vals.reduce((a, b) => a + b, 0) / vals.length).toFixed(2) : '—'
  }

  const baselineAcc = avgScore(scored.map(r => ({ acc: r.baseline_scores?.accuracy })), 'acc')
  const ragAcc      = avgScore(scored.map(r => ({ acc: r.rag_scores?.accuracy })), 'acc')

  const hallucBaseline = scored.filter(r => r.baseline_scores?.hallucination_present).length
  const hallucRag      = scored.filter(r => r.rag_scores?.hallucination_present).length

  // Per-category bar chart data
  const catData = Object.keys(CATEGORY_LABELS).map(cat => {
    const catScored = scored.filter(r => r.category === cat)
    const bAcc = catScored.map(r => r.baseline_scores?.accuracy).filter(Boolean)
    const rAcc = catScored.map(r => r.rag_scores?.accuracy).filter(Boolean)
    return {
      name: CATEGORY_LABELS[cat].replace(' ', '\n'),
      shortName: cat.split('_').map(w => w[0].toUpperCase()).join(''),
      Baseline: bAcc.length ? +(bAcc.reduce((a,b)=>a+b,0)/bAcc.length).toFixed(2) : 0,
      RAG:      rAcc.length ? +(rAcc.reduce((a,b)=>a+b,0)/rAcc.length).toFixed(2) : 0,
    }
  })

  // Radar chart data
  const radarDimensions = [
    { key: 'accuracy',           label: 'Accuracy',     max: 5 },
    { key: 'completeness',       label: 'Completeness', max: 5 },
    { key: 'planning_usefulness',label: 'Usefulness',   max: 5 },
    { key: 'grounding',          label: 'Grounding',    max: 2 },
  ]
  const radarData = radarDimensions.map(({ key, label, max }) => {
    const bVals = scored.map(r => r.baseline_scores?.[key]).filter(v => v != null)
    const rVals = scored.map(r => r.rag_scores?.[key]).filter(v => v != null)
    const norm  = v => +(v / max * 5).toFixed(2)   // normalise to 0–5 scale
    return {
      dimension: label,
      Baseline: bVals.length ? norm(bVals.reduce((a,b)=>a+b,0)/bVals.length) : 0,
      RAG:      rVals.length ? norm(rVals.reduce((a,b)=>a+b,0)/rVals.length) : 0,
    }
  })

  // Hallucination type breakdown
  const hallucTypeMap = {}
  scored.forEach(r => {
    const bt = r.baseline_scores?.hallucination_type
    const rt = r.rag_scores?.hallucination_type
    if (bt && bt !== 'none') hallucTypeMap[bt] = (hallucTypeMap[bt] || 0) + 1
    if (rt && rt !== 'none') hallucTypeMap[rt] = (hallucTypeMap[rt] || 0) + 1
  })
  const hallucTypeData = Object.entries(hallucTypeMap).map(([type, count]) => ({
    name: HALLUCINATION_LABELS[type] || type, count
  }))

  // RAGAS metrics
  const ragasResults = results.filter(r => r.ragas_faithfulness != null)
  const avgFaithfulness     = ragasResults.length
    ? (ragasResults.reduce((a,r) => a + r.ragas_faithfulness, 0) / ragasResults.length).toFixed(3)
    : '—'
  const avgRelevancy        = ragasResults.length
    ? (ragasResults.reduce((a,r) => a + r.ragas_answer_relevancy, 0) / ragasResults.length).toFixed(3)
    : '—'
  const avgContextPrecision = ragasResults.length
    ? (ragasResults.reduce((a,r) => a + r.ragas_context_precision, 0) / ragasResults.length).toFixed(3)
    : '—'

  if (loading) return (
    <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center', height: '60vh', gap: '16px', color: 'var(--text-secondary)' }}>
      <div className="spinner" style={{ width: '32px', height: '32px' }} /> 
      <div style={{ fontWeight: 500 }}>Loading Results...</div>
    </div>
  )

  if (results.length === 0) return (
    <motion.div initial={{ opacity: 0 }} animate={{ opacity: 1 }} className="card" style={{ textAlign: 'center', padding: '60px', maxWidth: '600px', margin: '40px auto' }}>
      <div style={{ width: '64px', height: '64px', borderRadius: '50%', background: 'var(--bg3)', color: 'var(--text-secondary)', display: 'flex', alignItems: 'center', justifyContent: 'center', margin: '0 auto 24px' }}>
        <BarChart3 size={32} />
      </div>
      <h2>No results yet</h2>
      <p style={{ color: 'var(--text-secondary)', marginTop: '12px', fontSize: '15px' }}>
        Run some tasks on the Run Experiment page, then score them in Evaluate.
      </p>
    </motion.div>
  )

  return (
    <motion.div initial={{ opacity: 0 }} animate={{ opacity: 1 }} transition={{ duration: 0.5 }}>
      {/* ── Page header ─────────────────────────────────────── */}
      <div style={{ display: 'flex', alignItems: 'flex-start', gap: '16px', marginBottom: '40px' }}>
        <div>
          <h1 style={{ fontSize: '32px' }}>Results &amp; Export</h1>
          <p style={{ color: 'var(--text-secondary)', fontSize: '15px', marginTop: '8px' }}>
            Charts, statistics, and CSV export for dissertation analysis.
          </p>
        </div>
        <div style={{ marginLeft: 'auto', display: 'flex', gap: '12px', flexWrap: 'wrap', justifyContent: 'flex-end' }}>
          <motion.button whileHover={{ scale: 1.02 }} whileTap={{ scale: 0.98 }} className="btn btn-secondary" onClick={handleRagas} disabled={runningRagas || !vsReady}
            title={!vsReady ? 'Live retrieval is unavailable on this deployment; RAGAS scores below are precomputed.' : undefined}>
            {runningRagas ? <><div className="spinner" style={{ width: '16px', height: '16px' }} /> Running RAGAS…</> : <><Zap size={16} /> Run RAGAS</>}
          </motion.button>
          <motion.button whileHover={{ scale: 1.02 }} whileTap={{ scale: 0.98 }} className="btn btn-secondary" onClick={handleExportJSON}>
            JSON
          </motion.button>
          <motion.button whileHover={{ scale: 1.02 }} whileTap={{ scale: 0.98 }} className="btn btn-primary" onClick={handleExportCSV} disabled={exporting}>
            {exporting ? <><div className="spinner" style={{ width: '16px', height: '16px' }} /> Exporting…</> : <><Download size={16} /> Download CSV</>}
          </motion.button>
        </div>
      </div>

      {/* ── KPIs ─────────────────────────────────────────────── */}
      <Section title="Summary Statistics">
        <div style={{ display: 'grid', gridTemplateColumns: 'repeat(4, 1fr)', gap: '20px', marginBottom: '20px' }}>
          <KPI label="Tasks Run"     value={results.length}  sub="With at least one output" />
          <KPI label="Tasks Scored"  value={scored.length}   sub="Both systems scored"      color="var(--purple)" />
          <KPI label="Baseline Accuracy" value={baselineAcc !== '—' ? `${baselineAcc}/5` : '—'} color="var(--amber)" sub="Average score" />
          <KPI label="RAG Accuracy"      value={ragAcc !== '—' ? `${ragAcc}/5` : '—'}           color="var(--green)" sub="Average score" />
        </div>
        <div style={{ display: 'grid', gridTemplateColumns: 'repeat(3, 1fr)', gap: '20px' }}>
          <KPI label="Baseline Hallucinations" value={`${hallucBaseline}/${scored.length}`} color="var(--red)"   sub="Tasks with hallucination" />
          <KPI label="RAG Hallucinations"      value={`${hallucRag}/${scored.length}`}      color="var(--green)" sub="Tasks with hallucination" />
          <KPI label="RAG RAGAS Evaluated"     value={ragasResults.length}                  sub="Automated metrics available" color="var(--teal)" />
        </div>
      </Section>

      {/* ── Cross-model validation ───────────────────────────── */}
      {validation && (
        <Section title="Cross-Model Validation">
          <div className="card" style={{ padding: '32px' }}>
            <p style={{ color: 'var(--text-secondary)', fontSize: '14px', marginBottom: '24px', maxWidth: '760px' }}>
              A second judge ({validation.judge_b}) re-scored the outputs, {validation.scope},
              and its scores are compared with the primary judge ({validation.judge_a}).
              This measures whether the rubric scores are consistent across models. It tests
              consistency, not correctness.
            </p>

            <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '32px' }}>
              <div>
                <div className="label" style={{ marginBottom: '12px' }}>Rubric agreement ({validation.n_outputs} outputs)</div>
                <table style={{ width: '100%', fontSize: '13px', borderCollapse: 'collapse' }}>
                  <thead><tr style={{ color: 'var(--text-tertiary)', textAlign: 'left' }}>
                    <th style={{ padding: '6px 8px' }}>Metric</th>
                    <th style={{ padding: '6px 8px' }}>Exact</th>
                    <th style={{ padding: '6px 8px' }}>Spearman</th>
                  </tr></thead>
                  <tbody>
                    {validation.metrics.map(m => (
                      <tr key={m.metric} style={{ borderTop: '1px solid var(--border)' }}>
                        <td style={{ padding: '8px', color: 'var(--text-primary)' }}>{m.metric}</td>
                        <td style={{ padding: '8px' }}>{Math.round(m.exact_agreement * 100)}%</td>
                        <td style={{ padding: '8px' }}>{m.spearman}</td>
                      </tr>
                    ))}
                    <tr style={{ borderTop: '1px solid var(--border)' }}>
                      <td style={{ padding: '8px', color: 'var(--text-primary)' }}>hallucination flag</td>
                      <td style={{ padding: '8px' }}>{Math.round(validation.hallucination.agreement * 100)}%</td>
                      <td style={{ padding: '8px' }}>κ={validation.hallucination.kappa}</td>
                    </tr>
                  </tbody>
                </table>
              </div>

              <div>
                <div className="label" style={{ marginBottom: '12px' }}>Direction check: does each judge rank RAG above baseline?</div>
                <table style={{ width: '100%', fontSize: '13px', borderCollapse: 'collapse' }}>
                  <thead><tr style={{ color: 'var(--text-tertiary)', textAlign: 'left' }}>
                    <th style={{ padding: '6px 8px' }}>Judge</th>
                    <th style={{ padding: '6px 8px' }}>Baseline</th>
                    <th style={{ padding: '6px 8px' }}>RAG</th>
                    <th style={{ padding: '6px 8px' }}>Δ</th>
                    <th style={{ padding: '6px 8px' }}>RAG higher?</th>
                  </tr></thead>
                  <tbody>
                    {validation.direction.map(d => (
                      <tr key={d.judge} style={{ borderTop: '1px solid var(--border)' }}>
                        <td style={{ padding: '8px', color: 'var(--text-primary)' }}>{d.judge}</td>
                        <td style={{ padding: '8px' }}>{d.baseline}</td>
                        <td style={{ padding: '8px' }}>{d.rag}</td>
                        <td style={{ padding: '8px', color: d.delta > 0 ? 'var(--green)' : 'var(--red)' }}>{d.delta > 0 ? '+' : ''}{d.delta}</td>
                        <td style={{ padding: '8px', color: d.delta > 0 ? 'var(--green)' : 'var(--red)', fontWeight: 600 }}>{d.delta > 0 ? 'yes' : 'no'}</td>
                      </tr>
                    ))}
                  </tbody>
                </table>
              </div>
            </div>
          </div>
        </Section>
      )}

      {/* ── Base-model robustness ────────────────────────────── */}
      {modelCmp && (
        <Section title="Base-Model Robustness">
          <div className="card" style={{ padding: '32px' }}>
            <p style={{ color: 'var(--text-secondary)', fontSize: '14px', marginBottom: '24px', maxWidth: '780px' }}>
              The same experiment run with a stronger generator ({modelCmp.models[1]?.model}) in place of
              gpt-4o-mini, scored by the deterministic citation instrument. It tests whether a more capable
              base model makes retrieval unnecessary. It does not: the stronger model fabricates local policy
              codes at least as often without grounding, and RAG corrects it.
            </p>
            <table style={{ width: '100%', fontSize: '13px', borderCollapse: 'collapse' }}>
              <thead><tr style={{ color: 'var(--text-tertiary)', textAlign: 'left' }}>
                <th style={{ padding: '8px' }}>Model</th>
                <th style={{ padding: '8px' }}>System</th>
                <th style={{ padding: '8px' }}>Codes cited</th>
                <th style={{ padding: '8px' }}>Fabricated</th>
                <th style={{ padding: '8px' }}>Misattributed</th>
                <th style={{ padding: '8px' }}>Bad codes</th>
              </tr></thead>
              <tbody>
                {modelCmp.models.flatMap(m => ['baseline', 'rag'].map(sys => {
                  const d = m[sys]; const bad = d.fabricated + d.misattributed
                  return (
                    <tr key={m.model + sys} style={{ borderTop: '1px solid var(--border)' }}>
                      <td style={{ padding: '8px', color: 'var(--text-primary)' }}>{m.model}</td>
                      <td style={{ padding: '8px', textTransform: 'uppercase', color: sys === 'rag' ? 'var(--green)' : 'var(--amber)', fontWeight: 600 }}>{sys}</td>
                      <td style={{ padding: '8px' }}>{d.cited}</td>
                      <td style={{ padding: '8px' }}>{d.fabricated}</td>
                      <td style={{ padding: '8px' }}>{d.misattributed}</td>
                      <td style={{ padding: '8px', fontWeight: 600, color: bad === 0 ? 'var(--green)' : bad > 20 ? 'var(--red)' : 'var(--text-primary)' }}>{bad}</td>
                    </tr>
                  )
                }))}
              </tbody>
            </table>
          </div>
        </Section>
      )}

      {/* ── Accuracy by category ─────────────────────────────── */}
      {scored.length > 0 && (
        <Section title="Accuracy by Task Category">
          <div className="card" style={{ padding: '32px' }}>
            <ResponsiveContainer width="100%" height={320}>
              <BarChart data={catData} barCategoryGap="28%" margin={{ top: 10, right: 10, left: -20, bottom: 0 }}>
                <CartesianGrid strokeDasharray="3 3" stroke="var(--border-light)" vertical={false} />
                <XAxis dataKey="shortName" tick={{ fill: 'var(--text-secondary)', fontSize: 13, fontWeight: 500 }} axisLine={false} tickLine={false} dy={10} />
                <YAxis domain={[0, 5]} tick={{ fill: 'var(--text-secondary)', fontSize: 13, fontWeight: 500 }} axisLine={false} tickLine={false} />
                <Tooltip content={<CustomTooltip />} cursor={{ fill: 'var(--bg3)' }} />
                <Legend wrapperStyle={{ fontSize: '14px', fontWeight: 500, color: 'var(--text-secondary)', paddingTop: '24px' }} iconType="circle" />
                <Bar dataKey="Baseline" fill="var(--amber)" radius={[6, 6, 0, 0]} maxBarSize={60} />
                <Bar dataKey="RAG"      fill="var(--green)" radius={[6, 6, 0, 0]} maxBarSize={60} />
              </BarChart>
            </ResponsiveContainer>
            <div style={{ marginTop: '24px', display: 'flex', gap: '24px', fontSize: '13px', color: 'var(--text-tertiary)', flexWrap: 'wrap', justifyContent: 'center' }}>
              {Object.entries(CATEGORY_LABELS).map(([k,v]) => (
                <span key={k}><strong style={{ color: CATEGORY_COLORS[k], fontWeight: 600 }}>{k.split('_').map(w=>w[0].toUpperCase()).join('')}</strong> = {v}</span>
              ))}
            </div>
          </div>
        </Section>
      )}

      {/* ── Radar chart ─────────────────────────────────────── */}
      {scored.length > 0 && (
        <Section title="Multi-Dimensional Quality Comparison">
          <div className="card" style={{ padding: '32px', display: 'flex', justifyContent: 'center' }}>
            <ResponsiveContainer width="100%" height={400}>
              <RadarChart data={radarData} outerRadius={140}>
                <PolarGrid stroke="var(--border)" strokeDasharray="3 3" />
                <PolarAngleAxis dataKey="dimension" tick={{ fill: 'var(--text-primary)', fontSize: 14, fontWeight: 600 }} />
                <Radar name="Baseline" dataKey="Baseline" stroke="var(--amber)" fill="var(--amber)" fillOpacity={0.2} strokeWidth={3} />
                <Radar name="RAG"      dataKey="RAG"      stroke="var(--green)" fill="var(--green)" fillOpacity={0.2} strokeWidth={3} />
                <Legend wrapperStyle={{ fontSize: '14px', fontWeight: 500, color: 'var(--text-secondary)', paddingTop: '16px' }} iconType="circle" />
                <Tooltip content={<CustomTooltip />} />
              </RadarChart>
            </ResponsiveContainer>
          </div>
        </Section>
      )}

      {/* ── Hallucination breakdown ──────────────────────────── */}
      {hallucTypeData.length > 0 && (
        <Section title="Hallucination Type Breakdown">
          <div className="card" style={{ padding: '32px' }}>
            <ResponsiveContainer width="100%" height={260}>
              <BarChart data={hallucTypeData} layout="vertical" margin={{ top: 0, right: 30, left: 10, bottom: 0 }}>
                <CartesianGrid strokeDasharray="3 3" stroke="var(--border-light)" horizontal={false} />
                <XAxis type="number" tick={{ fill: 'var(--text-secondary)', fontSize: 13 }} axisLine={false} tickLine={false} allowDecimals={false} />
                <YAxis dataKey="name" type="category" width={180} tick={{ fill: 'var(--text-primary)', fontSize: 13, fontWeight: 500 }} axisLine={false} tickLine={false} />
                <Tooltip content={<CustomTooltip />} cursor={{ fill: 'var(--bg3)' }} />
                <Bar dataKey="count" radius={[0, 6, 6, 0]} maxBarSize={40}>
                  {hallucTypeData.map((_, i) => (
                    <Cell key={i} fill={['#FF3B30', '#FF9500', '#AF52DE', '#5AC8FA'][i % 4]} />
                  ))}
                </Bar>
              </BarChart>
            </ResponsiveContainer>
          </div>
        </Section>
      )}

      {/* ── RAGAS metrics ────────────────────────────────────── */}
      {ragasResults.length > 0 && (
        <Section title="RAGAS Automated Metrics (RAG system)">
          <div style={{ display: 'grid', gridTemplateColumns: 'repeat(3, 1fr)', gap: '20px', marginBottom: '24px' }}>
            <KPI label="Avg Faithfulness"      value={avgFaithfulness}     color="var(--teal)"   sub="0–1 · Answers grounded in context" />
            <KPI label="Avg Answer Relevancy"  value={avgRelevancy}        color="var(--accent)" sub="0–1 · Answer addresses the question" />
            <KPI label="Avg Context Precision" value={avgContextPrecision} color="var(--purple)" sub="0–1 · Right chunks retrieved" />
          </div>
          
          <div className="card" style={{ padding: '32px' }}>
            <div className="label" style={{ marginBottom: '24px', fontSize: '14px', textAlign: 'center' }}>RAGAS Faithfulness vs Manual Accuracy (RAG)</div>
            <ResponsiveContainer width="100%" height={300}>
              <ScatterChart margin={{ top: 20, right: 20, bottom: 20, left: 20 }}>
                <CartesianGrid strokeDasharray="3 3" stroke="var(--border-light)" />
                <XAxis dataKey="faithfulness" name="Faithfulness" type="number" domain={[0,1]} tick={{ fill: 'var(--text-secondary)', fontSize: 13 }} axisLine={false} tickLine={false} label={{ value: 'Faithfulness (RAGAS)', position: 'bottom', offset: 0, fill: 'var(--text-primary)', fontSize: 14, fontWeight: 500 }} dy={10} />
                <YAxis dataKey="accuracy" name="Accuracy" type="number" domain={[1,5]} tick={{ fill: 'var(--text-secondary)', fontSize: 13 }} axisLine={false} tickLine={false} label={{ value: 'Manual Accuracy Score', angle: -90, position: 'left', offset: 0, fill: 'var(--text-primary)', fontSize: 14, fontWeight: 500 }} dx={-10} />
                <Tooltip cursor={{ strokeDasharray: '3 3', stroke: 'var(--border2)' }} content={({ active, payload }) => {
                  if (!active || !payload?.length) return null
                  const d = payload[0]?.payload
                  return (
                    <div style={{ background: 'rgba(255, 255, 255, 0.9)', backdropFilter: 'blur(10px)', border: '1px solid var(--border)', borderRadius: 'var(--radius-sm)', padding: '12px 16px', fontSize: '13px', boxShadow: 'var(--shadow)' }}>
                      <div style={{ fontFamily: 'var(--font-mono)', color: 'var(--teal)', fontWeight: 600, marginBottom: '8px' }}>{d?.task_id}</div>
                      <div style={{ marginBottom: '4px' }}>Faithfulness: <strong>{d?.faithfulness?.toFixed(3)}</strong></div>
                      <div>Accuracy: <strong>{d?.accuracy}/5</strong></div>
                    </div>
                  )
                }} />
                <Scatter
                  data={ragasResults
                    .filter(r => r.rag_scores?.accuracy)
                    .map(r => ({
                      task_id: r.task_id,
                      faithfulness: r.ragas_faithfulness,
                      accuracy: r.rag_scores.accuracy,
                    }))}
                  fill="var(--teal)"
                  r={6}
                />
              </ScatterChart>
            </ResponsiveContainer>
          </div>
        </Section>
      )}

      {/* ── Full results table ───────────────────────────────── */}
      <Section title="Full Results Table">
        <div className="card" style={{ padding: 0, overflow: 'hidden' }}>
          <div style={{ overflowX: 'auto' }}>
            <table style={{ width: '100%', borderCollapse: 'collapse' }}>
              <thead>
                <tr>
                  <th style={{ padding: '16px 24px', background: 'var(--bg3)', color: 'var(--text-secondary)', fontWeight: 600, fontSize: '13px', borderBottom: '1px solid var(--border)', textAlign: 'left' }}>Task</th>
                  <th style={{ padding: '16px 24px', background: 'var(--bg3)', color: 'var(--text-secondary)', fontWeight: 600, fontSize: '13px', borderBottom: '1px solid var(--border)', textAlign: 'left' }}>Category</th>
                  <th style={{ padding: '16px 12px', background: 'rgba(255, 149, 0, 0.1)', color: 'var(--amber)', fontWeight: 600, fontSize: '13px', borderBottom: '1px solid var(--border)', textAlign: 'center' }}>B·Acc</th>
                  <th style={{ padding: '16px 12px', background: 'rgba(255, 149, 0, 0.1)', color: 'var(--amber)', fontWeight: 600, fontSize: '13px', borderBottom: '1px solid var(--border)', textAlign: 'center' }}>B·Comp</th>
                  <th style={{ padding: '16px 12px', background: 'rgba(255, 149, 0, 0.1)', color: 'var(--amber)', fontWeight: 600, fontSize: '13px', borderBottom: '1px solid var(--border)', textAlign: 'center' }}>B·Use</th>
                  <th style={{ padding: '16px 12px', background: 'rgba(255, 149, 0, 0.1)', color: 'var(--amber)', fontWeight: 600, fontSize: '13px', borderBottom: '1px solid var(--border)', textAlign: 'center' }}>B·Halluc</th>
                  <th style={{ padding: '16px 12px', background: 'rgba(52, 199, 89, 0.1)', color: 'var(--green)', fontWeight: 600, fontSize: '13px', borderBottom: '1px solid var(--border)', textAlign: 'center' }}>R·Acc</th>
                  <th style={{ padding: '16px 12px', background: 'rgba(52, 199, 89, 0.1)', color: 'var(--green)', fontWeight: 600, fontSize: '13px', borderBottom: '1px solid var(--border)', textAlign: 'center' }}>R·Comp</th>
                  <th style={{ padding: '16px 12px', background: 'rgba(52, 199, 89, 0.1)', color: 'var(--green)', fontWeight: 600, fontSize: '13px', borderBottom: '1px solid var(--border)', textAlign: 'center' }}>R·Use</th>
                  <th style={{ padding: '16px 12px', background: 'rgba(52, 199, 89, 0.1)', color: 'var(--green)', fontWeight: 600, fontSize: '13px', borderBottom: '1px solid var(--border)', textAlign: 'center' }}>R·Halluc</th>
                  <th style={{ padding: '16px 24px', background: 'rgba(90, 200, 250, 0.1)', color: 'var(--teal)', fontWeight: 600, fontSize: '13px', borderBottom: '1px solid var(--border)', textAlign: 'center' }}>Faithful</th>
                </tr>
              </thead>
              <tbody>
                {results.map(r => {
                  const bs = r.baseline_scores
                  const rs = r.rag_scores
                  const improvement = bs?.accuracy && rs?.accuracy ? rs.accuracy - bs.accuracy : null
                  return (
                    <tr key={r.result_id} style={{ borderBottom: '1px solid var(--border)', transition: 'background 0.2s' }} onMouseEnter={e => e.currentTarget.style.background = 'var(--bg3)'} onMouseLeave={e => e.currentTarget.style.background = 'transparent'}>
                      <td style={{ padding: '16px 24px' }}>
                        <span style={{ fontFamily: 'var(--font-mono)', color: 'var(--accent)', fontSize: '13px', fontWeight: 500 }}>{r.task_id}</span>
                        {improvement !== null && (
                          <span className={`badge ${improvement > 0 ? 'badge-green' : improvement < 0 ? 'badge-red' : 'badge-gray'}`}
                            style={{ marginLeft: '8px', fontSize: '11px' }}>
                            {improvement > 0 ? `+${improvement}` : improvement}
                          </span>
                        )}
                      </td>
                      <td style={{ padding: '16px 24px' }}><span className="badge badge-gray" style={{ fontSize: '11px', background: 'var(--border-light)' }}>{CATEGORY_LABELS[r.category]}</span></td>
                      <td style={{ padding: '16px 12px', textAlign: 'center', fontWeight: 500 }}>{bs?.accuracy    ?? <span style={{ color: 'var(--text-tertiary)' }}>—</span>}</td>
                      <td style={{ padding: '16px 12px', textAlign: 'center', fontWeight: 500 }}>{bs?.completeness ?? <span style={{ color: 'var(--text-tertiary)' }}>—</span>}</td>
                      <td style={{ padding: '16px 12px', textAlign: 'center', fontWeight: 500 }}>{bs?.planning_usefulness ?? <span style={{ color: 'var(--text-tertiary)' }}>—</span>}</td>
                      <td style={{ padding: '16px 12px', textAlign: 'center' }}>{bs ? (bs.hallucination_present
                        ? <AlertCircle size={16} color="var(--red)" style={{ margin: '0 auto' }} />
                        : <span style={{ color: 'var(--text-tertiary)', fontSize: '12px' }}>No</span>)
                        : <span style={{ color: 'var(--text-tertiary)' }}>—</span>}
                      </td>
                      <td style={{ padding: '16px 12px', textAlign: 'center', fontWeight: 500 }}>{rs?.accuracy    ?? <span style={{ color: 'var(--text-tertiary)' }}>—</span>}</td>
                      <td style={{ padding: '16px 12px', textAlign: 'center', fontWeight: 500 }}>{rs?.completeness ?? <span style={{ color: 'var(--text-tertiary)' }}>—</span>}</td>
                      <td style={{ padding: '16px 12px', textAlign: 'center', fontWeight: 500 }}>{rs?.planning_usefulness ?? <span style={{ color: 'var(--text-tertiary)' }}>—</span>}</td>
                      <td style={{ padding: '16px 12px', textAlign: 'center' }}>{rs ? (rs.hallucination_present
                        ? <AlertCircle size={16} color="var(--red)" style={{ margin: '0 auto' }} />
                        : <span style={{ color: 'var(--text-tertiary)', fontSize: '12px' }}>No</span>)
                        : <span style={{ color: 'var(--text-tertiary)' }}>—</span>}
                      </td>
                      <td style={{ padding: '16px 24px', textAlign: 'center', fontFamily: 'var(--font-mono)', fontSize: '13px', color: 'var(--teal)', fontWeight: 500 }}>
                        {r.ragas_faithfulness != null ? r.ragas_faithfulness.toFixed(3) : '—'}
                      </td>
                    </tr>
                  )
                })}
              </tbody>
            </table>
          </div>
        </div>
      </Section>

      <AnimatePresence>
        {toast && (
          <motion.div 
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            exit={{ opacity: 0, y: 20 }}
            className="toast"
          >
            {toast}
          </motion.div>
        )}
      </AnimatePresence>
    </motion.div>
  )
}
