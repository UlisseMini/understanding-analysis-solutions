import csv
import pendulum
from datetime import datetime, timedelta

with open('status.csv', newline='') as f:
    reader = csv.reader(f)
    data = list(reader)

header, data = data[0], data[1:]

start_date = datetime.fromisoformat(data[0][1])
end_date = datetime.now()

def latest_data_on(date: datetime) -> list:
    # TODO: Get data on date 'date'. If no data on date then
    # return the first commit before it.
    # .strftime('%Y-%m-%d')

    latest = None
    for row in data:
        if date < datetime.fromisoformat(row[1]):
            break
        else:
            latest = row

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


print(completed_list)
import matplotlib.pyplot as plt
plt.plot(completed_list)
plt.savefig('foo.png')
plt.show()
