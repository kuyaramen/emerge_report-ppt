import re

def process_file():
    with open('index.html', 'r', encoding='utf-8') as f:
        html = f.read()

    split_marker = '<!-- ============================================ -->\n        <!-- SLIDE 15: SERVERLESS COST MODEL -->'
    if split_marker not in html:
        print("Could not find split marker.")
        return

    parts = html.split(split_marker)
    first_half = parts[0]
    second_half = split_marker + parts[1]

    # Increment slide IDs in the second half
    # Match id="slide-20" -> id="slide-21"
    for i in range(20, 14, -1):
        second_half = second_half.replace(f'id="slide-{i}"', f'id="slide-{i+1}"')
        second_half = second_half.replace(f'id="ans{i}"', f'id="ans{i+1}"')
        second_half = second_half.replace(f"ans{i}'", f"ans{i+1}'")
        second_half = second_half.replace(f'SLIDE {i}:', f'SLIDE {i+1}:')

    # Update slide counter at the bottom
    second_half = second_half.replace('1 / 20', '1 / 21')

    # Build new slide 15
    slide_15 = """        <!-- ============================================ -->
        <!-- SLIDE 15: SECURITY IN SERVERLESS COMPUTING -->
        <!-- ============================================ -->
        <div class="slide" id="slide-15" style="justify-content: flex-start; padding-top: 20px;">
            <h2 style="text-align: center; border-bottom: none; margin-bottom: 5px; text-transform: uppercase; letter-spacing: 2px;">Security in Serverless Computing</h2>
            <p style="text-align: center; color: var(--muted); max-width: 900px; margin: 0 auto 30px auto; font-size: 1.05rem;">
                Serverless platforms provide built-in security features, but developers must still protect application code, user data, and access permissions.
            </p>

            <style>
                #slide-15 .sec-layout {
                    display: flex; flex-direction: column; align-items: center; max-width: 1000px; margin: 0 auto; width: 100%; position: relative;
                }
                #slide-15 .sec-core-container {
                    position: relative; width: 350px; height: 350px; display: flex; justify-content: center; align-items: center; margin-bottom: 20px;
                }
                #slide-15 .sec-image {
                    width: 250px; height: 250px; border-radius: 50%; object-fit: cover; border: 3px solid var(--cyan); box-shadow: 0 0 30px rgba(34,211,238,0.4);
                    position: absolute; z-index: 2;
                }
                #slide-15 .sec-pulse {
                    position: absolute; width: 250px; height: 250px; border-radius: 50%; border: 2px solid var(--cyan);
                    animation: secPulse 3s infinite; z-index: 1;
                }
                @keyframes secPulse {
                    0% { transform: scale(1); opacity: 0.8; }
                    100% { transform: scale(1.5); opacity: 0; }
                }

                #slide-15 .sec-node {
                    position: absolute; width: 140px; padding: 10px; background: rgba(15,30,55,0.9); border: 1px solid rgba(255,255,255,0.2);
                    border-radius: 8px; color: white; text-align: center; cursor: pointer; transition: all 0.3s; z-index: 3;
                    font-size: 0.9rem; font-weight: 500; display: flex; justify-content: center; align-items: center;
                }
                #slide-15 .sec-node:hover, #slide-15 .sec-node.active {
                    border-color: var(--cyan); box-shadow: 0 0 15px rgba(34,211,238,0.3); transform: scale(1.05);
                }
                
                /* Node Positions */
                #slide-15 .node-1 { top: -10px; left: 105px; } /* Top center */
                #slide-15 .node-2 { top: 100px; right: -50px; } /* Right */
                #slide-15 .node-3 { bottom: 10px; right: 0px; } /* Bottom Right */
                #slide-15 .node-4 { bottom: 10px; left: 0px; } /* Bottom Left */
                #slide-15 .node-5 { top: 100px; left: -50px; } /* Left */

                #slide-15 .sec-panel {
                    max-width: 800px; margin: 0 auto; padding: 20px; background: rgba(34,211,238,0.05); border-left: 4px solid var(--cyan);
                    border-radius: 8px; display: none; text-align: left; animation: fadeIn 0.4s;
                }
                #slide-15 .sec-panel.active { display: block; }
                #slide-15 .sec-panel h4 { margin: 0 0 10px 0; color: var(--cyan); font-size: 1.1rem; }
                #slide-15 .sec-panel p { margin: 0 0 10px 0; color: #E2E8F0; font-size: 0.95rem; }
                #slide-15 .sec-panel .example { color: var(--muted); font-style: italic; margin: 0; font-size: 0.9rem; }

                @media (max-width: 800px) {
                    #slide-15 .sec-core-container { width: 100%; height: auto; flex-direction: column; gap: 15px; margin-bottom: 20px; }
                    #slide-15 .sec-image, #slide-15 .sec-pulse { position: static; width: 150px; height: 150px; animation: none; margin-bottom: 20px; }
                    #slide-15 .sec-node { position: static; width: 100%; max-width: 300px; transform: none !important; margin: 5px 0; }
                }
            </style>

            <div class="sec-layout">
                <div class="sec-core-container">
                    <div class="sec-pulse"></div>
                    <img src="images/secure_serverless_shield_1789216836744.png" alt="Serverless Security Core" class="sec-image">
                    
                    <div class="sec-node node-1" onclick="showSecPanel(event, 'sec-auth')">Authentication</div>
                    <div class="sec-node node-2" onclick="showSecPanel(event, 'sec-authz')">Authorization</div>
                    <div class="sec-node node-3" onclick="showSecPanel(event, 'sec-data')">Data Protection</div>
                    <div class="sec-node node-4" onclick="showSecPanel(event, 'sec-func')">Function Security</div>
                    <div class="sec-node node-5" onclick="showSecPanel(event, 'sec-mon')">Monitoring</div>
                </div>

                <div id="sec-auth" class="sec-panel">
                    <h4>Authentication</h4>
                    <p>Confirms the identity of users and applications before allowing them into the system.</p>
                    <p class="example">Example: A user signs in with a verified email before accessing a serverless application.</p>
                </div>
                <div id="sec-authz" class="sec-panel">
                    <h4>Authorization</h4>
                    <p>Determines which actions a user or function is permitted to perform after they are authenticated.</p>
                    <p class="example">Example: Only a system administrator is permitted to delete user records.</p>
                </div>
                <div id="sec-data" class="sec-panel">
                    <h4>Data Protection</h4>
                    <p>Protects information during storage (at rest) and transmission (in transit) using encryption.</p>
                    <p class="example">Example: Encrypt sensitive customer payment data before saving it to a database.</p>
                </div>
                <div id="sec-func" class="sec-panel">
                    <h4>Function Security</h4>
                    <p>Prevents unsafe requests and vulnerable code execution within the serverless environment.</p>
                    <p class="example">Example: Validate all API input data before running a backend cloud function.</p>
                </div>
                <div id="sec-mon" class="sec-panel">
                    <h4>Monitoring</h4>
                    <p>Detects unusual behavior, application errors, and active security threats in real-time.</p>
                    <p class="example">Example: Send an automatic alert to the developer when repeated failed login requests occur.</p>
                </div>
            </div>

            <p style="text-align: center; color: var(--muted); font-size: 0.95rem; font-style: italic; margin-top: 30px;">
                "Serverless reduces infrastructure management, but secure coding and proper access control remain essential."
            </p>
            
            <script>
                function showSecPanel(event, id) {
                    const slide = document.getElementById('slide-15');
                    if(!slide) return;
                    slide.querySelectorAll('.sec-panel').forEach(p => p.classList.remove('active'));
                    slide.querySelectorAll('.sec-node').forEach(n => n.classList.remove('active'));
                    
                    document.getElementById(id).classList.add('active');
                    event.currentTarget.classList.add('active');
                }
            </script>
        </div>\n\n"""

    new_html = first_half + slide_15 + second_half

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(new_html)
        print("Updated index.html successfully.")

    with open('script.js', 'r', encoding='utf-8') as f:
        script = f.read()
    script = script.replace('const totalSlides = 20;', 'const totalSlides = 21;')
    with open('script.js', 'w', encoding='utf-8') as f:
        f.write(script)
        print("Updated script.js successfully.")

process_file()
