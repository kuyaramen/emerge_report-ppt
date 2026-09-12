let currentSlideIndex = 1;
const totalSlides = 21;

// Quiz Data
const quizQuestions = [
    {
        q: "What is serverless computing?",
        options: [
            "A model where there are literally zero servers.",
            "A cloud model where developers run code without directly managing servers.",
            "A model used only for frontend web design.",
            "A type of physical hardware you can buy."
        ],
        correct: 1,
        explanation: "Serverless still uses servers, but the cloud provider manages them so developers don't have to."
    },
    {
        q: "What does FaaS stand for?",
        options: [
            "File as a Storage",
            "Frontend as a Service",
            "Function as a Service",
            "Fast Application Access Server"
        ],
        correct: 2,
        explanation: "FaaS stands for Function as a Service — it lets you run custom code on demand."
    },
    {
        q: "What does BaaS stand for?",
        options: [
            "Binary as a Service",
            "Backend as a Service",
            "Bandwidth as a Service",
            "Basic Application Automation System"
        ],
        correct: 1,
        explanation: "BaaS stands for Backend as a Service — it provides ready-made backend features like databases and authentication."
    },
    {
        q: "Which is an advantage of serverless computing?",
        options: [
            "It automatically writes code for you.",
            "It eliminates cold starts entirely.",
            "It allows apps to handle changing traffic automatically.",
            "It automatically manages database backups."
        ],
        correct: 2,
        explanation: "Automatic scaling means the platform can handle traffic spikes by spinning up more function instances."
    },
    {
        q: "Is serverless computing the same as cloud computing?",
        options: [
            "Yes, they are identical.",
            "No — serverless is one model within the broader category of cloud computing.",
            "No — serverless is broader than cloud computing.",
            "They are completely unrelated."
        ],
        correct: 1,
        explanation: "Cloud computing is the broad category. Serverless is a specific execution model within it."
    }
];

let currentQuizIndex = 0;

// ===================== Init =====================
document.addEventListener('DOMContentLoaded', () => {
    updateSlideVisibility();
    updateProgress();
    renderQuiz();

    let touchStartX = 0;

    // Keyboard navigation
    document.addEventListener('keydown', (e) => {
        switch (e.key) {
            case 'ArrowRight':
            case ' ':
                e.preventDefault();
                nextSlide();
                break;
            case 'ArrowLeft':
                e.preventDefault();
                prevSlide();
                break;
            case 'Home':
                e.preventDefault();
                currentSlideIndex = 1;
                updateSlideVisibility();
                updateProgress();
                break;
            case 'End':
                e.preventDefault();
                currentSlideIndex = totalSlides;
                updateSlideVisibility();
                updateProgress();
                break;
        }
    });

    // Touch / swipe navigation
    const pres = document.getElementById('presentation');

    pres.addEventListener('touchstart', e => {
        touchStartX = e.changedTouches[0].screenX;
    }, { passive: true });

    pres.addEventListener('touchend', e => {
        const diff = e.changedTouches[0].screenX - touchStartX;
        if (diff < -50) nextSlide();
        if (diff > 50)  prevSlide();
    }, { passive: true });
});

// ===================== Navigation =====================
function nextSlide() {
    if (currentSlideIndex < totalSlides) {
        currentSlideIndex++;
        updateSlideVisibility();
        updateProgress();
    }
}

function prevSlide() {
    if (currentSlideIndex > 1) {
        currentSlideIndex--;
        updateSlideVisibility();
        updateProgress();
    }
}

function restart() {
    currentSlideIndex = 1;
    currentQuizIndex = 0;
    renderQuiz();
    updateSlideVisibility();
    updateProgress();
}

function updateSlideVisibility() {
    document.querySelectorAll('.slide').forEach(s => s.classList.remove('active'));
    const el = document.getElementById(`slide-${currentSlideIndex}`);
    if (el) el.classList.add('active');

    document.getElementById('slide-counter').textContent = `${currentSlideIndex} / ${totalSlides}`;
    document.getElementById('prev-btn').disabled = (currentSlideIndex === 1);
    document.getElementById('next-btn').disabled = (currentSlideIndex === totalSlides);
}

function updateProgress() {
    const pct = ((currentSlideIndex - 1) / (totalSlides - 1)) * 100;
    document.getElementById('progress-bar').style.width = `${pct}%`;
}

function toggleFullscreen() {
    const el = document.documentElement;
    const btn = document.getElementById('fullscreen-btn');
    if (!document.fullscreenElement) {
        (el.requestFullscreen || el.webkitRequestFullscreen || el.msRequestFullscreen).call(el);
        btn.innerHTML = '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M8 3v3a2 2 0 0 1-2 2H3m18 0h-3a2 2 0 0 1-2-2V3m0 18v-3a2 2 0 0 1 2-2h3M3 16h3a2 2 0 0 1 2 2v3"/></svg> Exit Fullscreen';
    } else {
        (document.exitFullscreen || document.webkitExitFullscreen || document.msExitFullscreen).call(document);
        btn.innerHTML = '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M8 3H5a2 2 0 0 0-2 2v3m18 0V5a2 2 0 0 0-2-2h-3m0 18h3a2 2 0 0 0 2-2v-3M3 16v3a2 2 0 0 0 2 2h3"/></svg> Fullscreen';
    }
}

// ===================== Quiz =====================
function renderQuiz() {
    const container = document.getElementById('quiz-container');
    container.innerHTML = '';

    quizQuestions.forEach((q, i) => {
        const div = document.createElement('div');
        div.className = `mc-question ${i === currentQuizIndex ? 'active' : ''}`;
        div.id = `mc-q-${i}`;

        let opts = '';
        q.options.forEach((opt, oi) => {
            opts += `<button class="mc-option" onclick="selectAnswer(${i}, ${oi}, this)">${opt}</button>`;
        });

        div.innerHTML = `
            <h3>Question ${i + 1}</h3>
            <p style="font-size:1.05rem; margin-bottom:14px;">${q.q}</p>
            <div class="mc-options">${opts}</div>
            <div class="mc-feedback" id="feedback-${i}"></div>
        `;
        container.appendChild(div);
    });

    document.getElementById('quiz-progress').textContent = `Question ${currentQuizIndex + 1} of ${quizQuestions.length}`;
    document.getElementById('next-q-btn').style.display = 'none';
}

function selectAnswer(qIdx, selIdx, btn) {
    const q = quizQuestions[qIdx];
    const options = btn.parentElement.children;

    for (let o of options) { o.disabled = true; o.style.pointerEvents = 'none'; }

    const fb = document.getElementById(`feedback-${qIdx}`);

    if (selIdx === q.correct) {
        btn.classList.add('correct');
        fb.textContent = `Correct! ${q.explanation}`;
        fb.className = 'mc-feedback visible success';
    } else {
        btn.classList.add('wrong');
        options[q.correct].classList.add('correct');
        fb.textContent = `Incorrect. ${q.explanation}`;
        fb.className = 'mc-feedback visible';
    }

    if (qIdx < quizQuestions.length - 1) {
        document.getElementById('next-q-btn').style.display = 'inline-block';
    }
}

function nextQuestion() {
    if (currentQuizIndex < quizQuestions.length - 1) {
        document.getElementById(`mc-q-${currentQuizIndex}`).classList.remove('active');
        currentQuizIndex++;
        document.getElementById(`mc-q-${currentQuizIndex}`).classList.add('active');
        document.getElementById('quiz-progress').textContent = `Question ${currentQuizIndex + 1} of ${quizQuestions.length}`;
        document.getElementById('next-q-btn').style.display = 'none';
    }
}
