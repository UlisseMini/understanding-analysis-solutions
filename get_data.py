from subprocess import check_output, check_call, STDOUT
from tqdm import tqdm

lines = check_output(['git', 'log', '--pretty=format:%H %as']).decode().split('\n')

commits = []
for commit, date in (line.split(' ') for line in lines):
    # stop 
    if commit == '8b456ea2ba2fe11dfc0bfde251035c9ff65e75c0':
        break
    commits.append((commit, date))


with open('status.csv', 'w') as f:
    print('commit,date,completed,todos', file=f)


for commit, date in tqdm(commits):
    check_output(['git', 'checkout', commit], stderr=STDOUT)
    awk_output = check_output(['sh', '-c', 'awk -f count-solutions.awk chapters/*/*.tex']).decode()
    completed, todos = awk_output.split(' ')

    with open('status.csv', 'a') as f:
        f.write(f'{commit},{date},{completed},{todos}')


check_output(['git', 'checkout', 'main'], stderr=STDOUT)
