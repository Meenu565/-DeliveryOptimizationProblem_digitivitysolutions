
---

```markdown
🚚 Logistics Delivery Optimizer: Priority & Workload Balancer

Project Overview

This project is an automated delivery dispatching tool designed to assign tasks to 3 agents. The goal is to handle urgent deliveries first while ensuring that no single agent is overloaded.

I used a Greedy Algorithm combined with a Min-Heap (Priority Queue) to balance the total travel distance across all agents efficiently.

---
## 📸 Dashboard Preview

![Churn Distribution](Results/img1.png)

![Model Comparison](Results/img2.png)

![ROC Curves](Results/img3.png)

![Confusion Matrices](Results/img4.png)

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


