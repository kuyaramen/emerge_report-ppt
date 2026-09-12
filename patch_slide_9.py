import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

replacement = """        <div class="slide" id="slide-9" style="justify-content: flex-start; padding-top: 15px; position: relative;">
            <h2 style="text-align: center; border-bottom: none; margin-bottom: 5px; text-transform: uppercase; letter-spacing: 2px;">Backend as a Service — BaaS</h2>
            <p style="text-align: center; color: var(--muted); max-width: 900px; margin: 0 auto 10px auto; font-size: 0.95rem;">
                BaaS provides ready-made backend services such as authentication, databases, storage, and notifications, allowing developers to build applications faster without creating the entire backend from scratch.
            </p>
            <style>
                #slide-9 .baas-main {
                    display: flex; flex-direction: row; align-items: center; justify-content: space-between;
                    width: 100%; max-width: 1100px; margin: 20px auto 0 auto; flex: 1; gap: 30px; position: relative; z-index: 10;
                }
                
                /* Layout */
                #slide-9 .baas-left { width: 260px; display: flex; flex-direction: column; align-items: center; z-index: 10; }
                #slide-9 .baas-center { flex: 1; min-width: 200px; display: flex; flex-direction: column; align-items: center; justify-content: center; position: relative; z-index: 10; height: 350px;}
                #slide-9 .baas-right { width: 280px; display: flex; flex-direction: column; gap: 10px; z-index: 10; }

                /* App Preview */
                #slide-9 .baas-app-card {
                    width: 100%; height: 260px; background: rgba(15,30,55,0.9); border: 1px solid rgba(255,255,255,0.15);
                    border-radius: 16px; padding: 15px; display: flex; flex-direction: column; cursor: pointer; transition: all 0.3s;
                    box-shadow: 0 10px 30px rgba(0,0,0,0.5);
                }
                #slide-9 .baas-app-card:hover { border-color: rgba(34,211,238,0.4); transform: translateY(-3px); }
                #slide-9 .baas-app-card.selected { border-color: #22D3EE; box-shadow: 0 0 25px rgba(34,211,238,0.3); background: rgba(15,30,55,1); }
                #slide-9 .app-title { font-size: 0.8rem; font-weight: bold; color: white; text-align: center; text-transform: uppercase; margin-bottom: 15px; letter-spacing: 1px;}
                #slide-9 .app-header { height: 40px; background: rgba(255,255,255,0.05); border-radius: 8px; margin-bottom: 10px; display:flex; align-items:center; padding: 0 10px; gap: 8px; }
                #slide-9 .app-avatar { width: 20px; height: 20px; border-radius: 50%; background: #22D3EE; }
                #slide-9 .app-line { height: 6px; background: rgba(255,255,255,0.1); border-radius: 3px; flex:1; }
                #slide-9 .app-body { flex: 1; background: rgba(0,0,0,0.2); border-radius: 8px; border: 1px solid rgba(255,255,255,0.05); display: flex; flex-direction: column; gap: 10px; padding: 10px;}
                #slide-9 .app-box { height: 30px; background: rgba(255,255,255,0.05); border-radius: 6px; }

                /* BaaS Platform Core */
                #slide-9 .baas-core {
                    width: 140px; height: 140px; border-radius: 20px; position: relative;
                    background: rgba(37,99,235,0.1); border: 2px solid rgba(37,99,235,0.5);
                    display: flex; flex-direction: column; align-items: center; justify-content: center;
                    box-shadow: 0 0 30px rgba(37,99,235,0.2); transition: all 0.4s ease;
                }
                #slide-9 .baas-core.active {
                    border-color: #3B82F6; box-shadow: 0 0 50px rgba(37,99,235,0.5);
                    background: rgba(37,99,235,0.2);
                }
                #slide-9 .baas-core-icon { font-size: 2.5rem; }
                #slide-9 .baas-core-title { color: white; font-weight: bold; font-size: 0.8rem; letter-spacing: 1px; margin-top: 5px; text-align: center; }
                #slide-9 .baas-status-msg {
                    position: absolute; top: -40px; color: #3ECF8E; font-weight: bold; font-size: 0.85rem; opacity: 0; transition: opacity 0.3s;
                    text-shadow: 0 2px 10px rgba(0,0,0,0.8); text-align: center; width: 100%; pointer-events: none;
                }

                /* Services */
                #slide-9 .baas-srv {
                    background: rgba(15, 30, 55, 0.8); border: 1px solid rgba(255,255,255,0.1); border-radius: 10px;
                    padding: 10px 15px; display: flex; align-items: center; gap: 12px; cursor: pointer; transition: all 0.3s;
                }
                #slide-9 .baas-srv:hover { border-color: rgba(168,85,247,0.4); background: rgba(168,85,247,0.05); transform: translateX(-4px); }
                #slide-9 .baas-srv.selected { border-color: #A855F7; box-shadow: 0 0 20px rgba(168,85,247,0.3); background: rgba(15,30,55,1); }
                #slide-9 .baas-srv-icon { font-size: 1.2rem; background: rgba(255,255,255,0.05); width: 34px; height: 34px; border-radius: 8px; display:flex; align-items:center; justify-content:center; }
                #slide-9 .baas-srv-text { display: flex; flex-direction: column; }
                #slide-9 .baas-srv-title { color: white; font-weight: bold; font-size: 0.85rem; }
                #slide-9 .baas-srv-desc { color: var(--muted); font-size: 0.7rem; }

                /* SVG & Packet */
                #slide-9 .baas-svg-wrap {
                    position: absolute; top: 0; left: 0; width: 100%; height: 100%; z-index: 5; pointer-events: none; overflow: visible;
                }
                #slide-9 .baas-packet {
                    position: absolute; top: 0; left: 0; width: 10px; height: 10px; background: #22D3EE; border-radius: 50%; box-shadow: 0 0 12px #22D3EE;
                    z-index: 25; opacity: 0; transition: transform 0.6s ease-in-out, opacity 0.2s; pointer-events: none;
                }

                /* Quick Actions */
                #slide-9 .baas-actions { display: flex; flex-wrap: wrap; gap: 8px; justify-content: center; margin-top: 15px; }
                #slide-9 .baas-action-chip {
                    background: rgba(255,255,255,0.05); border: 1px solid rgba(255,255,255,0.1); padding: 6px 12px; border-radius: 20px;
                    color: white; font-size: 0.75rem; cursor: pointer; transition: all 0.2s;
                }
                #slide-9 .baas-action-chip:hover { background: rgba(34,211,238,0.1); border-color: rgba(34,211,238,0.4); color: #22D3EE; }

                /* Bottom Controls */
                #slide-9 .baas-controls { display: flex; gap: 15px; justify-content: center; margin-top: 20px; z-index: 10; position:relative; }
                #slide-9 .baas-btn {
                    padding: 12px 24px; background: rgba(37,99,235,0.1); border: 2px solid rgba(37,99,235,0.5);
                    color: #3B82F6; font-size: 0.9rem; font-weight: bold; border-radius: 8px; cursor: pointer; transition: all 0.2s; text-transform: uppercase; letter-spacing: 1px; min-width: 220px;
                }
                #slide-9 .baas-btn:hover { background: rgba(37,99,235,0.2); box-shadow: 0 0 15px rgba(37,99,235,0.3); transform: translateY(-2px); }
                #slide-9 .baas-btn.reset { background: rgba(255,255,255,0.05); border-color: rgba(255,255,255,0.2); color: white; min-width: 150px; }
                #slide-9 .baas-btn.reset:hover { background: rgba(255,255,255,0.1); box-shadow: 0 0 15px rgba(255,255,255,0.15); }
                #slide-9 .baas-btn:disabled { opacity: 0.5; pointer-events: none; filter: grayscale(1); }

                /* Detail Panel */
                #slide-9 .baas-detail {
                    position: absolute; bottom: 20px; left: 50%; transform: translateX(-50%); width: 90%; max-width: 600px;
                    background: rgba(15,30,55,0.95); border: 1px solid #A855F7; border-radius: 12px; padding: 20px; z-index: 30;
                    box-shadow: 0 20px 40px rgba(0,0,0,0.8); display: none; opacity: 0; transition: opacity 0.3s;
                }
                #slide-9 .baas-detail.show { display: block; opacity: 1; }
                #slide-9 .baas-detail-close { position: absolute; top: 15px; right: 15px; color: var(--muted); cursor: pointer; font-size: 0.8rem; text-transform: uppercase; letter-spacing: 1px; }
                #slide-9 .baas-detail-close:hover { color: white; }
                #slide-9 .baas-detail-title { color: white; font-size: 1.1rem; font-weight: bold; margin-bottom: 10px; display: flex; align-items: center; gap: 10px; }
                #slide-9 .baas-detail-text { color: var(--muted); font-size: 0.9rem; line-height: 1.5; margin-bottom: 8px;}
                #slide-9 .baas-detail-text strong { color: #A855F7; }

                @media (max-width: 900px) {
                    #slide-9 .baas-main { flex-direction: column; gap: 20px; }
                    #slide-9 .baas-left, #slide-9 .baas-right { width: 100%; max-width: 500px; }
                    #slide-9 .baas-center { height: 180px; }
                    #slide-9 .baas-svg-wrap, #slide-9 .baas-packet { display: none; }
                }
                @media (prefers-reduced-motion: reduce) {
                    #slide-9 * { transition: none !important; }
                }
            </style>

            <div class="baas-main" id="baas-main">
                <svg class="baas-svg-wrap" id="baas-svg"></svg>
                <div class="baas-packet" id="baas-packet"></div>

                <!-- LEFT: App Preview -->
                <div class="baas-left">
                    <div class="baas-app-card" id="baas-app" onclick="triggerAppConnection()">
                        <div class="app-title">YOUR APPLICATION</div>
                        <div class="app-header">
                            <div class="app-avatar"></div><div class="app-line"></div><div class="app-line" style="width:20px; flex:none;"></div>
                        </div>
                        <div class="app-body">
                            <div class="app-box"></div>
                            <div class="app-box"></div>
                            <div class="app-box" style="height:40px;"></div>
                        </div>
                    </div>
                    <div style="margin-top: 20px; font-size: 0.8rem; color: var(--muted); text-transform: uppercase; letter-spacing: 1px; font-weight: bold;">TRY A BACKEND SERVICE</div>
                    <div class="baas-actions">
                        <div class="baas-action-chip" onclick="triggerAction(0)">Login</div>
                        <div class="baas-action-chip" onclick="triggerAction(1)">Save Data</div>
                        <div class="baas-action-chip" onclick="triggerAction(2)">Upload File</div>
                        <div class="baas-action-chip" onclick="triggerAction(3)">Send Notification</div>
                        <div class="baas-action-chip" onclick="triggerAction(4)">View Analytics</div>
                    </div>
                </div>

                <!-- CENTER: BaaS Hub -->
                <div class="baas-center">
                    <div class="baas-status-msg" id="baas-msg"></div>
                    <div class="baas-core" id="baas-core">
                        <span class="baas-core-icon">☁️</span>
                        <span class="baas-core-title">BaaS<br>PLATFORM</span>
                    </div>
                </div>

                <!-- RIGHT: Services -->
                <div class="baas-right" id="baas-services">
                    <!-- JS generated -->
                </div>

                <!-- DETAIL PANEL -->
                <div class="baas-detail" id="baas-detail">
                    <div class="baas-detail-close" onclick="closeBaaSDetail()">Close ×</div>
                    <div class="baas-detail-title" id="baas-dt-title"><span id="baas-dt-icon"></span> <span id="baas-dt-name"></span></div>
                    <div class="baas-detail-text"><strong>Provides:</strong> <span id="baas-dt-provides"></span></div>
                    <div class="baas-detail-text"><strong>Example:</strong> <span id="baas-dt-example"></span></div>
                </div>
            </div>

            <div class="baas-controls">
                <button class="baas-btn" id="baas-demo-btn" onclick="runBaaSDemo()">Connect Application</button>
                <button class="baas-btn reset" id="baas-reset-btn" onclick="resetBaaS()">Reset Connection</button>
            </div>

            <script>
                const baasServicesData = [
                    { id: 'auth', title: 'Authentication', desc: 'Login and user identity.', icon: '🔐', provides: 'Login, registration, and user identity management.', example: 'A user signs in to a mobile application.', actionMsg: 'User authentication completed.', msg: 'Application connected to backend services.' },
                    { id: 'db', title: 'Database', desc: 'Store and retrieve application data.', icon: '🗄️', provides: 'A ready-made system for storing and retrieving data.', example: 'A student application saves user records and grades.', actionMsg: 'Data saved to the cloud database.', msg: 'Application connected to backend services.' },
                    { id: 'storage', title: 'Cloud Storage', desc: 'Save images, files, and documents.', icon: '📁', provides: 'Secure storage for uploaded files and images.', example: 'A user uploads a profile picture.', actionMsg: 'File stored in cloud storage.', msg: 'Application connected to backend services.' },
                    { id: 'notif', title: 'Notifications', desc: 'Send alerts and messages.', icon: '🔔', provides: 'Messages, alerts, and push notifications.', example: 'An application sends a notification about a new update.', actionMsg: 'Notification sent successfully.', msg: 'Application connected to backend services.' },
                    { id: 'analytics', title: 'Analytics', desc: 'Track application activity.', icon: '📊', provides: 'Information about how users interact with the application.', example: 'A developer checks how many users opened a feature.', actionMsg: 'Application activity retrieved.', msg: 'Application connected to backend services.' }
                ];

                const baasSrvContainer = document.getElementById('baas-services');
                
                baasServicesData.forEach((s, i) => {
                    let div = document.createElement('div');
                    div.className = 'baas-srv';
                    div.id = 'baas-srv-' + i;
                    div.onclick = () => triggerBaaSService(i);
                    div.innerHTML = `
                        <div class="baas-srv-icon">${s.icon}</div>
                        <div class="baas-srv-text">
                            <div class="baas-srv-title">${s.title}</div>
                            <div class="baas-srv-desc">${s.desc}</div>
                        </div>
                    `;
                    baasSrvContainer.appendChild(div);
                });

                function closeBaaSDetail() {
                    document.getElementById('baas-detail').classList.remove('show');
                }

                function showMessage(msg, color) {
                    let m = document.getElementById('baas-msg');
                    m.textContent = msg;
                    m.style.color = color || '#3ECF8E';
                    m.style.opacity = '1';
                }
                function hideMessage() {
                    document.getElementById('baas-msg').style.opacity = '0';
                }

                function resetBaaS() {
                    document.querySelectorAll('.baas-srv').forEach(el => el.classList.remove('selected'));
                    document.getElementById('baas-app').classList.remove('selected');
                    document.getElementById('baas-core').classList.remove('active');
                    hideMessage();
                    closeBaaSDetail();
                    document.getElementById('baas-svg').innerHTML = '';
                    document.getElementById('baas-packet').style.opacity = '0';
                    document.getElementById('baas-demo-btn').disabled = false;
                }

                function getBaaSLine(startEl, endEl, wrapEl) {
                    let wRect = wrapEl.getBoundingClientRect();
                    let sRect = startEl.getBoundingClientRect();
                    let eRect = endEl.getBoundingClientRect();
                    
                    let startX, startY, endX, endY;
                    
                    startX = sRect.left - wRect.left + (sRect.width / 2);
                    startY = sRect.top - wRect.top + (sRect.height / 2);
                    
                    endX = eRect.left - wRect.left + (eRect.width / 2);
                    endY = eRect.top - wRect.top + (eRect.height / 2);
                    
                    if (sRect.right < eRect.left) {
                        startX = sRect.right - wRect.left;
                        endX = eRect.left - wRect.left;
                    } else if (sRect.left > eRect.right) {
                        startX = sRect.left - wRect.left;
                        endX = eRect.right - wRect.left;
                    }
                    
                    return {startX, startY, endX, endY};
                }

                function animateBaaSPacket(startX, startY, endX, endY, color, callback) {
                    if(window.innerWidth <= 900) { if(callback) callback(); return; }
                    
                    var packet = document.getElementById('baas-packet');
                    packet.style.transition = 'none';
                    packet.style.background = color;
                    packet.style.boxShadow = '0 0 12px ' + color;
                    packet.style.transform = `translate(${startX-5}px, ${startY-5}px)`;
                    packet.style.opacity = '1';
                    
                    void packet.offsetWidth;
                    
                    packet.style.transition = 'transform 0.5s ease-in-out, opacity 0.2s';
                    packet.style.transform = `translate(${endX-5}px, ${endY-5}px)`;
                    
                    setTimeout(() => {
                        packet.style.opacity = '0';
                        if(callback) callback();
                    }, 500);
                }

                function triggerAppConnection() {
                    resetBaaS();
                    let app = document.getElementById('baas-app');
                    app.classList.add('selected');
                    
                    if(window.innerWidth > 900) {
                        let wrap = document.getElementById('baas-main');
                        let core = document.getElementById('baas-core');
                        let pos = getBaaSLine(app, core, wrap);
                        
                        document.getElementById('baas-svg').innerHTML = `<line x1="${pos.startX}" y1="${pos.startY}" x2="${pos.endX}" y2="${pos.endY}" stroke="rgba(34,211,238,0.3)" stroke-width="2" stroke-dasharray="4 4" />`;
                        
                        animateBaaSPacket(pos.startX, pos.startY, pos.endX, pos.endY, '#22D3EE', () => {
                            core.classList.add('active');
                            showMessage("Application connected to backend services.", "#22D3EE");
                        });
                    } else {
                        document.getElementById('baas-core').classList.add('active');
                        showMessage("Application connected to backend services.", "#22D3EE");
                    }
                }

                function triggerBaaSService(index) {
                    resetBaaS();
                    let srv = document.getElementById('baas-srv-' + index);
                    srv.classList.add('selected');
                    
                    let sData = baasServicesData[index];
                    document.getElementById('baas-dt-icon').textContent = sData.icon;
                    document.getElementById('baas-dt-name').textContent = sData.title;
                    document.getElementById('baas-dt-provides').textContent = sData.provides;
                    document.getElementById('baas-dt-example').textContent = sData.example;
                    
                    document.getElementById('baas-detail').classList.add('show');
                    
                    if(window.innerWidth > 900) {
                        let wrap = document.getElementById('baas-main');
                        let core = document.getElementById('baas-core');
                        core.classList.add('active');
                        
                        let pos = getBaaSLine(core, srv, wrap);
                        document.getElementById('baas-svg').innerHTML = `<line x1="${pos.startX}" y1="${pos.startY}" x2="${pos.endX}" y2="${pos.endY}" stroke="rgba(168,85,247,0.4)" stroke-width="2" stroke-dasharray="4 4" />`;
                        
                        animateBaaSPacket(pos.startX, pos.startY, pos.endX, pos.endY, '#A855F7', () => {});
                    } else {
                        document.getElementById('baas-core').classList.add('active');
                    }
                }

                function triggerAction(index) {
                    var btn = document.getElementById('baas-demo-btn');
                    if(btn.disabled) return;
                    btn.disabled = true;
                    
                    resetBaaS();
                    
                    let sData = baasServicesData[index];
                    let app = document.getElementById('baas-app');
                    let core = document.getElementById('baas-core');
                    let srv = document.getElementById('baas-srv-' + index);
                    let wrap = document.getElementById('baas-main');
                    
                    app.classList.add('selected');
                    
                    if(window.innerWidth > 900) {
                        let p1 = getBaaSLine(app, core, wrap);
                        let p2 = getBaaSLine(core, srv, wrap);
                        
                        document.getElementById('baas-svg').innerHTML = `
                            <line x1="${p1.startX}" y1="${p1.startY}" x2="${p1.endX}" y2="${p1.endY}" stroke="rgba(34,211,238,0.2)" stroke-width="2" stroke-dasharray="4 4" />
                            <line x1="${p2.startX}" y1="${p2.startY}" x2="${p2.endX}" y2="${p2.endY}" stroke="rgba(168,85,247,0.2)" stroke-width="2" stroke-dasharray="4 4" />
                        `;
                        
                        animateBaaSPacket(p1.startX, p1.startY, p1.endX, p1.endY, '#22D3EE', () => {
                            core.classList.add('active');
                            
                            setTimeout(() => {
                                srv.classList.add('selected');
                                animateBaaSPacket(p2.startX, p2.startY, p2.endX, p2.endY, '#A855F7', () => {
                                    setTimeout(() => {
                                        animateBaaSPacket(p2.endX, p2.endY, p2.startX, p2.startY, '#A855F7', () => {
                                            setTimeout(() => {
                                                animateBaaSPacket(p1.endX, p1.endY, p1.startX, p1.startY, '#3ECF8E', () => {
                                                    showMessage(sData.actionMsg, '#3ECF8E');
                                                    btn.disabled = false;
                                                });
                                            }, 200);
                                        });
                                    }, 400);
                                });
                            }, 200);
                        });
                    } else {
                        setTimeout(() => {
                            core.classList.add('active');
                            setTimeout(() => {
                                srv.classList.add('selected');
                                setTimeout(() => {
                                    showMessage(sData.actionMsg, '#3ECF8E');
                                    btn.disabled = false;
                                }, 800);
                            }, 600);
                        }, 400);
                    }
                }

                function runBaaSDemo() {
                    var btn = document.getElementById('baas-demo-btn');
                    if(btn.disabled) return;
                    btn.disabled = true;
                    
                    resetBaaS();
                    
                    let index = Math.floor(Math.random() * baasServicesData.length);
                    let app = document.getElementById('baas-app');
                    let core = document.getElementById('baas-core');
                    let srv = document.getElementById('baas-srv-' + index);
                    let wrap = document.getElementById('baas-main');
                    
                    app.classList.add('selected');
                    
                    if(window.innerWidth > 900) {
                        let p1 = getBaaSLine(app, core, wrap);
                        let p2 = getBaaSLine(core, srv, wrap);
                        
                        document.getElementById('baas-svg').innerHTML = `
                            <line x1="${p1.startX}" y1="${p1.startY}" x2="${p1.endX}" y2="${p1.endY}" stroke="rgba(34,211,238,0.2)" stroke-width="2" stroke-dasharray="4 4" />
                            <line x1="${p2.startX}" y1="${p2.startY}" x2="${p2.endX}" y2="${p2.endY}" stroke="rgba(168,85,247,0.2)" stroke-width="2" stroke-dasharray="4 4" />
                        `;
                        
                        animateBaaSPacket(p1.startX, p1.startY, p1.endX, p1.endY, '#22D3EE', () => {
                            core.classList.add('active');
                            
                            setTimeout(() => {
                                srv.classList.add('selected');
                                animateBaaSPacket(p2.startX, p2.startY, p2.endX, p2.endY, '#A855F7', () => {
                                    setTimeout(() => {
                                        animateBaaSPacket(p2.endX, p2.endY, p2.startX, p2.startY, '#A855F7', () => {
                                            setTimeout(() => {
                                                animateBaaSPacket(p1.endX, p1.endY, p1.startX, p1.startY, '#3ECF8E', () => {
                                                    showMessage("Backend service connected successfully.", '#3ECF8E');
                                                    btn.disabled = false;
                                                });
                                            }, 200);
                                        });
                                    }, 400);
                                });
                            }, 200);
                        });
                    } else {
                        setTimeout(() => {
                            core.classList.add('active');
                            setTimeout(() => {
                                srv.classList.add('selected');
                                setTimeout(() => {
                                    showMessage("Backend service connected successfully.", '#3ECF8E');
                                    btn.disabled = false;
                                }, 800);
                            }, 600);
                        }, 400);
                    }
                }
            </script>
        </div>"""

pattern = re.compile(r'<div class="slide" id="slide-9".*?</script>\s*</div>', re.DOTALL)
new_content = pattern.sub(replacement, content)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Patched Slide 9")
