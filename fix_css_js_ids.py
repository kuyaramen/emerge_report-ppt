import re

def fix_css_and_js_ids():
    with open('index.html', 'r', encoding='utf-8') as f:
        html = f.read()

    # Split again at Slide 16 (since it is now ID 16)
    split_marker = '<!-- ============================================ -->\n        <!-- SLIDE 16: SERVERLESS COST MODEL -->'
    if split_marker not in html:
        print("Could not find split marker.")
        return

    parts = html.split(split_marker)
    first_half = parts[0]
    second_half = split_marker + parts[1]

    # Shift all CSS #slide-X references and JS getElementById('slide-X')
    for i in range(20, 14, -1):
        second_half = second_half.replace(f'#slide-{i} ', f'#slide-{i+1} ')
        second_half = second_half.replace(f"getElementById('slide-{i}')", f"getElementById('slide-{i+1}')")

    new_html = first_half + second_half

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(new_html)
        print("Updated CSS and JS selectors successfully.")

fix_css_and_js_ids()
