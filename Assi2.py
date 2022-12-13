file = open('D:\pass 1 & DS\input1.txt','r')
lines = file.readlines()
mnt = []
macro_name = []
param_no = []
starting_idx = []
mdt = []
Dict_formvspos = {}
Dict_actvspos = {}
formvspos = {}
flag = 0

with open('data.txt', 'w') as f:
    for line in lines:
        # print(line)

        if 'MACRO' in line:
            starting_idx.append(len(mdt) + 1)
            n = line
            n = n.replace(',', ' ')
            n = n.replace('\t', ' ')
            n = n.strip()
            n = n.split(" ")
            m_name = n[1]
            list_of_args = []
            form_param = []
            pos_param = []
            a = 1
            for i in range(2, len(n)):
                s = "#"
                form_param.append(n[i])
                s += str(a)
                a += 1
                pos_param.append(s)
                formvspos[n[i]] = s
            list_of_args.append(form_param)
            list_of_args.append(pos_param)
            Dict_formvspos[m_name] = list_of_args
            macro_name.append(m_name)
            p_count = len(n) - 2
            param_no.append(p_count)
            flag = 1
        if flag == 1:
            m = line
            m = m.strip()
            m = m.replace('\t', ' ')
            if 'MACRO' not in line:
                mdt.append(m)
        if 'MEND' in line:
            flag = 0
        if flag == 0:
            if 'MEND' not in line:
                line = line.replace('\t', '')
                # f.write(line)

    mnt.append(macro_name)
    mnt.append(param_no)
    mnt.append(starting_idx)
    print("MNT", mnt)
    print("Formal vs Positional List=", Dict_formvspos)
    for line in lines:
        if 'MACRO' not in line:
            list_of_args = []
            act_param = []
            pos_param = []
            s = line
            s = s.replace(',', ' ')
            s = s.replace('\t', ' ')
            s = s.strip()
            s = s.split(" ")
            a = 1
            if s[0] in mnt[0]:
                for i in range(1, len(s)):
                    st = "#"
                    st += str(a)
                    a += 1
                    # Dict_actvspos[s[0]][s[i]]=st
                    act_param.append(s[i])
                    pos_param.append(st)
                list_of_args.append(act_param)
                list_of_args.append(pos_param)
                if s[0] not in Dict_actvspos.keys():
                    Dict_actvspos[s[0]] = list_of_args
                else:
                    r = Dict_actvspos[s[0]]
                    r[0].append(list_of_args[0][0])
                    r[1].append(list_of_args[1][0])
                    Dict_actvspos[s[0]] = r
    print("actual vs param list=", Dict_actvspos)

    for i in range(len(mdt)):
        y = mdt[i].split(" ")
        if len(y) > 1:
            if y[1] in formvspos.keys():
                mdt[i] = mdt[i].replace(y[1], formvspos[y[1]])
    print("MDT=", mdt)
    f.write(f'MDT : {mdt}\n')
    f.write(f'MNT : {mnt}\n')
    f.write(f'A vs P : {Dict_actvspos}\n')
    f.write(f'F vs P : {Dict_formvspos}\n')
    f.close()

