import json

transcript_path = r"C:\Users\johnl\.gemini\antigravity-ide\brain\a819ae44-22c0-445d-89ba-e9590dc49652\.system_generated\logs\transcript_full.jsonl"
full_reconstruction = []

with open(transcript_path, 'r', encoding='utf-8') as f:
    for i, line in enumerate(f):
        if 'Total Lines: 2989' in line and 'VIEW_FILE' in line:
            try:
                data = json.loads(line)
                content = data.get('content', '')
                
                # Check for relevant slides
                if 'slide-10' in content or 'slide-11' in content or 'slide-12' in content or 'slide-13' in content or 'slide-14' in content:
                    
                    # Extract the lines part
                    lines_part = content.split("The following code has been modified")[1].split("The above content")[0].strip()
                    
                    # Remove line numbers
                    clean_lines = []
                    for l in lines_part.split('\n'):
                        if ': ' in l:
                            clean_lines.append(l.split(': ', 1)[1])
                    
                    full_reconstruction.extend(clean_lines)
            except Exception as e:
                pass

with open('recovered_slides.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(full_reconstruction))

print("Recovered lines written to recovered_slides.txt")
