with open('yandex-ping.txt', 'r') as inpf, open('ping-filtered.txt', 'a') as outf:
    outf.truncate(0)
    inpf.readline()    #    первая строка с общей информацией
    while True:
        line = inpf.readline()
        if line == '\n':
            break
        outf.write(line[line.find('time=') + 5:line.find(' ms')] + '\n')
        