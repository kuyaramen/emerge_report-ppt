import re

def patch_slide_8():
    with open('index.html', 'r', encoding='utf-8') as f:
        html = f.read()

    # 1. Replace the CSS block for expandable code
    old_css_block = """                /* Expandable Code */
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
                }"""
                
    new_css_block = """                /* Expandable Code */
                #slide-8 .faas2-code-panel {
                    width: 100%; max-width: 1100px; margin: 20px auto 0 auto; background: rgba(15,30,55,0.8);
                    border: 1px solid rgba(255,255,255,0.1); border-radius: 12px; overflow: hidden; z-index: 10;
                }
                #slide-8 .faas2-code-header {
                    padding: 12px 20px; background: rgba(255,255,255,0.05); display: flex; justify-content: space-between; align-items: center; cursor: pointer;
                    width: 100%; border: none; color: white; text-align: left; font-family: inherit;
                }
                #slide-8 .faas2-code-header:focus { outline: 2px solid var(--cyan); }
                #slide-8 .faas2-code-content {
                    padding: 0 20px; max-height: 0; opacity: 0; transition: all 0.4s ease; overflow: hidden;
                }
                #slide-8 .faas2-code-content.open {
                    padding: 20px; max-height: 600px; opacity: 1; overflow-y: auto;
                }
                @keyframes spinSim { 0% { transform: rotate(0deg); } 100% { transform: rotate(360deg); } }
                .faas2-sim-spinner {
                    width: 12px; height: 12px; border: 2px solid rgba(255,255,255,0.3); border-top-color: #22D3EE;
                    border-radius: 50%; animation: spinSim 1s linear infinite; display: inline-block;
                }"""
    html = html.replace(old_css_block, new_css_block)

    # 2. Replace the HTML for the code panel
    old_html_block = """            <div class="faas2-code-panel">
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
            </div>"""
            
    new_html_block = """            <div class="faas2-code-panel">
                <button class="faas2-code-header" id="faas2-code-btn" aria-expanded="false" onclick="toggleFaaS2Code()">
                    <span style="color: white; font-weight: bold; font-size: 0.95rem;">View Simple Function</span>
                    <span id="faas2-code-arrow" style="color: var(--cyan); transition: transform 0.3s; font-size: 0.8rem; margin-left: 10px;">▼</span>
                </button>
                <div class="faas2-code-content" id="faas2-code-content">
                    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px;">
                        <h4 style="color: white; margin: 0; font-size: 1rem;">Simple Cloud Function Example</h4>
                        <span id="faas2-code-status" style="color: var(--muted); font-size: 0.8rem; background: rgba(255,255,255,0.05); padding: 3px 8px; border-radius: 4px; display: flex; align-items: center; gap: 5px;">JavaScript • Example Function</span>
                    </div>
                    
                    <pre style="background: rgba(0,0,0,0.4); padding: 15px; border-radius: 8px; margin: 0 0 15px 0; font-size: 0.85rem; border: 1px solid rgba(255,255,255,0.05); color: #E2E8F0; overflow-x: auto;"><code class="language-javascript"><span style="color: #F59E0B">function</span> <span style="color: #22D3EE">handler</span>(event) {
  <span style="color: #F59E0B">const</span> name = event.name || <span style="color: #3ECF8E">"Student"</span>;

  <span style="color: #F59E0B">return</span> {
    message: <span style="color: #3ECF8E">`Hello, ${name}!`</span>,
    status: <span style="color: #3ECF8E">"success"</span>
  };
}</code></pre>
                    
                    <p style="color: var(--muted); font-size: 0.85rem; margin: 0 0 15px 0;">This function receives an event, processes the data, and returns a result.</p>
                    
                    <div style="background: rgba(255,255,255,0.03); padding: 15px; border-radius: 8px; border: 1px solid rgba(255,255,255,0.05); display: flex; flex-direction: column; gap: 10px;">
                        <label for="faas2-sim-input" style="color: var(--cyan); font-size: 0.85rem; font-weight: bold;">Enter your name</label>
                        <div style="display: flex; gap: 10px; flex-wrap: wrap;">
                            <input type="text" id="faas2-sim-input" placeholder="Example: Louie" style="flex: 1; min-width: 150px; padding: 10px 15px; border-radius: 6px; border: 1px solid rgba(34,211,238,0.3); background: rgba(15,30,55,0.9); color: white; outline: none; font-size: 0.95rem;">
                            <button onclick="runSimulatedCode()" style="padding: 10px 20px; background: #22D3EE; color: #0B1F35; font-weight: bold; border: none; border-radius: 6px; cursor: pointer; min-width: 120px; font-size: 0.95rem; display: flex; align-items: center; justify-content: center; gap: 5px; transition: all 0.2s;">
                                Run Code
                            </button>
                        </div>
                    </div>
                    
                    <div id="faas2-sim-output-panel" style="display: none; margin-top: 15px;">
                        <div style="color: #3ECF8E; font-size: 0.85rem; font-weight: bold; margin-bottom: 8px; display: flex; align-items: center; gap: 5px;">
                            <span>✓</span> Function executed successfully.
                        </div>
                        <pre style="background: rgba(15,30,55,0.8); padding: 15px; border-radius: 8px; margin: 0; font-size: 0.85rem; border: 1px solid rgba(62,207,142,0.3); color: #3ECF8E; overflow-x: auto;" id="faas2-sim-output-code"></pre>
                    </div>
                </div>
            </div>"""
    html = html.replace(old_html_block, new_html_block)

    # 3. Replace JS toggleFaaS2Code()
    old_js_toggle = """                function toggleFaaS2Code() {
                    var content = document.getElementById('faas2-code-content');
                    var arrow = document.getElementById('faas2-code-arrow');
                    if (content.classList.contains('open')) {
                        content.classList.remove('open');
                        arrow.style.transform = 'rotate(0deg)';
                    } else {
                        content.classList.add('open');
                        arrow.style.transform = 'rotate(180deg)';
                    }
                }"""
                
    new_js_toggle = """                function toggleFaaS2Code() {
                    var content = document.getElementById('faas2-code-content');
                    var arrow = document.getElementById('faas2-code-arrow');
                    var btn = document.getElementById('faas2-code-btn');
                    if (content.classList.contains('open')) {
                        content.classList.remove('open');
                        arrow.textContent = '▼';
                        arrow.style.transform = 'rotate(0deg)';
                        btn.setAttribute('aria-expanded', 'false');
                    } else {
                        content.classList.add('open');
                        arrow.textContent = '▲';
                        arrow.style.transform = 'rotate(0deg)';
                        btn.setAttribute('aria-expanded', 'true');
                    }
                }"""
    html = html.replace(old_js_toggle, new_js_toggle)

    # 4. Inject runSimulatedCode() into the script block
    sim_js = """
                function runSimulatedCode() {
                    var btn = document.getElementById('faas2-demo-btn');
                    btn.disabled = true;

                    // 1. Change status
                    const statusEl = document.getElementById('faas2-code-status');
                    statusEl.innerHTML = '<span class="faas2-sim-spinner"></span> Running...';
                    statusEl.style.color = '#22D3EE';
                    
                    // Hide output if previously open
                    document.getElementById('faas2-sim-output-panel').style.display = 'none';

                    // Clear existing demo timeline states but don't reset inputs
                    document.querySelectorAll('.faas2-card').forEach(n => n.classList.remove('selected'));
                    document.getElementById('faas2-svg').innerHTML = '';
                    document.getElementById('faas2-packet').style.opacity = '0';
                    document.getElementById('faas2-result-msg').style.opacity = '0';
                    
                    for(let i=1; i<=4; i++) {
                        let st = document.getElementById('faas2-step-' + i);
                        st.className = 'faas2-step';
                        st.querySelector('.faas2-step-dot').innerHTML = i;
                    }

                    // 2. Activate core
                    var core = document.getElementById('faas2-core');
                    core.classList.add('active');
                    
                    var coreStatus = document.getElementById('faas2-core-status');
                    coreStatus.textContent = 'RUNNING';
                    coreStatus.style.color = '#A855F7';
                    coreStatus.style.borderColor = 'rgba(168,85,247,0.5)';

                    // 3. Timeline Simulation
                    setFaaS2Step(1, "Event detected: User Input");
                    
                    setTimeout(() => {
                        setFaaS2Step(2, "Function triggered by Simulator");
                    }, 400);

                    setTimeout(() => {
                        setFaaS2Step(3, "Executing user code...");
                    }, 800);

                    setTimeout(() => {
                        setFaaS2Step(4, "Result returned");
                        
                        // Core status back
                        core.classList.remove('active');
                        coreStatus.textContent = 'COMPLETE';
                        coreStatus.style.color = '#3ECF8E';
                        coreStatus.style.borderColor = 'rgba(62,207,142,0.5)';
                        
                        // Output
                        let nameVal = document.getElementById('faas2-sim-input').value.trim();
                        if(!nameVal) nameVal = "Student";
                        
                        const outputObj = {
                            message: `Hello, ${nameVal}!`,
                            status: "success"
                        };
                        
                        document.getElementById('faas2-sim-output-code').textContent = JSON.stringify(outputObj, null, 2);
                        document.getElementById('faas2-sim-output-panel').style.display = 'block';
                        
                        statusEl.innerHTML = '✓ Complete';
                        statusEl.style.color = '#3ECF8E';
                        
                        btn.disabled = false;
                    }, 1400);
                }
"""
    html = html.replace(new_js_toggle, new_js_toggle + sim_js)

    # 5. Update resetFaaS2()
    old_reset = """                function resetFaaS2() {
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
                }"""
                
    new_reset = """                function resetFaaS2() {
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

                    // Reset code simulator
                    var simInput = document.getElementById('faas2-sim-input');
                    if (simInput) simInput.value = '';
                    var simOutputPanel = document.getElementById('faas2-sim-output-panel');
                    if (simOutputPanel) simOutputPanel.style.display = 'none';
                    var simOutputCode = document.getElementById('faas2-sim-output-code');
                    if (simOutputCode) simOutputCode.textContent = '';
                    var codeStatus = document.getElementById('faas2-code-status');
                    if (codeStatus) {
                        codeStatus.innerHTML = 'JavaScript • Example Function';
                        codeStatus.style.color = 'var(--muted)';
                    }
                }"""
    html = html.replace(old_reset, new_reset)

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("Slide 8 simulation panel successfully injected.")

patch_slide_8()
