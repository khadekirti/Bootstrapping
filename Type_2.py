
import pandas as pd
import os
import numpy as np
import heapq
import matplotlib.pyplot as plt
# Get the data
df = pd.read_csv('data_orIginal.csv')
# Set the number of counters
n=4
# Get the queue for all the counters
queue = {0: [] , 1 : [] , 2 : [] , 3 : [] } ######################################################## ########################################################
# Create a class object defining the system state
# counter_id will tell which counter will the customer prefer depending on the lenght of the queue # arrival_time is the time of arrival
# event_type is the state of the customer, namely "Arrived" or "Departure"
# all_containers_start, all_containers_end : A list to currate the start time and end time

class state:
	def __init__(self, arrival_time, event_type, counter_id, all_containers_start, all_containers_end ):
		# Arrivalt time
		self.m_arrival_time = arrival_time self.m_event_type = event_type self.m_counter_id = counter_id self.m_all_containers_start = all_containers_start self.m_all_containers_end = all_containers_end
	def Print(self):
		print(self.m_arrival_time, self.m_counter_id , (",self.m_event_type,"))

######################################################## ########################################################
# This is for priority queue priorityQueue = []
# All done events
ell = []
# FLAG container if occupied counter = [0 for _ in range(n)] #indicates the current time t_current = 0
# Create first object
interval_ = np.random.choice(df['inter_arrival_time'], size= 1, replace=True)[0] # Get the data
t_current += interval_
data = state(t_current , "ARRIVAL", 0,[-1] * n, [-1] * n)
# push the entry in the queue s heapq.heappush(priorityQueue,(t_current,data))
while(t_current < 3000 ):
	# Get the object in the priority queue
	obj = heapq.heappop(priorityQueue)
	# the event details
	event = obj[1]
	t_current = obj[0]
	# If arrival 
	######################################################## 
	######################################################## 
	if (event.m_event_type) == "ARRIVAL":
	# identify the counter that has shortest queues
	len_ = [len(value) for key, value in queue.items()]
	# shortest queue includes the customer in the counter as well for i in range(len(len_)):
	len_[i] += counter[i]
	counter_ = len_.index(min(len_))
	event.m_counter_id = counter_
	# For the object that has arrived, check if the counter is free or not if counter[event.m_counter_id] == 0:
	# make it busy
	counter[event.m_counter_id] = 1
	# mark the event as done
	event.m_event_type = "DONE"
	# change the counter start time and end time
	event.m_all_containers_start[event.m_counter_id] = t_current event.m_all_containers_end[event.m_counter_id] = t_current + np.random.choice(df['service_time']) heapq.heappush(priorityQueue,(event.m_all_containers_end[event.m_counter_id] ,event))
	# if the counter is busy, move the object to the list else:
	queue[event.m_counter_id].append(event)
	 ######################################################## 
	 # During the arrival we stimulate the arrival of others


	 inter_arrival = np.random.choice(df['inter_arrival_time'])
 # Get the next time
 t_next = t_current + inter_arrival
 #Choose a counter depending on the length of the queue
 len_ = [len(value) for key, value in queue.items()]
 for i in range(len(len_)):
 len_[i] += counter[i]
 counter_ = len_.index(min(len_))
 data = state(t_next, "ARRIVAL", counter_ , [-1] * n ,[-1] * n)
 # push to the queue
 heapq.heappush(priorityQueue,(t_next ,data))
 ########################################################
 ########################################################
 # At departute
 elif (event.m_event_type) == "DONE":
 # Add events to the list
 ell.append(event)
 # Free the counter
 counter[event.m_counter_id] = 0
 # If list is the queue is greater than 0,
 if(len(queue[event.m_counter_id])!=0):
 counter[event.m_counter_id] = 1
 # get the first customer in the queue
 queue_waiting = queue[event.m_counter_id].pop(0)
 # Set the event as
 queue_waiting.m_event_type = "DONE"
 queue_waiting.m_all_containers_start[event.m_counter_id] = t_current
 queue_waiting.m_all_containers_end[event.m_counter_id] = t_current +
np.random.choice(df['service_time'])
 # push the event to priority queue
 heapq.heappush(priorityQueue,(queue_waiting.m_all_containers_end[event.m_counter_id]
,queue_waiting))
 else:
 print("ERROR") 


 ########################################################
#######################################################
# Get the waiting time
all_waiting_time = []
for i in range(len(ell)):
 waiting_time = ell[i].m_all_containers_start[ell[i].m_counter_id] - ell[i].m_arrival_time
 all_waiting_time.append(waiting_time)
########################################################
#######################################################
# Get the edcf plot
import statsmodels.api as sm # recommended import according to the docs
import matplotlib.pyplot as plt
sample = all_waiting_time
ecdf = sm.distributions.ECDF(sample)
x = np.linspace(min(sample), max(sample))
y = ecdf(x)
plt.step(x, y)
plt.plot( [8] * 50 , np.linspace(min(y), max(y)))
plt.title('ECDF #Counter = 4', fontsize=20) 


plt.xlabel('waiting time', fontsize=18)
plt.ylabel('F(x)', fontsize=16)
plt.show()
########################################################
#######################################################
# To esttimate the mean and the standard deviation, we have
N = len(all_waiting_time)
all_probability = []
for i in range(1,N):
 # get 100 random index
 batch = np.random.choice(all_waiting_time , size = 100, replace= True)
 if (len(batch)) != 0:
 # Get the probability
 all_probability.append(len([i for i in batch if i <= 8])/len(batch))

tmean = np.mean(all_probability)
tstd = np.std(all_probability)
print(np.percentile(all_probability,2.5) , np.percentile(all_probability,97.5)) 

