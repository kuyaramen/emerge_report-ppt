import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

new_slide_14 = """        <div class="slide" id="slide-14" style="justify-content: flex-start; padding-top: 20px;">
            <h2 style="text-align: center; border-bottom: none; margin-bottom: 5px; text-transform: uppercase; letter-spacing: 2px;">Cloud Computing vs Serverless</h2>
            <p style="text-align: center; color: var(--muted); max-width: 900px; margin: 0 auto 20px auto; font-size: 1.05rem;">
                <strong style="color: var(--cyan);">Important concept:</strong> Serverless is one model within the broader category of cloud computing.
            </p>

            <style>
                #slide-14 .c-layout {
                    display: flex; gap: 40px; align-items: center; max-width: 1100px; margin: 0 auto; width: 100%; height: 400px;
                }
                #slide-14 .c-left {
                    flex: 1.2; position: relative; height: 100%; display: flex; justify-content: center; align-items: center;
                }
                #slide-14 .c-right {
                    flex: 1; display: flex; flex-direction: column; gap: 20px;
                }
                
                #slide-14 .info-card {
                    padding: 25px; border-radius: 12px; cursor: pointer; transition: all 0.3s ease;
                    background: rgba(15,30,55,0.7); border: 2px solid rgba(255,255,255,0.1); position: relative; overflow: hidden;
                }
                #slide-14 .info-card:hover { background: rgba(15,30,55,0.9); }
                #slide-14 .info-card.selected { border-color: var(--cyan); box-shadow: 0 0 20px rgba(34,211,238,0.2); }
                
                #slide-14 .detail-panel {
                    margin-top: 15px; padding-top: 15px; border-top: 1px solid rgba(255,255,255,0.1); display: none; font-size: 0.95rem; color: #E2E8F0; line-height: 1.5;
                }
                #slide-14 .info-card.selected .detail-panel { display: block; animation: fadeIn 0.5s ease-in-out; }

                /* SVG Styles */
                #slide-14 .cloud-outer { transition: all 0.5s ease; fill: rgba(37,99,235,0.05); stroke: rgba(37,99,235,0.5); }
                #slide-14 .cloud-inner { transition: all 0.5s ease; opacity: 0; transform: scale(0.9); transform-origin: center; }
                
                #slide-14.state-cloud .cloud-outer { fill: rgba(37,99,235,0.15); stroke: rgba(37,99,235,1); filter: drop-shadow(0 0 10px rgba(37,99,235,0.3)); }
                #slide-14.state-cloud .cloud-inner { opacity: 0.5; }
                
                #slide-14.state-serverless .cloud-outer { opacity: 0.5; }
                #slide-14.state-serverless .cloud-inner { opacity: 1; transform: scale(1); filter: drop-shadow(0 0 15px rgba(34,211,238,0.4)); }
                #slide-14.state-serverless .serverless-box { stroke: var(--cyan); stroke-width: 3; fill: rgba(34,211,238,0.1); }
                
                @media (max-width: 900px) {
                    #slide-14 .c-layout { flex-direction: column; height: auto; }
                    #slide-14 .c-left { height: 300px; width: 100%; }
                }
            </style>

            <div class="c-layout">
                <div class="c-left">
                    <svg width="100%" height="100%" viewBox="0 0 500 400" style="overflow: visible;">
                        <defs>
                            <linearGradient id="cloudGrad" x1="0%" y1="0%" x2="100%" y2="100%">
                                <stop offset="0%" stop-color="rgba(37,99,235,0.1)" />
                                <stop offset="100%" stop-color="rgba(15,30,55,0.8)" />
                            </linearGradient>
                        </defs>
                        <!-- Main Cloud (Cloud Computing) -->
                        <g class="cloud-outer" stroke-width="2">
                            <rect x="10" y="30" width="480" height="340" rx="40" fill="url(#cloudGrad)" />
                            <text x="250" y="70" fill="var(--muted)" font-size="20" font-weight="700" text-anchor="middle" letter-spacing="4">CLOUD COMPUTING</text>
                            
                            <!-- Other Models -->
                            <g opacity="0" transform="translate(0, -10)">
                                <animate attributeName="opacity" from="0" to="1" dur="1s" begin="0.5s" fill="freeze" />
                                <rect x="40" y="110" width="130" height="70" rx="10" fill="rgba(255,255,255,0.05)" stroke="rgba(255,255,255,0.2)" stroke-width="1.5" />
                                <text x="105" y="150" fill="#CBD5E1" font-size="12" font-weight="600" text-anchor="middle">VIRTUAL MACHINES</text>

                                <rect x="185" y="110" width="130" height="70" rx="10" fill="rgba(255,255,255,0.05)" stroke="rgba(255,255,255,0.2)" stroke-width="1.5" />
                                <text x="250" y="150" fill="#CBD5E1" font-size="12" font-weight="600" text-anchor="middle">CONTAINERS</text>

                                <rect x="330" y="110" width="130" height="70" rx="10" fill="rgba(255,255,255,0.05)" stroke="rgba(255,255,255,0.2)" stroke-width="1.5" />
                                <text x="395" y="150" fill="#CBD5E1" font-size="12" font-weight="600" text-anchor="middle">MANAGED SERVICES</text>
                            </g>
                        </g>
                        
                        <!-- Serverless Computing Module -->
                        <g class="cloud-inner">
                            <animate attributeName="opacity" from="0" to="1" dur="1s" begin="1s" fill="freeze" />
                            <rect class="serverless-box" x="40" y="210" width="420" height="130" rx="15" fill="rgba(34,211,238,0.05)" stroke="rgba(34,211,238,0.5)" stroke-width="2" stroke-dasharray="6,4" />
                            <text x="250" y="245" fill="var(--cyan)" font-size="18" font-weight="700" text-anchor="middle" letter-spacing="2">SERVERLESS</text>
                            <text x="250" y="265" fill="#94A3B8" font-size="12" text-anchor="middle" font-style="italic">"One model within cloud computing"</text>
                            
                            <!-- Sub-elements -->
                            <rect x="70" y="280" width="160" height="40" rx="6" fill="rgba(15,30,55,0.8)" stroke="rgba(255,255,255,0.15)" stroke-width="1" />
                            <text x="150" y="305" fill="#F8FAFC" font-size="12" font-weight="500" text-anchor="middle">CLOUD FUNCTIONS</text>
                            
                            <rect x="270" y="280" width="160" height="40" rx="6" fill="rgba(15,30,55,0.8)" stroke="rgba(255,255,255,0.15)" stroke-width="1" />
                            <text x="350" y="305" fill="#F8FAFC" font-size="12" font-weight="500" text-anchor="middle">AUTOMATIC SCALING</text>
                        </g>
                    </svg>
                </div>
                
                <div class="c-right">
                    <div class="info-card" id="card-cloud" onclick="selectSlide14State('cloud')">
                        <h3 style="color: var(--blue); margin-top: 0; font-size: 1.2rem; letter-spacing: 1px;">CLOUD COMPUTING</h3>
                        <p style="margin: 0; font-size: 1rem; color: var(--muted);">The delivery of computing services over the internet.</p>
                        <div class="detail-panel">
                            Cloud Computing provides computing services through the internet, including servers, storage, databases, networking, and more.
                        </div>
                    </div>
                    
                    <div class="info-card" id="card-serverless" onclick="selectSlide14State('serverless')">
                        <h3 style="color: var(--cyan); margin-top: 0; font-size: 1.2rem; letter-spacing: 1px;">SERVERLESS COMPUTING</h3>
                        <p style="margin: 0; font-size: 1rem; color: var(--muted);">A specific model where the provider manages the underlying servers.</p>
                        <div class="detail-panel">
                            Serverless is a cloud-computing model where the provider manages the underlying servers and infrastructure.
                        </div>
                    </div>
                </div>
            </div>

            <script>
                function selectSlide14State(state) {
                    const slide = document.getElementById('slide-14');
                    if (!slide) return;
                    const cCloud = document.getElementById('card-cloud');
                    const cServ = document.getElementById('card-serverless');
                    
                    slide.classList.remove('state-cloud', 'state-serverless');
                    cCloud.classList.remove('selected');
                    cServ.classList.remove('selected');
                    
                    slide.classList.add('state-' + state);
                    if(state === 'cloud') cCloud.classList.add('selected');
                    if(state === 'serverless') cServ.classList.add('selected');
                }
            </script>
            
            <div class="quiz-section" style="margin-top: 20px; text-align: center;">
                <button class="btn btn-outline" style="padding: 10px 20px; border-radius: 8px; background: rgba(34,211,238,0.1); color: var(--cyan); border: 1px solid var(--cyan); cursor: pointer;" onclick="document.getElementById('ans14').style.display = 'block'; this.style.display='none';">Show Answer</button>
                <div class="answer-box glass-card" id="ans14" style="display: none; padding: 15px; margin-top: 15px; background: rgba(15,30,55,0.9); border: 1px solid var(--cyan); color: white;">
                    <strong>A:</strong> Yes, it is a specific model within cloud computing.
                </div>
            </div>
        </div>"""

pattern = r'<div class="slide" id="slide-14".*?<!-- SLIDE 15: SERVERLESS COST MODEL -->'
match = re.search(pattern, content, re.DOTALL)

if match:
    new_content = content[:match.start()] + new_slide_14 + "\n\n        <!-- ============================================ -->\n        <!-- SLIDE 15: SERVERLESS COST MODEL -->" + content[match.end():]
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("Patched Slide 14 successfully.")
else:
    print("Could not find Slide 14 section to replace.")
