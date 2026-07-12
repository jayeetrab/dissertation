import React from 'react'
import { BrowserRouter, Routes, Route, NavLink, useLocation } from 'react-router-dom'
import { motion, AnimatePresence } from 'framer-motion'
import { LayoutDashboard, Play, CheckCircle, BarChart2, SplitSquareHorizontal } from 'lucide-react'

import Dashboard from './pages/dashboard.jsx'
import RunExperiment from './pages/runexperiment.jsx'
import Evaluate from './pages/evaluate.jsx'
import Results from './pages/results.jsx'
import Compare from './pages/compare.jsx'

// ── API base URL ──────────────────────────────────────────────
export const API = (() => {
  const base = import.meta.env.VITE_API_URL
  return base ? base : '/api'
})()

// ── Navigation ────────────────────────────────────────────────
function Nav() {
  const location = useLocation()

  const links = [
    { to: '/', label: 'Dashboard', icon: <LayoutDashboard size={16} /> },
    { to: 'run', label: 'Run Experiment', icon: <Play size={16} /> },
    { to: 'evaluate', label: 'Evaluate', icon: <CheckCircle size={16} /> },
    { to: 'results', label: 'Results & Export', icon: <BarChart2 size={16} /> },
    { to: 'compare', label: 'Compare Sources', icon: <SplitSquareHorizontal size={16} /> },
  ]

  return (
    <nav style={{
      background: 'rgba(20, 20, 25, 0.6)',
      backdropFilter: 'blur(32px) saturate(150%)',
      WebkitBackdropFilter: 'blur(32px) saturate(150%)',
      borderBottom: '1px solid var(--border)',
      boxShadow: '0 4px 24px rgba(0,0,0,0.2)',
      padding: '0 32px',
      display: 'flex',
      alignItems: 'center',
      gap: '24px',
      height: '64px',
      position: 'sticky',
      top: 0,
      zIndex: 100,
    }}>
      {/* Logo */}
      <div style={{ marginRight: '32px', display: 'flex', alignItems: 'center', gap: '8px' }}>
        <div style={{
          width: '24px', height: '24px', borderRadius: '4px',
          background: 'var(--text-primary)', display: 'flex',
          alignItems: 'center', justifyContent: 'center',
          fontSize: '12px', fontWeight: '700', color: 'white',
          fontFamily: 'var(--font-sans)',
        }}>P</div>
        <span style={{
          fontFamily: 'var(--font-sans)',
          fontWeight: '600', fontSize: '15px', color: 'var(--text-primary)',
          letterSpacing: '-0.01em'
        }}>PlanningRAG</span>
      </div>

      {/* Nav links */}
      <div style={{ display: 'flex', height: '100%', gap: '8px' }}>
        {links.map(link => {
          const isActive = location.pathname === link.to || (link.to !== '/' && location.pathname.startsWith(`/${link.to}`));
          return (
            <NavLink
              key={link.to}
              to={link.to}
              end={link.to === '/'}
              style={{
                position: 'relative',
                padding: '0 16px',
                height: '100%',
                display: 'flex',
                alignItems: 'center',
                gap: '8px',
                fontSize: '14px',
                fontWeight: isActive ? '600' : '500',
                color: isActive ? 'var(--text-primary)' : 'var(--text-secondary)',
                textDecoration: 'none',
                transition: 'color 0.2s',
              }}
            >
              <span style={{ display: 'flex', opacity: isActive ? 1 : 0.7 }}>{link.icon}</span>
              {link.label}
              
              {isActive && (
                <motion.div
                  layoutId="nav-indicator"
                  transition={{ type: "spring", stiffness: 400, damping: 40 }}
                  style={{
                    position: 'absolute',
                    bottom: -1,
                    left: 0,
                    right: 0,
                    height: '2px',
                    background: 'var(--accent)',
                    boxShadow: '0 -2px 10px rgba(96, 165, 250, 0.4)',
                    borderTopLeftRadius: '2px',
                    borderTopRightRadius: '2px'
                  }}
                />
              )}
            </NavLink>
          )
        })}
      </div>

      {/* Right side — dissertation info */}
      <div style={{ marginLeft: 'auto', display: 'flex', alignItems: 'center', gap: '12px' }}>
        <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'flex-end' }}>
          <span style={{ fontSize: '12px', fontWeight: 500, color: 'var(--text-primary)' }}>Jayeetra B.</span>
          <span style={{ fontSize: '11px', color: 'var(--text-secondary)' }}>MSc Business Analytics</span>
        </div>
      </div>
    </nav>
  )
}

// ── AppContent ────────────────────────────────────────────────
function AppContent() {
  const location = useLocation()
  return (
    <>
      <Nav />
      <AnimatePresence mode="wait">
        <motion.main 
          key={location.pathname}
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          exit={{ opacity: 0 }}
          transition={{ duration: 0.2 }}
          style={{ flex: 1, padding: '40px 32px', maxWidth: '1400px', margin: '0 auto', width: '100%' }}
        >
          <Routes location={location}>
            <Route path="/"          element={<Dashboard />} />
            <Route path="/run"       element={<RunExperiment />} />
            <Route path="/evaluate"  element={<Evaluate />} />
            <Route path="/results"   element={<Results />} />
            <Route path="/compare"   element={<Compare />} />
          </Routes>
        </motion.main>
      </AnimatePresence>
    </>
  )
}

// ── App ───────────────────────────────────────────────────────
export default function App() {
  return (
    <BrowserRouter>
      <AppContent />
    </BrowserRouter>
  )
}