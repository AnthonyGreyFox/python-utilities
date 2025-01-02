import pandas as pd

data = pd.read_csv('data/report_intervals.csv')

df = pd.DataFrame(data)
df["CreatedOn"] = pd.to_datetime(df["CreatedOn"])
df["ProjectedComputeShutdown"] = pd.to_datetime(df["ProjectedComputeShutdown"])
df = df.sort_values("CreatedOn")

intervals = []
current_interval = None

for _, row in df.iterrows():
    if current_interval is None:
        current_interval = {"start": row["CreatedOn"], "end": row["ProjectedComputeShutdown"]}
    else:
        if row["CreatedOn"] <= current_interval["end"]:
            current_interval["end"] = max(current_interval["end"], row["ProjectedComputeShutdown"])
        else:
            intervals.append(current_interval)
            current_interval = {"start": row["CreatedOn"], "end": row["ProjectedComputeShutdown"]}

if current_interval is not None:
    intervals.append(current_interval)

# print(intervals)

intervals_df = pd.DataFrame(intervals)
intervals_df["duration"] = (intervals_df["end"] - intervals_df["start"]).dt.total_seconds() / 3600


agg_df = intervals_df.agg({"duration": ["sum", "mean", "max"]})

print(agg_df.head(5))

# total_uptime = sum((end - start).total_seconds() for start, end in intervals)
# total_uptime_minutes = total_uptime / 60

# print("Uptime Intervals:")
# for start, end in intervals:
#     print(f"Start: {start}, End: {end}")

# print(f"\nTotal Uptime: {total_uptime_minutes:.2f} minutes")