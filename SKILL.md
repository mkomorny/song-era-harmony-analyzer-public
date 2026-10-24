---
name: song-era-harmony-analyzer
description: Analyzes harmonic trends, chord vocabularies, popular 4-chord loops, and songwriting tropes across musical decades (1960s through 2010s) using 16,800+ dated songs from the Lakh MIDI dataset. Triggered in chat whenever the user asks about chord habits of an era, vintage songwriting styles, or decade comparisons.
---

# Song Era Harmony Analyzer

Profiles the chord vocabularies, signature chord loops, and harmonic evolution of 16,800+ dated songs across the 1960s, 1970s, 1980s, 1990s, and 2000s from `B:\AI Directories_Databases\Datasets\midi_datasets\lmd_chords`.

Whenever the user asks about the harmonic DNA of a musical decade, vintage chord tropes, or era-specific songwriting habits, activate this skill.

---

## When to Activate

Trigger this skill whenever the user says things like:
* *"What chords made 80s synth-pop sound the way it did?"*
* *"What were the most popular chord progressions of the 1970s?"*
* *"Give me authentic, period-accurate chord loops for a 90s R&B or grunge track."*
* *"How did chord vocabulary change between the 60s and 2000s?"*
* *"What chord tricks did 80s songwriters use for dramatic choruses?"*

---

## How to Execute Under the Hood (Silent Agent Workflow)

You do **NOT** ask the user to run scripts in PowerShell. Run the query invisibly using terminal/bash commands:

```bash
# Analyze a specific decade:
python "<skill_dir>/scripts/era_harmony.py" --decade "80s"
python "<skill_dir>/scripts/era_harmony.py" --decade "70s"
python "<skill_dir>/scripts/era_harmony.py" --decade "90s"
python "<skill_dir>/scripts/era_harmony.py" --decade "60s"
python "<skill_dir>/scripts/era_harmony.py" --decade "2000s"
```

The script processes thousands of dated songs in under 2 seconds and returns JSON with:
* Chord quality breakdown (Triads vs 7ths vs Extended/Altered).
* The top recurring 4-chord loops of that decade.
* Real song examples with artists, song titles, and exact years.

---

## Chat Presentation Guidelines

When presenting the era analysis to the user in chat:

1. **The Era's Harmonic Identity:** Summarize the defining musical mood of the decade (e.g. 60s blues/folk-rock foundations, 70s sophisticated minor 7ths & modal funk, 80s soaring suspended chords & power cadences, 90s alternative loops).
2. **Chord Vocabulary Breakdown:** Show the percentage of basic triads vs 7ths and extended chords.
3. **Top Signature Progressions:** List the top 3–4 chord sequences that defined that era.
4. **Song DNA Citing:** Reference 2–3 famous tracks from that decade in the database (e.g. Sting, ZZ Top, Soundgarden, Prince).
5. **Authentic Songwriting Recipe:** Provide 3 actionable tips for writing a song with authentic vintage sound today, and offer to export a `.mid` clip to Ableton using `ableton-midi-chord-builder`!
