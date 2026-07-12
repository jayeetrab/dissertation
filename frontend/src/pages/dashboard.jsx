import React, { useEffect, useState } from 'react'
import { motion } from 'framer-motion'
import { API } from '../app.jsx'

const CATEGORY_LABELS = {
  policy_compliance:         'Policy Compliance',
  evidence_synthesis:        'Evidence Synthesis',
  site_appraisal:            'Site Appraisal',
  stakeholder_communication: 'Stakeholder Communication',
  strategic_analysis:        'Strategic Analysis',
}

function StatCard({ label, value, sub, delay = 0 }) {
  return (
    <motion.div 
      initial={{ opacity: 0, y: 10 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ delay, duration: 0.5, ease: [0.16, 1, 0.3, 1] }}
      className="card" 
      style={{ 
        display: 'flex', flexDirection: 'column', gap: '8px'
      }}
    >
      <div className="label">{label}</div>
      <div style={{ fontSize: '32px', fontWeight: '500', color: 'var(--text-primary)', letterSpacing: '-0.02em', lineHeight: 1 }}>
        {value ?? '—'}
      </div>
      {sub && <div style={{ fontSize: '13px', color: 'var(--text-secondary)' }}>{sub}</div>}
    </motion.div>
  )
}

export default function Dashboard() {
  const [stats, setStats]   = useState(null)
  const [health, setHealth] = useState(null)
  const [tasks, setTasks]   = useState([])
  const [loading, setLoading] = useState(true)
  const [validation, setValidation] = useState(null)
  const [modelCmp, setModelCmp] = useState(null)

  useEffect(() => {
    Promise.all([
      fetch(`${API}/stats`).then(r => r.json()).catch(() => null),
      fetch(`${API}/health`).then(r => r.json()).catch(() => null),
      fetch(`${API}/tasks`).then(r => r.json()).catch(() => []),
    ]).then(([s, h, t]) => {
      setStats(s)
      setHealth(h)
      setTasks(t)
      setLoading(false)
    })
    fetch(`${API}/validation`).then(r => r.json()).then(setValidation).catch(() => {})
    fetch(`${API}/model-comparison`).then(r => r.json()).then(setModelCmp).catch(() => {})
  }, [])

  const byCat = {}
  tasks.forEach(t => { byCat[t.category] = (byCat[t.category] || 0) + 1 })

  if (loading) return (
    <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center', height: '60vh', gap: '16px', color: 'var(--text-secondary)' }}>
      <div className="spinner" /> 
      <div style={{ fontWeight: 500 }}>Loading Dashboard...</div>
    </div>
  )

  const vsStatus = health?.vectorstore
  const vsReady  = vsStatus?.ready
  const hasResults = (stats?.tasks_run || 0) > 0

  return (
    <motion.div 
      initial={{ opacity: 0, y: 10 }} 
      animate={{ opacity: 1, y: 0 }} 
      transition={{ duration: 0.4, ease: [0.16, 1, 0.3, 1] }}
    >
      {/* Header */}
      <div style={{ marginBottom: '40px' }}>
        <h1 style={{ fontSize: '24px' }}>Dashboard Overview</h1>
        <p style={{ color: 'var(--text-secondary)', marginTop: '8px', fontSize: '14px' }}>
          Urban Planning Evaluation System — Master's Dissertation
        </p>
      </div>

      {/* System Status */}
      <motion.div 
        initial={{ opacity: 0, y: 20 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.5, ease: [0.16, 1, 0.3, 1] }}
        className="card" 
        style={{ 
          marginBottom: '32px', display: 'flex', alignItems: 'center', gap: '20px', padding: '20px 24px',
          borderLeft: `3px solid ${vsReady ? 'var(--green)' : hasResults ? 'var(--amber)' : 'var(--red)'}`,
          boxShadow: vsReady ? 'inset 2px 0 20px -10px rgba(52, 211, 153, 0.2), var(--shadow)' : 'var(--shadow)'
        }}
      >
        <div>
          <div style={{ fontSize: '14px', fontWeight: '500', color: 'var(--text-primary)' }}>
            {vsReady ? `Vector Store: Ready — ${vsStatus.chunk_count} chunks`
              : hasResults ? `Stored results loaded — ${stats?.tasks_run} tasks`
              : 'Vector Store: Not Ready'}
          </div>
          <div style={{ fontSize: '13px', color: 'var(--text-secondary)', marginTop: '4px' }}>
            {vsReady
              ? 'Documents ingested. The system is ready to run experiments.'
              : hasResults
              ? 'Showing the completed experiment results. Live retrieval (Run and Compare) needs the vector store, which is not loaded on this deployment.'
              : 'The vector store is empty. Run ingest.py to load the planning documents.'}
          </div>
        </div>
        <div style={{ marginLeft: 'auto', textAlign: 'right' }}>
          <div style={{ fontSize: '20px', fontWeight: 500, color: 'var(--text-primary)' }}>{stats?.docs_in_corpus || 0}</div>
          <div style={{ fontSize: '11px', color: 'var(--text-tertiary)', fontWeight: 600, textTransform: 'uppercase', letterSpacing: '0.05em' }}>PDFs in Corpus</div>
        </div>
      </motion.div>

      {/* Stats grid */}
      <div style={{ display: 'grid', gridTemplateColumns: 'repeat(4, 1fr)', gap: '16px', marginBottom: '32px' }}>
        <StatCard label="Total Tasks"   value={stats?.total_tasks}   sub="Across 5 categories" />
        <StatCard label="Tasks Run"     value={stats?.tasks_run}     sub="Results generated" />
        <StatCard label="Tasks Scored"  value={stats?.tasks_auto_scored ?? stats?.tasks_scored}  sub="Rubric scored" />
        <StatCard label="Chunks in DB"  value={stats?.chunks_in_db}  sub="Planning document segments" />
      </div>

      {/* Accuracy & Hallucination Stats */}
      {(stats?.avg_baseline_accuracy || stats?.avg_rag_accuracy || stats?.hallucination_rate_baseline != null) && (
        <div style={{ display: 'grid', gridTemplateColumns: 'repeat(4, 1fr)', gap: '16px', marginBottom: '40px' }}>
          <StatCard
            label="Avg Baseline Accuracy"
            value={stats?.avg_baseline_accuracy ? `${stats.avg_baseline_accuracy}` : '—'}
            sub="Out of 5"
           
          />
          <StatCard
            label="Avg RAG Accuracy"
            value={stats?.avg_rag_accuracy ? `${stats.avg_rag_accuracy}` : '—'}
            sub="Out of 5"
           
          />
          <StatCard
            label="Baseline Hallucination"
            value={stats?.hallucination_rate_baseline != null ? `${(stats.hallucination_rate_baseline * 100).toFixed(0)}%` : '—'}
            sub="Rate of false claims"
           
          />
          <StatCard
            label="RAG Hallucination"
            value={stats?.hallucination_rate_rag != null ? `${(stats.hallucination_rate_rag * 100).toFixed(0)}%` : '—'}
            sub="Rate of false claims"
           
          />
        </div>
      )}

      {/* Validation highlight (detail on Results & Export) */}
      {(validation || modelCmp) && (
        <motion.div
          initial={{ opacity: 0, y: 10 }} animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.5, ease: [0.16, 1, 0.3, 1] }}
          className="card"
          style={{ marginBottom: '40px', padding: '20px 24px', borderLeft: '3px solid var(--accent)' }}
        >
          <div style={{ fontSize: '11px', fontWeight: 600, color: 'var(--text-tertiary)', textTransform: 'uppercase', letterSpacing: '0.05em', marginBottom: '12px' }}>
            Validation
          </div>
          <div style={{ display: 'flex', gap: '40px', flexWrap: 'wrap', fontSize: '14px', color: 'var(--text-secondary)' }}>
            {validation && (
              <div>
                <div style={{ color: 'var(--text-primary)', fontWeight: 500 }}>Cross-model judge agreement</div>
                Both {validation.judge_a} and {validation.judge_b} rank RAG above baseline
                {validation.direction?.every(d => d.rag > d.baseline) ? '' : ' (mixed)'}. Absolute
                scores are model-sensitive (accuracy {Math.round((validation.metrics?.[0]?.exact_agreement || 0) * 100)}% exact match).
              </div>
            )}
            {modelCmp && (
              <div>
                <div style={{ color: 'var(--text-primary)', fontWeight: 500 }}>Base-model robustness</div>
                Without retrieval, {modelCmp.models[1]?.model} fabricated {modelCmp.models[1]?.baseline.fabricated} local
                policy codes; with RAG, {modelCmp.models[1]?.rag.fabricated}. A stronger model does not remove the need for grounding.
              </div>
            )}
          </div>
        </motion.div>
      )}

      <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '32px', marginBottom: '40px' }}>
        {/* Task library breakdown */}
        <div>
          <h2 style={{ marginBottom: '16px', fontSize: '14px', textTransform: 'uppercase', letterSpacing: '0.05em', color: 'var(--text-secondary)' }}>Task Library Breakdown</h2>
          <div style={{ display: 'flex', flexDirection: 'column', gap: '8px' }}>
            {Object.entries(CATEGORY_LABELS).map(([key, label], index) => (
              <motion.div 
                key={key}
                initial={{ opacity: 0, x: -10 }}
                animate={{ opacity: 1, x: 0 }}
                transition={{ duration: 0.4, ease: [0.16, 1, 0.3, 1] }}
                style={{ 
                  display: 'flex', alignItems: 'center', justifyContent: 'space-between',
                  padding: '12px 16px', background: 'var(--bg2)', border: '1px solid var(--border)', borderRadius: 'var(--radius-sm)'
                }}
              >
                <div style={{ fontSize: '13px', fontWeight: 500, color: 'var(--text-primary)' }}>{label}</div>
                <div style={{ fontSize: '14px', fontWeight: 500, color: 'var(--text-secondary)' }}>
                  {byCat[key] || 0}
                </div>
              </motion.div>
            ))}
          </div>
        </div>

        {/* Workflow guide */}
        <div>
          <h2 style={{ marginBottom: '16px', fontSize: '14px', textTransform: 'uppercase', letterSpacing: '0.05em', color: 'var(--text-secondary)' }}>Experiment Workflow</h2>
          <div style={{ display: 'flex', flexDirection: 'column', gap: '8px' }}>
            {[
              { step: '1', title: 'Ingest Documents', desc: 'Planning PDFs loaded into ChromaDB', done: vsReady || hasResults },
              { step: '2', title: 'Run Experiment',   desc: 'Execute tasks through baseline and RAG systems', done: (stats?.tasks_run || 0) > 0 },
              { step: '3', title: 'Evaluate',         desc: 'Score outputs on accuracy and hallucination', done: (stats?.tasks_scored || 0) > 0 },
              { step: '4', title: 'Export Results',   desc: 'Download CSV for dissertation analysis', done: (stats?.tasks_run || 0) > 0 },
            ].map((s, index) => (
              <motion.div 
                key={s.step}
                initial={{ opacity: 0, x: -10 }}
                animate={{ opacity: 1, x: 0 }}
                transition={{ duration: 0.4, ease: [0.16, 1, 0.3, 1] }}
                style={{ 
                  display: 'flex', alignItems: 'center', gap: '16px',
                  padding: '12px 16px', background: 'var(--bg2)', border: '1px solid var(--border)', borderRadius: 'var(--radius-sm)',
                  opacity: (index > 0 && !s.done && !([
              { step: '1', title: 'Ingest Documents', desc: 'Planning PDFs loaded into ChromaDB', done: vsReady || hasResults },
              { step: '2', title: 'Run Experiment',   desc: 'Execute tasks through baseline and RAG systems', done: (stats?.tasks_run || 0) > 0 },
              { step: '3', title: 'Evaluate',         desc: 'Manually score outputs on accuracy and hallucination', done: (stats?.tasks_scored || 0) > 0 },
              { step: '4', title: 'Export Results',   desc: 'Download CSV for dissertation analysis', done: (stats?.tasks_run || 0) > 0 },
            ][index - 1].done)) ? 0.3 : 1
                }}
              >
                <div style={{
                  width: '24px', height: '24px', borderRadius: '4px',
                  background: s.done ? 'var(--green)' : 'var(--bg3)',
                  display: 'flex', alignItems: 'center', justifyContent: 'center',
                  color: s.done ? '#000' : 'var(--text-secondary)',
                  fontSize: '12px', fontWeight: 500, flexShrink: 0
                }}>
                  {s.done ? '✓' : s.step}
                </div>
                <div>
                  <div style={{ fontSize: '13px', fontWeight: 500, color: 'var(--text-primary)' }}>{s.title}</div>
                  <div style={{ fontSize: '12px', color: 'var(--text-secondary)' }}>{s.desc}</div>
                </div>
              </motion.div>
            ))}
          </div>
        </div>
      </div>

    </motion.div>
  )
}