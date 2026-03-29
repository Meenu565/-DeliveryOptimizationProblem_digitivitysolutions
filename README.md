
---

```markdown
🚚 Logistics Delivery Optimizer: Priority & Workload Balancer

Project Overview

This project is an automated delivery dispatching tool designed to assign tasks to 3 agents. The goal is to handle urgent deliveries first while ensuring that no single agent is overloaded.

I used a Greedy Algorithm combined with a Min-Heap (Priority Queue) to balance the total travel distance across all agents efficiently.

---

📽️ Project Demo

> [!IMPORTANT]  
> 🔗 INSERT LINK TO YOUR VIDEO DEMO HERE  
*(Tip: Record a short clip showing CSV upload and dashboard usage.)*

---

📸 Dashboard Screenshots

| 📋 Optimized Delivery Plan | 📊 Workload Analytics |
|--------------------------|----------------------|
| ![Plan Screenshot](https://via.placeholder.com/400x220?text=Insert+Plan+Tab+Screenshot) | ![Analytics Screenshot](https://via.placeholder.com/400x220?text=Insert+Analytics+Tab+Screenshot) |

| 📈 Agent Deep-Dive | 📦 Dashboard Overview |
|------------------|---------------------|
| ![Deep Dive](https://via.placeholder.com/400x220?text=Insert+Deep-Dive+Tab+Screenshot) | ![Main UI](https://via.placeholder.com/400x220?text=Insert+Main+UI+Screenshot) |
<img width="1903" height="1057" alt="image" src="https://github.com/user-attachments/assets/e7039ed7-0620-46e4-8a1d-b83d7b3b5e32" />
<img width="1911" height="1073" alt="image" src="https://github.com/user-attachments/assets/1fc71db9-1765-4dff-a0a8-296257e09378" />
<img width="1908" height="1063" alt="image" src="https://github.com/user-attachments/assets/d0322b08-9c5c-47af-ba6c-71113e12fa42" />
<img width="1919" height="989" alt="image" src="https://github.com/user-attachments/assets/180178f9-9169-4126-a4da-d2d5af79f3b9" />
<img width="1896" height="1050" alt="image" src="https://github.com/user-attachments/assets/4418702d-273f-45dc-8fd9-ae0f6068131f" />

---

🧠 The Algorithm (How it Works)

1️⃣ Multi-Level Sorting

Before assignment:
- Primary Rule: Priority → High > Medium > Low  
- Secondary Rule: Distance → Shortest first within same priority  

---

2️⃣ Greedy Load Balancing using Min-Heap

A Min-Heap is used to track agent workload.

At each step:
- Select the agent with the least total distance  
- Assign next delivery  
- Update and push back into heap  

---

📌 Example Trace

| Order | Delivery | Agent Loads (A1, A2, A3) | Logic   | Result  |
|------ |---------|-------------------------- |---------|---------|
| #01   | 30km    | [0, 0, 0]                 | Pick A1 | A1 → 30 |
| #02   | 25km    | [30, 0, 0]                | Pick A2 | A2 → 25 |
| #03   | 20km    | [30, 25, 0]               | Pick A3 | A3 → 20 |
| #04   | 10km    | [30, 25, 20]              | Pick A3 | A3 → 30 |

Final Balance:
- Agent 1 → 30 km  
- Agent 2 → 25 km  
- Agent 3 → 30 km  

✔ Workload is evenly distributed

---

🛠️ Tech Stack

- Python → Core logic  
- Pandas → CSV handling  
- Streamlit → Dashboard  
- Plotly → Interactive charts  
- Heapq → Min-Heap implementation  

---

```
📂 Project Structure

```

delivery-optimizer/
├── app.py                # Streamlit app entry point
├── source/
│   ├── **init**.py      # Package initialization
│   ├── logic.py         # Core algorithm (sorting + heap)
│   └── ui.py            # Dashboard UI components
├── data/
│   └── sample_input.csv # Sample dataset
├── requirements.txt     # Dependencies
└── README.md            # Project documentation

````

---

🚀 Setup & Installation

1️⃣ Clone Repository

```bash
git clone https://github.com/Meenu565/-DeliveryOptimizationProblem_digitivitysolutions.git
cd delivery-optimizer
````

---

2️⃣ Create Virtual Environment

```bash
python -m venv .venv
```

Activate:

```bash
# Windows
.venv\Scripts\activate
```

---

3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

4️⃣ Run Application

```bash
streamlit run app.py
```

---

📊 Dashboard Features

Delivery Plan

* Shows assignment order
* Displays agent load before assignment

Workload Analytics

* Bar chart comparison
* Pie chart distribution

Agent Deep-Dive

* Priority distribution per agent
* Box plot for delivery spread

---

🎓 Conclusion

This project demonstrates how a Greedy Algorithm with Min-Heap can efficiently solve a real-world logistics problem.

By separating logic and UI:

* Code remains clean
* Scalable for future improvements

---

👤 Author

Name: Indhu Meenaakshi

Course: M.Sc Decision and Computing Sciences

---


---


