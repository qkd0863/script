def solution(id_list, report, k):
    answer = [0] * len(id_list)
    reports = {x: 0 for x in id_list}
    print(reports)
    print(answer)

    for i in set(report):
        reports[i.split()[1]] += 1

    for i in set(report):
        if reports[i.split()[1]] >= k:
            answer[id_list.index(i.split()[0])] += 1

    return answer
