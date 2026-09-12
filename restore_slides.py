import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

slides_html = """
        <!-- ============================================ -->
        <!-- SLIDE 10: FAAS VS BAAS -->
        <!-- ============================================ -->
        <div class="slide" id="slide-10" style="justify-content: center;">
            <h2 style="text-align: center; border-bottom: none; margin-bottom: 40px; text-transform: uppercase; letter-spacing: 2px;">FaaS vs BaaS</h2>
            
            <div class="glass-card" style="padding: 30px; margin: 0 auto; max-width: 900px; display: flex; flex-direction: column; justify-content: center;">
                <table class="modern-table" style="width: 100%; text-align: left; border-collapse: collapse; font-size: 1rem;">
                    <thead>
                        <tr>
                            <th style="padding-bottom: 20px; color: white; width: 30%; font-weight: 600; font-size: 1.1rem; border-bottom: 1px solid rgba(255,255,255,0.1);">Feature</th>
                            <th style="padding-bottom: 20px; color: var(--cyan); width: 35%; font-weight: 600; font-size: 1.1rem; border-bottom: 1px solid rgba(255,255,255,0.1);">FaaS</th>
                            <th style="padding-bottom: 20px; color: var(--blue); width: 35%; font-weight: 600; font-size: 1.1rem; border-bottom: 1px solid rgba(255,255,255,0.1);">BaaS</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td style="padding: 15px 0; color: white; font-weight: bold; border-bottom: 1px solid rgba(255,255,255,0.05);">What it does</td>
                            <td style="padding: 15px 0; color: var(--muted); border-bottom: 1px solid rgba(255,255,255,0.05);">Runs your custom code.</td>
                            <td style="padding: 15px 0; color: var(--muted); border-bottom: 1px solid rgba(255,255,255,0.05);">Provides ready-made backend services.</td>
                        </tr>
                        <tr>
                            <td style="padding: 15px 0; color: white; font-weight: bold; border-bottom: 1px solid rgba(255,255,255,0.05);">Developer Role</td>
                            <td style="padding: 15px 0; color: var(--muted); border-bottom: 1px solid rgba(255,255,255,0.05);">You write the functions.</td>
                            <td style="padding: 15px 0; color: var(--muted); border-bottom: 1px solid rgba(255,255,255,0.05);">You connect to ready-made features.</td>
                        </tr>
                        <tr>
                            <td style="padding: 15px 0; color: white; font-weight: bold; border-bottom: 1px solid rgba(255,255,255,0.05);">Focus</td>
                            <td style="padding: 15px 0; color: var(--muted); border-bottom: 1px solid rgba(255,255,255,0.05);">Code execution</td>
                            <td style="padding: 15px 0; color: var(--muted); border-bottom: 1px solid rgba(255,255,255,0.05);">Backend functionality</td>
                        </tr>
                        <tr>
                            <td style="padding: 15px 0; color: white; font-weight: bold;">Memory Tip</td>
                            <td style="padding: 15px 0; color: var(--cyan); font-weight: bold;">"Run my code"</td>
                            <td style="padding: 15px 0; color: var(--blue); font-weight: bold;">"Give me backend services"</td>
                        </tr>
                    </tbody>
                </table>
            </div>
            
            <div class="quiz-section" style="margin-top: 40px; text-align: center;">
                <p class="question-text" style="color: var(--muted); font-size: 1.1rem; margin-bottom: 15px;">Q: Which type of serverless computing focuses on running your own code?</p>
                <button class="btn btn-outline" style="padding: 10px 20px; border-radius: 8px; background: rgba(34,211,238,0.1); color: var(--cyan); border: 1px solid var(--cyan); cursor: pointer;" onclick="document.getElementById('ans10').style.display = 'block'; this.style.display='none';">Show Answer</button>
                <div class="answer-box glass-card" id="ans10" style="display: none; padding: 15px; margin-top: 15px; background: rgba(15,30,55,0.9); border: 1px solid var(--cyan); color: white;">
                    <strong>A:</strong> FaaS — Function as a Service
                </div>
            </div>
        </div>

        <!-- ============================================ -->
        <!-- SLIDE 11: ADVANTAGES -->
        <!-- ============================================ -->
        <div class="slide" id="slide-11" style="justify-content: flex-start; padding-top: 40px;">
            <h2 style="text-align: center; border-bottom: none; margin-bottom: 40px; text-transform: uppercase; letter-spacing: 2px;">Advantages of Serverless Computing</h2>
            
            <div style="display: flex; flex-direction: column; gap: 15px; max-width: 900px; margin: 0 auto; width: 100%;">
                <div class="glass-card" style="padding: 20px; display: flex; align-items: center; gap: 20px; border-left: 4px solid #3ECF8E;">
                    <div style="font-size: 2rem; width: 50px; text-align: center;">⚙️</div>
                    <div>
                        <h4 style="color: white; margin: 0 0 5px 0; font-size: 1.1rem;">No direct server management</h4>
                        <p style="color: var(--muted); margin: 0; font-size: 0.95rem;">Focus purely on coding.</p>
                    </div>
                </div>
                <div class="glass-card" style="padding: 20px; display: flex; align-items: center; gap: 20px; border-left: 4px solid #3ECF8E;">
                    <div style="font-size: 2rem; width: 50px; text-align: center;">📈</div>
                    <div>
                        <h4 style="color: white; margin: 0 0 5px 0; font-size: 1.1rem;">Automatic scaling</h4>
                        <p style="color: var(--muted); margin: 0; font-size: 0.95rem;">Handles 1 user or 10,000 users automatically.</p>
                    </div>
                </div>
                <div class="glass-card" style="padding: 20px; display: flex; align-items: center; gap: 20px; border-left: 4px solid #3ECF8E;">
                    <div style="font-size: 2rem; width: 50px; text-align: center;">💰</div>
                    <div>
                        <h4 style="color: white; margin: 0 0 5px 0; font-size: 1.1rem;">Usage-based pricing</h4>
                        <p style="color: var(--muted); margin: 0; font-size: 0.95rem;">You only pay when the code actually runs.</p>
                    </div>
                </div>
                <div class="glass-card" style="padding: 20px; display: flex; align-items: center; gap: 20px; border-left: 4px solid #3ECF8E;">
                    <div style="font-size: 2rem; width: 50px; text-align: center;">🚀</div>
                    <div>
                        <h4 style="color: white; margin: 0 0 5px 0; font-size: 1.1rem;">Faster development</h4>
                        <p style="color: var(--muted); margin: 0; font-size: 0.95rem;">Quicker to build and launch apps.</p>
                    </div>
                </div>
            </div>
            
            <div class="quiz-section" style="margin-top: 30px; text-align: center;">
                <p class="question-text" style="color: var(--muted); font-size: 1.1rem; margin-bottom: 15px;">Q: Which advantage allows serverless applications to handle changing numbers of users?</p>
                <button class="btn btn-outline" style="padding: 10px 20px; border-radius: 8px; background: rgba(34,211,238,0.1); color: var(--cyan); border: 1px solid var(--cyan); cursor: pointer;" onclick="document.getElementById('ans11').style.display = 'block'; this.style.display='none';">Show Answer</button>
                <div class="answer-box glass-card" id="ans11" style="display: none; padding: 15px; margin-top: 15px; background: rgba(15,30,55,0.9); border: 1px solid #3ECF8E; color: white;">
                    <strong>A:</strong> Automatic scaling
                </div>
            </div>
        </div>

        <!-- ============================================ -->
        <!-- SLIDE 12: DISADVANTAGES -->
        <!-- ============================================ -->
        <div class="slide" id="slide-12" style="justify-content: flex-start; padding-top: 40px;">
            <h2 style="text-align: center; border-bottom: none; margin-bottom: 40px; text-transform: uppercase; letter-spacing: 2px;">Disadvantages of Serverless</h2>
            
            <div style="display: flex; flex-direction: column; gap: 15px; max-width: 900px; margin: 0 auto; width: 100%;">
                <div class="glass-card" style="padding: 20px; display: flex; align-items: center; gap: 20px; border-left: 4px solid #F59E0B;">
                    <div style="font-size: 2rem; width: 50px; text-align: center;">❄️</div>
                    <div>
                        <h4 style="color: white; margin: 0 0 5px 0; font-size: 1.1rem;">Cold starts</h4>
                        <p style="color: var(--muted); margin: 0; font-size: 0.95rem;">A slight delay when a function runs after being inactive.</p>
                    </div>
                </div>
                <div class="glass-card" style="padding: 20px; display: flex; align-items: center; gap: 20px; border-left: 4px solid #F59E0B;">
                    <div style="font-size: 2rem; width: 50px; text-align: center;">⏱️</div>
                    <div>
                        <h4 style="color: white; margin: 0 0 5px 0; font-size: 1.1rem;">Execution time limits</h4>
                        <p style="color: var(--muted); margin: 0; font-size: 0.95rem;">Functions cannot run forever (e.g., max 15 minutes).</p>
                    </div>
                </div>
                <div class="glass-card" style="padding: 20px; display: flex; align-items: center; gap: 20px; border-left: 4px solid #F59E0B;">
                    <div style="font-size: 2rem; width: 50px; text-align: center;">☁️</div>
                    <div>
                        <h4 style="color: white; margin: 0 0 5px 0; font-size: 1.1rem;">Dependency on internet & cloud</h4>
                        <p style="color: var(--muted); margin: 0; font-size: 0.95rem;">If the provider goes down, you go down.</p>
                    </div>
                </div>
                <div class="glass-card" style="padding: 20px; display: flex; align-items: center; gap: 20px; border-left: 4px solid #F59E0B;">
                    <div style="font-size: 2rem; width: 50px; text-align: center;">🔒</div>
                    <div>
                        <h4 style="color: white; margin: 0 0 5px 0; font-size: 1.1rem;">Vendor lock-in</h4>
                        <p style="color: var(--muted); margin: 0; font-size: 0.95rem;">Hard to move from AWS to Google Cloud.</p>
                    </div>
                </div>
            </div>
            
            <div class="quiz-section" style="margin-top: 30px; text-align: center;">
                <p class="question-text" style="color: var(--muted); font-size: 1.1rem; margin-bottom: 15px;">Q: What is a cold start?</p>
                <button class="btn btn-outline" style="padding: 10px 20px; border-radius: 8px; background: rgba(34,211,238,0.1); color: var(--cyan); border: 1px solid var(--cyan); cursor: pointer;" onclick="document.getElementById('ans12').style.display = 'block'; this.style.display='none';">Show Answer</button>
                <div class="answer-box glass-card" id="ans12" style="display: none; padding: 15px; margin-top: 15px; background: rgba(15,30,55,0.9); border: 1px solid #F59E0B; color: white;">
                    <strong>A:</strong> A cold start is the extra startup delay that may occur when a serverless environment needs to wake up and prepare before running.
                </div>
            </div>
        </div>

        <!-- ============================================ -->
        <!-- SLIDE 13: TRADITIONAL VS SERVERLESS -->
        <!-- ============================================ -->
        <div class="slide" id="slide-13" style="justify-content: center;">
            <h2 style="text-align: center; border-bottom: none; margin-bottom: 40px; text-transform: uppercase; letter-spacing: 2px;">Traditional Server vs Serverless</h2>
            
            <div class="glass-card" style="padding: 30px; margin: 0 auto; max-width: 900px; display: flex; flex-direction: column; justify-content: center;">
                <table class="modern-table" style="width: 100%; text-align: left; border-collapse: collapse; font-size: 1rem;">
                    <thead>
                        <tr>
                            <th style="padding-bottom: 20px; color: white; width: 50%; font-weight: 600; font-size: 1.1rem; border-bottom: 1px solid rgba(255,255,255,0.1);">Traditional Server</th>
                            <th style="padding-bottom: 20px; color: var(--cyan); width: 50%; font-weight: 600; font-size: 1.1rem; border-bottom: 1px solid rgba(255,255,255,0.1);">Serverless</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td style="padding: 15px 0; color: var(--muted); border-bottom: 1px solid rgba(255,255,255,0.05);">You manage the operating system and updates</td>
                            <td style="padding: 15px 0; color: white; border-bottom: 1px solid rgba(255,255,255,0.05);">The cloud provider manages the infrastructure</td>
                        </tr>
                        <tr>
                            <td style="padding: 15px 0; color: var(--muted); border-bottom: 1px solid rgba(255,255,255,0.05);">The server runs continuously (24/7)</td>
                            <td style="padding: 15px 0; color: white; border-bottom: 1px solid rgba(255,255,255,0.05);">Functions run only when triggered</td>
                        </tr>
                        <tr>
                            <td style="padding: 15px 0; color: var(--muted); border-bottom: 1px solid rgba(255,255,255,0.05);">Scaling requires manual setup</td>
                            <td style="padding: 15px 0; color: white; border-bottom: 1px solid rgba(255,255,255,0.05);">Scaling is handled automatically</td>
                        </tr>
                        <tr>
                            <td style="padding: 15px 0; color: var(--muted);">You must configure resources</td>
                            <td style="padding: 15px 0; color: white;">Developers focus entirely on the code</td>
                        </tr>
                    </tbody>
                </table>
            </div>
            
            <div class="quiz-section" style="margin-top: 40px; text-align: center;">
                <p class="question-text" style="color: var(--muted); font-size: 1.1rem; margin-bottom: 15px;">Q: What is the main difference between a traditional server and serverless computing?</p>
                <button class="btn btn-outline" style="padding: 10px 20px; border-radius: 8px; background: rgba(34,211,238,0.1); color: var(--cyan); border: 1px solid var(--cyan); cursor: pointer;" onclick="document.getElementById('ans13').style.display = 'block'; this.style.display='none';">Show Answer</button>
                <div class="answer-box glass-card" id="ans13" style="display: none; padding: 15px; margin-top: 15px; background: rgba(15,30,55,0.9); border: 1px solid var(--cyan); color: white;">
                    <strong>A:</strong> In traditional computing, the developer manages the server. In serverless, the cloud provider manages the underlying infrastructure.
                </div>
            </div>
        </div>

        <!-- ============================================ -->
        <!-- SLIDE 14: CLOUD VS SERVERLESS -->
        <!-- ============================================ -->
        <div class="slide" id="slide-14" style="justify-content: center;">
            <h2 style="text-align: center; border-bottom: none; margin-bottom: 40px; text-transform: uppercase; letter-spacing: 2px;">Cloud Computing vs Serverless</h2>
            
            <div style="display: flex; flex-direction: column; align-items: center; max-width: 800px; margin: 0 auto;">
                <p style="color: white; font-size: 1.1rem; text-align: center; margin-bottom: 30px;">
                    <strong style="color: var(--cyan);">Important concept:</strong> Serverless is one model within the broader category of cloud computing.
                </p>
                
                <!-- Nested Diagram -->
                <div class="glass-card" style="padding: 40px; border: 2px solid rgba(255,255,255,0.2); border-radius: 20px; width: 100%; text-align: center; position: relative;">
                    <h3 style="color: var(--muted); font-size: 1.5rem; margin-top: 0;">CLOUD COMPUTING</h3>
                    <p style="color: rgba(255,255,255,0.5); font-size: 1rem; margin-bottom: 30px;">The delivery of computing services over the internet.</p>
                    
                    <div class="glass-card" style="padding: 30px; border: 2px solid var(--cyan); border-radius: 15px; background: rgba(34,211,238,0.05); display: inline-block;">
                        <h3 style="color: white; font-size: 1.3rem; margin-top: 0;">SERVERLESS COMPUTING</h3>
                        <p style="color: var(--cyan); font-size: 1rem; margin: 0;">A specific model where the provider manages the underlying servers.</p>
                    </div>
                </div>
            </div>
            
            <div class="quiz-section" style="margin-top: 40px; text-align: center;">
                <p class="question-text" style="color: var(--muted); font-size: 1.1rem; margin-bottom: 15px;">Q: Is serverless computing a type of cloud computing?</p>
                <button class="btn btn-outline" style="padding: 10px 20px; border-radius: 8px; background: rgba(34,211,238,0.1); color: var(--cyan); border: 1px solid var(--cyan); cursor: pointer;" onclick="document.getElementById('ans14').style.display = 'block'; this.style.display='none';">Show Answer</button>
                <div class="answer-box glass-card" id="ans14" style="display: none; padding: 15px; margin-top: 15px; background: rgba(15,30,55,0.9); border: 1px solid var(--cyan); color: white;">
                    <strong>A:</strong> Yes, it is a specific model within cloud computing.
                </div>
            </div>
        </div>
"""

# Find the end of Slide 9
pattern = r'(<div class="slide" id="slide-9".*?</script>\s*</div>)'
match = re.search(pattern, content, re.DOTALL)

if match:
    new_content = content[:match.end()] + "\n" + slides_html + content[match.end():]
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("Successfully restored slides 10-14")
else:
    print("Could not find Slide 9 to insert after.")
