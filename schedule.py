# Multi-level 8 Feedback Queue Scheduling
# Student: Dlo Jiwan Bagari
# id: 114702261
from Queue import Queue
from process import Process

class Schedule:

    def __init__(self):
        self.__currentPro = None
        self.__queues = [ Queue(i*2, i) for i in range(8)]
        # loop over each of the 8 queues 
        self.__process()

    def __run(self):
        # is true except for the very first process to be scheduled.
        if self.__currentPro is not None:
            position = currentPro.priority
            queue = self.__queues[position]
            process = currentPro
            # if process is requesting for I/O
            if process.blocking == 1:
                # save process state to block
                Q.getFirst()

                # if process is at the top level
                if position == 0:
                    queue.append(p)

                # if process is not at the top level
                else:
                    queues[position-1].append(p)

            # in all other cases, the process is marked as running
            else:
                #time for task has been used up
                process.quantumTime =-1
                #time has been completed
                process.time -=1
                # if the task has used up available quantum time
                if process.quantumTime <= 0:
                    # save process state
                    # remove from current queue
                    process.getFirst()
                    # and is not yet completed
                    if process.time > 0:
                        # add to next lowest queue
                        queues[position + 1].append(p)
                    # and is completed
                    else:
                        #  terminate process
                        pass
                # if quantum time is not complete but task is completed
                elif process.time <= 0:
                    queue.getFirst()
                    #terminate p
                #nothing to be done.
                else:
                    pass
                   
        
    def __process(self):
        for queue in enumerate(queues):
            if not queue.isEmpty():
                # assign CPU to first process in first nonempty queue
                self.__currentPro = Q.peek()
                #send p to CPU
                break
        ##send process to CPU, run the task
        self.__run()

