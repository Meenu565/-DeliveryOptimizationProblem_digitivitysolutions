import pandas as pd
import heapq

def assign_deliveries(df):
    # Mapping priorities to numbers for easy sorting (High=1, Low=3)
    rank_map = {'High': 1, 'Medium': 2, 'Low': 3}
    df = df.copy()
    df['Rank'] = df['Priority'].map(rank_map)

    # Sort by priority first, then distance
    df_sorted = df.sort_values(by=['Rank', 'Distance']).reset_index(drop=True)

    # Track [total_distance, agent_name, tasks] in a heap to always find the free agent
    agents = [[0, "Agent 1", []], [0, "Agent 2", []], [0, "Agent 3", []]]
    heapq.heapify(agents)

    final_results = []
    counter = 1 

    for _, row in df_sorted.iterrows():
        current_km, name, tasks = heapq.heappop(agents)
        
        delivery = {
            "Order": f"#{counter:02d}",
            "Location": row['Location_ID'],
            "Priority": row['Priority'],
            "KM": row['Distance'],
            "Assigned To": name,
            "Agent Load Before": f"{current_km} km"
        }
        
        tasks.append(delivery)
        # Add task distance and put agent back in the heap
        heapq.heappush(agents, [current_km + row['Distance'], name, tasks])
        counter += 1

    for _, _, tasks in agents:
        final_results.extend(tasks)

    plan_df = pd.DataFrame(final_results).sort_values(by="Order")
    summary_df = pd.DataFrame([{"Agent": a[1], "Total KM": a[0]} for a in agents])

    return plan_df, summary_df