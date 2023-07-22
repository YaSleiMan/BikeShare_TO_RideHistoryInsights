from datetime import datetime


def cost_savings_calculator():
    # Read the text file and convert it into a list of lists
    dataset = []
    with open('Outputs/list_file.txt', 'r') as file:
        for line in file:
            elements = line.strip().split(',')
            dataset.append(elements)
    # print(dataset[0])
    # print(dataset[4])

    datetime_time = [datetime.strptime(time.strip(), '%m-%d-%Y %H:%M:%S') for time in dataset[0]]
    numeric_durations = [(dt.year * 365*30*24*60*60) + (dt.month * 30*24*60*60) + (dt.day * 24*60*60) + (dt.hour * 60*60) + (dt.minute * 60) + dt.second for dt in datetime_time]

    ebike_costs = sum([float(cost[9:]) for cost in dataset[4]])
    print("You spent this much on ebikes: $"+str(ebike_costs))

    ttc_trip_cost = 3.3         # Cost of a TTC ticket
    max_connection_time = 2     # Number of our hours you can wait before you have to buy another ticket
    bikeshare_subscription_cost = 120*1.13 + ebike_costs # Cost of yearly subscription to Toronto Bike Share + taxes + cost of ebike rides

    equivalent_ttc_tickets = 0
    for i in range(len(numeric_durations)-1):
        if numeric_durations[i+1] > (numeric_durations[i] + max_connection_time*60*60):
            equivalent_ttc_tickets = equivalent_ttc_tickets + 1

    savings = (ttc_trip_cost * equivalent_ttc_tickets) - bikeshare_subscription_cost
    if savings > 0:
        print("By using Toronto Bike Share you've saved at least $" + str(savings))
    else:
        print("You didn't take enough trips, you've lost $" + str(savings))

    return([savings,ebike_costs])

# Test
# cost_savings_calculator()