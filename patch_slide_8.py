import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

replacement = """        <div class="slide" id="slide-8" style="justify-content: flex-start; padding-top: 15px; position: relative;">
            <h2 style="text-align: center; border-bottom: none; margin-bottom: 5px; text-transform: uppercase; letter-spacing: 2px;">Function as a Service — FaaS</h2>
            <p style="text-align: center; color: var(--muted); max-width: 900px; margin: 0 auto 10px auto; font-size: 0.95rem;">
                FaaS allows developers to run small pieces of code without managing servers. The cloud provider starts and scales the function when an event occurs.
            </p>

            <style>
                #slide-8 .faas2-main {
                    display: flex; flex-direction: row; align-items: stretch; justify-content: space-between;
                    width: 100%; max-width: 1100px; margin: 15px auto 0 auto; flex: 1; gap: 20px; position: relative;
                }
                
                /* SVG and Packets for Data Lines */
                #slide-8 .faas2-svg {
                    position: absolute; top: 0; left: 0; width: 100%; height: 100%; z-index: 5; pointer-events: none; overflow: visible;
                }
                #slide-8 .faas2-packet {
                    position: absolute; top: 0; left: 0; width: 12px; height: 12px; background: #22D3EE; border-radius: 50%; box-shadow: 0 0 15px #22D3EE;
                    z-index: 25; opacity: 0; transition: transform 0.6s ease-in-out, opacity 0.2s; pointer-events: none;
                }
                #slide-8 .faas2-packet.returning {
                    background: #A855F7; box-shadow: 0 0 15px #A855F7;
                }

                /* Left: Dock */
                #slide-8 .faas2-left {
                    display: flex; flex-direction: column; justify-content: center; gap: 12px; width: 280px; z-index: 10;
                }
                #slide-8 .faas2-card {
                    background: rgba(15, 30, 55, 0.9); border: 1px solid rgba(255,255,255,0.15); border-radius: 12px;
                    padding: 12px 15px; display: flex; align-items: center; gap: 15px; cursor: pointer;
                    transition: all 0.3s cubic-bezier(0.2, 0.8, 0.2, 1);
                }
                #slide-8 .faas2-card:hover {
                    border-color: rgba(34, 211, 238, 0.4); background: rgba(34, 211, 238, 0.05); transform: translateX(4px);
                }
                #slide-8 .faas2-card.selected {
                    border-color: #22D3EE; background: rgba(15, 30, 55, 1); box-shadow: 0 0 20px rgba(34, 211, 238, 0.3);
                }
                #slide-8 .faas2-card-icon {
                    font-size: 1.5rem; width: 44px; height: 44px; display: flex; align-items: center; justify-content: center;
                    background: rgba(255,255,255,0.05); border-radius: 8px; flex-shrink: 0;
                }
                #slide-8 .faas2-card-texts {
                    display: flex; flex-direction: column; text-align: left;
                }
                #slide-8 .faas2-card-title {
                    color: white; font-weight: bold; font-size: 0.95rem;
                }
                #slide-8 .faas2-card-sub {
                    color: var(--muted); font-size: 0.75rem; text-transform: uppercase; letter-spacing: 0.5px; margin-top: 2px;
                }

                /* Center: Core */
                #slide-8 .faas2-center {
                    flex: 1; position: relative; display: flex; flex-direction: column; align-items: center; justify-content: center;
                    min-width: 250px; z-index: 10;
                }
                #slide-8 .faas2-core {
                    width: 150px; height: 150px; border-radius: 50%; position: relative;
                    background: radial-gradient(circle, rgba(34,211,238,0.1) 0%, rgba(15,30,55,0.95) 70%);
                    border: 2px solid rgba(34,211,238,0.5); display: flex; flex-direction: column; align-items: center; justify-content: center;
                    z-index: 20; box-shadow: 0 0 30px rgba(34,211,238,0.2); transition: all 0.4s ease;
                }
                #slide-8 .faas2-core.active {
                    border-color: #A855F7; box-shadow: 0 0 50px rgba(168,85,247,0.5);
                    background: radial-gradient(circle, rgba(168,85,247,0.2) 0%, rgba(15,30,55,0.95) 70%);
                }
                #slide-8 .faas2-core-icon { font-size: 2.5rem; }
                #slide-8 .faas2-core-title { color: white; font-weight: bold; font-size: 0.7rem; letter-spacing: 1.5px; margin-top: 5px; text-align: center; }
                #slide-8 .faas2-core-status {
                    position: absolute; bottom: -15px; background: rgba(15,30,55,1); border: 1px solid rgba(34,211,238,0.5);
                    color: #22D3EE; padding: 4px 14px; border-radius: 20px; font-size: 0.75rem; font-weight: bold; text-transform: uppercase; letter-spacing: 1px;
                }
                #slide-8 .faas2-result-msg {
                    position: absolute; top: -30px; color: #3ECF8E; font-weight: bold; font-size: 0.9rem; opacity: 0; transition: opacity 0.3s;
                    text-shadow: 0 2px 10px rgba(0,0,0,0.8); text-align: center; width: 100%; pointer-events: none;
                }

                /* Right: Timeline */
                #slide-8 .faas2-right {
                    width: 280px; display: flex; flex-direction: column; justify-content: center; z-index: 10;
                }
                #slide-8 .faas2-timeline {
                    background: rgba(0,0,0,0.2); border: 1px solid rgba(255,255,255,0.1); border-radius: 12px; padding: 20px;
                }
                #slide-8 .faas2-timeline-header {
                    color: white; font-weight: bold; font-size: 0.85rem; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 20px; text-align: left;
                }
                #slide-8 .faas2-step {
                    display: flex; align-items: flex-start; gap: 15px; position: relative; padding-bottom: 22px;
                }
                #slide-8 .faas2-step:last-child { padding-bottom: 0; }
                #slide-8 .faas2-step::before {
                    content: ''; position: absolute; left: 11px; top: 24px; bottom: 0; width: 2px; background: rgba(255,255,255,0.1);
                }
                #slide-8 .faas2-step:last-child::before { display: none; }
                #slide-8 .faas2-step.active::before { background: rgba(34,211,238,0.5); }
                #slide-8 .faas2-step-dot {
                    width: 24px; height: 24px; border-radius: 50%; border: 2px solid rgba(255,255,255,0.2); background: rgba(15,30,55,1);
                    color: var(--muted); display: flex; align-items: center; justify-content: center; font-size: 0.75rem; font-weight: bold; z-index: 2; transition: all 0.3s; flex-shrink: 0;
                }
                #slide-8 .faas2-step.done .faas2-step-dot {
                    background: #3ECF8E; border-color: #3ECF8E; color: black;
                }
                #slide-8 .faas2-step.active .faas2-step-dot {
                    background: #22D3EE; border-color: #22D3EE; color: black; box-shadow: 0 0 10px #22D3EE;
                }
                #slide-8 .faas2-step-text {
                    color: var(--muted); font-size: 0.9rem; padding-top: 2px; transition: color 0.3s;
                }
                #slide-8 .faas2-step.active .faas2-step-text, #slide-8 .faas2-step.done .faas2-step-text { color: white; }

                /* Controls */
                #slide-8 .faas2-bottom-controls {
                    display: flex; gap: 15px; margin-top: 20px; justify-content: center; width: 100%; z-index: 10;
                }
                #slide-8 .faas2-btn {
                    padding: 12px 30px; background: rgba(34,211,238,0.1); border: 2px solid rgba(34,211,238,0.5);
                    color: #22D3EE; font-size: 0.9rem; font-weight: bold; border-radius: 8px; cursor: pointer; transition: all 0.2s;
                    text-transform: uppercase; letter-spacing: 1px; min-width: 200px;
                }
                #slide-8 .faas2-btn:hover {
                    background: rgba(34,211,238,0.2); box-shadow: 0 0 15px rgba(34,211,238,0.3); transform: translateY(-2px);
                }
                #slide-8 .faas2-btn.reset {
                    background: rgba(255,255,255,0.05); border-color: rgba(255,255,255,0.2); color: white; min-width: 150px;
                }
                #slide-8 .faas2-btn.reset:hover {
                    background: rgba(255,255,255,0.1); box-shadow: 0 0 15px rgba(255,255,255,0.15);
                }
                #slide-8 .faas2-btn:disabled { opacity: 0.5; pointer-events: none; filter: grayscale(1); }

                /* Expandable Code */
                #slide-8 .faas2-code-panel {
                    width: 100%; max-width: 1100px; margin: 20px auto 0 auto; background: rgba(15,30,55,0.8);
                    border: 1px solid rgba(255,255,255,0.1); border-radius: 12px; overflow: hidden; z-index: 10;
                }
                #slide-8 .faas2-code-header {
                    padding: 12px 20px; background: rgba(255,255,255,0.05); display: flex; justify-content: space-between; align-items: center; cursor: pointer;
                }
                #slide-8 .faas2-code-content {
                    padding: 0 20px; max-height: 0; opacity: 0; transition: all 0.4s ease; overflow: hidden;
                }
                #slide-8 .faas2-code-content.open {
                    padding: 20px; max-height: 250px; opacity: 1;
                }

                @media (max-width: 900px) {
                    #slide-8 .faas2-main { flex-direction: column; gap: 30px; align-items: center; }
                    #slide-8 .faas2-left { width: 100%; max-width: 400px; }
                    #slide-8 .faas2-right { width: 100%; max-width: 400px; }
                    #slide-8 .faas2-svg, #slide-8 .faas2-packet { display: none; }
                    #slide-8 .faas2-center { min-width: unset; margin: 20px 0; }
                }
                @media (prefers-reduced-motion: reduce) {
                    #slide-8 .faas2-packet, #slide-8 .faas2-core, #slide-8 .faas2-card { transition: none !important; }
                }
            </style>

            <div class="faas2-main" id="faas2-main">
                <svg class="faas2-svg" id="faas2-svg"></svg>
                <div class="faas2-packet" id="faas2-packet"></div>

                <div class="faas2-left" id="faas2-dock">
                    <!-- Event triggers rendered via JS -->
                </div>

                <div class="faas2-center">
                    <div class="faas2-result-msg" id="faas2-result-msg"></div>
                    <div class="faas2-core" id="faas2-core">
                        <span class="faas2-core-icon">⚡</span>
                        <span class="faas2-core-title">CLOUD<br>FUNCTION</span>
                        <span class="faas2-core-status" id="faas2-core-status">IDLE</span>
                    </div>
                </div>

                <div class="faas2-right">
                    <div class="faas2-timeline">
                        <div class="faas2-timeline-header">Function Execution</div>
                        <div class="faas2-step" id="faas2-step-1">
                            <div class="faas2-step-dot">1</div>
                            <div class="faas2-step-text" id="faas2-text-1">Waiting for event</div>
                        </div>
                        <div class="faas2-step" id="faas2-step-2">
                            <div class="faas2-step-dot">2</div>
                            <div class="faas2-step-text" id="faas2-text-2">Function triggered</div>
                        </div>
                        <div class="faas2-step" id="faas2-step-3">
                            <div class="faas2-step-dot">3</div>
                            <div class="faas2-step-text" id="faas2-text-3">Code is running</div>
                        </div>
                        <div class="faas2-step" id="faas2-step-4">
                            <div class="faas2-step-dot">4</div>
                            <div class="faas2-step-text" id="faas2-text-4">Result returned</div>
                        </div>
                    </div>
                </div>
            </div>

            <div class="faas2-bottom-controls">
                <button class="faas2-btn" id="faas2-demo-btn" onclick="runFaaS2Demo()">Run Function Demo</button>
                <button class="faas2-btn reset" id="faas2-reset-btn" onclick="resetFaaS2()">Reset Demo</button>
            </div>

            <div class="faas2-code-panel">
                <div class="faas2-code-header" onclick="toggleFaaS2Code()">
                    <span style="color: white; font-weight: bold; font-size: 0.95rem;">View Simple Function</span>
                    <span id="faas2-code-arrow" style="color: var(--cyan); transition: transform 0.3s;">▼</span>
                </div>
                <div class="faas2-code-content" id="faas2-code-content">
                    <pre style="background: rgba(0,0,0,0.4); padding: 15px; border-radius: 8px; margin: 0 0 10px 0; font-size: 0.85rem; border: 1px solid rgba(255,255,255,0.05); color: #E2E8F0;"><code class="language-javascript"><span style="color: #F59E0B">function</span> <span style="color: #22D3EE">handler</span>(event) {
  <span style="color: #F59E0B">return</span> {
    message: <span style="color: #3ECF8E">"Hello from the cloud function!"</span>
  };
}</code></pre>
                    <p style="color: var(--muted); font-size: 0.85rem; margin: 0;">The function runs <strong>when an event triggers it</strong>.</p>
                </div>
            </div>

            <script>
                const faas2Events = [
                    { id: 'btn', title: 'Button Click', sub: 'User action', icon: '🖱️', msg: 'User action triggered the function.' },
                    { id: 'api', title: 'API Request', sub: 'Web request', icon: '🌐', msg: 'Incoming API request triggered the function.' },
                    { id: 'file', title: 'File Upload', sub: 'New file', icon: '📁', msg: 'New file detected and processed.' },
                    { id: 'sensor', title: 'Sensor Data', sub: 'Sensor reading', icon: '📡', msg: 'Sensor reading sent to the cloud function.' },
                    { id: 'cron', title: 'Scheduled Task', sub: 'Scheduled event', icon: '⏱️', msg: 'Scheduled event started the function.' }
                ];

                const faas2Dock = document.getElementById('faas2-dock');
                const faas2Svg = document.getElementById('faas2-svg');

                faas2Events.forEach((ev, i) => {
                    let card = document.createElement('div');
                    card.className = 'faas2-card';
                    card.id = 'faas2-card-' + i;
                    card.onclick = () => triggerFaaS2(i);
                    card.innerHTML = `
                        <div class="faas2-card-icon">${ev.icon}</div>
                        <div class="faas2-card-texts">
                            <div class="faas2-card-title">${ev.title}</div>
                            <div class="faas2-card-sub">${ev.sub}</div>
                        </div>
                    `;
                    faas2Dock.appendChild(card);
                });

                function toggleFaaS2Code() {
                    var content = document.getElementById('faas2-code-content');
                    var arrow = document.getElementById('faas2-code-arrow');
                    if (content.classList.contains('open')) {
                        content.classList.remove('open');
                        arrow.style.transform = 'rotate(0deg)';
                    } else {
                        content.classList.add('open');
                        arrow.style.transform = 'rotate(180deg)';
                    }
                }

                function resetFaaS2() {
                    document.querySelectorAll('.faas2-card').forEach(n => n.classList.remove('selected'));
                    var core = document.getElementById('faas2-core');
                    core.classList.remove('active');
                    
                    var statusEl = document.getElementById('faas2-core-status');
                    statusEl.textContent = 'IDLE';
                    statusEl.style.color = '#22D3EE';
                    statusEl.style.borderColor = 'rgba(34,211,238,0.5)';
                    
                    document.getElementById('faas2-packet').style.opacity = '0';
                    document.getElementById('faas2-result-msg').style.opacity = '0';
                    document.getElementById('faas2-svg').innerHTML = '';
                    document.getElementById('faas2-demo-btn').disabled = false;
                    
                    for(let i=1; i<=4; i++) {
                        let st = document.getElementById('faas2-step-' + i);
                        st.className = 'faas2-step';
                        st.querySelector('.faas2-step-dot').innerHTML = i;
                    }
                    document.getElementById('faas2-text-1').textContent = 'Waiting for event...';
                }

                function setFaaS2Step(step, text) {
                    for(let i=1; i<=4; i++) {
                        let st = document.getElementById('faas2-step-' + i);
                        if (i < step) {
                            st.className = 'faas2-step done';
                            st.querySelector('.faas2-step-dot').innerHTML = '✓';
                        } else if (i === step) {
                            st.className = 'faas2-step active';
                        } else {
                            st.className = 'faas2-step';
                            st.querySelector('.faas2-step-dot').innerHTML = i;
                        }
                    }
                    if(text) document.getElementById('faas2-text-' + step).textContent = text;
                }

                function triggerFaaS2(index) {
                    var btn = document.getElementById('faas2-demo-btn');
                    if(btn.disabled) return;
                    btn.disabled = true;

                    resetFaaS2();

                    var card = document.getElementById('faas2-card-' + index);
                    card.classList.add('selected');
                    
                    setFaaS2Step(1, "Event detected: " + faas2Events[index].title);
                    
                    if (window.innerWidth > 900) {
                        var main = document.getElementById('faas2-main');
                        var core = document.getElementById('faas2-core');
                        
                        let mRect = main.getBoundingClientRect();
                        let cRect = card.getBoundingClientRect();
                        let coreRect = core.getBoundingClientRect();
                        
                        let startX = cRect.right - mRect.left;
                        let startY = cRect.top - mRect.top + (cRect.height / 2);
                        
                        let endX = coreRect.left - mRect.left;
                        let endY = coreRect.top - mRect.top + (coreRect.height / 2);
                        
                        faas2Svg.innerHTML = `<line x1="${startX}" y1="${startY}" x2="${endX}" y2="${endY}" stroke="rgba(255,255,255,0.15)" stroke-width="2" stroke-dasharray="4 4" />`;
                        
                        var packet = document.getElementById('faas2-packet');
                        packet.className = 'faas2-packet';
                        packet.style.transition = 'none';
                        packet.style.transform = `translate(${startX}px, ${startY - 6}px)`;
                        packet.style.opacity = '1';
                        
                        void packet.offsetWidth;
                        
                        setTimeout(() => {
                            packet.style.transition = 'transform 0.6s ease-in-out, opacity 0.2s';
                            packet.style.transform = `translate(${endX - 12}px, ${endY - 6}px)`;
                            
                            setTimeout(() => {
                                document.getElementById('faas2-core-status').textContent = 'TRIGGERED';
                                document.getElementById('faas2-core-status').style.color = '#F59E0B';
                                document.getElementById('faas2-core-status').style.borderColor = '#F59E0B';
                                setFaaS2Step(2, "Function triggered");
                                
                                setTimeout(() => {
                                    core.classList.add('active');
                                    packet.style.opacity = '0';
                                    document.getElementById('faas2-core-status').textContent = 'RUNNING';
                                    document.getElementById('faas2-core-status').style.color = '#22D3EE';
                                    document.getElementById('faas2-core-status').style.borderColor = '#22D3EE';
                                    setFaaS2Step(3, "Code is running");
                                    
                                    setTimeout(() => {
                                        core.classList.remove('active');
                                        document.getElementById('faas2-core-status').textContent = 'COMPLETE';
                                        document.getElementById('faas2-core-status').style.color = '#3ECF8E';
                                        document.getElementById('faas2-core-status').style.borderColor = '#3ECF8E';
                                        
                                        packet.className = 'faas2-packet returning';
                                        packet.style.transition = 'none';
                                        packet.style.transform = `translate(${endX - 12}px, ${endY - 6}px)`;
                                        packet.style.opacity = '1';
                                        
                                        void packet.offsetWidth;
                                        
                                        setTimeout(() => {
                                            packet.style.transition = 'transform 0.6s ease-in-out, opacity 0.2s';
                                            packet.style.transform = `translate(${startX}px, ${startY - 6}px)`;
                                            setFaaS2Step(4, "Result returned");
                                            
                                            setTimeout(() => {
                                                packet.style.opacity = '0';
                                                var msg = document.getElementById('faas2-result-msg');
                                                msg.textContent = faas2Events[index].msg;
                                                msg.style.opacity = '1';
                                                
                                                document.getElementById('faas2-step-4').classList.replace('active', 'done');
                                                document.querySelector('#faas2-step-4 .faas2-step-dot').innerHTML = '✓';
                                                btn.disabled = false;
                                            }, 600);
                                        }, 50);
                                    }, 1000);
                                }, 400);
                            }, 600);
                        }, 50);
                    } else {
                        // Mobile fallback (no packet animation)
                        setTimeout(() => {
                            document.getElementById('faas2-core-status').textContent = 'RUNNING';
                            document.getElementById('faas2-core-status').style.color = '#22D3EE';
                            document.getElementById('faas2-core-status').style.borderColor = '#22D3EE';
                            setFaaS2Step(2, "Function triggered");
                            setTimeout(() => {
                                setFaaS2Step(3, "Code is running");
                                setTimeout(() => {
                                    document.getElementById('faas2-core-status').textContent = 'COMPLETE';
                                    document.getElementById('faas2-core-status').style.color = '#3ECF8E';
                                    document.getElementById('faas2-core-status').style.borderColor = '#3ECF8E';
                                    setFaaS2Step(4, "Result returned");
                                    var msg = document.getElementById('faas2-result-msg');
                                    msg.textContent = faas2Events[index].msg;
                                    msg.style.opacity = '1';
                                    document.getElementById('faas2-step-4').classList.replace('active', 'done');
                                    document.querySelector('#faas2-step-4 .faas2-step-dot').innerHTML = '✓';
                                    btn.disabled = false;
                                }, 800);
                            }, 800);
                        }, 400);
                    }
                }

                function runFaaS2Demo() {
                    var rand = Math.floor(Math.random() * faas2Events.length);
                    triggerFaaS2(rand);
                }
            </script>
        </div>"""

pattern = re.compile(r'<div class="slide" id="slide-8".*?</script>\s*</div>', re.DOTALL)
new_content = pattern.sub(replacement, content)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_content)
