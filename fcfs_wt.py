# Function to calculate waiting time
def calc_waiting_time(process_queue, n):
    
    # sort the processes queue ascending by arrival time
    process_queue.sort(key = lambda process_queue:(process_queue[1]))

    # loop throug the processes starting from the second process as the first one has 0 waiting time
    # Calculate the waiting time of each process
    # If arrival time of the process is greater than the sum of arrival and burst time of the pervious process in the queue
    # then the process didn't wait in the queue and waiting time equals 0
    # Otherwise the waiting time equals the subtraction of the arrival time of the process
    # from the sum of arrival and burst time of the previous process
    
    # Waiting Time for the first process
    process_queue[0].append('0')
    
    # The loop to calculate and append each process waiting time
    for i in range (1,n):
        if process_queue[i][1] > process_queue[i-1][2]+process_queue[i-1][1]:
            waiting_time = 0
        else:        
            waiting_time = process_queue[i-1][2]+process_queue[i-1][1]-process_queue[i][1]
        process_queue[i].append(waiting_time)
    
    # Print table of the processes:
    print('Process_ID\tArrival_Time\tBurst_Time\tWaiting_Time')
    for i in range(n):
        print(process_queue[i][0],'\t\t',process_queue[i][1],'\t\t',process_queue[i][2],'\t\t',process_queue[i][3])
    
    #return the new processes queue with calculated waiting time
    return process_queue
    
def calc_total_waiting_time(new_process_queue, n):
    
    # Initiate a variable for the total waiting time
    total_waiting_time = 0
    
    # Summition of the total waiting times to calculate the total
    for i in range(1,n):
        total_waiting_time += new_process_queue[i][3]
    
    # Print total waiting time
    print('Total Waiting Time: {}'.format(total_waiting_time))
    
    # Return total waiting time
    return total_waiting_time

def calc_avg_waiting_time(total_waiting_time, n):
    
    #calculate average waiting time and print it
    avg_waiting_time = total_waiting_time / n
    print('The Average Waiting Time: {}'.format(avg_waiting_time))
