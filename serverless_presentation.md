# SERVERLESS COMPUTING
## Understanding Cloud-Based Application Execution

---

## SLIDE 1 — TITLE SLIDE

**Title:** SERVERLESS COMPUTING
**Subtitle:** Understanding Cloud-Based Application Execution

**Presented by:** 
* ABAO JOHN LOUIE B.
* AURE LORNA JAY
* KURT CHUA
* NIKKOS CHARLES

**Course / Subject:** EMERGING TECHNOLOGY  
**Instructor:** Engr. Catherine M. Verallo  
**Date:** 9/12/2026  

**Visual Description:** A professional, dark navy background with subtle cyan and blue accents. A clean, modern cloud computing illustration featuring stylized servers, floating code snippets, and connected devices in the center. Large, bold, white typography for the main title.

**Speaker Notes:**
> "Good morning, everyone. Today, we will be discussing Serverless Computing—a modern approach to how applications are built and run in the cloud. My name is [Your Name], and together with my group mates John Louie, Lorna Jay, Kurt, and Nikkos, we will explain what serverless is, how it works, and why it is so important in modern technology."

---

## SLIDE 2 — LEARNING OBJECTIVES

**Title:** What We Will Learn

**Content:**
1. Define serverless computing.
2. Explain how serverless works.
3. Identify FaaS and BaaS.
4. Discuss advantages and disadvantages.
5. Compare cloud computing and serverless computing.
6. Apply serverless concepts to a real website.

**Visual Description:** A clean roadmap or a six-step learning journey graphic stretching across the slide. Each step has a simple, modern icon.

**Speaker Notes:**
> "Before we dive in, let's look at our roadmap for today. We'll start by defining what cloud and serverless computing are. Then, we will look at how it works behind the scenes, the two main types you should know, and the pros and cons. Finally, we'll compare it to traditional servers and apply what we've learned to a real-world example."

---

## SLIDE 3 — INTRODUCTION TO CLOUD COMPUTING

**Title:** What Is Cloud Computing?

**Content:**
Cloud computing is the delivery of computing services over the internet.

**Examples of services:**
* Servers
* Storage
* Databases
* Networking
* Software

**Simple example:**
Instead of buying and maintaining your own computer server, you use computing resources provided by a cloud company (e.g., AWS, Azure, Google Cloud).

**Visual Description:** A simple, high-quality diagram showing a User connecting to the Internet, which then connects to a "Cloud" containing icons for Servers, Storage, and Databases.

**Question 1:**
*What is cloud computing?*

**Speaker Notes:**
> "To understand serverless, we first need to understand cloud computing. Put simply, cloud computing is just delivering computing services over the internet. Instead of buying a physical server and putting it in your room, you rent one from companies like Amazon, Microsoft, or Google. 
> 
> **Question for the class:** What is cloud computing?
> **Answer:** Cloud computing is the delivery of computing services over the internet."

---

## SLIDE 4 — INTRODUCTION TO SERVERLESS COMPUTING

**Title:** What Is Serverless Computing?

**Content:**
Serverless computing is a cloud computing model where developers run code without directly managing the underlying servers.

* Servers still exist!
* The cloud provider manages the infrastructure.
* Developers focus entirely on writing and deploying code.
* Functions run only when needed.

> **Important:** Serverless does NOT mean there are no servers.

**Visual Description:** A graphic showing a Developer pushing code to a "Cloud Platform" box, which then automatically handles the "Managed Servers" hidden behind a shield or gear icon.

**Question 2:**
*Why is it called serverless if servers still exist?*

**Speaker Notes:**
> "Now, what is serverless computing? It is a specific type of cloud computing where developers run code without worrying about managing the servers. 
> An important thing to remember: Serverless does NOT mean there are no servers. Servers definitely exist in massive data centers. It just means *you* don't have to deal with them.
> 
> **Question for the class:** Why is it called serverless if servers still exist?
> **Answer:** Because the cloud provider manages the underlying servers, so developers do not have to manage them directly."

---

## SLIDE 5 — HOW SERVERLESS COMPUTING WORKS

**Title:** How Serverless Computing Works

**Content:**
1. A user sends a request.
2. The cloud receives the request.
3. A serverless function runs.
4. The function processes the request.
5. The result is returned.
6. The function execution ends.

**Visual Description:** A clean, horizontal process diagram. User Request (Smartphone Icon) → Cloud Platform (Cloud Icon) → Serverless Function (Gear/Code Icon) → Process Data (Database Icon) → Return Response (Checkmark).

**Question 3:**
*What triggers a serverless function to run?*

**Speaker Notes:**
> "How does this actually work? Unlike traditional servers that are always on and waiting, serverless functions only run when something happens. A user sends a request, the cloud receives it, the code spins up, processes the data, returns the result, and then the function shuts down entirely.
> 
> **Question for the class:** What triggers a serverless function to run?
> **Answer:** A request or event (like a button click) triggers the function to run."

---

## SLIDE 6 — REAL-LIFE EXAMPLE

**Title:** Example: Get Latest News

**Scenario:** A user clicks "Get Latest News" on a website.

**Process:**
1. User clicks the button.
2. The request goes to the cloud.
3. The serverless function runs.
4. The function retrieves news from the database.
5. The website displays the news.

**Visual Description:** A visual flow showing a Website UI (clicking a button) → A Serverless Function block (lighting up) → A Database block (fetching data) → The Website UI (showing the news).

**Question 4:**
*What does the serverless function do in the news website example?*

**Speaker Notes:**
> "Let’s look at a simple real-life example. Imagine you are on a news website and click 'Get Latest News'. That click sends a request to the cloud. A serverless function wakes up, grabs the latest news from the database, sends it back to your screen, and goes back to sleep.
> 
> **Question for the class:** What does the serverless function do in this news website example?
> **Answer:** It processes the request and retrieves the news from the database."

---

## SLIDE 7 — TYPES OF SERVERLESS COMPUTING

**Title:** Two Main Types of Serverless Computing

**Content:**
**1. Function as a Service (FaaS)**
Run your own custom code only when needed.

**2. Backend as a Service (BaaS)**
Use ready-made backend services provided by a cloud platform.

**Visual Description:** Two professional comparison cards side-by-side. The left card (FaaS) has a code bracket icon `</>`. The right card (BaaS) has a stacked database/API icon.

**Question 5:**
*What are the two main types of serverless computing discussed in this presentation?*

**Speaker Notes:**
> "There are two main flavors of serverless computing you need to know: FaaS and BaaS. FaaS is for when you want to run your own custom code. BaaS is when you want to use ready-made backend features like databases without building them yourself.
> 
> **Question for the class:** What are the two main types of serverless computing discussed?
> **Answer:** Function as a Service (FaaS) and Backend as a Service (BaaS)."

---

## SLIDE 8 — FUNCTION AS A SERVICE (FAAS)

**Title:** Function as a Service (FaaS)

**Content:**
FaaS allows developers to run small pieces of code in response to events or requests.

* You write a function.
* The cloud runs it when needed.
* You do not manage the underlying server.
* Example: AWS Lambda.

**Code Example (JavaScript):**
```javascript
function calculateTotal(price, quantity) {
  return price * quantity;
}
console.log(calculateTotal(50, 2)); // Output: 100
```

**Visual Description:** A diagram showing a Button → Triggering a Function → Returning a Result. The simple code snippet is displayed in a clean, dark-themed code editor box.

**Question 6:**
*What does FaaS allow developers to run?*

**Speaker Notes:**
> "Let's dive into FaaS. Function as a Service lets you run small pieces of code. You just write the logic, upload it, and the cloud handles the rest. On the slide is a simple JavaScript function multiplying price by quantity. In a FaaS model, this code only runs when a user buys something, and you only pay for the exact milliseconds it takes to run.
> 
> **Question for the class:** What does FaaS allow developers to run?
> **Answer:** It allows developers to run their own functions or pieces of code when needed."

---

## SLIDE 9 — BACKEND AS A SERVICE (BAAS)

**Title:** Backend as a Service (BaaS)

**Content:**
BaaS provides ready-made backend services so developers do not need to build everything from scratch.

**Common BaaS Services:**
* Databases
* User authentication (Logins)
* File storage
* APIs and Notifications

**Example:** Supabase, Firebase.

**Visual Description:** A central application icon connected by glowing lines to four surrounding icons representing Database, Authentication, Storage, and APIs.

**Question 7:**
*What is the main purpose of BaaS?*

**Speaker Notes:**
> "Next is BaaS, or Backend as a Service. Building a login system or a secure database from scratch is hard. BaaS providers give you these features ready to use out of the box. You just connect your app to them.
> 
> **Question for the class:** What is the main purpose of BaaS?
> **Answer:** To provide ready-made backend services that developers can easily plug into their applications."

---

## SLIDE 10 — FAAS VS BAAS

**Title:** FaaS vs BaaS

**Content:**
| Feature | FaaS (Function as a Service) | BaaS (Backend as a Service) |
| :--- | :--- | :--- |
| **What it does** | Runs your custom code. | Provides ready-made backend services. |
| **Developer role** | You write the functions. | You connect to ready-made features. |
| **Example** | AWS Lambda | Supabase |
| **Focus** | Code execution | Backend functionality |

**Memory Tip:**
* "FaaS = Run my code."
* "BaaS = Give me backend services."

**Visual Description:** A clean, modern comparison table with subtle row highlighting. The memory tips are displayed in a callout box at the bottom.

**Question 8:**
*Which type of serverless computing focuses on running your own code?*

**Speaker Notes:**
> "To summarize the difference: FaaS is about running your specific code logic. BaaS is about giving you pre-built tools like databases. Just remember: FaaS equals 'Run my code', and BaaS equals 'Give me backend services'.
> 
> **Question for the class:** Which type of serverless computing focuses on running your own code?
> **Answer:** FaaS — Function as a Service."

---

## SLIDE 11 — ADVANTAGES OF SERVERLESS COMPUTING

**Title:** Advantages of Serverless Computing

**Content:**
1. **No direct server management:** Focus purely on coding.
2. **Automatic scaling:** Handles 1 user or 10,000 users automatically.
3. **Usage-based pricing:** You only pay when the code actually runs.
4. **Faster development:** Quicker to build and launch apps.
5. **Focus on application code:** Less time spent on server maintenance.

**Visual Description:** Five distinct visual cards with sleek icons (e.g., a shield for management, an expanding arrow for scaling, a coin for pricing). 

**Question 9:**
*Which advantage allows serverless applications to handle changing numbers of users?*

**Speaker Notes:**
> "Why do companies love serverless? First, no server maintenance. Second, it scales automatically. If your app suddenly goes viral, the platform instantly spins up more function instances to handle the traffic. Third, it's cost-effective; if nobody uses your app, your functions don't run, and you pay zero.
> 
> **Question for the class:** Which advantage allows serverless apps to handle changing numbers of users?
> **Answer:** Automatic scaling."

---

## SLIDE 12 — DISADVANTAGES OF SERVERLESS COMPUTING

**Title:** Disadvantages of Serverless Computing

**Content:**
1. **Cold starts:** A slight delay when a function runs after being inactive.
2. **Execution time limits:** Functions cannot run forever (e.g., max 15 minutes).
3. **Dependency on internet & cloud:** If the provider goes down, you go down.
4. **Vendor lock-in:** Hard to move from AWS to Google Cloud.
5. **Cost spikes:** High usage can sometimes become more expensive than traditional servers.

**Visual Description:** A warning-themed but professional layout, using subtle orange/yellow accent colors for the icons to contrast with the navy background.

**Question 10:**
*What is a cold start?*

**Speaker Notes:**
> "But it’s not perfect. A major issue is 'Cold Starts'. If a function hasn't been used in a while, it goes to sleep. Waking it up takes an extra second or two, causing a slight delay for the user. Also, you have execution limits—functions are meant for quick tasks, not hour-long processes.
> 
> **Question for the class:** What is a cold start?
> **Answer:** A cold start is the extra startup delay that may occur when a serverless environment needs to wake up and prepare before running."

---

## SLIDE 13 — TRADITIONAL SERVER VS SERVERLESS

**Title:** Traditional Server vs Serverless

**Content:**
**Traditional Server:**
* You manage the operating system and updates.
* The server runs continuously (24/7).
* You must configure and manage resources.
* Scaling requires manual setup and predicting traffic.

**Serverless Computing:**
* The cloud provider manages the infrastructure.
* Functions run only when triggered.
* Scaling is handled automatically.
* Developers focus entirely on the code.

**Visual Description:** A side-by-side comparison diagram. Left side shows a physical server rack with complex dials. Right side shows a clean, glowing cloud with a code icon inside.

**Question 11:**
*What is the main difference between a traditional server and serverless computing?*

**Speaker Notes:**
> "Comparing the two directly: A traditional server is like owning a car. You have to maintain it, park it, and pay for it even when you aren't driving. Serverless is like taking a taxi. You only pay for the exact trip, and the taxi company handles all the maintenance and driving.
> 
> **Question for the class:** What is the main difference between a traditional server and serverless computing?
> **Answer:** In traditional computing, the developer manages the server. In serverless, the cloud provider manages the underlying infrastructure."

---

## SLIDE 14 — CLOUD COMPUTING VS SERVERLESS COMPUTING

**Title:** Cloud Computing vs Serverless Computing

**Content:**
* **Cloud Computing:** The broader category. The delivery of any computing service over the internet (servers, storage, networking).
* **Serverless Computing:** A specific model *within* cloud computing where the provider manages the underlying servers for code execution.

**Visual Description:** A large circle labeled "Cloud Computing". Inside it, a smaller circle labeled "Serverless Computing". This visually demonstrates that serverless is a subset of cloud computing.

**Question 12:**
*Is serverless computing a type of cloud computing?*

**Speaker Notes:**
> "A common point of confusion is thinking cloud and serverless are two completely different things. They aren't. Cloud computing is the massive overarching category. Serverless computing is just one specific way to use the cloud.
> 
> **Question for the class:** Is serverless computing a type of cloud computing?
> **Answer:** Yes, it is a specific model within cloud computing."

---

## SLIDE 15 — REAL-WORLD SERVERLESS SERVICES

**Title:** Examples of Serverless Platforms

**Content:**
1. **AWS Lambda:** Runs code in response to events.
2. **Vercel:** Hosts web applications and runs serverless functions seamlessly.
3. **Google Cloud Functions:** Runs backend code without direct server management.
4. **Supabase:** Provides ready-made backend services (BaaS) like databases and auth.

**Visual Description:** Four professional cards featuring the logos/icons of AWS, Vercel, Google Cloud, and Supabase.

**Question 13:**
*Which service is an example of a platform that runs serverless functions?*

**Speaker Notes:**
> "Here are some of the biggest names in the industry. AWS Lambda and Google Cloud Functions are your classic FaaS providers. Vercel is highly popular for hosting modern websites that use serverless APIs. And Supabase is a fantastic example of a BaaS providing database services.
> 
> **Question for the class:** Which service on this list runs serverless functions?
> **Answer:** AWS Lambda (or Google Cloud Functions / Vercel)."

---

## SLIDE 16 — SDN PRIME APPLICATION

**Title:** Serverless Computing in SDN PRIME

**Scenario:** An admin adds a new news article to the website.

**Architecture Workflow:**
1. **Admin** submits a news article form.
2. The request goes to the **Vercel Serverless Backend Function**.
3. The function validates the data and sends it to the **Supabase Database**.
4. The database stores the article.
5. The public **SDN PRIME Website** displays the updated news.

**Visual Description:** A clean flowchart. Admin (User Icon) → Serverless Function (Vercel logo/icon) → Database (Supabase logo/icon) → Public Website (Globe Icon).

**Question 14:**
*How can serverless computing help an SDN PRIME website?*

**Speaker Notes:**
> "Let's apply this to a practical project, like the SDN PRIME website. If an admin wants to post news, they fill out a form. Instead of a traditional server, a Vercel serverless function catches that data, makes sure it's valid, and saves it into a Supabase database. 
> 
> **Question for the class:** How can serverless computing help an SDN PRIME website?
> **Answer:** It allows the site to run backend processes, like saving news, without requiring the student team to manually manage and pay for a 24/7 server."

---

## SLIDE 17 — WHEN SHOULD WE USE SERVERLESS?

**Title:** When Is Serverless a Good Choice?

**Content:**
**Great fit for Serverless:**
* APIs and Website backend functions.
* Form submissions and processing.
* Event-driven tasks (e.g., resizing an uploaded image).
* Small or unpredictable/changing workloads.

**Consider alternatives (Traditional Servers) for:**
* Long-running computational processes (hours of processing).
* Highly specialized or constant heavy workloads.

**Visual Description:** A split layout. The left side (Green checkmark) lists good fits. The right side (Grey circle/dash) lists alternatives.

**Question 15:**
*Give one example of an application task that can use serverless computing.*

**Speaker Notes:**
> "Serverless is amazing, but it isn't for everything. It is perfect for APIs, form submissions, and websites where traffic goes up and down. But if you are rendering a 3D movie that takes 10 hours of non-stop computing, a traditional dedicated server is a much better choice.
> 
> **Question for the class:** Give one example of a task that is good for serverless computing.
> **Answer:** An API request, form submission, or a website backend function."

---

## SLIDE 18 — KEY TAKEAWAYS

**Title:** What We Learned

**Content:**
1. Serverless is a specific cloud computing model.
2. Servers still exist, but the provider manages them.
3. FaaS (Function as a Service) runs your custom code.
4. BaaS (Backend as a Service) provides ready-made backend systems.
5. Serverless scales automatically and you pay for what you use.
6. It has limitations like "cold starts" and execution limits.

**Visual Description:** A clean summary checklist with subtle checkmark animations or bullet points.

**Speaker Notes:**
> "To wrap up our main concepts: Serverless means the cloud provider manages the servers. FaaS is for running code, BaaS is for backend services. It scales easily and saves money, but you do have to watch out for cold starts."

---

## SLIDE 19 — FINAL KNOWLEDGE CHECK

**Title:** Final Knowledge Check

**Content:**
1. **What is serverless computing?**
2. **What does FaaS stand for?**
3. **What does BaaS stand for?**
4. **Why is automatic scaling an advantage?**
5. **Is serverless computing the same thing as cloud computing?**

*(Answers will be revealed by the presenter)*

**Visual Description:** A quiz slide with the 5 questions listed clearly.

**Speaker Notes:**
> "Let's see what everyone remembers! 
> 1. What is serverless? (Answer: A cloud model where providers manage the servers.)
> 2. What does FaaS stand for? (Answer: Function as a Service.)
> 3. What does BaaS stand for? (Answer: Backend as a Service.)
> 4. Why is scaling an advantage? (Answer: It handles user traffic automatically.)
> 5. Is serverless the exact same as cloud computing? (Answer: No, cloud computing is the broader category, serverless is a model inside it.)"

---

## SLIDE 20 — THANK YOU / QUESTIONS

**Title:** Thank You!
**Subtitle:** Any Questions?

**Closing Quote:**
"Serverless computing helps developers focus on building applications while cloud providers manage the underlying infrastructure."

**Visual Description:** A clean professional closing visual, maintaining the dark navy and cyan theme, perhaps featuring a subtle glowing cloud icon in the center.

**Speaker Notes:**
> "Thank you all for listening. Serverless computing is truly the future of web development, allowing us to focus on writing great apps rather than managing hardware. Are there any questions?"
