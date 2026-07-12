import React, { useEffect, useState } from 'react'
import { motion, AnimatePresence } from 'framer-motion'
import { Play, RotateCw, ChevronDown, ChevronUp, AlertCircle, CheckCircle2, FileText, Settings, PlayCircle } from 'lucide-react'
import { API } from '../app.jsx'

const CATEGORY_LABELS = {
  policy_compliance:         'Policy Compliance',
  evidence_synthesis:        'Evidence Synthesis',
  site_appraisal:            'Site Appraisal',
  stakeholder_communication: 'Stakeholder Communication',
  strategic_analysis:        'Strategic Analysis',
}

const CATEGORY_COLORS = {
  policy_compliance:         '#0071E3',
  evidence_synthesis:        '#34C759',
  site_appraisal:            '#FF9500',
  stakeholder_communication: '#AF52DE',
  strategic_analysis:        '#5AC8FA',
}

function OutputPanel({ title, content, chunks, tokens, color, delay = 0 }) {
  const [showChunks, setShowChunks] = useState(false)

  if (!content) return (
    <div style={{
      flex: 1, background: 'var(--bg3)', border: '1px dashed var(--border2)',
      borderRadius: 'var(--radius)', padding: '32px',
      display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center',
      color: 'var(--text-tertiary)', fontSize: '14px', gap: '8px'
    }}>
      <Settings size={24} style={{ opacity: 0.5 }} />
      Waiting to run...
    </div>
  )

  const isError = content.startsWith('[ERROR')
  return (
    <motion.div 
      initial={{ opacity: 0 }}
      animate={{ opacity: 1 }}
      transition={{ delay, duration: 0.3 }}
      style={{ flex: 1, display: 'flex', flexDirection: 'column' }}
    >
      <div style={{ display: 'flex', alignItems: 'center', gap: '8px', marginBottom: '12px' }}>
        <div style={{ width: '8px', height: '8px', borderRadius: '50%', background: color }} />
        <span style={{ fontWeight: '600', color: 'var(--text-primary)', fontSize: '15px' }}>{title}</span>
        {tokens && (
          <span style={{ marginLeft: 'auto', fontSize: '12px', color: 'var(--text-tertiary)', fontWeight: 500, display: 'flex', alignItems: 'center', gap: '4px' }}>
            <FileText size={12} /> {tokens} tokens
          </span>
        )}
      </div>

      <div className="output-box" style={{ 
        borderColor: isError ? 'var(--red)' : 'var(--border)', 
        minHeight: '200px', flex: 1,
        background: isError ? 'rgba(255, 59, 48, 0.05)' : 'var(--bg)',
        borderWidth: isError ? '2px' : '1px'
      }}>
        {isError && <div style={{ color: 'var(--red)', fontWeight: 600, display: 'flex', alignItems: 'center', gap: '6px', marginBottom: '12px' }}><AlertCircle size={16} /> Error Occurred</div>}
        {content}
      </div>

      {/* Retrieved chunks (RAG only) */}
      {chunks && chunks.length > 0 && (
        <div style={{ marginTop: '16px' }}>
          <button 
            className="btn btn-secondary btn-sm" 
            style={{ width: '100%', justifyContent: 'space-between', background: 'var(--bg3)' }}
            onClick={() => setShowChunks(!showChunks)}
          >
            <span style={{ display: 'flex', alignItems: 'center', gap: '6px', color: 'var(--text-secondary)' }}>
              <Database size={14} /> {chunks.length} chunks retrieved
            </span>
            {showChunks ? <ChevronUp size={14} /> : <ChevronDown size={14} />}
          </button>
          
          <AnimatePresence>
            {showChunks && (
              <motion.div 
                initial={{ opacity: 0, height: 0 }}
                animate={{ opacity: 1, height: 'auto' }}
                exit={{ opacity: 0, height: 0 }}
                style={{ overflow: 'hidden' }}
              >
                <div style={{ marginTop: '12px', display: 'flex', flexDirection: 'column', gap: '12px', paddingBottom: '8px' }}>
                  {chunks.map((c, i) => (
                    <motion.div 
                      key={i} 
                      initial={{ opacity: 0, x: -10 }}
                      animate={{ opacity: 1, x: 0 }}
                      transition={{ }}
                      style={{
                        background: 'var(--bg2)', border: '1px solid var(--border)',
                        borderRadius: 'var(--radius-sm)', padding: '16px',
                        boxShadow: 'var(--shadow-sm)'
                      }}
                    >
                      <div style={{ display: 'flex', gap: '8px', marginBottom: '12px', flexWrap: 'wrap' }}>
                        <span className="badge badge-blue">{c.source_doc}</span>
                        <span className="badge badge-gray">Page {c.page_number}</span>
                        <span className="badge badge-teal">
                          Relevance: {(c.relevance_score * 100).toFixed(0)}%
                        </span>
                        {c.distance_km !== null && c.distance_km !== undefined && (
                          <span className="badge badge-purple" style={{ display: 'flex', alignItems: 'center', gap: '4px' }}>
                            📍 {c.distance_km}km away
                          </span>
                        )}
                      </div>
                      <div style={{ fontSize: '13px', color: 'var(--text-secondary)', lineHeight: '1.6' }}>
                        {c.content.substring(0, 300)}{c.content.length > 300 ? '...' : ''}
                      </div>
                    </motion.div>
                  ))}
                </div>
              </motion.div>
            )}
          </AnimatePresence>
        </div>
      )}
    </motion.div>
  )
}

function Database({ size }) {
  // Lucide database icon
  return (
    <svg width={size} height={size} viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
      <ellipse cx="12" cy="5" rx="9" ry="3"></ellipse>
      <path d="M21 12c0 1.66-4 3-9 3s-9-1.34-9-3"></path>
      <path d="M3 5v14c0 1.66 4 3 9 3s9-1.34 9-3V5"></path>
    </svg>
  );
}

export default function RunExperiment() {
  const [tasks, setTasks]       = useState([])
  const [catFilter, setCatFilter] = useState('all')
  const [results, setResults]   = useState({})  // keyed by task_id
  const [running, setRunning]   = useState(null) // task_id currently running
  const [runningAll, setRunningAll] = useState(false)
  const [progress, setProgress] = useState(null)
  const [toast, setToast]       = useState(null)

  useEffect(() => {
    fetch(`${API}/tasks`).then(r => r.json()).then(setTasks)
    fetch(`${API}/results`).then(r => r.json()).then(data => {
      const map = {}
      data.forEach(r => { map[r.task_id] = r })
      setResults(map)
    })
  }, [])

  const showToast = (msg) => {
    setToast(msg)
    setTimeout(() => setToast(null), 3000)
  }

  const runTask = async (taskId) => {
    setRunning(taskId)
    try {
      const res = await fetch(`${API}/run/task`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ task_id: taskId, run_baseline: true, run_rag: true })
      })
      if (!res.ok) throw new Error('API error')
      const data = await res.json()
      setResults(prev => ({ ...prev, [taskId]: data }))
      showToast(`Task ${taskId} complete ✓`)
    } catch (e) {
      showToast(`Error running ${taskId}: ${e.message}`)
    } finally {
      setRunning(null)
    }
  }

  const runAll = async () => {
    const filtered = catFilter === 'all' ? tasks : tasks.filter(t => t.category === catFilter)
    setRunningAll(true)
    showToast(`Starting ${filtered.length} tasks in background...`)
    try {
      await fetch(`${API}/run/all`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          category_filter: catFilter === 'all' ? null : catFilter,
          run_baseline: true,
          run_rag: true
        })
      })
      const poll = setInterval(async () => {
        try {
          const [prog, res] = await Promise.all([
            fetch(`${API}/run/progress`).then(r => r.json()),
            fetch(`${API}/results`).then(r => r.json())
          ])
          const map = {}
          res.forEach(r => { map[r.task_id] = r })
          setResults(map)
          setProgress(prog)
          if (!prog.running) {
            clearInterval(poll)
            setRunningAll(false)
            setProgress(null)
            showToast(`Done! ${prog.completed}/${prog.total} tasks complete.`)
          }
        } catch (e) { console.error(e) }
      }, 3000)
    } catch (e) {
      showToast(`Error: ${e.message}`)
      setRunningAll(false)
    }
  }

  const filtered = catFilter === 'all' ? tasks : tasks.filter(t => t.category === catFilter)

  return (
    <motion.div initial={{ opacity: 0 }} animate={{ opacity: 1 }} transition={{ duration: 0.5 }}>
      <div style={{ display: 'flex', alignItems: 'center', gap: '16px', marginBottom: '32px' }}>
        <div>
          <h1 style={{ fontSize: '32px' }}>Experiment Runner</h1>
          <p style={{ color: 'var(--text-secondary)', fontSize: '15px', marginTop: '8px' }}>
            Execute planning tasks through the Baseline LLM and RAG system.
          </p>
        </div>
        <div style={{ marginLeft: 'auto', display: 'flex', gap: '16px', alignItems: 'center' }}>
          <select
            value={catFilter}
            onChange={e => setCatFilter(e.target.value)}
            style={{ width: '200px', fontWeight: 500 }}
          >
            <option value="all">All Categories</option>
            {Object.entries(CATEGORY_LABELS).map(([k, v]) => (
              <option key={k} value={k}>{v}</option>
            ))}
          </select>
          <motion.button
            whileHover={{ scale: 1.02 }}
            whileTap={{ scale: 0.98 }}
            className="btn btn-primary"
            onClick={runAll}
            disabled={runningAll || running !== null}
            style={{ padding: '12px 24px' }}
          >
            {runningAll ? <><div className="spinner" /> Running...</> : <><PlayCircle size={18} /> Run All Tasks</>}
          </motion.button>
        </div>
      </div>

      {/* Task list */}
      <div style={{ display: 'flex', flexDirection: 'column', gap: '24px' }}>
        {filtered.map((task, index) => {
          const result = results[task.id]
          const isRunning = running === task.id
          const hasResult = result?.baseline_output || result?.rag_output

          return (
            <motion.div 
              key={task.id} 
              initial={{ opacity: 0 }}
              animate={{ opacity: 1 }}
              transition={{ }}
              className="card" 
              style={{
                borderLeft: `4px solid ${CATEGORY_COLORS[task.category]}`
              }}
            >
              {/* Task header */}
              <div style={{ display: 'flex', alignItems: 'flex-start', gap: '20px', marginBottom: hasResult ? '24px' : '0' }}>
                <div style={{ flex: 1 }}>
                  <div style={{ display: 'flex', gap: '10px', marginBottom: '12px', flexWrap: 'wrap', alignItems: 'center' }}>
                    <span className="badge badge-gray" style={{ fontFamily: 'var(--font-mono)' }}>{task.id}</span>
                    <span className="badge" style={{
                      background: `${CATEGORY_COLORS[task.category]}15`,
                      color: CATEGORY_COLORS[task.category]
                    }}>{CATEGORY_LABELS[task.category]}</span>
                    <span className={`badge ${task.difficulty === 'hard' ? 'badge-red' : task.difficulty === 'easy' ? 'badge-green' : 'badge-amber'}`}>
                      {task.difficulty}
                    </span>
                    {hasResult && <span className="badge badge-green" style={{ display: 'flex', alignItems: 'center', gap: '4px' }}><CheckCircle2 size={12} /> Completed</span>}
                  </div>
                  <p style={{ fontSize: '15px', color: 'var(--text-primary)', lineHeight: '1.6', fontWeight: 500 }}>
                    {task.task}
                  </p>
                  {task.notes && (
                    <p style={{ fontSize: '13px', color: 'var(--text-tertiary)', marginTop: '8px' }}>
                      <span style={{ fontWeight: 600 }}>Note:</span> {task.notes}
                    </p>
                  )}
                </div>
                <button
                  className={`btn ${hasResult ? 'btn-secondary' : 'btn-primary'}`}
                  onClick={() => runTask(task.id)}
                  disabled={isRunning || runningAll}
                  style={{ flexShrink: 0, minWidth: '120px' }}
                >
                  {isRunning
                    ? <><div className="spinner" style={{ width: '16px', height: '16px' }} /> Running</>
                    : hasResult ? <><RotateCw size={16} /> Re-run</> : <><Play size={16} /> Run Task</>}
                </button>
              </div>

              {/* Side-by-side outputs */}
              {hasResult && (
                <div style={{ display: 'flex', gap: '24px' }}>
                  <OutputPanel
                    title="Baseline LLM"
                    content={result.baseline_output}
                    tokens={result.baseline_tokens_used}
                    color="var(--amber)"
                   
                  />
                  <OutputPanel
                    title="RAG System"
                    content={result.rag_output}
                    chunks={result.retrieved_chunks}
                    tokens={result.rag_tokens_used}
                    color="var(--green)"
                   
                  />
                </div>
              )}
            </motion.div>
          )
        })}
      </div>

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