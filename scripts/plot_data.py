import csv
import pendulum
from datetime import datetime, timedelta

with open('status.csv', newline='') as f:
    reader = csv.reader(f)
    data = list(reader)

header, data = data[0], data[1:]

start_date = datetime.fromisoformat(data[0][1])
end_date = datetime.now()

def latest_data_on(date: datetime) -> tuple:
    # TODO: Get data on date 'date'. If no data on date then
    # return the first commit before it.
    # .strftime('%Y-%m-%d')

    latest = None
    for row in data:
        if date < datetime.fromisoformat(row[1]):
            break
        else:
            latest = (row[0], row[1], int(row[2]), int(row[3]))

    assert latest is not None
    return latest


days = (end_date - start_date).days
completed_list = []
todo_list = []

for d in range(days):
    date = start_date + timedelta(days=d)
    _, _, completed, todo = latest_data_on(date)
    completed_list.append(completed)
    todo_list.append(todo)


import matplotlib.pyplot as plt
# there are 490 exercises in abbott, not including the extras (section 8)
fig = plt.figure()
ax = fig.add_subplot()

ax.set_ylabel('Exercises')
ax.set_xlabel('Days')

plt.ylim(ymin=0, ymax=490)
plt.plot(completed_list)
plt.show()
