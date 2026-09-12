import re

html_path = 'index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

new_slide = """        <!-- ============================================ -->
        <!-- SLIDE 7: Two Main Types of Serverless Computing -->
        <!-- ============================================ -->
        <div class="slide" id="slide-7">
            <h2>Two Main Types of Serverless Computing</h2>
            <p>Serverless services are commonly divided into two main types:</p>
            
            <div class="two-column" style="margin-top:28px;">
                <div class="card primary text-center" style="opacity: 0; animation: fadeSlideUp 0.8s ease-out 0.2s forwards;">
                    <div style="font-size:2.5rem; margin-bottom:12px; color:var(--cyan);">{"\\u26A1"}</div>
                    <h3 style="color:var(--white); margin-bottom:16px;">FaaS — Function as a Service</h3>
                    <p style="color:var(--muted); font-size:1rem;">Run small pieces of code when triggered by an event or request.</p>
                    <ul style="text-align:left; color:var(--muted); font-size:0.95rem; margin-top:16px;">
                        <li>Code execution</li>
                        <li>Event-triggered functions</li>
                        <li>Example: AWS Lambda</li>
                    </ul>
                </div>
                
                <div class="card secondary text-center" style="opacity: 0; animation: fadeSlideUp 0.8s ease-out 0.5s forwards;">
                    <div style="font-size:2.5rem; margin-bottom:12px; color:var(--cyan);">{"\\uD83D\\uDDC4\\uFE0F"}</div>
                    <h3 style="color:var(--white); margin-bottom:16px;">BaaS — Backend as a Service</h3>
                    <p style="color:var(--muted); font-size:1rem;">Use ready-made backend services such as authentication, databases, and storage.</p>
                    <ul style="text-align:left; color:var(--muted); font-size:0.95rem; margin-top:16px;">
                        <li>Ready-made backend services</li>
                        <li>Authentication and databases</li>
                        <li>Example: Firebase or Supabase</li>
                    </ul>
                </div>
            </div>
            
            <h4 style="text-align:center; color:var(--cyan); margin-top:36px; font-weight:600;">Serverless = Managed Infrastructure + Flexible Services</h4>
        </div>

"""

split_marker = "        <!-- ============================================ -->\n        <!-- SLIDE 7: FaaS -->"
if split_marker not in content:
    # Try finding just SLIDE 7
    parts = content.split("<!-- SLIDE 7:")
    if len(parts) == 2:
        first_part = parts[0]
        second_part = "<!-- SLIDE 7:" + parts[1]
    else:
        print("Could not find SLIDE 7 marker.")
        exit(1)
else:
    parts = content.split(split_marker)
    first_part = parts[0]
    second_part = split_marker + parts[1]

def replacer(match):
    num = int(match.group(1))
    return f'SLIDE {num + 1}'

second_part = re.sub(r'SLIDE (\d+)', replacer, second_part)

def id_replacer(match):
    num = int(match.group(1))
    return f'id="slide-{num + 1}"'

second_part = re.sub(r'id="slide-(\d+)"', id_replacer, second_part)

new_content = first_part + new_slide + second_part

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Updated index.html successfully.")
