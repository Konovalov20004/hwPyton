def rem():
    data = open('Te.txt', 'r')
    a = input()
    x = (data.read()).split('\n')
    for i in range(len(x)):
        if a in x[i].split(' '):
            print(x[i])
            print('change - c, delete - d, skip - enter')
            move = input()
            if move == 'c':
                change(x, i)
                record(x)
            if move == 'd':
                delete(x, i)
                print(x)
                record(x)
    data.close()

def change(x, i):
    print('Change ' + x[i])
    x[i] = input()
    return(x)

def delete(x, i):
    print('Delete')
    a = i
    for a in range(len(x) - 1):
        x[i] = x[i + 1]
    return(x)

def record(x):
    data = open('Te.txt', 'w')
    data = open('Te.txt', 'a')
    for i in x:
        y = data.write(i + '\n')

rem()