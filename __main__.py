# FCFS is an algorithm to schudeling CPU processes by sorting the processes in a queue
# depending on the arrival time of the processes, if there are two or more processes have the same arrival time
# will be sorted in the order of entering the queue
# First Come First Served

import fcfs_wt as fcfs

# Excuted Program
if __name__ == '__main__':
    
    #read process file and the lines excluding the header line
    with open('processes.csv', 'r') as process_file:
        lines = process_file.readlines()
        lines.remove(lines[0])
    
    # Initiate a list for the queue
    process_queue = []
    
    # Iterate through line of the file
    for line in lines:
        # Split each line in CSV to the components (ID, Arrival Time, Burst Time) and append it to nested list
        # to create the process queue
        line = line.replace('\n','').split(",")
        # Change the times in line from string to float
        for i in [1,2]:
            line[i] = float(line[i])
        # Create the queue
        process_queue.append(line)
            
    # Number of Processes
    n = len(process_queue)

    # Calculate waiting time for each process and create a new process queue with the waiting time and print the table
    new_process_queue = fcfs.calc_waiting_time(process_queue, n)
    
    # Calculate the total waiting time and print it
    total_waiting_time = fcfs.calc_total_waiting_time(new_process_queue, n)
    
    # Calculate the average waiting time and print it
    average_waiting_time = fcfs.calc_avg_waiting_time(total_waiting_time, n)