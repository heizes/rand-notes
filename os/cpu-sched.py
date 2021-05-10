#!/usr/bin/python3

import os, time, sys
import pandas as pd
from prettytable import PrettyTable

time_formats = ["HH:MM","HH:MM:SS","HH", "MM","SS"]

def converter(format, number):
    if number == 0:
        conv = format.split(":")
        return round(int(conv[1]) / 60 + int(conv[0]), 3)
    elif number == 1:
        conv = format.split(":")
        return round(int(conv[1]) / 60 + int(conv[0]), 3)
    elif number == 2:
        return int(format)
    elif number == 3:
        return round(int(format) / 60, 3)
    elif number == 4:
        return int(format)

def main_df():
    jobs_num = None
    while jobs_num not in [x for x in range(2, 16)]:
        try:
            jobs_num = int(input("Enter number of JOBS (min=2/max=15): "))
            df = pd.DataFrame(index=[x for x in range(1, jobs_num+1)], columns=["J#", "AT", "RT", "ST", "FT", "WT", "TAT"])
        except KeyboardInterrupt:
            sys.exit(0)
        except ValueError:
            jobs = None

        if jobs_num not in [x for x in range(2, 16)]:
            print('Incorrect!')

    print("[TIME FORMATS]")
    for formats in range(len(time_formats)):
        print(f"{formats+1}) {time_formats[formats]}")

    print("Note: Just type the number not the whole format\n")

    arrival_time = None
    while arrival_time not in [x for x in range (1, 6)]:
        try:
            arrival_time = int(input("Enter arrival time format: "))
        except KeyboardInterrupt:
            sys.exit(0)
        except ValueError:
            arrival_time = None

        if arrival_time not in [x for x in range(1, 6)]:
            print('Incorrect!')

    run_time = None
    while run_time not in [x for x in range (1, 6)]:
        try:
            run_time = int(input("Enter burst time format: "))
        except KeyboardInterrupt:
            sys.exit(0)
        except ValueError:
            run_time = None

        if run_time not in [x for x in range(1, 6)]:
            print('Incorrect!')

    print(f"[AT] => {time_formats[arrival_time-1]}\n[RT] => {time_formats[run_time-1]}\n")

    for at_rt in range(len(df)):
        df.iloc[at_rt][0] = at_rt+1

        at_num = input(f"Enter value of AT ({time_formats[arrival_time-1]}): ")
        df.iloc[at_rt][1] = (converter(at_num, arrival_time-1))
        rt_num = input(f"Enter value of RT ({time_formats[run_time-1]}): ")
        df.iloc[at_rt][2] = (converter(rt_num, run_time-1))
    return df

def fifo(df):

    fifo_table = PrettyTable(field_names=list(df.columns))

    for st_ft in range(len(df)):
        if df.iloc[st_ft][1] < df.iloc[st_ft-1][4]:
            df.iloc[st_ft][3] =  df.iloc[st_ft-1][4]
        else:
            df.iloc[st_ft][3] = df.iloc[st_ft][1]

        df.iloc[st_ft][4] = round(df.iloc[st_ft][2] + df.iloc[st_ft][3], 3)

    for wt_tat in range(len(df)):
        df.iloc[wt_tat][5] = round(df.iloc[wt_tat][3] - df.iloc[wt_tat][1], 3)
        df.iloc[wt_tat][6] = round(df.iloc[wt_tat][4] - df.iloc[wt_tat][1], 3)

    for pretable in range(len(df)):
        fifo_table.add_row(df.iloc[pretable])

    print(fifo_table)

    print(f"Average WT: {round(df['WT'].mean(), 3)}")
    print(f"Average TAT: {round(df['TAT'].mean(), 3)}")


def sjf(df):

    df_finish = pd.DataFrame(index=[x for x in range(1, len(df)+1)],columns=["J#", "AT", "RT", "ST", "FT", "WT", "TAT"])
    sjf_table = PrettyTable(field_names=list(df.columns))

    df_new = df.sort_values(by=['AT'])
    df_neww = df_new[['J#','AT']].copy()

    ft = 0
    for st_ft in range(len(df_new)):
        df_news = pd.DataFrame()

        if df_new.iloc[0][1] <= ft:
            df_news = df_new[df_new.AT > ft].sort_values(by=['RT'], ascending=True)
            df_new.loc[(df['AT'] <= ft), 'AT'] = ft
            df_new = df_new[df_new.AT <= ft].sort_values(by=['RT'], ascending=True)
            df_new = df_new.append(df_news, ignore_index=True)

        df_new.iloc[0][3] = float(df_new.iloc[0][1])

        df_new.iloc[0][4] = round(df_new.iloc[0][2] + df_new.iloc[0][3], 3)

        ft = df_new.iloc[0][4]
        df_finish.iloc[st_ft] = df_new.iloc[0]

        df_new = df_new.iloc[1:]

        if df_new.empty:
            break

    df_finish = pd.merge(df_finish, df_neww[['J#','AT']],  how='left',on=['J#']).drop(columns=['AT_x']).rename(columns={'AT_y':'AT'})
    df_finish = df_finish[['J#', 'AT', 'RT', 'ST', 'FT', 'WT', 'TAT']]
    df_finish['WT'] = round(df_finish.apply(lambda x: x['ST'] - x['AT'], axis = 1), 3)
    df_finish['TAT'] = round(df_finish.apply(lambda x: x['FT'] - x['AT'], axis = 1), 3)
    df_finish = df_finish.sort_values(by='J#', ascending=True)

    for pretable in range(len(df)):
        sjf_table.add_row(df_finish.iloc[pretable])

    print(sjf_table)

    print(f"Average WT: {round(df_finish['WT'].mean(), 3)}")
    print(f"Average TAT: {round(df_finish['TAT'].mean(), 3)}")

def main():
    os.system('cls')
    print("""
    __  __ __        __     __
    |_ ||_ /  \   /  (_   ||_
    |  ||  \__/  /   __)__)|
    """)
    try:
        ch = int(input("Choose the type of Scheduling\n1. FIFO\n2. SJF\n=> "))
        if ch == 1:
            fifo(main_df())
        elif ch == 2:
            sjf(main_df())
        else:
            print("error: invalid choice.")

    except KeyboardInterrupt:
        pass
    except ValueError:
        print("Invalid value!")
        time.sleep(1)
        os.system('cls')
        main()

main()