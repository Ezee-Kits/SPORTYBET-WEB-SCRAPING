from func import scrolling,saving_files,drop_duplicate,headless_selenium_init,saving_path_csv
from bs4 import BeautifulSoup
import time
from lxml import html
import pandas as pd



def get_arrange_matches(path,wait,EC,By):
    matches = wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="importMatch"]')))
    matches = matches.text.replace('\n','!').split('!')
    # print(matches)

    int_vals = [str(x) for x in range(1,3)]
    other_vals = ['Matches', 'Outrights', 'Other Markets', 'Goals', 'Over', 'Under','X']
    int_vals = int_vals + other_vals

    new_matches = []

    for x in matches:
        x = x.strip()
        if '/' in x or '\ue6a3' in x or 'ID' in x or '+' in x or x in int_vals:
            pass

        else:
            new_matches.append(x)

    time_value = []
    time_index = []

    for i,x in enumerate(new_matches):
        if ':' in x:
            indx = new_matches.index(x,i,len(new_matches))
            time_index.append(indx)
            time_value.append(x)

    # print(new_matches)
    # print(time_index)
    # print(time_value)

    for x in time_index:
        try:
            f_elem_indx = time_index.index(x)
            s_elem_indx = time_index.index(x) + 1

            if (time_index[s_elem_indx] - time_index[f_elem_indx]) == 9:
                all_info = new_matches[ time_index[f_elem_indx]:time_index[s_elem_indx] ]
                match_time = all_info[0]
                home_team = all_info[1]
                away_team = all_info[2]

                home_odd = float(all_info[3])
                draw_odd = float(all_info[4])
                away_odd = float(all_info[5])
                bookmaker = 'SPORTYBET'

                data = {
                    'TIME':match_time,
                    'HOME TEAM':home_team,
                    'AWAY TEAM':away_team,

                    'HOME ODD': home_odd,
                    'DRAW ODD':draw_odd,
                    'AWAY ODD':away_odd,
                    'BOOKMAKER':bookmaker
                }
                saving_files(data=[data],path=path)
        except:
            pass

 

def sportybet_func():
    path = f'{saving_path_csv}/SPORTYBET.csv'
    driver,wait,EC,By = headless_selenium_init()
    driver.get('https://www.sportybet.com/ng/sport/football?time=24')


    try:
        for x in range(10):

            time.sleep(2)
            wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="importMatch"]/div[2]/div/div[4]/div[2]/div[1]/div/div[2]/div[1]')))
            time.sleep(2)

            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            get_arrange_matches(wait=wait,By=By,path=path,EC=EC)

            next = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'#importMatch > div.pagination.pagination > span.pageNum.icon-next')))
            next.click()
            time.sleep(1)
    except:
        pass      

    drop_duplicate(path=path)
