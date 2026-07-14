import React, { useEffect, useState, useMemo } from 'react'
import { motion, AnimatePresence } from 'framer-motion'
import { API } from '../app.jsx'
import { Search, Play, ChevronDown, ChevronUp, AlertCircle, FileText, SplitSquareHorizontal, BarChart3 } from 'lucide-react'

// Source ablation: run the same task against different document subsets
// to show which PDFs contribute most to answer quality.

// Source-ablation subsets are built per task from the selected task's city
// (see buildSubsets), so the "local plan" condition follows the task instead
// of being hardcoded to Bristol. Retrieval is restricted via city_filter:
//   NPPF Only     -> ['national']         (national policy alone)
//   <City> LP Only-> [city]               (that city's adopted plan alone)
//   NPPF + Local  -> [city, 'national']   (both sources combined)
function buildSubsets(city) {
  const cityLabel = city
    ? city.charAt(0).toUpperCase() + city.slice(1)
    : 'Local'
  return [
    { id: 'nppf_only',  label: 'NPPF Only',            city_filter: ['national'],                     color: 'var(--accent)' },
    { id: 'local_only', label: `${cityLabel} LP Only`, city_filter: city ? [city] : null,             color: 'var(--green)' },
    { id: 'both',       label: 'NPPF + Local',         city_filter: city ? [city, 'national'] : null, color: 'var(--teal)' },
  ]
}

const CATEGORY_LABELS = {
  policy_compliance: 'Policy Compliance',
  evidence_synthesis: 'Evidence Synthesis',
  site_appraisal: 'Site Appraisal',
  stakeholder_communication: 'Stakeholder Communication',
  strategic_analysis: 'Strategic Analysis',
}

function OutputCard({ subset, result, running, delay = 0 }) {
  const [showChunks, setShowChunks] = useState(false)

  if (running) {
    return (
      <motion.div 
        initial={{ opacity: 0 }}
        animate={{ opacity: 1 }}
        transition={{ delay, duration: 0.3 }}
        style={{
          background: 'var(--bg2)', border: '1px solid var(--border)',
          borderTop: `4px solid ${subset.color}`, borderRadius: 'var(--radius)',
          padding: '24px', flex: 1, boxShadow: 'var(--shadow-sm)',
          display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center', minHeight: '280px'
        }}
      >
        <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', gap: '16px' }}>
          <div className="spinner" style={{ width: '24px', height: '24px', borderTopColor: subset.color }} />
          <div style={{ fontWeight: 600, color: subset.color, fontSize: '14px' }}>{subset.label}</div>
          <div style={{ color: 'var(--text-tertiary)', fontSize: '13px' }}>Running retrieval and generation...</div>
        </div>
      </motion.div>
    )
  }

  if (!result) {
    return (
      <motion.div 
        initial={{ opacity: 0 }}
        animate={{ opacity: 1 }}
        transition={{ delay, duration: 0.3 }}
        style={{
          background: 'var(--bg)', border: '1px dashed var(--border2)',
          borderTop: `4px solid ${subset.color}40`, borderRadius: 'var(--radius)',
          padding: '24px', flex: 1, display: 'flex', alignItems: 'center',
          justifyContent: 'center', color: 'var(--text-tertiary)', fontSize: '14px',
          fontWeight: 500, minHeight: '280px'
        }}
      >
        {subset.label} — not run yet
      </motion.div>
    )
  }

  const chunks = result.retrieved_chunks || []
  const isError = result.rag_output?.startsWith('ERROR')

  return (
    <motion.div 
      initial={{ opacity: 0 }}
      animate={{ opacity: 1 }}
      transition={{ delay, duration: 0.3 }}
      style={{
        background: 'var(--bg2)', border: '1px solid var(--border)',
        borderTop: `4px solid ${subset.color}`, borderRadius: 'var(--radius)',
        padding: '24px', flex: 1, boxShadow: 'var(--shadow-sm)'
      }}
    >
      {/* Header */}
      <div style={{ display: 'flex', alignItems: 'center', gap: '8px', marginBottom: '16px' }}>
        <div style={{ width: '8px', height: '8px', borderRadius: '50%', background: subset.color }} />
        <span style={{ fontWeight: 600, color: subset.color, fontSize: '15px' }}>{subset.label}</span>
        {result.rag_tokens_used && (
          <span style={{ marginLeft: 'auto', fontSize: '12px', color: 'var(--text-tertiary)', display: 'flex', alignItems: 'center', gap: '4px', fontWeight: 500 }}>
            <FileText size={14} /> {result.rag_tokens_used} tokens
          </span>
        )}
      </div>

      {/* Chunk stats row */}
      {chunks.length > 0 && (
        <div style={{ display: 'flex', gap: '8px', marginBottom: '16px', flexWrap: 'wrap' }}>
          <span className="badge badge-teal" style={{ background: 'rgba(90, 200, 250, 0.15)', color: '#0C85A8' }}>
            {chunks.length} chunks
          </span>
          <span className="badge badge-blue">
            Avg Relevance: {(chunks.reduce((a, c) => a + c.relevance_score, 0) / chunks.length * 100).toFixed(0)}%
          </span>
        </div>
      )}

      {/* Output text */}
      <div className="output-box" style={{
        borderColor: isError ? 'rgba(255, 59, 48, 0.3)' : 'var(--border)',
        background: isError ? 'rgba(255, 59, 48, 0.05)' : 'var(--bg)',
        minHeight: '200px', fontSize: '13px',
      }}>
        {isError && <div style={{ color: 'var(--red)', fontWeight: 600, display: 'flex', alignItems: 'center', gap: '6px', marginBottom: '12px' }}><AlertCircle size={16} /> Error Occurred</div>}
        {result.rag_output || 'No output generated'}
      </div>

      {/* Retrieved chunks toggle */}
      {chunks.length > 0 && (
        <div style={{ marginTop: '16px' }}>
          <button
            className="btn btn-secondary btn-sm"
            onClick={() => setShowChunks(!showChunks)}
            style={{ width: '100%', justifyContent: 'space-between', background: 'var(--bg3)', padding: '8px 12px' }}
          >
            <span style={{ fontWeight: 500 }}>{chunks.length} Retrieved Chunks</span>
            {showChunks ? <ChevronUp size={16} /> : <ChevronDown size={16} />}
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
                      initial={{ opacity: 0 }}
                      animate={{ opacity: 1 }}
                      transition={{ }}
                      style={{
                        background: 'var(--bg2)', border: '1px solid var(--border)',
                        borderRadius: 'var(--radius-sm)', padding: '16px',
                        boxShadow: 'var(--shadow-sm)'
                      }}
                    >
                      <div style={{ display: 'flex', gap: '8px', marginBottom: '12px', flexWrap: 'wrap' }}>
                        <span className="badge badge-teal" style={{ background: 'var(--bg3)', color: 'var(--text-secondary)' }}>{c.source_doc}</span>
                        <span className="badge badge-gray">p.{c.page_number}</span>
                        <span className="badge badge-blue">
                          {(c.relevance_score * 100).toFixed(0)}% match
                        </span>
                        {c.distance_km !== null && c.distance_km !== undefined && (
                          <span className="badge badge-purple" style={{ display: 'flex', alignItems: 'center', gap: '4px' }}>
                            📍 {c.distance_km}km
                          </span>
                        )}
                      </div>
                      <div style={{ fontSize: '13px', color: 'var(--text-secondary)', lineHeight: '1.6' }}>
                        {c.content.substring(0, 250)}{c.content.length > 250 ? '…' : ''}
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

export default function Compare() {
  const [tasks, setTasks] = useState([])
  const [selectedTask, setSelectedTask] = useState(null)
  const [catFilter, setCatFilter] = useState('all')
  const [results, setResults] = useState({})   // keyed by subset.id
  const [running, setRunning] = useState({})   // keyed by subset.id → bool
  const [runningAll, setRunningAll] = useState(false)
  const [toast, setToast] = useState(null)
  const [vsReady, setVsReady] = useState(true)

  const showToast = (msg) => {
    setToast(msg)
    setTimeout(() => setToast(null), 3500)
  }

  // Ablation subsets follow the selected task's city (not a fixed Bristol set)
  const subsets = useMemo(() => buildSubsets(selectedTask?.city), [selectedTask?.city])

  useEffect(() => {
    fetch(`${API}/tasks`)
      .then(r => r.json())
      .then(data => {
        setTasks(data)
        if (data.length > 0) setSelectedTask(data[0])
      })
    fetch(`${API}/health`).then(r => r.json()).then(h => setVsReady(!!h?.vectorstore?.ready)).catch(() => {})
  }, [])

  // When task changes, clear previous comparison results
  useEffect(() => {
    setResults({})
    setRunning({})
  }, [selectedTask?.id])

  const runSubset = async (subset) => {
    if (!selectedTask) return
    setRunning(prev => ({ ...prev, [subset.id]: true }))
    try {
      const res = await fetch(`${API}/run/task`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          task_id: selectedTask.id,
          run_baseline: false,
          run_rag: true,
          city_filter: subset.city_filter ?? null,
        })
      })
      if (!res.ok) throw new Error(await res.text())
      const data = await res.json()
      setResults(prev => ({ ...prev, [subset.id]: data }))
    } catch (e) {
      showToast(`Error running ${subset.label}: ${e.message}`)
    } finally {
      setRunning(prev => ({ ...prev, [subset.id]: false }))
    }
  }

  const runAll = async () => {
    if (!selectedTask) return
    setRunningAll(true)
    showToast(`Running all 3 source subsets for ${selectedTask.id}...`)
    for (const subset of subsets) {
      await runSubset(subset)
    }
    setRunningAll(false)
    showToast('Source ablation complete! Compare the outputs below.')
  }

  const filteredTasks = catFilter === 'all'
    ? tasks
    : tasks.filter(t => t.category === catFilter)

  const anyRunning = Object.values(running).some(Boolean) || runningAll

  const getChunkSources = (subsetId) => {
    const r = results[subsetId]
    if (!r?.retrieved_chunks) return []
    return [...new Set(r.retrieved_chunks.map(c => c.source_doc))]
  }

  return (
    <motion.div initial={{ opacity: 0 }} animate={{ opacity: 1 }} transition={{ duration: 0.5 }}>
      {/* Page header */}
      <div style={{ display: 'flex', alignItems: 'flex-start', gap: '16px', marginBottom: '32px' }}>
        <div>
          <h1 style={{ fontSize: '32px' }}>Source Ablation</h1>
          <p style={{ color: 'var(--text-secondary)', fontSize: '15px', marginTop: '8px', maxWidth: '800px' }}>
            Run the same task against different document subsets to isolate which source drives each answer.
            Useful for your dissertation's ablation study section.
          </p>
        </div>
        <div style={{ marginLeft: 'auto', display: 'flex', gap: '10px', alignItems: 'center' }}>
          <select
            value={catFilter}
            onChange={e => { setCatFilter(e.target.value) }}
            style={{ width: 'auto', fontWeight: 500 }}
          >
            <option value="all">All Categories</option>
            {Object.entries(CATEGORY_LABELS).map(([k, v]) => (
              <option key={k} value={k}>{v}</option>
            ))}
          </select>
        </div>
      </div>

      {!vsReady && (
        <div className="card" style={{
          marginBottom: '24px', padding: '14px 20px',
          borderLeft: '3px solid var(--amber)', display: 'flex', alignItems: 'center', gap: '10px',
          fontSize: '13px', color: 'var(--text-secondary)'
        }}>
          <AlertCircle size={16} style={{ color: 'var(--amber)', flexShrink: 0 }} />
          Source ablation runs live retrieval, which is unavailable on this deployment (the vector store is not loaded). This page is interactive when run locally after ingesting the corpus.
        </div>
      )}

      <div style={{ display: 'grid', gridTemplateColumns: '320px 1fr', gap: '24px' }}>
        {/* Left: task picker */}
        <div>
          <div className="card" style={{ padding: 0, overflow: 'hidden', height: 'calc(100vh - 200px)', display: 'flex', flexDirection: 'column' }}>
            <div style={{
              padding: '16px 20px', borderBottom: '1px solid var(--border)',
              background: 'var(--bg)', display: 'flex', alignItems: 'center', gap: '8px'
            }}>
              <Search size={16} color="var(--text-tertiary)" />
              <span style={{ fontSize: '13px', fontWeight: 600, color: 'var(--text-secondary)', textTransform: 'uppercase', letterSpacing: '0.05em' }}>
                Select Task
              </span>
            </div>
            <div style={{ overflowY: 'auto', flex: 1 }}>
              {filteredTasks.map((task, index) => {
                const isSelected = selectedTask?.id === task.id
                const hasResult = results['both'] || results['nppf_only'] || results['local_only']
                return (
                  <motion.button
                    initial={{ opacity: 0 }}
                    animate={{ opacity: 1 }}
                    transition={{ }}
                    key={task.id}
                    onClick={() => setSelectedTask(task)}
                    style={{
                      display: 'block', width: '100%', textAlign: 'left',
                      padding: '16px 20px', border: 'none', borderBottom: '1px solid var(--border)',
                      background: isSelected ? 'rgba(0, 113, 227, 0.08)' : 'transparent',
                      cursor: 'pointer', transition: 'all 0.2s',
                      borderLeft: isSelected ? '4px solid var(--accent)' : '4px solid transparent',
                    }}
                  >
                    <div style={{ display: 'flex', gap: '8px', alignItems: 'center', marginBottom: '8px' }}>
                      <span style={{
                        fontFamily: 'var(--font-mono)', fontSize: '12px',
                        color: isSelected ? 'var(--accent)' : 'var(--text-tertiary)',
                        fontWeight: 600,
                      }}>
                        {task.id}
                      </span>
                      {(results[task.id] || (isSelected && Object.keys(results).length > 0)) && (
                        <span className="badge badge-green" style={{ fontSize: '10px' }}>Ran</span>
                      )}
                    </div>
                    <div style={{
                      fontSize: '13px', color: isSelected ? 'var(--text-primary)' : 'var(--text-secondary)',
                      lineHeight: '1.6', fontWeight: isSelected ? 500 : 400,
                      display: '-webkit-box', WebkitLineClamp: 2,
                      WebkitBoxOrient: 'vertical', overflow: 'hidden',
                    }}>
                      {task.task}
                    </div>
                  </motion.button>
                )
              })}
            </div>
          </div>
        </div>

        {/* Right: comparison area */}
        <div style={{ display: 'flex', flexDirection: 'column', gap: '24px' }}>
          {/* Selected task info */}
          <AnimatePresence mode="wait">
            {selectedTask ? (
              <motion.div 
                key={selectedTask.id}
                initial={{ opacity: 0 }}
                animate={{ opacity: 1 }}
                exit={{ opacity: 0 }}
                className="card" 
                style={{ padding: '24px' }}
              >
                <div style={{ display: 'flex', gap: '12px', marginBottom: '16px', flexWrap: 'wrap', alignItems: 'center' }}>
                  <span className="badge badge-gray" style={{ fontFamily: 'var(--font-mono)' }}>
                    {selectedTask.id}
                  </span>
                  <span className="badge" style={{ background: 'var(--bg3)', color: 'var(--accent)' }}>
                    {CATEGORY_LABELS[selectedTask.category] || selectedTask.category}
                  </span>
                  <span className={`badge ${
                    selectedTask.difficulty === 'hard' ? 'badge-red'
                    : selectedTask.difficulty === 'easy' ? 'badge-green'
                    : 'badge-amber'
                  }`}>
                    {selectedTask.difficulty}
                  </span>
                  {selectedTask.expected_source && (
                    <span className="badge badge-teal" style={{ background: 'rgba(90, 200, 250, 0.15)', color: '#0C85A8' }}>
                      Expected: {selectedTask.expected_source.replace('.pdf', '')}
                    </span>
                  )}
                </div>
                <p style={{ fontSize: '16px', lineHeight: '1.6', color: 'var(--text-primary)', marginBottom: '24px', fontWeight: 500 }}>
                  {selectedTask.task}
                </p>

                {/* Run controls */}
                <div style={{ display: 'flex', gap: '12px', flexWrap: 'wrap', alignItems: 'center', background: 'var(--bg)', padding: '16px', borderRadius: 'var(--radius-sm)', border: '1px solid var(--border)' }}>
                  <motion.button
                    whileHover={{ scale: 1.02 }}
                    whileTap={{ scale: 0.98 }}
                    className="btn btn-primary"
                    onClick={runAll}
                    disabled={anyRunning || !vsReady}
                    style={{ padding: '10px 20px' }}
                  >
                    {anyRunning
                      ? <><div className="spinner" style={{ width: '16px', height: '16px' }} /> Running All</>
                      : <><Play size={16} /> Run All 3 Subsets</>
                    }
                  </motion.button>
                  <span style={{ fontSize: '13px', color: 'var(--text-tertiary)', fontWeight: 500, margin: '0 8px' }}>OR RUN INDIVIDUALLY:</span>
                  {subsets.map(subset => (
                    <button
                      key={subset.id}
                      className="btn btn-secondary btn-sm"
                      onClick={() => runSubset(subset)}
                      disabled={anyRunning || !vsReady}
                      style={{ 
                        borderColor: running[subset.id] ? subset.color : 'var(--border2)', 
                        color: running[subset.id] ? subset.color : 'var(--text-secondary)',
                        background: running[subset.id] ? `${subset.color}15` : 'var(--bg2)'
                      }}
                    >
                      {running[subset.id]
                        ? <><div className="spinner" style={{ width: '14px', height: '14px', borderTopColor: subset.color }} /> Running</>
                        : subset.label
                      }
                    </button>
                  ))}
                </div>
              </motion.div>
            ) : (
              <div className="card" style={{ textAlign: 'center', padding: '80px 40px', display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center' }}>
                <div style={{ width: '64px', height: '64px', borderRadius: '50%', background: 'var(--bg3)', color: 'var(--text-tertiary)', display: 'flex', alignItems: 'center', justifyContent: 'center', marginBottom: '24px' }}>
                  <SplitSquareHorizontal size={32} />
                </div>
                <h2 style={{ fontSize: '24px', marginBottom: '12px', letterSpacing: '-0.01em' }}>Select a task to begin</h2>
                <p style={{ color: 'var(--text-secondary)', fontSize: '15px', maxWidth: '400px' }}>
                  Pick a planning task from the left panel, then run it against each document subset.
                </p>
              </div>
            )}
          </AnimatePresence>

          {selectedTask && (
            <>
              {/* 3-column output comparison */}
              <div style={{ display: 'flex', gap: '20px', alignItems: 'stretch' }}>
                {subsets.map((subset, i) => (
                  <OutputCard
                    key={subset.id}
                    subset={subset}
                    result={results[subset.id]}
                    running={!!running[subset.id]}
                   
                  />
                ))}
              </div>

              {/* Analysis summary — only shown once all 3 subsets have run */}
              <AnimatePresence>
                {subsets.every(s => results[s.id]) && (
                  <motion.div 
                    initial={{ opacity: 0 }}
                    animate={{ opacity: 1 }}
                    className="card" 
                    style={{ marginTop: '8px', borderLeft: '4px solid var(--accent)' }}
                  >
                    <h3 style={{ marginBottom: '20px', fontSize: '18px', display: 'flex', alignItems: 'center', gap: '8px' }}>
                      <BarChart3 size={20} color="var(--accent)" /> Ablation Summary
                    </h3>
                    <div style={{ display: 'grid', gridTemplateColumns: 'repeat(3, 1fr)', gap: '20px' }}>
                      {subsets.map(subset => {
                        const r = results[subset.id]
                        const chunks = r?.retrieved_chunks || []
                        const avgRel = chunks.length
                          ? (chunks.reduce((a, c) => a + c.relevance_score, 0) / chunks.length * 100).toFixed(1)
                          : null
                        const sources = getChunkSources(subset.id)
                        return (
                          <div key={subset.id} style={{
                            background: 'var(--bg)', borderRadius: 'var(--radius-sm)',
                            padding: '16px', borderTop: `3px solid ${subset.color}`,
                            border: '1px solid var(--border)', borderTopWidth: '3px'
                          }}>
                            <div style={{ fontWeight: 600, color: subset.color, fontSize: '14px', marginBottom: '12px' }}>
                              {subset.label}
                            </div>
                            <div style={{ display: 'flex', flexDirection: 'column', gap: '8px', fontSize: '13px', color: 'var(--text-secondary)' }}>
                              <div style={{ display: 'flex', justifyContent: 'space-between' }}>
                                <span>Chunks:</span> <strong style={{ color: 'var(--text-primary)' }}>{chunks.length}</strong>
                              </div>
                              {avgRel && (
                                <div style={{ display: 'flex', justifyContent: 'space-between' }}>
                                  <span>Relevance:</span> <strong style={{ color: 'var(--text-primary)' }}>{avgRel}%</strong>
                                </div>
                              )}
                              <div style={{ display: 'flex', justifyContent: 'space-between' }}>
                                <span>Tokens:</span> <strong style={{ color: 'var(--text-primary)' }}>{r?.rag_tokens_used ?? '—'}</strong>
                              </div>
                              <div style={{ display: 'flex', flexDirection: 'column', marginTop: '4px' }}>
                                <span style={{ marginBottom: '4px' }}>Sources used:</span>
                                <strong style={{ color: 'var(--teal)', fontSize: '12px', background: 'rgba(90, 200, 250, 0.1)', padding: '4px 8px', borderRadius: '4px' }}>
                                  {sources.length > 0 ? sources.map(s => s.replace('.pdf','')).join(', ') : 'None'}
                                </strong>
                              </div>
                            </div>
                          </div>
                        )
                      })}
                    </div>
                    <div style={{
                      marginTop: '24px', padding: '16px 20px',
                      background: 'rgba(0, 113, 227, 0.05)', borderRadius: 'var(--radius-sm)',
                      border: '1px solid rgba(0, 113, 227, 0.15)', fontSize: '13px', color: 'var(--text-secondary)',
                      lineHeight: 1.6, display: 'flex', gap: '12px'
                    }}>
                      <div style={{ fontSize: '18px' }}>💡</div>
                      <div>
                        <strong style={{ color: 'var(--accent)', display: 'block', marginBottom: '4px' }}>Dissertation Note</strong>
                        Compare the "Both Docs" answer against single-source answers to identify whether the RAG system
                        correctly retrieves from the most relevant document, and whether combining sources improves
                        answer completeness or introduces conflation errors.
                      </div>
                    </div>
                  </motion.div>
                )}
              </AnimatePresence>
            </>
          )}
        </div>
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
