#! /usr/bin/env python3

from __future__ import print_function
import sys
from optparse import OptionParser
import random
# using copy module to prevent error
import copy

# to make Python2 and Python3 act the same -- how dumb
def random_seed(seed):
    try:
        random.seed(seed, version=1)
    except:
        random.seed(seed)
    return

parser = OptionParser()
parser.add_option("-s", "--seed", default=0, help="the random seed", action="store", type="int", dest="seed")
parser.add_option("-j", "--jobs", default=3, help="number of jobs in the system", action="store", type="int", dest="jobs")
parser.add_option("-l", "--jlist", default="", help="instead of random jobs, provide a comma-separated list of run times", action="store", type="string", dest="jlist")
parser.add_option("-m", "--maxlen", default=10, help="max length of job", action="store", type="int", dest="maxlen")
parser.add_option("-p", "--policy", default="FIFO", help="sched policy to use: SJF, FIFO, RR", action="store", type="string", dest="policy")
parser.add_option("-q", "--quantum", help="length of time slice for RR policy", default=1, action="store", type="int", dest="quantum")
parser.add_option("-c", help="compute answers for me", action="store_true", default=False, dest="solve")
# make option for arrivaltime
parser.add_option("-a", "--arrivaltime", default = "", help = "instead of random arrival time, provide arrival time of each job", action = "store", type="string", dest = "arrivaltime" )

(options, args) = parser.parse_args()

random_seed(options.seed)

print('ARG policy', options.policy)
if options.jlist == '':
    print('ARG jobs', options.jobs)
    print('ARG maxlen', options.maxlen)
    print('ARG seed', options.seed)
else:
    print('ARG jlist', options.jlist)
print('')

print('Here is the job list, with the run time of each job: ')

joblist = []

# make jlist to use at policy
# if jlist is not customized
if options.jlist == '':
    cnt = 0
    arrivetimelist= [] #list of arrivaltime
    # if arrivaltime is not customized
    if options.arrivaltime == '':
        for jobnum in range(0, options.jobs):
            # Make random arrivaltime
            arrivaltime = int(options.maxlen * random.random()) + 1
            arrivetimelist.append(float(arrivaltime))
    # if arrivaltime is customized
    else:
        for arrivetime in options.arrivaltime.split(','):
            arrivetimelist.append(float(arrivetime))
            cnt += 1

    # check arrivaltime is options.jobs(default = 3)
    if cnt == options.jobs:
        for jobnum in range(0,options.jobs):
            runtime = int(options.maxlen * random.random()) + 1
            arrivaltime = arrivetimelist[jobnum]
            joblist.append([jobnum, runtime, arrivaltime])
            print('  Job', jobnum, '( length = ' + str(runtime) + ' )', 
                '(arrive time = ' + str(arrivaltime), ')')
    # print error
    else:
        print('Error : please insert joblist or jobs')

# if there is a customized joblist
else:
    jobnum = 0 # number of job
    runtimelist= [] # list of runtime
    cnt = 0 # number of runtime(jlist)

    for runtime in options.jlist.split(','):
        # make runtimelist
        runtimelist.append(float(runtime))
        cnt +=1
    
    # if there is no arrival time then
    if options.arrivaltime == '':
        print('Error : There is no arrival time')
    else:
        for arr_time in options.arrivaltime.split(','):
            joblist.append([jobnum, runtimelist[jobnum], float(arr_time)])
            jobnum += 1
        # check the # of jlist and arrivaltime is same
        if (cnt==jobnum):
            for job in joblist:
                print('  Job', job[0], '( length = ' + str(job[1]) + ' )', 
                '( arrival time = ' + str(job[2]) + ')')
        else:
            print('Error : The number of jlist and arrivaltime is not matched')

print('\n')

# sort by arrived time
joblist.sort(key= lambda x:x[2])

# prevent error 
# using at final statistics
static_list = copy.deepcopy(joblist)
static_list.sort(key = lambda x : x[0])

if options.solve == True:
    print('** Solutions **\n')

    # new policy STCF
    if options.policy =='STCF':
        # sort by arrivetime, runtime
        joblist.sort(key= lambda x:(x[2],x[1]))

        print('Execution trace:')

        turnaround = {} # turnaround time to calculate later
        response = {} # response time to calculate later
        lastran = {} # recent ran time
        wait = {} # wait time to calculate later
        check = {} # check the job, which can run
        
        jobcount = len(joblist)
        for i in range(0,jobcount):
            lastran[i] = 0.0
            turnaround[i] = 0.0
            response[i] = -1
            # if check = -1 then job can run
            # if check= 0 then job cannot run
            check[i] = -1 
        
        # make copy list
        runlist = []
        for e in joblist:
            runlist.append(e)

        thetime  = joblist[0][2] # current time      
        next_time = 0 # next job's arrive time
        
        while 1:
            excute_list =[] # the job (arrivetime come)
            notnow_list = [] # the job (arrivetime doesn't come)
            for j in range(jobcount):
                jobnum = runlist[j][0]
                # make two lists seperately, I only run excute_list
                if(runlist[j][2] <= thetime) and (check[jobnum]== -1):
                    excute_list.append([jobnum, runlist[j][1], runlist[j][2]])
                elif(check[jobnum]== -1):
                    notnow_list.append([runlist[j][0], runlist[j][1], runlist[j][2]])
            
            if(len(notnow_list) != 0):
                notnow_list.sort(key = lambda x: (x[2], x[1]))
                # when next arrive time, we must compare each other
                next_time = notnow_list[0][2]
            else:
                next_time = 0
            
            # when next_time is exist
            if (next_time != 0) :
                if(len(excute_list) != 0):
                # only run shortest runtime job
                    excute_list.sort(key = lambda x : x[1])
                    jobnum = excute_list[0][0]
                    ranfor = next_time - excute_list[0][2]
                    runlist[jobnum][1] -= ranfor
                    if runlist[jobnum][1] == 0:
                        print('  [ time %.2f ] Run job %3d for %.2f secs ( DONE at %.2f )' 
                        % (thetime, jobnum, ranfor, thetime + ranfor))
                        
                        if check[jobnum] == -1:
                            response[jobnum] = thetime - excute_list[0][2]
                            check[jobnum] = 0
                        turnaround[jobnum] = thetime + ranfor - excute_list[0][2]

                    # change ranfor when minus
                    elif runlist[jobnum][1] <0:
                        runlist[jobnum][1] =0
                        ranfor = excute_list[0][1]
                        print('  [ time %.2f ] Run job %3d for %.2f secs ( DONE at %.2f )' 
                        % (thetime, jobnum, ranfor, thetime + ranfor))
                        if check[jobnum] == -1:
                            response[jobnum] = thetime - excute_list[0][2]
                            check[jobnum] = 0
                        turnaround[jobnum] = thetime + ranfor - excute_list[0][2]

                    # this job will run later
                    else:
                        print('  [ time %.2f ] Run job %3d for %.2f secs' 
                        % (thetime, jobnum, ranfor))
                        if response[jobnum] == -1:
                            response[jobnum] = thetime - excute_list[0][2]
                    # update thetime
                    thetime += ranfor

                # no notnow_list but, excute_list is exist
                # so we must run the job
                else:
                    notnow_list.sort(key = lambda x : x[1])
                    thetime = notnow_list[0][2]
                    jobnum = notnow_list[0][0]
                    if (len(notnow_list) >= 2):
                        ranfor = notnow_list[1][2] - notnow_list[0][2]
                    else:
                        ranfor = notnow_list[0][1]

                    runlist[jobnum][1] -= ranfor

                    if runlist[jobnum][1] == 0:
                        print('  [ time %.2f ] Run job %3d for %.2f secs ( DONE at %.2f )' 
                        % (thetime, jobnum, ranfor, thetime + ranfor))
                        # after run, we must finish the job
                        if check[jobnum] == -1:
                            response[jobnum] = thetime - excute_list[0][2]
                            check[jobnum] == 0
                        turnaround[jobnum] = thetime + ranfor - excute_list[0][2]

                    # change ranfor when minus
                    elif runlist[jobnum][1] <0:
                        runlist[jobnum][1] =0
                        ranfor = excute_list[0][1]
                        print('  [ time %.2f ] Run job %3d for %.2f secs ( DONE at %.2f )' 
                        % (thetime, jobnum, ranfor, thetime + ranfor))
                        if check[jobnum] == -1:
                            response[jobnum] = thetime - excute_list[0][2]
                            check[jobnum] = 0
                        turnaround[jobnum] = thetime + ranfor - excute_list[0][2]
                    
                    # this job will run later
                    else:
                        print('  [ time %.2f ] Run job %3d for %.2f secs' 
                        % (thetime, jobnum, ranfor))
                        if response[jobnum]== -1 :
                            response[jobnum] = thetime - excute_list[0][2]

                    thetime += ranfor

            # SJF again, there is no arrivetime
            else:
                while len(excute_list) !=0 :
                    excute_list.sort(key = lambda x: x[1])
                    job = excute_list.pop(0)
                    jobnum = job[0]
                    ranfor = job[1]
                    curr_arrivetime = job[2]
                    print('  [ time %.2f ] Run job %3d for %.2f secs ( DONE at %.2f )' 
                        % (thetime, jobnum, ranfor, thetime + ranfor))
                    if response[jobnum] == -1:
                        response[jobnum] = thetime - curr_arrivetime
                        check[jobnum] = 0
                    turnaround[jobnum] = thetime + ranfor - curr_arrivetime
                    thetime += ranfor
                break

        print()
        print('\nFinal statistics:')
        turnaroundSum = 0.0
        waitSum       = 0.0
        responseSum   = 0.0

        # using wait time = turnaroundtime - runtime
        for i in range(0,len(joblist)):
            turnaroundSum += turnaround[i]
            responseSum += response[i]
            wait[i] = turnaround[i] - static_list[i][1]
            waitSum += wait[i]
            print('  Job %3d -- Response: %3.2f  Turnaround %3.2f  Wait %3.2f' 
            % (i, response[i], turnaround[i], wait[i]))
        count = len(joblist)
        
        print('\n  Average -- Response: %3.2f  Turnaround %3.2f  Wait %3.2f\n' 
        % (responseSum/count, turnaroundSum/count, waitSum/count))
        

    if options.policy =='SJF':
        # sort by arrivetime, runtime
        joblist.sort(key= lambda x:(x[2],x[1]))
        print('Execution trace:')

        turnaround = {} # turnaround time to calculate later
        response = {} # response time to calculate later
        wait = {} # wait time to calculate later
        
        
        jobcount = len(joblist)
        for i in range(0,jobcount):
            turnaround[i] = 0.0
            response[i] = -1

        # make copy list
        runlist = []
        for e in joblist:
            runlist.append(e)
        
        thetime  = joblist[0][2] # current time      

        for i in range(jobcount):
            excute_list =[] # the job can run in thetime
            notnow_list = [] # job cannot be run in thetime
            for j in range(jobcount):
                jobnum = runlist[j][0]
                # make two lists seperately, I only run excute_list
                if(runlist[j][2] <= thetime) and (response[jobnum]== -1):
                    excute_list.append([jobnum, runlist[j][1], runlist[j][2]])
                elif(response[jobnum]== -1):
                    notnow_list.append([runlist[j][0], runlist[j][1], runlist[j][2]])
            
            if(len(excute_list) != 0):
                # only run shortest runtime job
                excute_list.sort(key = lambda x : x[1])
                jobnum = excute_list[0][0]
                ranfor = excute_list[0][1] # runtime
                print('  [ time %.2f ] Run job %3d for %.2f secs ( DONE at %.2f )' 
                    % (thetime, jobnum, ranfor, thetime + ranfor))
                # after run, we must finish the job
                response[jobnum] = thetime - excute_list[0][2]
                turnaround[jobnum] = thetime + ranfor - excute_list[0][2]
                thetime += ranfor

            # when thetime is smaller than arrivaltime    
            elif(len(excute_list) == 0):
                notnow_list.sort(key = lambda x : (x[2],x[1]))
                thetime = notnow_list[0][2]
                jobnum = notnow_list[0][0]
                ranfor = notnow_list[0][1]
                print('  [ time %.2f ] Run job %3d for %.2f secs ( DONE at %.2f )' 
                    % (thetime, jobnum, ranfor, thetime + ranfor))
                # after run, we must finish the job
                response[jobnum] = thetime - notnow_list[0][2]
                turnaround[jobnum] = thetime + ranfor - notnow_list[0][2]
                thetime += ranfor


        print()
        print('\nFinal statistics:')
        turnaroundSum = 0.0
        waitSum       = 0.0
        responseSum   = 0.0

        # waittime = responsetime
        for i in range(0,len(joblist)):
            turnaroundSum += turnaround[i]
            responseSum += response[i]
            wait[i] = response[i]
            waitSum += wait[i]
            print('  Job %3d -- Response: %3.2f  Turnaround %3.2f  Wait %3.2f' 
            % (i, response[i], turnaround[i], wait[i]))
        count = len(joblist)
        
        print('\n  Average -- Response: %3.2f  Turnaround %3.2f  Wait %3.2f\n' 
        % (responseSum/count, turnaroundSum/count, waitSum/count))
    
    
    if options.policy == 'FIFO':
    
        print('Execution trace:')
        # past_time is time when previous job is finished 
        past_time = 0
        # append job's first time
        first_time_list = []
        # append job's finish time 
        done_time_list = []
        for job in joblist:
            # 1st case, end time by previous job is larger than current arrvial time
            if ((past_time) >= job[2]):
                print('  [ time %.2f ] Run job %d for %.2f secs ( DONE at %.2f )'
            % (past_time, job[0], job[1], past_time + job[1]))
                first_time_list.append(past_time)
                past_time = past_time + job[1]
                done_time_list.append(past_time)

            # 2nd case, current arrival time is larger than end time by previous job
            else:
                print('  [ time %.2f ] Run job %d for %.2f secs ( DONE at %.2f )'
            % (job[2], job[0], job[1], job[2] + job[1]))
                first_time_list.append(job[2])
                past_time = job[2] + job[1]
                done_time_list.append(past_time)
        
                
        print('\nFinal statistics:')
        count = 0
        turnaroundSum = 0.0
        waitSum       = 0.0
        responseSum   = 0.0
        time_list =[]
        for tmp in joblist:
            jobnum  = tmp[0]
            runtime = tmp[1]
            arrivetime = tmp[2]
            first_time = first_time_list[count]
            done_time = done_time_list[count]
            
            response   = first_time - arrivetime
            turnaround = done_time - arrivetime
            wait       = response

            responseSum   += response
            turnaroundSum += turnaround
            waitSum       += wait
            count = count + 1
            
            time_list.append([jobnum,response, turnaround, wait])

        # sort by jobnum
        time_list.sort(key = lambda x:x[0])
        for time in time_list:
            print('  Job %3d -- Response: %3.2f  Turnaround %3.2f  Wait %3.2f' % (time[0], time[1], time[2], time[3]))
        print('\n  Average -- Response: %3.2f  Turnaround %3.2f  Wait %3.2f\n' 
        % (responseSum/count, turnaroundSum/count, waitSum/count))
    
             
    if options.policy == 'RR':
        print('Execution trace:')
        turnaround = {} # turnaround time to calculate later
        response = {} # response time to calculate later
        lastran = {} # recent ran time
        wait = {} # wait time to calculate later
        cnt = {} # to find the job which is the first time
        # quantum(time_slice) : default = 1
        quantum  = float(options.quantum)  
        jobcount = len(joblist)

        for i in range(0,jobcount):
            lastran[i] = 0.0
            turnaround[i] = 0.0
            response[i] = -1
            cnt[i] = 0
            wait[i] = 0

        # make copy list
        runlist = []
        for e in joblist:
            runlist.append(e)

        thetime  = joblist[0][2] # current time
        while jobcount > 0:
            # use queue
            job = runlist.pop(0)
            jobnum  = job[0]
            runtime = float(job[1])
            curr_arrivetime = float(job[2])
            
            # if job is not arrived yet, then skip this job
            if curr_arrivetime > thetime:
                runlist.append([jobnum, runtime, curr_arrivetime])
                continue

            # job is arrived
            else:
                if response[jobnum] == -1:
                    response[jobnum] = thetime - curr_arrivetime
                # job can run in whole quantum
                if runtime > quantum:
                    runtime -= quantum
                    ranfor = quantum
                    print('  [ time %.2f ] Run job %3d for %.2f secs' % (thetime, jobnum, ranfor))
                    runlist.append([jobnum, runtime, curr_arrivetime])

                # job can run only its runtime
                else:
                    ranfor = runtime;
                    print('  [ time %.2f ] Run job %3d for %.2f secs ( DONE at %.2f )' % (thetime, jobnum, ranfor, thetime + ranfor))
                    turnaround[jobnum] = thetime + ranfor - curr_arrivetime
                    jobcount -= 1
                thetime += ranfor
                lastran[jobnum] = thetime

        print()
        print('\nFinal statistics:')
        turnaroundSum = 0.0
        waitSum       = 0.0
        responseSum   = 0.0

        # there is some change
        # I use the formula wait_time = turnaround_time - runtime
        # so I don't use wait list

        for i in range(0,len(joblist)):
            turnaroundSum += turnaround[i]
            responseSum += response[i]
            wait[i] = turnaround[i] - static_list[i][1]
            waitSum += wait[i]
            print('  Job %3d -- Response: %3.2f  Turnaround %3.2f  Wait %3.2f' % (i, response[i], turnaround[i], wait[i]))
        count = len(joblist)
        
        print('\n  Average -- Response: %3.2f  Turnaround %3.2f  Wait %3.2f\n' % (responseSum/count, turnaroundSum/count, waitSum/count))

    if options.policy != 'FIFO' and options.policy != 'SJF' and options.policy != 'RR' and options.policy != 'STCF': 
        print('Error: Policy', options.policy, 'is not available.')
        sys.exit(0)
else:
    print('Compute the turnaround time, response time, and wait time for each job.')
    print('When you are done, run this program again, with the same arguments,')
    print('but with -c, which will thus provide you with the answers. You can use')
    print('-s <somenumber> or your own job list (-l 10,15,20 for example)')
    print('to generate different problems for yourself.')
    print('')
