import React from 'react'

/**
 * Hallucination taxonomy from the dissertation:
 * - fabricated_clause      Invented policy paragraph that doesn't exist
 * - outdated_policy        Applied a pre-2024 NPPF version
 * - spatial_misattribution Wrong geographic policy applied
 * - confident_ambiguity    Definitive answer where policy is genuinely vague
 */

const HALLUCINATION_TYPES = [
  {
    value: 'fabricated_clause',
    label: 'Fabricated clause',
    description: 'Invented policy paragraph or rule that does not exist in source documents',
    color: 'var(--red)',
    icon: '🔴',
  },
  {
    value: 'outdated_policy',
    label: 'Outdated policy',
    description: 'Applied pre-2024 NPPF rules or superseded local plan policies',
    color: 'var(--amber)',
    icon: '🟡',
  },
  {
    value: 'spatial_misattribution',
    label: 'Spatial misattribution',
    description: 'Applied a policy from the wrong geographic area or authority',
    color: 'var(--purple)',
    icon: '🟣',
  },
  {
    value: 'confident_ambiguity',
    label: 'Confident ambiguity',
    description: 'Gave a definitive answer where policy is genuinely unclear or contested',
    color: 'var(--teal)',
    icon: '🔵',
  },
]

/**
 * HallucinationTag — UI for classifying hallucinations in an LLM output.
 *
 * Props:
 *   present         {bool}   Whether a hallucination is present
 *   type            {string} Hallucination type value (or 'none')
 *   detail          {string} Exact quoted text of the hallucination
 *   onPresentChange {fn}     Called with new bool when toggled
 *   onTypeChange    {fn}     Called with new type string on selection
 *   onDetailChange  {fn}     Called with new detail string on input
 */
export default function HallucinationTag({
  present,
  type,
  detail,
  onPresentChange,
  onTypeChange,
  onDetailChange,
}) {
  const selectedType = HALLUCINATION_TYPES.find(t => t.value === type)

  return (
    <div>
      <div className="label">Hallucination Assessment</div>

      {/* Present toggle */}
      <label style={{
        display: 'flex', alignItems: 'center', gap: '10px',
        cursor: 'pointer', marginBottom: '12px', userSelect: 'none',
      }}>
        <input
          type="checkbox"
          checked={present}
          onChange={e => onPresentChange(e.target.checked)}
          style={{ width: 'auto', accentColor: 'var(--red)', cursor: 'pointer' }}
        />
        <span style={{
          fontSize: '13px',
          color: present ? 'var(--red)' : 'var(--text2)',
          fontWeight: present ? '500' : '400',
          transition: 'color 0.15s',
        }}>
          {present ? '⚠ Hallucination detected' : 'No hallucination detected'}
        </span>
      </label>

      {/* Type selector — shown only when hallucination is present */}
      {present && (
        <div style={{ display: 'flex', flexDirection: 'column', gap: '10px' }}>

          {/* Visual type picker */}
          <div>
            <div className="label" style={{ marginBottom: '8px' }}>Hallucination Type</div>
            <div style={{ display: 'flex', flexDirection: 'column', gap: '6px' }}>
              {HALLUCINATION_TYPES.map(t => (
                <label
                  key={t.value}
                  style={{
                    display: 'flex', alignItems: 'flex-start', gap: '10px',
                    cursor: 'pointer',
                    background: type === t.value ? `${t.color}15` : 'var(--bg3)',
                    border: `1px solid ${type === t.value ? t.color : 'var(--border)'}`,
                    borderRadius: 'var(--radius-sm)', padding: '10px 12px',
                    transition: 'all 0.12s',
                  }}
                >
                  <input
                    type="radio"
                    name="halluc-type"
                    value={t.value}
                    checked={type === t.value}
                    onChange={() => onTypeChange(t.value)}
                    style={{ marginTop: '2px', accentColor: t.color, flexShrink: 0, cursor: 'pointer' }}
                  />
                  <div>
                    <div style={{ fontWeight: '500', fontSize: '13px', color: type === t.value ? t.color : 'var(--text)' }}>
                      {t.icon} {t.label}
                    </div>
                    <div style={{ fontSize: '11px', color: 'var(--text3)', marginTop: '2px', lineHeight: '1.5' }}>
                      {t.description}
                    </div>
                  </div>
                </label>
              ))}
            </div>
          </div>

          {/* Verbatim quote */}
          {type && type !== 'none' && (
            <div>
              <div className="label">Quote the hallucination verbatim</div>
              <textarea
                value={detail}
                onChange={e => onDetailChange(e.target.value)}
                placeholder={`Copy the exact hallucinated text here — e.g. "Policy H3 requires a 40% affordable housing contribution on all sites above 5 units"`}
                style={{
                  minHeight: '72px',
                  borderColor: detail ? `${selectedType?.color}66` : 'var(--border)',
                  fontFamily: 'var(--font-mono)',
                  fontSize: '12px',
                }}
              />
              {detail && (
                <div style={{
                  display: 'inline-block', marginTop: '6px',
                  background: `${selectedType?.color}15`,
                  border: `1px solid ${selectedType?.color}44`,
                  borderRadius: 'var(--radius-sm)', padding: '4px 10px',
                  fontSize: '11px', color: selectedType?.color,
                }}>
                  {selectedType?.icon} {selectedType?.label} · {detail.length} chars
                </div>
              )}
            </div>
          )}
        </div>
      )}
    </div>
  )
}
