from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication,  QWidget, QTableWidget, QTableWidgetItem, QVBoxLayout
import sys
# ------------------------Sho8l Seka ----------------------

import tkinter as tk
from tkinter import ttk
from tkinter.ttk import *


class App(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.CreateUI()
        self.LoadTable()
        self.grid(sticky = (N,S,W,E))
        parent.grid_rowconfigure(0, weight = 1)
        parent.grid_columnconfigure(0, weight = 1)

    def CreateUI(self):
        tv = Treeview(self)
        tv['columns'] = ('limit', 'base', )
        tv.heading("#0", text='Sources', anchor='w')
        tv.column("#0", anchor="w")
        tv.heading('limit', text='limit')
        tv.column('limit', anchor='center', width=100)
        tv.heading('base', text='base')
        tv.column('base', anchor='center', width=100)

        tv.grid(sticky = (N,S,W,E))
        self.treeview = tv
        self.grid_rowconfigure(0, weight = 1)
        self.grid_columnconfigure(0, weight = 1)

    def LoadTable(self):
        self.treeview.insert('', 'end', text="First", values=('10:00',
                             '10:10'))
        self.treeview.insert('', 'end', text="First", values=('10:00',
                                                              '10:10'))

def gant_chart(list1, time_list, waiting_time):
    import matplotlib.pyplot as plt

    fig, gnt = plt.subplots()
    # out_p=["a","b","c","d","f","g","h"]
    # out_time=[0,15,30,50,57,70,77,90 ]

    out_edited = [((200 / time_list[len(time_list) - 1]) * x) for x in time_list]
    print(out_edited)
    colors = ["green", "red", "blue"]

    for i in range(0, len(list1)):
        index = i
        gnt.broken_barh([(out_edited[index], out_edited[index + 1] - out_edited[index])], (15, 9),
                        facecolors='tab:{}'.format(colors[index % 3]))
        plt.text(x=((out_edited[index + 1] + out_edited[index]) / 2), y=20, s=list1[index], size=13)

    plt.text(x=100, y=40, s="avg waiting time is :{}".format(waiting_time), size=20)
    gnt.set_ylim(0, 50)
    gnt.set_xlim(0, 200)

    gnt.set_xlabel('seconds since start')
    gnt.set_ylabel('Processor')

    gnt.set_yticks([15])
    gnt.set_yticklabels([""])
    gnt.set_xticks(out_edited)
    gnt.set_xticklabels(time_list)

    gnt.grid(True)
    plt.show()


def Time1(time):
    Q = round(time, 1)
    return Q


def CheckArrive(Time, ArriveTime):
    if ArriveTime <= Time:
        return True
    else:
        return False


def InputSjfPreemptive():
    Process = processes_id
    NoOfProcesses = num_of_processes
    ArrivalT = arrival_time
    Burst = burst_time
    RemainingTime = []
    for i in range(NoOfProcesses):
        RemainingTime.append(round(float(Burst[i]), 1))

    return NoOfProcesses, Process, ArrivalT, Burst, RemainingTime


def SJFPreemptive(NoOfProcesses, Process, ArrivalT, Burst, RemainingTime):
    ProcessIn = []
    TimeIn = []
    zyadat = []
    min = 10000
    AA = 0
    index = 0
    while AA < NoOfProcesses:
        zyadat.append(1000)
        AA += 1
    mgmo3Elzyadat = 0
    TotalWaitingTime = 0
    for i in range(NoOfProcesses):
        for x in range(i + 1, NoOfProcesses):
            if ((float(ArrivalT[i]) + float(Burst[i])) < float(ArrivalT[x])):
                if ((float(ArrivalT[x]) - (float(ArrivalT[i]) + float(Burst[i]))) < zyadat[i]):
                    zyadat[i] = float(ArrivalT[x]) - (float(ArrivalT[i]) + float(Burst[i]))
    for i in range(NoOfProcesses):
        if float(ArrivalT[i]) < min:
            min = float(ArrivalT[i])
            index = i
    if min > 0:
        mgmo3Elzyadat += min

    for i in range(NoOfProcesses):
        if (zyadat[i] < 1000):
            mgmo3Elzyadat += zyadat[i]

    Time = 0
    TimeAfter = 0
    i = 0
    z = 0
    flag = 0
    TotalBurst = 0
    while z < NoOfProcesses:
        TotalBurst += float(Burst[z])
        z += 1
    TotalBurst += mgmo3Elzyadat
    TrueIndex = index
    while Time1(Time) <= TotalBurst:
        while i < 100000:
            if (CheckArrive(TimeAfter, float(ArrivalT[TrueIndex])) == True and flag == 1):
                TimeIn.append(Time1(Time))
                ProcessIn.append("Null")
                flag = 0

            elif (CheckArrive(TimeAfter, float(ArrivalT[TrueIndex]))) == True and (RemainingTime[TrueIndex] > 0.11):
                flag1 = 0
                counter = 0
                while counter < (len(Process)):
                    if (CheckArrive(Time1(Time), float(ArrivalT[counter])) == True) and (
                            RemainingTime[counter] < RemainingTime[TrueIndex]) and (RemainingTime[counter] > 0):
                        ProcessIn.append(Process[TrueIndex])
                        TimeIn.append(Time1(Time))
                        if ((TimeIn[len(TimeIn) - 1] == TimeIn[len(TimeIn) - 2]) and len(TimeIn) > 1):
                            ProcessIn.pop()
                            TimeIn.pop()
                        # print(Process[TrueIndex])
                        # print(Time1(Time))
                        flag1 = 1
                        IndexProcessOfLeastBurst = counter
                        TrueIndex = IndexProcessOfLeastBurst
                        TimeAfter = Time1(Time)
                    elif (CheckArrive(Time1(Time), float(ArrivalT[counter])) != True) or (
                            RemainingTime[counter] > RemainingTime[TrueIndex] or (len(Process) == 1)):
                        if flag1 != 1:
                            IndexProcessOfLeastBurst = TrueIndex

                    counter += 1
                RemainingTime[IndexProcessOfLeastBurst] -= 0.1
                RemainingTime1 = ['%.1f' % elem for elem in RemainingTime]
                # print(RemainingTime1[IndexProcessOfLeastBurst])
                Time += round(0.1, 1)

                i += 1

            elif (CheckArrive(TimeAfter, float(ArrivalT[TrueIndex]))) == True and (
                    -0.1 <= RemainingTime[TrueIndex] <= 0.12):
                # print(Process[TrueIndex]+" is finished")
                Time += 0.1
                ProcessIn.append(Process[TrueIndex])
                TimeIn.append(Time1(Time))
                ProcessWaitingTime = (Time1(Time)) - round(float(ArrivalT[TrueIndex]), 1) - round(
                    float(Burst[TrueIndex]), 1)
                # print(("Process Waiting time is: ")+str(Time1(ProcessWaitingTime)))
                TotalWaitingTime += ProcessWaitingTime
                del Process[TrueIndex]
                del ArrivalT[TrueIndex]
                del Burst[TrueIndex]
                del RemainingTime[TrueIndex]
                del RemainingTime1[TrueIndex]
                i += 1
                TrueIndex = 0
                TimeAfter = Time1(Time)
                if (len(Process) == 0):
                    break

            elif (CheckArrive(TimeAfter, float(ArrivalT[TrueIndex])) == False):
                flag = 1
                Time += 0.1
                Time = Time1(Time)
                TimeAfter = Time1(Time)
        if (len(Process) == 0):
            break
    # for b in range(len(ProcessIn)):
    #     print(ProcessIn[b])
    #     print(TimeIn[b])

    AvgWaitingTime = TotalWaitingTime / NoOfProcesses
    return ProcessIn, TimeIn, AvgWaitingTime
    # print(("total AVG waiting time: ") + str(AvgWaitingTime))


def InputSjfNonPreemptive():
    NoOfProcesses = int(input())  # "Enter the no. of processes: "
    Process = []
    ArrivalT = []
    Burst = []
    for i in range(NoOfProcesses):
        data = input()  # Enter the process,arrival time,burst time
        X = data.split(',')
        Process.append(X[0])
        ArrivalT.append(X[1])
        Burst.append(X[2])

    return NoOfProcesses, Process, ArrivalT, Burst


def SJFNonPreemptive(NoOfProcesses, Process, ArrivalT, Burst):
    zyadat = []
    ProcessIn = []
    TimeIn = []
    flag = 0
    AA = 0
    index = 0
    min = 10000
    while AA < NoOfProcesses:
        zyadat.append(1000)
        AA += 1
    mgmo3Elzyadat = 0
    TotalWaitingTime = 0
    for i in range(NoOfProcesses):
        for x in range(i + 1, NoOfProcesses):
            if (float(ArrivalT[i]) + float(Burst[i]) < float(ArrivalT[x])):
                if ((float(ArrivalT[x]) - (float(ArrivalT[i]) + float(Burst[i]))) < zyadat[i]):
                    zyadat[i] = float(ArrivalT[x]) - (float(ArrivalT[i]) + float(Burst[i]))

    for i in range(NoOfProcesses):
        if float(ArrivalT[i]) < min:
            min = float(ArrivalT[i])
            index = i
    if min > 0:
        mgmo3Elzyadat += min

    for i in range(NoOfProcesses):
        if (zyadat[i] < 1000):
            mgmo3Elzyadat += zyadat[i]

    Time = 0
    TotalBurst = 0
    z = 0
    while z < NoOfProcesses:
        TotalBurst += float(Burst[z])
        z += 1
    TotalBurst += mgmo3Elzyadat
    TrueIndex = index
    while Time <= TotalBurst:
        while i < 100000:
            if (CheckArrive(Time, float(ArrivalT[TrueIndex])) == True and flag == 1):
                TimeIn.append(Time1(Time))
                ProcessIn.append("Null")
                flag = 0
            elif (CheckArrive(Time, float(ArrivalT[TrueIndex])) == True):
                flag1 = 0
                counter = 0
                while counter < len(Process):
                    if (CheckArrive(Time, float(ArrivalT[counter])) == True and float(Burst[counter]) < float(
                            Burst[TrueIndex])):
                        flag1 = 1
                        IndexProcessOfLeastBurst = counter
                        TrueIndex = IndexProcessOfLeastBurst
                    else:
                        if flag1 != 1:
                            IndexProcessOfLeastBurst = TrueIndex
                    counter += 1

                i += 1
                Time += float(Burst[TrueIndex])
                ProcessIn.append(Process[TrueIndex])
                TimeIn.append(Time1(Time))
                # print(Time)
                # print(Process[TrueIndex]+" is finshed")
                ProcessWaitingTime = (Time1(Time)) - round(float(ArrivalT[TrueIndex]), 1) - round(
                    float(Burst[TrueIndex]), 1)  # print(("Process Waiting time is: ")+str(ProcessWaitingTime))
                TotalWaitingTime += ProcessWaitingTime
                del Process[TrueIndex]
                del ArrivalT[TrueIndex]
                del Burst[TrueIndex]
                TrueIndex = 0
                if (len(Process) == 0):
                    break
            elif (CheckArrive(Time, float(ArrivalT[TrueIndex])) == False):
                flag = 1
                Time += 0.1
                Time = Time1(Time)
        if (len(Process) == 0):
            break
    # for b in range(len(ProcessIn)):
    # print(ProcessIn[b])
    # print(TimeIn[b])
    AvgWaitingTime = TotalWaitingTime / NoOfProcesses
    # print(("total AVG waiting time: ") + str(AvgWaitingTime))
    return ProcessIn, TimeIn, AvgWaitingTime


# ------------------sh8l hassan----------------------------
def RR_With_arrival_input(no_pro, arr, time_slice):
    no_pro = no_pro  # int(input ("Enter the num of proccess"))
    bigger_list = []
    smaller_list = []

    total_time = 0

    for iterator in range(0, no_pro):
        smaller_list = arr[iterator].split(
            ",")  # input("please input the time and arraival time of the process sperated by comma ").split(",")  #here we take the input as list
        smaller_list.append("0")  # waiting
        smaller_list.append("0")  # case
        smaller_list.append("0")  # last finish

        smaller_list = [int(i) for i in smaller_list]
        smaller_list.insert(0, str("p{}".format(iterator)))  # here we write the name of each processor

        total_time = total_time + int(smaller_list[1])
        bigger_list.append(smaller_list)  # here we make list of lists

    time_slice = time_slice  # int(input ("decide the time slice "))

    return time_slice, bigger_list, no_pro


############################


def ROUND_ROBIN(time_slice, bigger_list, no_pro):
    queue = []
    out_time = []
    out_queue = []
    waiting_time_name = []
    waiting_time_val = []
    turn_around_queue = []
    current_time = 0

    bigger_list.sort(key=lambda x: x[2])

    out_time.append(current_time)

    i = 0
    while (i + 1 != len(bigger_list)):  # here we puttin the proccess that reached at the second zero into the queue

        if (bigger_list[i][2] == 0):
            queue.append(bigger_list[i])
            bigger_list.pop(i)
            i = i - 1
        i = i + 1

    while (len(queue) != 0 or len(bigger_list) != 0):

        if (len(
                queue) == 0):  #### this while to handle the issue if the processor was idle for a time it fill the queue again with the next one
            bigger_list.sort(key=lambda x: x[2])
            element = bigger_list[0]
            while (True):
                queue.append(bigger_list[0])

                current_time = bigger_list[0][2]
                bigger_list.pop(0)
                if (len(bigger_list) == 0):
                    break
                if (current_time != bigger_list[0][2]):
                    break
            out_queue.append("null")
            out_time.append(current_time)

        chosen_val = queue[0][1]

        if (time_slice < chosen_val):  # lw el ba2i fl time bta3 el process is more  than the time slice or equal
            if (queue[0][4] == 0):
                queue[0][4] = queue[0][4] + 1
                queue[0][3] = current_time - queue[0][2]

            else:
                queue[0][3] = queue[0][3] + current_time - queue[0][5]

            current_time = current_time + time_slice  # here we increase current_time by time slice
            queue[0][5] = current_time
            out_time.append(current_time)
            queue[0][
                1] = chosen_val - time_slice  # here we update the chosen  value after decreasing time slice from it
            out_queue.append(queue[0][0])
            # print(queue[0][0])
            flag_trminated = False



        elif (time_slice == chosen_val or time_slice > chosen_val):
            if (time_slice == chosen_val):
                if (queue[0][4] == 0):
                    queue[0][4] = queue[0][4] + 1
                    queue[0][3] = current_time - queue[0][2]

                else:
                    queue[0][3] = queue[0][3] + current_time - queue[0][5]

                current_time = current_time + time_slice  # here we decrese every process py "el ba2i fiha " after excucuting it
                queue[0][5] = current_time
                out_time.append(current_time)
                queue[0][1] = chosen_val - time_slice
                out_queue.append(queue[0][0])
                # print(queue[0][0])
                waiting_time_name.append(queue[0][0])
                waiting_time_val.append(queue[0][3])
                turn_around_queue.append(queue[0][5] - queue[0][2])
                queue.pop(0)
                flag_trminated = True

            elif (time_slice > chosen_val):
                if (queue[0][4] == 0):
                    queue[0][4] = queue[0][4] + 1
                    queue[0][3] = current_time - queue[0][2]

                else:
                    queue[0][3] = queue[0][3] + current_time - queue[0][5]

                current_time = current_time + chosen_val  # here we decrese every process py "el ba2i fiha " after excucuting it
                queue[0][5] = current_time
                out_time.append(current_time)
                queue[0][1] = 0
                out_queue.append(queue[0][0])
                # print(queue[0][0])
                waiting_time_name.append(queue[0][0])
                waiting_time_val.append(queue[0][3])
                turn_around_queue.append(queue[0][5] - queue[0][2])
                queue.pop(0)
                flag_trminated = True

        while (len(bigger_list) and current_time >= bigger_list[0][2]):
            queue.append(bigger_list[0])
            bigger_list.pop(0)

        if (flag_trminated == False):
            the_completed_process = queue[0]
            queue.pop(0)
            queue.append(the_completed_process)
    total_waiting = 0
    total_turnaround = 0
    for i in range(0, len(waiting_time_name)):
        total_waiting = waiting_time_val[i] + total_waiting
        total_turnaround = turn_around_queue[i] + total_turnaround
    avg_waiting = (total_waiting / no_pro)
    avg_turn = (total_turnaround / no_pro)
    return out_queue, out_time, waiting_time_name, waiting_time_val, turn_around_queue, avg_waiting, avg_turn


def piriority_with_RR_input(no_pro, arr, time_slice):
    time_slice = time_slice

    no_pro = no_pro  # int(input ("Enter the num of proccess"))
    bigger_list = []
    total_time = 0
    smaller_list = []

    for iterator in range(0, no_pro):
        smaller_list = arr[iterator].split(
            ",")  # input("please input the time  and arraival time and piriority of the process sperated by comma ").split(",")  #here we take the input as list
        smaller_list.append(0)
        smaller_list.append(0)
        smaller_list.append(0)
        smaller_list = [int(i) for i in smaller_list]
        smaller_list.insert(0, str("p{}".format(iterator)))  # here we write the name of each processor

        total_time = total_time + int(smaller_list[1])
        bigger_list.append(smaller_list)  # here we make list of lists

    return time_slice, bigger_list, no_pro, total_time


def same_piriority(queue):
    same_piriority_queue = []
    for i in range(1, len(queue)):
        if (queue[0][3] == queue[i][3]):

            same_piriority_queue.append(queue[i])
            if (len(same_piriority_queue) == 1):
                same_piriority_queue.insert(0, queue[0])

    return same_piriority_queue


def piriority_with_RR(time_slice, bigger_list, no_pro, total_time):
    current_time = 0
    queue = []
    out_time = []
    out_queue = []
    waiting_time_name = []
    waiting_time_val = []
    turn_around_queue = []

    bigger_list.sort(key=lambda x: x[2])

    i = 0
    while (i != len(bigger_list)):  # here we puttin the proccess that reached at the second zero into the queue

        if (bigger_list[i][2] == 0):
            queue.append(bigger_list[i])
            bigger_list.pop(i)
            i = i - 1
        i = i + 1
    # same_piriority(queue)

    while (current_time != total_time):
        if (current_time == 0):
            out_time.append(0)

        while (len(bigger_list) and current_time >= bigger_list[0][2]):
            queue.append(bigger_list[0])
            bigger_list.pop(0)

        queue.sort(key=lambda x: x[3])

        if (len(
                queue) == 0):  #### this while to handle the issue if the processor was idle for a time it fill the queue again with the next one
            bigger_list.sort(key=lambda x: x[2])
            element = bigger_list[0]
            while (True):
                queue.append(bigger_list[0])

                current_time = bigger_list[0][2]
                bigger_list.pop(0)

                if (element[2] != bigger_list[0][2]):
                    break;
            out_queue.append("null")
            out_time.append(current_time)

        if (len(same_piriority(queue))):

            same_piriority_queue = same_piriority(queue)
            length_of_same_piriority_queue = len(same_piriority_queue)

            while (len(same_piriority_queue)):

                chosen_val = same_piriority_queue[0][1]

                if (
                        time_slice < chosen_val):  # lw el ba2i fl time bta3 el process is more  than the time slice or equal
                    if (queue[0][5] == 0):
                        same_piriority_queue[0][5] = same_piriority_queue[0][5] + 1
                        same_piriority_queue[0][4] = current_time - same_piriority_queue[0][2]

                    else:
                        same_piriority_queue[0][4] = same_piriority_queue[0][4] + current_time - \
                                                     same_piriority_queue[0][6]

                    current_time = current_time + time_slice  # here we increase current_time by time slice
                    out_time.append(current_time)
                    # waiting_time_val.append(same_piriority_queue[0][4])
                    # waiting_time_name.append(same_piriority_queue[0][0])
                    # turn_around_queue.append(current_time-same_piriority_queue[0][2])
                    same_piriority_queue[0][6] = current_time
                    same_piriority_queue[0][
                        1] = chosen_val - time_slice  # here we update the chosen  value after decreasing time slice from it
                    out_queue.append(same_piriority_queue[0][0])
                    # print(same_piriority_queue[0][0])
                    flag_trminated = False



                elif (time_slice == chosen_val or time_slice > chosen_val):

                    if (queue[0][5] == 0):
                        same_piriority_queue[0][5] = same_piriority_queue[0][5] + 1
                        same_piriority_queue[0][4] = current_time - same_piriority_queue[0][2]

                    else:
                        same_piriority_queue[0][4] = same_piriority_queue[0][4] + current_time - \
                                                     same_piriority_queue[0][6]

                    if (time_slice == chosen_val):

                        current_time = current_time + time_slice  # here we decrese every process py "el ba2i fiha " after excucuting it
                        out_time.append(current_time)
                        waiting_time_val.append(same_piriority_queue[0][4])
                        waiting_time_name.append(same_piriority_queue[0][0])
                        turn_around_queue.append(same_piriority_queue[0][6] - same_piriority_queue[0][2])
                        same_piriority_queue[0][6] = current_time
                        same_piriority_queue[0][1] = chosen_val - time_slice
                        out_queue.append(same_piriority_queue[0][0])
                        # print(same_piriority_queue[0][0])

                        same_piriority_queue.pop(0)
                        flag_trminated = True


                    elif (time_slice > chosen_val):

                        current_time = current_time + chosen_val
                        out_time.append(current_time)
                        waiting_time_name.append(same_piriority_queue[0][0])
                        waiting_time_val.append(same_piriority_queue[0][4])
                        turn_around_queue.append(same_piriority_queue[0][6] - same_piriority_queue[0][2])
                        same_piriority_queue[0][6] = current_time
                        same_piriority_queue[0][1] = 0
                        out_queue.append(same_piriority_queue[0][0])
                        # print(same_piriority_queue[0][0])
                        same_piriority_queue.pop(0)
                        flag_trminated = True

                if (flag_trminated == False):
                    the_completed_process = same_piriority_queue[0]
                    same_piriority_queue.pop(0)
                    same_piriority_queue.append(the_completed_process)

            for i in range(0, length_of_same_piriority_queue):
                queue.pop(0)

        else:
            waiting_time_name.append(queue[0][0])
            waiting_time_val.append(current_time - queue[0][2])
            current_time = current_time + queue[0][1]
            out_time.append(
                current_time)  # here is different from RR_WITH arrivel as we out time [] is printed before adding current time
            turn_around_queue.append(current_time - queue[0][2])
            queue[0][6] = current_time
            out_queue.append(queue[0][0])
            # print(queue.pop(0))
            queue.pop(0)

    total_waiting = 0
    total_turnaround = 0
    for i in range(0, len(waiting_time_name)):
        total_waiting = waiting_time_val[i] + total_waiting
        total_turnaround = turn_around_queue[i] + total_turnaround

    avg_waiting = (total_waiting / no_pro)
    avg_turn = (total_turnaround / no_pro)

    return out_queue, out_time, waiting_time_name, waiting_time_val, turn_around_queue, avg_waiting, avg_turn


#############################################################################################

def findWaitingTime_fcfs(processes, n, bt, wt, at):
    service_time = [0] * n
    service_time[0] = 0
    wt[0] = 0
    j = 0
    m = 0

    for i in range(0, n - 1):
        for j in range(i + 1, n):
            if (int(at[i]) > int(at[j])):
                temp1 = int(at[i])
                at[i] = int(at[j])
                at[j] = temp1
                temp2 = int(bt[i])
                bt[i] = int(bt[j])
                bt[j] = temp2

    for i in range(1, n):

        service_time[i] = service_time[i - 1] + int(bt[i - 1])

        wt[i] = service_time[i] - int(at[i])
        # If waiting time for a process is in
        # negative that means it is already
        # in the ready queue before CPU becomes
        # idle so its waiting time is 0
        if (wt[i] < 0):
            wt[i] = 0
            service_time[i] = service_time[i] + 1


def findTurnAroundTime_fcfs(processes, n, bt, wt, tat):
    for i in range(n):
        tat[i] = int(bt[i]) + wt[i]


def findavgTime_Fcfs(processes, n, bt, at):
    wt = [0] * n
    tat = [0] * n
    final_p = []
    t = 0
    m = 0
    tem = []
    arr = []
    sortee = 0

    for i in range(0, n - 1):
        sortee = 1
        for j in range(i + 1, n):
            if (int(at[i]) > int(at[j])):
                temp1 = int(at[i])
                at[i] = int(at[j])
                at[j] = temp1
                temp2 = int(bt[i])
                bt[i] = int(bt[j])
                bt[j] = temp2
                temp3 = processes[i]
                processes[i] = processes[j]
                processes[j] = temp3
    # if(sortee==1):
    # for i in range(1,n):
    # if((int(at[i-1])+int(bt[i-1]))<int(at[i])):
    # at[i]=int(at[i-1])+int(bt[i-1])

    for i in range(1, n):

        if ((int(at[i - 1]) + int(bt[i - 1]) - int(at[i])) < 0):
            tem.append(i)
            t = t + 1
            # arr.insert(i,at[i-1]+bt[i-1])

    # print(t)
    # for i in range(0,len(tem)):
    # print(tem[i])
    final_p = processes.copy()
    arr = at.copy()
    for i in range(0, t):
        final_p.insert(tem[m] + i, 'null')
        m = m + 1

    findWaitingTime_fcfs(processes, n, bt, wt, at)
    findTurnAroundTime_fcfs(processes, n, bt, wt, tat)

    # print("Processes   Burst Time   Arrival Time     Waiting","Time   Turn-Around Time  Completion Time \n")
    total_wt = 0
    total_tat = 0
    slice_time = []
    arrival = []
    k = 0
    for i in range(n):
        total_wt = total_wt + int(wt[i])
        total_tat = total_tat + tat[i]
        compl_time = tat[i] + int(at[i])
        slice_time.append(compl_time)
        arrival.append(at[i])

    #### 3shan azbt l arrival fl sorting
    if (sortee == 1):
        for i in range(1, n):
            if ((int(arr[i - 1]) + int(bt[i - 1])) > int(arr[i])):
                arr[i] = int(arr[i - 1]) + int(bt[i - 1])
    tt = 0
    mm = 1
    for i in range(1, n):

        if ((int(at[i - 1]) + int(bt[i - 1]) - int(at[i])) < 0):
            # tem.append(i)
            # t = t + 1
            arr.insert(i + tt, slice_time[i - mm])
            slice_time.insert(i + tt, at[i])
            tt = tt + 1
            mm = mm - 1

    # print(" ", i + 1, "\t\t", bt[i], "\t\t", at[i], "\t\t", wt[i], "\t\t ", tat[i], "\t\t ", compl_time)

    # print("Average waiting time = %.5f " % (total_wt / n))

    # print("\nAverage turn around time = ", total_tat / n)
    for i in range(0, n + t):
        final_p[i] = "p" + str(final_p[i])
    return total_wt / int(n), final_p, slice_time, arr


import tkinter
from tkinter import *
from tkinter import ttk

num_of_processes = 0
quantum = 0
processes_id = []
burst_time = []
arrival_time = []
priority = []
type = "NONE"

def quit_function():
    global type
    type = "QUIT"
    window.destroy()

def exit_function():
    window.destroy()


def BuSaveData():
    global num_of_processes
    global processes_id
    global burst_time
    global arrival_time
    global priority
    global quantum
    num_of_processes = int(EntryNumberOfProcesses.get())
    processes_id = EntryID.get()
    processes_id = processes_id.split(',')
    quantum = EntryQuantum.get()
    burst_time = EntryBurstTime.get()
    burst_time = burst_time.split(',')
    arrival_time = EntryArrivalTime.get()
    arrival_time = arrival_time.split(',')
    priority = EntryPriority.get()
    priority = priority.split(',')
    EntryArrivalTime.delete(0, 'end')
    EntryBurstTime.delete(0, 'end')
    EntryID.delete(0, 'end')
    EntryQuantum.delete(0, 'end')
    EntryPriority.delete(0, 'end')
    EntryNumberOfProcesses.delete(0, 'end')
    print(num_of_processes)
    print(quantum)
    print(processes_id)
    print(priority)
    print(burst_time)
    print(arrival_time)


def PP():
    global type
    type = "PP"
    page2text.pack_forget()
    page1text.pack_forget()
    page5btn.pack_forget()
    page2btn.pack_forget()
    page3btn.pack_forget()
    page4btn.pack_forget()
    page6btn.pack_forget()
    page9btn.pack_forget()
    ttk.Label(window, text="Number of processes: ").pack()
    EntryNumberOfProcesses.pack()
    ttk.Label(window, text="Processes ID: ").pack()
    EntryID.pack()
    ttk.Label(window, text="Priority: ").pack()
    EntryPriority.pack()
    ttk.Label(window, text="Burst Time: ").pack()
    EntryBurstTime.pack()
    ttk.Label(window, text="Arrival Time: ").pack()
    EntryArrivalTime.pack()
    buSubmit.pack()
    page7btn.pack()
    #page8btn.pack()
    page9btn.pack()


def PNP():
    global type
    type = "PriorityWithRoundRobbin"
    page2text.pack_forget()
    page1text.pack_forget()
    page1btn.pack_forget()
    page5btn.pack_forget()
    page3btn.pack_forget()
    page4btn.pack_forget()
    page6btn.pack_forget()
    page9btn.pack_forget()
    ttk.Label(window, text="Number of processes: ").pack()
    EntryNumberOfProcesses.pack()
    ttk.Label(window, text="Quantum: ").pack()
    EntryQuantum.pack()
    ttk.Label(window, text="Priority: ").pack()
    EntryPriority.pack()
    ttk.Label(window, text="Burst Time: ").pack()
    EntryBurstTime.pack()
    ttk.Label(window, text="Arrival Time: ").pack()
    EntryArrivalTime.pack()
    buSubmit.pack()
    page7btn.pack()
    #page8btn.pack()
    page9btn.pack()


def RR():
    global type
    type = "RR"
    page2text.pack_forget()
    page1text.pack_forget()
    page1btn.pack_forget()
    page2btn.pack_forget()
    page5btn.pack_forget()
    page4btn.pack_forget()
    page6btn.pack_forget()
    page9btn.pack_forget()
    ttk.Label(window, text="Number of processes: ").pack()
    EntryNumberOfProcesses.pack()
    ttk.Label(window, text="Quantum: ").pack()
    EntryQuantum.pack()
    ttk.Label(window, text="Burst Time: ").pack()
    EntryBurstTime.pack()
    ttk.Label(window, text="Arrival Time: ").pack()
    EntryArrivalTime.pack()
    buSubmit.pack()
    page7btn.pack()
    #page8btn.pack()
    page9btn.pack()


def SjfPreemptive():
    global type
    type = "SjfPreemptive"
    page2text.pack_forget()
    page1text.pack_forget()
    page1btn.pack_forget()
    page2btn.pack_forget()
    page3btn.pack_forget()
    page5btn.pack_forget()
    page6btn.pack_forget()
    page9btn.pack_forget()
    ttk.Label(window, text="Number of processes: ").pack()
    EntryNumberOfProcesses.pack()
    ttk.Label(window, text="Processes ID: ").pack()
    EntryID.pack()
    ttk.Label(window, text="Burst Time: ").pack()
    EntryBurstTime.pack()
    ttk.Label(window, text="Arrival Time: ").pack()
    EntryArrivalTime.pack()
    buSubmit.pack()
    page7btn.pack()
    #page8btn.pack()
    page9btn.pack()


def SjfNonPreemptive():
    global type
    type = "SjfNonPreemptive"
    page2text.pack_forget()
    page1text.pack_forget()
    page1btn.pack_forget()
    page2btn.pack_forget()
    page3btn.pack_forget()
    page4btn.pack_forget()
    page6btn.pack_forget()
    page9btn.pack_forget()
    ttk.Label(window, text="Number of processes: ").pack()
    EntryNumberOfProcesses.pack()
    ttk.Label(window, text="Processes ID: ").pack()
    EntryID.pack()
    ttk.Label(window, text="Burst Time: ").pack()
    EntryBurstTime.pack()
    ttk.Label(window, text="Arrival Time: ").pack()
    EntryArrivalTime.pack()
    buSubmit.pack()
    page7btn.pack()
    #page8btn.pack()
    page9btn.pack()
    # page9btn.pack()


def FCFS():
    global type
    type = "FCFS"
    page2text.pack_forget()
    page1text.pack_forget()
    page1btn.pack_forget()
    page2btn.pack_forget()
    page3btn.pack_forget()
    page4btn.pack_forget()
    page5btn.pack_forget()
    page9btn.pack_forget()
    ttk.Label(window, text="Number of processes: ").pack()
    EntryNumberOfProcesses.pack()
    ttk.Label(window, text="Processes ID: ").pack()
    EntryID.pack()
    ttk.Label(window, text="Burst Time: ").pack()
    EntryBurstTime.pack()
    ttk.Label(window, text="Arrival Time: ").pack()
    EntryArrivalTime.pack()
    buSubmit.pack()
    page7btn.pack()
    #page8btn.pack()
    page9btn.pack()
    # page9btn.pack()


class PriorityWithPreemptive:

    def input_process_data(self, n):
        processes_data = []
        for i in range(0, n):
            temp = []
            _process_id = processes_id[i]
            _arrival_time = int(arrival_time[i])
            _burst_time = int(burst_time[i])
            _priority_ = int(priority[i])

            temp.extend([_process_id, _arrival_time, _burst_time, _priority_, 0, _burst_time,
                         _arrival_time])  # 0 is the state of the process
            processes_data.append(temp)

        seq_of_processes, waiting_time = PriorityWithPreemptive.scheduling(self, processes_data)
        return seq_of_processes, waiting_time

    def turnaround_time(self, processes_data):
        total_around_time = 0
        for i in range(len(processes_data)):
            turn_around_time = processes_data[i][7] - processes_data[i][1]  # compilation - arrival
            total_around_time = total_around_time + turn_around_time
            processes_data[i].append(turn_around_time)
        average_turnaround_time = total_around_time / len(processes_data)
        return average_turnaround_time

    def waiting_time(self, processes_data):
        total_waiting_time = 0
        for i in range(len(processes_data)):
            waiting_time = processes_data[i][7] - processes_data[i][1] - processes_data[i][5]  # turnaround - burst
            total_waiting_time = total_waiting_time + waiting_time
            processes_data[i].append(waiting_time)
        average_waiting_time = total_waiting_time / len(processes_data)
        return average_waiting_time

    def scheduling(self, processes_data):
        time = 0
        start_times = []  # may use it for gantt chart
        exit_times = []
        seq_of_processes = []
        processes_data.sort(key=lambda x: x[1])  # sort processes with arrival_time
        while 1:
            ready_processes = []
            not_ready_processes = []  # processes which haven't been arrived yet
            temp = []
            '''
            for i in range(len(processes_data)):
                if time > processes_data[i][6] + 10 and processes_data[i][4] == 0:
                    processes_data[i][3] -= 1
                    processes_data[i][6] += 10
            '''

            for i in range(len(processes_data)):
                if processes_data[i][1] <= time and processes_data[i][4] == 0:
                    ready_processes.append((processes_data[i]))
                elif processes_data[i][4] == 0:
                    not_ready_processes.append(processes_data[i])

            if len(ready_processes) == 0 and len(not_ready_processes) == 0:
                break
            if len(ready_processes) != 0:
                ready_processes.sort(key=lambda x: x[3])  # sort according to priority
                start_times.append(time)
                time = time + 1
                exit_times.append(time)
                seq_of_processes.append(ready_processes[0][0])
                for k in range(len(processes_data)):
                    if processes_data[k][0] == ready_processes[0][0]:
                        break
                processes_data[k][2] = processes_data[k][2] - 1
                if processes_data[k][2] == 0:
                    processes_data[k][4] = 1
                    processes_data[k].append(time)
            if len(ready_processes) == 0:
                not_ready_processes.sort(key=lambda x: x[1])
                if time < not_ready_processes[0][1]:
                    seq_of_processes.append("NULL");
                    # time = not_ready_processes[0][1]
                # if there is no processes in ready we can jump to the first processes in not ready with time = arrival
                # start_times.append(time)
                time = time + 1
                # exit_times.append(time)
                # seq_of_processes.append(not_ready_processes[0][0])
                # for k in range(len(processes_data)):
                #   if processes_data[k][0] == not_ready_processes[0][0]:
                #      break
                # processes_data[k][2] = processes_data[k][2] - 1
                # if processes_data[k][2] == 0:
                #   processes_data[k][4] = 1
                #  processes_data[k].append(time)

        turnaround_time = PriorityWithPreemptive.turnaround_time(self, processes_data)
        waiting_time = PriorityWithPreemptive.waiting_time(self, processes_data)
        PriorityWithPreemptive.print_data(self, processes_data, turnaround_time, waiting_time, seq_of_processes)
        return seq_of_processes, waiting_time

    def print_data(self, processes_data, average_turnaround_time, average_waiting_time, seq_of_processes):
        processes_data.sort(key=lambda x: x[0])

        print(
            "Process_ID  Arrival_Time  Rem_Burst_Time   Priority        Completed  Orig_Burst_Time fakeattival_Time  Completion_Time  Turnaround_Time  Waiting_time")
        for i in range(len(processes_data)):
            for j in range(len(processes_data[i])):
                print(processes_data[i][j], end="				")
            print()

        print(f'Average Turnaround Time: {average_turnaround_time}')

        print(f'Average Waiting Time: {average_waiting_time}')

        print(f'Sequence of Process: {seq_of_processes}')

    # PriorityWithPreemptive.Gantt_chart(self, seq_of_processes)


while (1):
    window = tkinter.Tk()
    root = Tk()
    App(root)


    # style
    style = ttk.Style()
    style.theme_use('classic')
    style.configure('TLabel', backgorund="#e1d8b2")
    style.configure('TButton', backgorund="#e1d8b2")
    page1text = tkinter.Label(window, text="Schedular Type: ")
    page1text.pack()
    page1btn = tkinter.Button(window, text="PriorityPreemptive", command=PP)
    page2btn = tkinter.Button(window, text="PriorityNonPreemptive", command=PNP)
    page3btn = tkinter.Button(window, text="RoundRobin", command=RR)
    page4btn = tkinter.Button(window, text="SjfPreemptive", command=SjfPreemptive)
    page5btn = tkinter.Button(window, text="SjfNonPreemptive", command=SjfNonPreemptive)
    page6btn = tkinter.Button(window, text="FCFS", command=FCFS)
    page7btn = tkinter.Button(window, text="RUN", command=exit_function)
    #page8btn = tkinter.Button(window, text="Choose another schdular", command=exit_function)
    page9btn = tkinter.Button(window, text="exit", command=quit_function)
    page9btn.config(height=1, width=6)
    page7btn.config(height=1, width=6)
    # page9btn = tkinter.Button(window, text="Gantt Chart", command=gantt_chart)

    ###

    # Processes Data
    EntryNumberOfProcesses = ttk.Entry(window, width=30, font=('Arial', 16))
    EntryPriority = ttk.Entry(window, width=30, font=('Arial', 16))
    EntryArrivalTime = ttk.Entry(window, width=30, font=('Arial', 16))
    EntryBurstTime = ttk.Entry(window, width=30, font=('Arial', 16))
    EntryID = ttk.Entry(window, width=30, font=('Arial', 16))
    EntryQuantum = ttk.Entry(window, width=30, font=('Arial', 16))
    buSubmit = ttk.Button(window, text="Submit")
    buSubmit.config(command=BuSaveData)
    ###

    page2text = tkinter.Label(window, text="This is page 2")

    page1btn.pack()
    page2btn.pack()
    page3btn.pack()
    page4btn.pack()
    page5btn.pack()
    page6btn.pack()
    page9btn.pack()

    window.mainloop()
    root.mainloop()


    ###
    if type == "QUIT":
        break
    elif type == "PP":
        no_of_processes = num_of_processes
        print(no_of_processes)
        prio = PriorityWithPreemptive()
        seq_of_processes, waiting_time = prio.input_process_data(no_of_processes)
        times = [None] * (len(seq_of_processes) + 1)
        times[0] = 0
        for i in range(1, len(seq_of_processes) + 1):
            times[i] = i
        print(seq_of_processes)
        processes = [None] * len(seq_of_processes)
        j, k = 0, 0
        while j < len(seq_of_processes):
            k = j
            while k < len(seq_of_processes):
                if seq_of_processes[j] == seq_of_processes[k]:
                    k = k + 1
                else:
                    break
            processes.append(seq_of_processes[j])
            j = k

        processes = [elem for elem in processes if elem != None]
        # print(processes)

        from itertools import groupby

        a = [len(list(group)) for key, group in groupby(seq_of_processes)]
        # print(f"a:{a}")
        for l in range(1, len(a)):
            a[l] = a[l] + a[l - 1]
        # print(a)

        # print(waiting_time)
        # print(times)
        a.insert(0, 0)
        print(a)

        gant_chart(processes, a, waiting_time)
    elif type == "SjfNonPreemptive":
        # NoOfProcesses, Process, ArrivalT, Burst = InputSjfNonPreemptive()
        ProcessIn, TimeIn, AvgWaitingTime = SJFNonPreemptive(num_of_processes, processes_id, arrival_time, burst_time)
        # --------------------------------For Testing Only---------------------------------
        #
        print(ProcessIn)
        TimeIn.insert(0, 0)
        print(TimeIn)
        print(("total AVG waiting time: ") + str(AvgWaitingTime))
        gant_chart(ProcessIn, TimeIn, AvgWaitingTime)
    elif type == "SjfPreemptive":
        NoOfProcesses, Process, ArrivalT, Burst, RemainingTime = InputSjfPreemptive()
        ProcessIn, TimeIn, AvgWaitingTime = SJFPreemptive(NoOfProcesses, Process, ArrivalT, Burst, RemainingTime)

        # --------------------------------For Testing Only---------------------------------
        print(ProcessIn)
        TimeIn.insert(0, 0)
        print(TimeIn)
        print(("total AVG waiting time: ") + str(AvgWaitingTime))
        gant_chart(ProcessIn, TimeIn, AvgWaitingTime)

    elif type == "FCFS":
        processes_FCFS = []
        time_FCFS = []
        arrival_FCFS = []
        a, processes_FCFS, time_FCFS, arrival_FCFS = findavgTime_Fcfs(processes_id, num_of_processes, burst_time,
                                                                      arrival_time)
        time_FCFS = list(map(int, time_FCFS))
        # print(time_FCFS) # a = waiting time
        # print(processes_FCFS)
        time_FCFS.insert(0, 0)
        gant_chart(processes_FCFS, time_FCFS, a)

    elif type == "RR":
        bigger_list0 = [None] * num_of_processes
        for i in range(0, num_of_processes):
            bigger_list0[i] = str(burst_time[i]) + "," + str(arrival_time[i])
        for i in range(0, num_of_processes):
            print(bigger_list0[i])
        print(bigger_list0)
        time_slice, bigger_list, no_pro = RR_With_arrival_input(int(num_of_processes), bigger_list0, int(quantum))
        list1, list2, list3, list4, list5, avgwaiting, avgturn = ROUND_ROBIN(time_slice, bigger_list, no_pro)
        gant_chart(list1, list2, avgwaiting)

    elif type == "PriorityWithRoundRobbin":
        bigger_list0 = [None] * num_of_processes
        for i in range(0, num_of_processes):
            bigger_list0[i] = str(burst_time[i]) + "," + str(arrival_time[i]) + "," + str(priority[i])
        time_slice, bigger_list, no_pro, total_time = piriority_with_RR_input(int(num_of_processes), bigger_list0,
                                                                              int(quantum))
        list1, list2, list3, list4, list5, avgwaiting, avgturn = piriority_with_RR(time_slice, bigger_list, no_pro,
                                                                                   total_time)
        gant_chart(list1, list2, avgwaiting)