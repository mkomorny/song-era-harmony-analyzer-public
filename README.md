# Song Era Harmony Analyzer

> **Tri-Platform Agent Skill** for Claude Desktop / Code, Grok CLI, and Google Antigravity / Gemini.  
> Analyzes harmonic trends, chord vocabularies, popular 4-chord loops, and songwriting tropes across musical decades (1960s through 2010s) using 16,800+ dated songs from the Lakh MIDI dataset on Drive B.

---

## Overview

Musical decades have distinct harmonic identities:
- **1960s**: Folk-rock and blues roots, dominance of basic major and minor triads with blues dominant 7ths.
- **1970s**: Emergence of funk, disco, and fusion, with heavy usage of minor 7ths, Dorian progressions, and acoustic major 7ths.
- **1980s**: Soaring synth-pop and stadium rock characterized by suspended chords ($\text{sus2}/\text{sus4}$), $\flat\text{VI} - \flat\text{VII} - \text{i}$ power cadences, and added 9ths.
- **1990s**: Alternative, grunge, and neo-soul shifting between melancholic minor loops and rich extended harmonies.
- **2000s / Y2K**: Pop-punk power chords, looping four-chord pop progressions ($vi - IV - I - V$), and modern R&B grooves.

**`song-era-harmony-analyzer`** parses 16,800+ dated song files in milliseconds using Apache PyArrow, delivering statistical chord quality distributions, top 4-chord loops, and famous song citations.

---

## Dataset & Technical Specs

- **Source File**: `B:\DATABASES\Music_Audio\Music_Theory\midi_datasets\lmd_chords\train-00000-of-00001.parquet`
- **Dated Songs Cataloged**: 16,800+ songs with confirmed release year metadata.
- **Query Engine**: `scripts/era_harmony.py` leveraging PyArrow Parquet columnar reads.

---

## CLI Usage

Run the analyzer standalone for any decade:

```bash
python scripts/era_harmony.py --decade "80s"
```

### JSON Output Example:
```json
{
  "decade": "1980s",
  "songs_analyzed": 2435,
  "total_chords_profiled": 206077,
  "top_harmonic_qualities": [
    { "quality": "Major Triad", "count": 100030, "percentage": 48.5 },
    { "quality": "Minor Triad", "count": 34993, "percentage": 17.0 },
    { "quality": "Minor 7th", "count": 24068, "percentage": 11.7 },
    { "quality": "Extended/Altered", "count": 17269, "percentage": 8.4 },
    { "quality": "Dominant 7th", "count": 14424, "percentage": 7.0 },
    { "quality": "Major 7th", "count": 14052, "percentage": 6.8 }
  ],
  "most_common_4_chord_loops": [
    { "progression": "C -> F -> G -> C", "occurrences": 200 },
    { "progression": "G -> C -> D -> G", "occurrences": 198 },
    { "progression": "D -> G -> C -> D", "occurrences": 193 },
    { "progression": "G -> F -> C -> G", "occurrences": 184 },
    { "progression": "C -> G -> F -> C", "occurrences": 181 }
  ],
  "iconic_songs_from_era": [
    { "artist": "Sting", "title": "Englishman In New York", "year": 1987, "preview_chords": "Em7 -> A6 -> Bm -> A6" },
    { "artist": "ZZ Top", "title": "Sharp Dressed Man", "year": 1983, "preview_chords": "C -> Cm -> Cm7b5/Bb -> Fm7" },
    { "artist": "Soundgarden", "title": "Gun", "year": 1989, "preview_chords": "G -> Fmaj7 -> D7 -> E7" }
  ]
}
```

---

## Agent Chat Presentation Protocol

1. **The Era's Harmonic Identity**: Concise summary of the decade's stylistic mood and core sound.
2. **Chord Vocabulary Breakdown**: Major/minor triads vs 7ths and extended chords.
3. **Top 4-Chord Loops**: Recurring chord sequences that define the era.
4. **Song DNA Citing**: 2–3 famous tracks from that decade in the database.
5. **Authentic Songwriting Recipe**: Concrete production tips and optional MIDI clip export via `ableton-midi-chord-builder`.

---

## Tri-Platform Architecture

Zero duplicate code across tools. Canonical source resides in `.agents`:
- **Canonical**: `C:\Users\<you>\.agents\skills\song-era-harmony-analyzer`
- **Claude**: `C:\Users\<you>\.claude\skills\song-era-harmony-analyzer` (NTFS Junction)
- **Grok**: `C:\Users\<you>\.grok\skills\song-era-harmony-analyzer` (NTFS Junction)
- **Antigravity**: `C:\Users\<you>\.gemini\config\skills\song-era-harmony-analyzer` (NTFS Junction)

---

## Documentation Suite

- [`HOW_TO_USE.txt`](file:///C:/Users/<you>/.agents/skills/song-era-harmony-analyzer/HOW_TO_USE.txt): Standardized user guide and prompt templates.
- [`IMPLEMENTATION_PLAN.md`](file:///C:/Users/<you>/.agents/skills/song-era-harmony-analyzer/IMPLEMENTATION_PLAN.md): Feature checklist and roadmap.
- [`App Changes Tracker.html`](file:///C:/Users/<you>/.agents/skills/song-era-harmony-analyzer/App%20Changes%20Tracker.html): Interactive visual version log.
- [`SKILL.md`](file:///C:/Users/<you>/.agents/skills/song-era-harmony-analyzer/SKILL.md): Agent system instructions and triggers.
