r"""
Song Era Harmony Analyzer
Mines 16,800+ dated songs from B:\DATABASES\Music_Audio\Music_Theory\midi_datasets\lmd_chords to extract decade-by-decade chord vocabularies, popular loops, and harmonic tropes.
"""

import sys
import json
import argparse
from pathlib import Path
from collections import Counter

try:
    import pyarrow.parquet as pq
except ImportError:
    import subprocess
    subprocess.check_call([sys.executable, "-m", "pip", "install", "pyarrow"])
    import pyarrow.parquet as pq

DATASET_PATH = Path(r"B:\DATABASES\Music_Audio\Music_Theory\midi_datasets\lmd_chords\train-00000-of-00001.parquet")

DECADE_ALIASES = {
    "60s": 1960, "1960s": 1960, "60": 1960, "1960": 1960,
    "70s": 1970, "1970s": 1970, "70": 1970, "1970": 1970,
    "80s": 1980, "1980s": 1980, "80": 1980, "1980": 1980,
    "90s": 1990, "1990s": 1990, "90": 1990, "1990": 1990,
    "00s": 2000, "2000s": 2000, "2000": 2000, "y2k": 2000,
    "2010s": 2010, "10s": 2010, "2010": 2010
}

def clean_decade(d_input):
    s = str(d_input).strip().lower()
    return DECADE_ALIASES.get(s, None) or (int(s) if s.isdigit() and len(s) == 4 else 1980)

def extract_chord_quality(chord_str):
    if not chord_str or chord_str == "N":
        return None
    c = chord_str.split("/")[0]
    if len(c) > 1 and c[1] in ["#", "b", "B"]:
        q = c[2:].lower()
    else:
        q = c[1:].lower()
    if q.startswith(":"):
        q = q[1:]
    if q in ["", "maj", "major"]:
        return "Major Triad"
    if q in ["m", "min", "minor"]:
        return "Minor Triad"
    if "maj7" in q:
        return "Major 7th"
    if "min7" in q or "m7" in q:
        return "Minor 7th"
    if "7" in q:
        return "Dominant 7th"
    if "sus" in q:
        return "Suspended (sus2/sus4)"
    if "9" in q:
        return "9th Extension"
    if "dim" in q:
        return "Diminished"
    return "Extended/Altered"

def analyze_decade(target_decade, top_k=5):
    table = pq.read_table(str(DATASET_PATH), columns=['title', 'artist', 'year', 'chords'])
    num_rows = table.num_rows
    
    qualities_counter = Counter()
    loops_counter = Counter()
    matching_songs = []
    total_chords_analyzed = 0
    songs_in_decade = 0
    
    for i in range(num_rows):
        y = table['year'][i].as_py()
        if not isinstance(y, int) or (y // 10) * 10 != target_decade:
            continue
            
        songs_in_decade += 1
        symbols = [s for s in table['chords'][i]['symbol'].as_py() if s != 'N']
        if len(symbols) < 4:
            continue
            
        artist = table['artist'][i].as_py() or "Unknown Artist"
        title = table['title'][i].as_py() or "Untitled"
        
        # Save sample songs
        if len(matching_songs) < 8 and (artist, title) not in [(s['artist'], s['title']) for s in matching_songs]:
            matching_songs.append({
                "artist": artist,
                "title": title,
                "year": y,
                "preview_chords": " -> ".join(symbols[:6])
            })
            
        # Count qualities
        for sym in symbols:
            q = extract_chord_quality(sym)
            if q:
                qualities_counter[q] += 1
                total_chords_analyzed += 1
                
        # Count 4-chord sequential loops
        for j in range(len(symbols) - 3):
            sub = tuple(symbols[j:j+4])
            # Avoid single repeated chord like (C, C, C, C)
            if len(set(sub)) >= 3:
                loops_counter[sub] += 1

    quality_breakdown = []
    for q, cnt in qualities_counter.most_common():
        quality_breakdown.append({
            "quality": q,
            "count": cnt,
            "percentage": round((cnt / (total_chords_analyzed or 1)) * 100, 1)
        })
        
    top_loops = []
    for loop, cnt in loops_counter.most_common(top_k):
        top_loops.append({
            "progression": " -> ".join(loop),
            "occurrences": cnt
        })

    return {
        "decade": f"{target_decade}s",
        "songs_analyzed": songs_in_decade,
        "total_chords_profiled": total_chords_analyzed,
        "top_harmonic_qualities": quality_breakdown[:6],
        "most_common_4_chord_loops": top_loops,
        "iconic_songs_from_era": matching_songs
    }

def main():
    parser = argparse.ArgumentParser(description="Analyze harmonic traits and chord loops by musical decade.")
    parser.add_argument("--decade", default="80s", help="Decade to analyze (e.g. 60s, 70s, 80s, 90s, 2000s)")
    args = parser.parse_args()
    
    dec = clean_decade(args.decade)
    res = analyze_decade(dec)
    print(json.dumps(res, indent=2))

if __name__ == "__main__":
    main()
