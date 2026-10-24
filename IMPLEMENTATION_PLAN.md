# Implementation Plan: Song Era Harmony Analyzer

Profiles the chord vocabularies, signature chord loops, and harmonic evolution of 16,800+ dated songs across the 1960s through 2000s from the Lakh MIDI dataset on Drive B.

---

## Deliverables Checklist

### v1.0.0 — Initial Release
- [x] **Core Era Miner**: `scripts/era_harmony.py` querying PyArrow Parquet table across dated songs (`train-00000-of-00001.parquet`). ✅ done in v1.0.0
- [x] **Decade Normalizer & Aliases**: Flexible decade string parsing (`60s`, `1970s`, `80`, `90s`, `y2k`, `2000s`). ✅ done in v1.0.0
- [x] **Harmonic Quality Classifier**: Categorizes chords into Major Triads, Minor Triads, Minor 7ths, Dominant 7ths, Major 7ths, Suspended, 9ths, and Diminished. ✅ done in v1.0.0
- [x] **Sequential 4-Chord Loop Extractor**: Identifies signature recurring loops while filtering out trivial static repeats. ✅ done in v1.0.0
- [x] **Tri-Platform Accessibility**: Canonical `.agents` installation linked to Claude, Grok, and Antigravity via NTFS junctions. ✅ done in v1.0.0
- [x] **Standard Documentation Suite**: `SKILL.md`, `HOW_TO_USE.txt`, `README.md`, `App Changes Tracker.html`, and `dev-notes-v1.0.0.md`. ✅ done in v1.0.0

---

## Roadmap & Future Enhancements

### v1.1.0 — Comparative Multi-Decade Analysis
- [ ] Add side-by-side `--compare "70s,80s"` mode illustrating harmonic shift metrics.
- [ ] Tempo (BPM) distribution correlation per decade.
- [ ] Key and mode preference trends across eras (e.g. rise of minor key pop in the 2000s).

### v1.2.0 — Genre Sub-Filtering & DAW Integration
- [ ] Cross-reference genre tags (Rock vs Funk vs Disco vs Synth-pop vs Grunge).
- [ ] Direct export of era-authentic 4-chord loops into Ableton User Library via `ableton-midi-chord-builder`.
