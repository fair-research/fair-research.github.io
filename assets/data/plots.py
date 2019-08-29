import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# Read CSV files
condor_date_parser = lambda date: pd.datetime.strptime(date, "%m/%d %H:%M:%S").replace(year=2018)
condor =  pd.read_csv("condor_wgsa.csv", parse_dates=["StartTime", "EndTime"], date_parser=condor_date_parser)
aws = pd.read_csv("aws_daily_i3.8xlarge_wgsa.csv", parse_dates=["UsageStartDate", "UsageEndDate"])
aws_condor = pd.read_csv("aws_condor.csv")


# Calculate the total cost of all spot instances and estimate a corresponding cost of On Demand instances.
# When jobs are executed on Spot instances, the jobs get evicted when Amazon terminates a Spot instance.
# It causes an addtional cost that has to be subtracted when estimating a cost of running jobs on On Demand instances.
i38xlarge_on_demand_price = 2.496
evicted_job_execution_time = condor[condor["Status"] == "evicted"].ExecutionTimeSeconds.sum()
completed_job_execution_time = condor[condor["Status"] == "terminated"].ExecutionTimeSeconds.sum()
print("Total evicted job execution time (sec): {}".format(evicted_job_execution_time))
print("Total completed job execution time (sec): {}".format(completed_job_execution_time))
unblended_cost = aws["UnblendedCost"].sum()
usage_amount = aws["UsageAmount"].sum()
print("Total i3.8xlarge Spot instance cost: ${:.2f}".format(unblended_cost))
print("Estimated i3.8xlarge On Demand instance cost: ${:.2f}". format(
        usage_amount * i38xlarge_on_demand_price *
        completed_job_execution_time / (evicted_job_execution_time + completed_job_execution_time)))


# Show terminated jobs aggregated by the number of RequestCpus
cst = pd.value_counts(condor.loc[condor["Status"] == "terminated"]["RequestCpus"].values)
#print("The number of completed jobs with different CPU allocation")
#print("CPUs\tJobs")
#print(cst.sort_index())
#cst.sort_index().plot.bar(title="Number of completed jobs with different CPU allocation")

# Show evicted jobs jobs aggregated by the number of RequestCpus
cse = pd.value_counts(condor.loc[condor["Status"] == "evicted"]["RequestCpus"].values)
#print("The number of evicted jobs with different CPU allocation")
#print("CPUs\tJobs")
#print(cse.sort_index())
#cse.sort_index().plot.bar(title="Number of jobs with with different CPU allocation)

pd.concat([cst, cse], axis=1).plot.bar()
plt.xlabel("Condor RequestCpus")
plt.ylabel("Number of Jobs")
plt.legend(["Completed Jobs", "Evicted Jobs"])


cpu1 = condor[(condor["Status"] == "terminated") & (condor["RequestCpus"] == 1)]
cpu1.hist(column="ExecutionTimeSeconds", bins=100, log=True)
plt.xlim(0, 250000)
plt.xlabel("Execution Time (sec)")
plt.ylabel("Number of 1 CPU Jobs")
plt.title("1 CPU Jobs")

cpu2 = condor[(condor["Status"] == "terminated") & (condor["RequestCpus"] == 2)]
cpu2.hist(column="ExecutionTimeSeconds", bins=100, log=True)
plt.xlim(0, 250000)
plt.xlabel("Execution Time (sec)")
plt.ylabel("Number of 2 CPU Jobs")
plt.title("2 CPU Jobs")

cpu4 = condor[(condor["Status"] == "terminated") & (condor["RequestCpus"] == 4)]
cpu4.hist(column="ExecutionTimeSeconds", bins=100, log=True)
plt.xlim(0, 250000)
plt.xlabel("Execution Time (sec)")
plt.ylabel("Number of 4 CPU Jobs")
plt.title("4 CPU Jobs")

cpu6 = condor[(condor["Status"] == "terminated") & (condor["RequestCpus"] == 6)]
cpu6.hist(column="ExecutionTimeSeconds", bins=100, log=True)
plt.xlim(0, 250000)
plt.xlabel("Execution Time (sec)")
plt.ylabel("Number of 6 CPU Jobs")
plt.title("6 CPU Jobs")

cpu16 = condor[(condor["Status"] == "terminated") & (condor["RequestCpus"] == 16)]
cpu16.hist(column="ExecutionTimeSeconds", bins=100, log=True)
plt.xlim(0, 250000)
plt.xlabel("Execution Time (sec)")
plt.ylabel("Number of 16 CPU Jobs")
plt.title("16 CPU Jobs")

cpu32 = condor[(condor["Status"] == "terminated") & (condor["RequestCpus"] == 32)]
cpu32.hist(column="ExecutionTimeSeconds", bins=100, log=True)
plt.xlim(0, 250000)
plt.xlabel("Execution Time (sec)")
plt.ylabel("Number of 32 CPU Jobs")
plt.title("32 CPU Jobs")

terminated = condor[condor["Status"] == "terminated"]
terminated.hist(column="ExecutionTimeSeconds", bins=100, log=True)
plt.xlim(0, 250000)
plt.xlabel("Execution Time (sec)")
plt.ylabel("Number of Completed Jobs")
plt.title("Successfully Completed Jobs")

evicted = condor[condor["Status"] == "evicted"]
evicted.hist(column="ExecutionTimeSeconds", bins=100, log=True)
plt.xlim(0, 250000)
plt.xlabel("Execution Time (sec)")
plt.ylabel("Number of Evicted Jobs")
plt.title("Evicted Jobs")


# Number of active Spot instances (Oct 19-31)
start_count = aws.UsageStartDate.value_counts()
end_count = aws.UsageEndDate.value_counts()
df = pd.concat([start_count, end_count], axis=1, keys=["UsageStartDate", "UsageEndDate"])
df.fillna(0, inplace=True)
df["diff"] = df["UsageStartDate"] - df["UsageEndDate"]
counts = df["diff"].resample("5min").sum().fillna(0).cumsum()
plt.figure()
ax = counts.plot()

# Number of evicted Condor jobs
start_count_evicted = condor[condor["Status"] == "evicted"].StartTime.value_counts()
end_count_evicted = condor[condor["Status"] == "evicted"].EndTime.value_counts()
df_evicted = pd.concat([start_count_evicted, end_count_evicted], axis=1, keys=["StartTime", "EndTime"])
df_evicted.fillna(0, inplace=True)
df_evicted["diff"] = df_evicted["StartTime"] - df_evicted["EndTime"]
counts_evicted = df_evicted["diff"].resample("5min").sum().fillna(0).cumsum()
counts_evicted.plot(ax=ax)

# Number of completed Condor jobs
start_count_completed = condor[condor["Status"] == "terminated"].StartTime.value_counts()
end_count_completed = condor[condor["Status"] == "terminated"].EndTime.value_counts()
df_completed = pd.concat([start_count_completed, end_count_completed], axis=1, keys=["StartTime", "EndTime"])
df_completed.fillna(0, inplace=True)
df_completed["diff"] = df_completed["StartTime"] - df_completed["EndTime"]
counts_completed = df_completed["diff"].resample("5min").sum().fillna(0).cumsum()
counts_completed.plot(ax=ax)
plt.ylim(0, 1600)
plt.xlabel("Date")
plt.ylabel("Number of Active Spot Instances/Number of Condor Jobs")
plt.legend(["Active Spot Instances", "Evicted Condor Jobs", "Successfully Completed Condor Jobs"])


plt.show()

