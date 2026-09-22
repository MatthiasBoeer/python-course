

def task_1():
    list = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1),(0,),(-1,),(6,)]
    list.sort(key = lambda x: x[-1])
    print(list)

def task_2(s1):
    summe = 0
    number_of_digits = 0
    for i in range(0,len(s1)):
        if s1[i].isdigit():
            summe += int(s1[i])
            number_of_digits += 1

    durchschnitt = summe/number_of_digits
    print(summe, durchschnitt)
    return summe,durchschnitt

def task_3():
    dictionary_list =  [{'make': ' Google ', 'model': 216, 'color': 'Black'}, {'make': 'Mi Max', 'model': '2', 'color':
        'Gold'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]
    dictionary_list.sort(key = lambda x: int(x['model']), reverse = True)
    print(dictionary_list)

def task_4(list_of_strings):
    result = list(map(list,list_of_strings))
    print(list_of_strings)
    print(result)
    return result

def task_5(dic_of_events):
    the_date = "19.09.2026"
    events_on_date = []
    for event, date in dic_of_events.items():
        if date == the_date:
            events_on_date.append(event)

    print(events_on_date)
    return events_on_date

def main():
    # task_1()
    # task_2("123456")
    # task_3()
    # task_4(["one", "two", "three", "four", "five", "six"])
    events = {"Event 1" : "17.09.2026",
              "Event 2" : "19.09.2026",
              "Event 3" : "21.09.2026",
              "Event 4" : "19.09.2026",
              "Event 5" : "09.09.2026",
              "Event 6" : "10.09.2026",
              "Event 7" : "19.09.2026",
              "Event 8" : "18.09.2026",
              "Event 9" : "19.09.2026"
              }
    task_5(events)

if __name__ == "__main__":
    main()
