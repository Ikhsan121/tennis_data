from bs4 import BeautifulSoup


def player_women(response, name):
    soup = BeautifulSoup(response, 'html.parser')
    player_name = name
    try:
        # career_tour
        table_career_tour = soup.find('table',  attrs={'id': 'tour-years'})
        career_tour_M = table_career_tour.find_all('tr')[-1].find_all('td')[1].text
        career_tour_Win_percentage = table_career_tour.find_all('tr')[-1].find_all('td')[4].text.split("%")[0]
        career_tour_MS = table_career_tour.find_all('tr')[-1].find_all('td')[11].text
        career_tour_TPW = table_career_tour.find_all('tr')[-1].find_all('td')[21].text.split("%")[0]
    except AttributeError:
        career_tour_M = ''
        career_tour_Win_percentage = ''
        career_tour_MS = ''
        career_tour_TPW = ''
#####################################################################################################################
    # Initialize variables with default values
    tour_2023_M = ''
    tour_2023_Win_percentage = ''
    tour_2023_MS = ''
    tour_2023_TPW = ''
    tour_2022_M = ''
    tour_2022_Win_percentage = ''
    tour_2022_MS = ''
    tour_2022_TPW = ''
    try:
        # career tour for 2023 and 2022
        table_career_tour = soup.find('table',  attrs={'id': 'tour-years'})
        rows = table_career_tour.find_all('tr')
        for row in rows:
            first_column_cell = row.find('td')
            # Extract the text from the first column cell
            if first_column_cell:
                first_column_item = first_column_cell.get_text(strip=True)
                if first_column_item == '2023':
                    matching_row = row
                    # tour-2023
                    tour_2023_M = matching_row.find_all('td')[1].text
                    tour_2023_Win_percentage = matching_row.find_all('td')[4].text.split("%")[0]
                    tour_2023_MS = matching_row.find_all('td')[11].text
                    tour_2023_TPW = matching_row.find_all('td')[21].text.split("%")[0]
                elif first_column_item == '2022':
                    matching_row = row
                    # tour-2022
                    tour_2022_M = matching_row.find_all('td')[1].text
                    tour_2022_Win_percentage = matching_row.find_all('td')[4].text.split("%")[0]
                    tour_2022_MS = matching_row.find_all('td')[11].text
                    tour_2022_TPW = matching_row.find_all('td')[21].text.split("%")[0]
    except AttributeError:
        pass
#######################################################################################################################
    # Initialize variables with default values
    career_hard_M = ''
    career_hard_Win_percentage = ''
    career_hard_MS = ''
    career_hard_TPW = ''
    career_clay_M = ''
    career_clay_Win_percentage = ''
    career_clay_MS = ''
    career_clay_TPW = ''
    career_grass_M = ''
    career_grass_Win_percentage = ''
    career_grass_MS = ''
    career_grass_TPW = ''
    try:
        # check if table career  tour split available
        table_career_level = soup.find('table', attrs={'id': 'career-splits'})
        rows = table_career_level.find_all('tr')
        for row in rows:
            first_column_cell = row.find('td')
            # Extract the text from the first column cell
            if first_column_cell:
                first_column_item = first_column_cell.get_text(strip=True)
                if first_column_item == 'Hard':
                    matching_row = row
                    # career-hard
                    career_hard_M = matching_row.find_all('td')[1].text
                    career_hard_Win_percentage = matching_row.find_all('td')[4].text.split("%")[0]
                    career_hard_MS = matching_row.find_all('td')[11].text
                    career_hard_TPW = matching_row.find_all('td')[21].text.split("%")[0]
                elif first_column_item == 'Clay':
                    matching_row = row
                    # career-clay
                    career_clay_M = matching_row.find_all('td')[1].text
                    career_clay_Win_percentage = matching_row.find_all('td')[4].text.split("%")[0]
                    career_clay_MS = matching_row.find_all('td')[11].text
                    career_clay_TPW = matching_row.find_all('td')[21].text.split("%")[0]
                elif first_column_item == 'Grass':
                    matching_row = row
                    # career-grass
                    career_grass_M = matching_row.find_all('td')[1].text
                    career_grass_Win_percentage = matching_row.find_all('td')[4].text.split("%")[0]
                    career_grass_MS = matching_row.find_all('td')[11].text
                    career_grass_TPW = matching_row.find_all('td')[21].text.split("%")[0]
    except AttributeError:
        pass
#######################################################################################################################
    # l52
    # Initialize variables with default values
    career_l52_hard_M = ''
    career_l52_hard_Win_percentage = ''
    career_l52_hard_MS = ''
    career_l52_hard_TPW = ''
    career_l52_clay_M = ''
    career_l52_clay_Win_percentage = ''
    career_l52_clay_MS = ''
    career_l52_clay_TPW = ''
    career_l52_grass_M = ''
    career_l52_grass_Win_percentage = ''
    career_l52_grass_MS = ''
    career_l52_grass_TPW = ''
    try:
        # we check if hard, clay, grass available
        table_l52_level = soup.find('table', attrs={'id': 'last52-splits'})
        rows = table_l52_level.find_all('tr')
        for row in rows:
            first_column_cell = row.find('td')
            # Extract the text from the first column cell
            if first_column_cell:
                first_column_item = first_column_cell.get_text(strip=True)
                if first_column_item == 'Hard':
                    matching_row = row
                    # l52-hard
                    career_l52_hard_M = matching_row.find_all('td')[1].text
                    career_l52_hard_Win_percentage = matching_row.find_all('td')[4].text.split("%")[0]
                    career_l52_hard_MS = matching_row.find_all('td')[11].text
                    career_l52_hard_TPW = matching_row.find_all('td')[21].text.split("%")[0]
                elif first_column_item == 'Clay':
                    matching_row = row
                    # l52-clay
                    career_l52_clay_M = matching_row.find_all('td')[1].text
                    career_l52_clay_Win_percentage = matching_row.find_all('td')[4].text.split("%")[0]
                    career_l52_clay_MS = matching_row.find_all('td')[11].text
                    career_l52_clay_TPW = matching_row.find_all('td')[21].text.split("%")[0]
                elif first_column_item == 'Grass':
                    matching_row = row
                    # l52-grass
                    career_l52_grass_M = matching_row.find_all('td')[1].text
                    career_l52_grass_Win_percentage = matching_row.find_all('td')[4].text.split("%")[0]
                    career_l52_grass_MS = matching_row.find_all('td')[11].text
                    career_l52_grass_TPW = matching_row.find_all('td')[21].text.split("%")[0]
    except AttributeError:
        pass
#######################################################################################################################
    # table ITF-career
    try:
        table_itf_career = soup.find('table', attrs={'id': 'chall-years'})
        itf_career_M = table_itf_career.find_all('tr')[-1].find_all('td')[1].text
        itf_career_Win_percentage = table_itf_career.find_all('tr')[-1].find_all('td')[4].text.split("%")[0]
        itf_career_MS = table_itf_career.find_all('tr')[-1].find_all('td')[11].text
        itf_career_TPW = table_itf_career.find_all('tr')[-1].find_all('td')[21].text.split("%")[0]
    except AttributeError:
        itf_career_M = ''
        itf_career_Win_percentage = ''
        itf_career_MS = ''
        itf_career_TPW = ''
#######################################################################################################################
    # Initialize variables with default values

    itf_career_2023_M = ''
    itf_career_2023_Win_percentage = ''
    itf_career_2023_MS = ''
    itf_career_2023_TPW = ''
    itf_career_2022_M = ''
    itf_career_2022_Win_percentage = ''
    itf_career_2022_MS = ''
    itf_career_2022_TPW = ''
    try:
        table_itf_career = soup.find('table', attrs={'id': 'chall-years'})
        rows = table_itf_career.find_all('tr')
        for row in rows:
            first_column_cell = row.find('td')
            # Extract the text from the first column cell
            if first_column_cell:
                first_column_item = first_column_cell.get_text(strip=True)
                if first_column_item == '2023':
                    matching_row = row
                    itf_career_2023_M = matching_row.find_all('td')[1].text
                    itf_career_2023_Win_percentage = matching_row.find_all('td')[4].text.split("%")[0]
                    itf_career_2023_MS = matching_row.find_all('td')[11].text
                    itf_career_2023_TPW = matching_row.find_all('td')[21].text.split("%")[0]
                elif first_column_item == '2022':
                    matching_row = row
                    itf_career_2022_M = matching_row.find_all('td')[1].text
                    itf_career_2022_Win_percentage = matching_row.find_all('td')[4].text.split("%")[0]
                    itf_career_2022_MS = matching_row.find_all('td')[11].text
                    itf_career_2022_TPW = matching_row.find_all('td')[21].text.split("%")[0]
    except AttributeError:
        pass
    row_data = [
        player_name,
        career_tour_M,
        career_tour_Win_percentage,
        career_tour_MS,
        career_tour_TPW,
        tour_2023_M,
        tour_2023_Win_percentage,
        tour_2023_MS,
        tour_2023_TPW,
        tour_2022_M,
        tour_2022_Win_percentage,
        tour_2022_MS,
        tour_2022_TPW,
        career_hard_M,
        career_hard_Win_percentage,
        career_hard_MS,
        career_hard_TPW,
        career_clay_M,
        career_clay_Win_percentage,
        career_clay_MS,
        career_clay_TPW,
        career_grass_M,
        career_grass_Win_percentage,
        career_grass_MS,
        career_grass_TPW,
        career_l52_hard_M,
        career_l52_hard_Win_percentage,
        career_l52_hard_MS,
        career_l52_hard_TPW,
        career_l52_clay_M,
        career_l52_clay_Win_percentage,
        career_l52_clay_MS,
        career_l52_clay_TPW,
        career_l52_grass_M,
        career_l52_grass_Win_percentage,
        career_l52_grass_MS,
        career_l52_grass_TPW,
        itf_career_M,
        itf_career_Win_percentage,
        itf_career_MS,
        itf_career_TPW,
        itf_career_2023_M,
        itf_career_2023_Win_percentage,
        itf_career_2023_MS,
        itf_career_2023_TPW,
        itf_career_2022_M,
        itf_career_2022_Win_percentage,
        itf_career_2022_MS,
        itf_career_2022_TPW,
    ]
    # formatting data type form string into float
    converted_list = [float(item) if item.replace('.', '', 1).isdigit() else item for item in row_data]
    print(f'{name}: success')
    return converted_list
