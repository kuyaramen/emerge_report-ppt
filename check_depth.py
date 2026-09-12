import re

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

def check_html(text):
    # Strip script and style blocks to avoid false positives
    text = re.sub(r'<script.*?>.*?</script>', '', text, flags=re.DOTALL)
    text = re.sub(r'<style.*?>.*?</style>', '', text, flags=re.DOTALL)
    
    tags = re.findall(r'</?div[^>]*>', text)
    depth = 0
    slide_depths = []
    
    for tag in tags:
        if tag.startswith('</div'):
            depth -= 1
            if depth == 0:
                print("Container div closed!")
        elif not tag.endswith('/>'):
            depth += 1
            if 'id="slide-' in tag:
                print(f"Slide tag at depth {depth}: {tag[:30]}")
                slide_depths.append(depth)
                
    print(f"Final depth: {depth}")

check_html(text)
