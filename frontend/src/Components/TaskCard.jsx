import React, { useState } from 'react'

const CATEGORY_COLORS = {
  policy_compliance:         'var(--accent)',
  evidence_synthesis:        'var(--green)',
  site_appraisal:            'var(--amber)',
  stakeholder_communication: 'var(--purple)',
  strategic_analysis:        'var(--teal)',
}

const CATEGORY_LABELS = {
  policy_compliance:         'Policy Compliance',
  evidence_synthesis:        'Evidence Synthesis',
  site_appraisal:            'Site Appraisal',
  stakeholder_communication: 'Stakeholder Communication',
  strategic_analysis:        'Strategic Analysis',
}

/**
 * TaskCard — displays a single planning task with its metadata badges.
 *
 * Props:
 *   task        {object}  Task object from /tasks API
 *   result      {object?} TaskResult if the task has been run
 *   onRun       {fn}      Called when the "Run" button is clicked
 *   isRunning   {bool}    Whether this task is currently running
 *   disabled    {bool}    Whether any run action is currently blocked
 */
export default function TaskCard({ task, result, onRun, isRunning, disabled }) {
  const [expanded, setExpanded] = useState(false)

  const hasResult    = result?.baseline_output || result?.rag_output
  const fullyScored  = result?.baseline_scores && result?.rag_scores
  const catColor     = CATEGORY_COLORS[task.category] || 'var(--accent)'

  return (
    <div
      className="card"
      style={{
        borderLeft: `3px solid ${catColor}`,
        transition: 'box-shadow 0.15s',
      }}
    >
      {/* ── Header row ─────────────────────────────────────── */}
      <div style={{ display: 'flex', alignItems: 'flex-start', gap: '12px' }}>
        <div style={{ flex: 1 }}>
          {/* Badges */}
          <div style={{ display: 'flex', gap: '6px', marginBottom: '8px', flexWrap: 'wrap', alignItems: 'center' }}>
            <span className="badge badge-gray" style={{ fontFamily: 'var(--font-mono)' }}>
              {task.id}
            </span>
            <span className="badge" style={{
              background: `${catColor}22`,
              color: catColor,
            }}>
              {CATEGORY_LABELS[task.category]}
            </span>
            <span className={`badge ${
              task.difficulty === 'hard'   ? 'badge-red'   :
              task.difficulty === 'easy'   ? 'badge-green' :
              'badge-amber'
            }`}>
              {task.difficulty}
            </span>
            {hasResult   && <span className="badge badge-green">✓ Done</span>}
            {fullyScored && <span className="badge badge-purple">✓ Scored</span>}
          </div>

          {/* Task text */}
          <p style={{ fontSize: '13px', color: 'var(--text)', lineHeight: '1.65' }}>
            {task.task}
          </p>

          {/* Optional note */}
          {task.notes && (
            <p style={{ fontSize: '12px', color: 'var(--text3)', marginTop: '4px', fontStyle: 'italic' }}>
              ℹ {task.notes}
            </p>
          )}

          {/* Expected source */}
          {task.expected_source && (
            <div style={{ marginTop: '6px', display: 'flex', gap: '6px', flexWrap: 'wrap' }}>
              <span className="badge badge-teal" style={{ fontSize: '10px' }}>
                Source: {task.expected_source}
              </span>
              {task.expected_paragraphs?.map(p => (
                <span key={p} className="badge badge-blue" style={{ fontSize: '10px' }}>{p}</span>
              ))}
            </div>
          )}
        </div>

        {/* Run / re-run button */}
        <div style={{ display: 'flex', flexDirection: 'column', gap: '6px', flexShrink: 0 }}>
          <button
            className={`btn ${hasResult ? 'btn-secondary' : 'btn-primary'} btn-sm`}
            onClick={() => onRun(task.id)}
            disabled={isRunning || disabled}
          >
            {isRunning
              ? <><div className="spinner" style={{ width: '13px', height: '13px' }} /> Running</>
              : hasResult ? '↺ Re-run' : '▶ Run'
            }
          </button>

          {/* Expand/collapse results */}
          {hasResult && (
            <button
              className="btn btn-ghost btn-sm"
              onClick={() => setExpanded(e => !e)}
              style={{ fontSize: '11px' }}
            >
              {expanded ? '▲ Hide' : '▼ Outputs'}
            </button>
          )}
        </div>
      </div>

      {/* ── Expanded output preview ─────────────────────────── */}
      {expanded && hasResult && (
        <div style={{ marginTop: '16px', display: 'flex', gap: '14px' }}>
          {/* Baseline */}
          <div style={{ flex: 1 }}>
            <div style={{ display: 'flex', alignItems: 'center', gap: '6px', marginBottom: '6px' }}>
              <div style={{ width: '7px', height: '7px', borderRadius: '50%', background: 'var(--amber)' }} />
              <span style={{ fontSize: '12px', fontWeight: '500', color: 'var(--amber)' }}>Baseline</span>
              {result.baseline_tokens_used && (
                <span style={{ marginLeft: 'auto', fontSize: '11px', color: 'var(--text3)' }}>
                  {result.baseline_tokens_used} tokens
                </span>
              )}
            </div>
            <div className="output-box" style={{ maxHeight: '160px', fontSize: '12px' }}>
              {result.baseline_output || 'No output'}
            </div>
            {result.baseline_scores && (
              <div style={{ display: 'flex', gap: '6px', marginTop: '6px', flexWrap: 'wrap' }}>
                <span className="badge badge-amber" style={{ fontSize: '10px' }}>Acc {result.baseline_scores.accuracy}/5</span>
                <span className="badge badge-gray"  style={{ fontSize: '10px' }}>Comp {result.baseline_scores.completeness}/5</span>
                {result.baseline_scores.hallucination_present
                  ? <span className="badge badge-red"   style={{ fontSize: '10px' }}>Halluc ✗</span>
                  : <span className="badge badge-green" style={{ fontSize: '10px' }}>Halluc ✓</span>
                }
              </div>
            )}
          </div>

          {/* RAG */}
          <div style={{ flex: 1 }}>
            <div style={{ display: 'flex', alignItems: 'center', gap: '6px', marginBottom: '6px' }}>
              <div style={{ width: '7px', height: '7px', borderRadius: '50%', background: 'var(--green)' }} />
              <span style={{ fontSize: '12px', fontWeight: '500', color: 'var(--green)' }}>RAG</span>
              {result.rag_tokens_used && (
                <span style={{ marginLeft: 'auto', fontSize: '11px', color: 'var(--text3)' }}>
                  {result.rag_tokens_used} tokens
                </span>
              )}
            </div>
            <div className="output-box" style={{ maxHeight: '160px', fontSize: '12px' }}>
              {result.rag_output || 'No output'}
            </div>
            {result.rag_scores && (
              <div style={{ display: 'flex', gap: '6px', marginTop: '6px', flexWrap: 'wrap' }}>
                <span className="badge badge-green" style={{ fontSize: '10px' }}>Acc {result.rag_scores.accuracy}/5</span>
                <span className="badge badge-gray"  style={{ fontSize: '10px' }}>Comp {result.rag_scores.completeness}/5</span>
                {result.rag_scores.hallucination_present
                  ? <span className="badge badge-red"   style={{ fontSize: '10px' }}>Halluc ✗</span>
                  : <span className="badge badge-green" style={{ fontSize: '10px' }}>Halluc ✓</span>
                }
              </div>
            )}
          </div>
        </div>
      )}
    </div>
  )
}
