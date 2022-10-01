from numpy import random
from numpy import zeros
from numpy import sum
from numpy.ma import max


def arrivals(t):
  arrivals = []
  timeElapse = 0

  while timeElapse < t:
    timeElapse += random.poisson(10)
    if timeElapse <= t:
      arrivals.append(timeElapse)
    else:
      break

  return arrivals


def services(arrivals):
  # wait, begin, time spent, idle, service end, server
  services = zeros((len(arrivals), 6)) # array of zeros customer rows and 6 cols
  servers = [0, 0]

  for i in range(len(arrivals)):
    service = []
    if servers[0] <= servers[1]:
      server = 0
    else:
      server = 1

    # calc wait & begin
    if arrivals[i] < servers[server]:
      services[i][0] = servers[server] - arrivals[i]
      services[i][1] = servers[server]
    else:
      services[i][0] = 0
      services[i][1] = arrivals[i]
    # calc time spent, idle, service end, server used
    services[i][2] = services[i][0] + random.poisson(20)
    services[i][3] = services[i][1] - servers[server]
    services[i][4] = services[i][1] + services[i][2] - services[i][0]
    services[i][5] = server
    # set server
    servers[server] = services[i][4]
  
  return services

def simulation(t, sim_runs):
  # customers, wait, timespent, idle, overtime
  data = zeros((sim_runs, 5))

  for r in range(sim_runs):
    run_arrivals = arrivals(t)
    run_services = services(run_arrivals)
    data[r][0] = len(run_arrivals)
    run_sum = sum(run_services, axis = 0)
    data[r][1] = run_sum[0]
    data[r][2] = run_sum[2]
    data[r][3] = run_sum[3]
    data[r][4] = max(run_services, axis = 0)[4] - t

  data_sum = sum(data, axis = 0)

  return 'Total Customers: ' + str(data_sum[0]) + '\nAverage Customers per sim: ' + str(data_sum[0]/sim_runs) + '\nTotal Wait: ' + str(data_sum[1]) + '\nAverage Wait per cus: ' + str(data_sum[1]/data_sum[0]) + '\ntotal time spent: ' + str(data_sum[2]) + '\nAverage time spent per cus: ' + str(data_sum[2]/data_sum[0]) + '\ntotal idle: ' + str(data_sum[3]) + '\nAverage idle per sim: ' + str(data_sum[3]/sim_runs) + '\nTotal Overtime: ' + str(data_sum[4]) + '\nAverage Overtime per sim: ' + str(data_sum[4]/sim_runs)
  


  # print('Total Customers: ' + str(data_sum[0]))
  # print('Average Customers per sim: ' + str(data_sum[0]/sim_runs))
  # print('Total Wait: ' + str(data_sum[1]))
  # print('Average Wait per cus: ' + str(data_sum[1]/data_sum[0]))
  # print('total time spent: ' + str(data_sum[2]))
  # print('Average time spent per cus: ' + str(data_sum[2]/data_sum[0]))
  # print('total idle: ' + str(data_sum[3]))
  # print('Average idle per sim: ' + str(data_sum[3]/sim_runs))
  # print('Total Overtime: ' + str(data_sum[4]))
  # print('Average Overtime per sim: ' + str(data_sum[4]/sim_runs))

print(simulation(540, 1000))
