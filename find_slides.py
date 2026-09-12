import json

# Read the transcript to find all VIEW_FILE entries for index.html
# that show data in the range where slides 10-14 would be (lines 1100-1600 of the 2989-line file)
transcript_path = r"C:\Users\johnl\.gemini\antigravity-ide\brain\a819ae44-22c0-445d-89ba-e9590dc49652\.system_generated\logs\transcript_full.jsonl"

results = []
with open(transcript_path, 'r', encoding='utf-8') as f:
    for i, line in enumerate(f):
        if 'Total Lines: 2989' in line and 'VIEW_FILE' in line:
            try:
                data = json.loads(line)
                content = data.get('content', '')
                # Check if this view covers lines in the 1100-1600 range
                if 'slide-10' in content or 'slide-11' in content or 'slide-12' in content or 'slide-13' in content or 'slide-14' in content:
                    results.append((i+1, content[:200]))
            except:
                pass

for r in results:
    print(f"Line {r[0]}: {r[1]}")
    print("---")
