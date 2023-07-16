from bs4 import BeautifulSoup


def player_men(response, name):
    soup = BeautifulSoup(response, 'html.parser')
    player_name = name
    try:
        # career_tour
        table_career_tour = soup.find('table', attrs={'id': 'tour-years'})
        career_tour_M = table_career_tour.find_all('tr')[-1].find_all('td')[1].text
        career_tour_Win_percentage = table_career_tour.find_all('tr')[-1].find_all('td')[4].text.split("%")[0]
        career_tour_MS = table_career_tour.find_all('tr')[-1].find_all('td')[11].text
        career_tour_TPW = table_career_tour.find_all('tr')[-1].find_all('td')[21].text.split("%")[0]
    except AttributeError:
        career_tour_M = ''
        career_tour_Win_percentage = ''
        career_tour_MS = ''
        career_tour_TPW = ''
#########################################################################################################
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
        # career_tour
        table_career_tour = soup.find('table', attrs={'id': 'tour-years'})
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
                    tour_2022_M = matching_row.find_all('td')[1].text
                    tour_2022_Win_percentage = matching_row.find_all('td')[4].text.split("%")[0]
                    tour_2022_MS = matching_row.find_all('td')[11].text
                    tour_2022_TPW = matching_row.find_all('td')[21].text.split("%")[0]
    except AttributeError:
        pass

#######################################################################################################################
    # Initialize variables with default values
    # career-hard
    career_hard_M = ''
    career_hard_Win_percentage = ''
    career_hard_MS = ''
    career_hard_TPW = ''
    # career-clay
    career_clay_M = ''
    career_clay_Win_percentage = ''
    career_clay_MS = ''
    career_clay_TPW = ''
    # career-grass
    career_grass_M = ''
    career_grass_Win_percentage = ''
    career_grass_MS = ''
    career_grass_TPW = ''
    # check if table career  tour split available
    try:
        # we check if hard, clay, grass available
        table_career_level = soup.find('table', attrs={'id': 'career-splits'})
        rows = table_career_level.find_all('tr')
        for row in rows:
            first_column_cell = row.find('td')
            # Extract the text from the first column cell
            if first_column_cell:
                first_column_item = first_column_cell.get_text(strip=True)
                if first_column_item == 'Hard':
                    matching_row = row
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
    # Initialize variables with default values
    # tour-l52-hard
    career_tour_l52_hard_M = ''
    career_tour_l52_hard_Win_percentage = ''
    career_tour_l52_hard_MS = ''
    career_tour_l52_hard_TPW = ''
    # tour-l52-clay
    career_tour_l52_clay_M = ''
    career_tour_l52_clay_Win_percentage = ''
    career_tour_l52_clay_MS = ''
    career_tour_l52_clay_TPW = ''
    # tour-l52-grass
    career_tour_l52_grass_M = ''
    career_tour_l52_grass_Win_percentage = ''
    career_tour_l52_grass_MS = ''
    career_tour_l52_grass_TPW = ''
    # check if table career  tour l52 exist
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
                    # tour-l52-hard
                    matching_row = row
                    career_tour_l52_hard_M = matching_row.find_all('td')[1].text
                    career_tour_l52_hard_Win_percentage = matching_row.find_all('td')[4].text.split("%")[0]
                    career_tour_l52_hard_MS = matching_row.find_all('td')[11].text
                    career_tour_l52_hard_TPW = matching_row.find_all('td')[21].text.split("%")[0]
                elif first_column_item == 'Clay':
                    matching_row = row
                    # l52-clay
                    career_tour_l52_clay_M = matching_row.find_all('td')[1].text
                    career_tour_l52_clay_Win_percentage = matching_row.find_all('td')[4].text.split("%")[0]
                    career_tour_l52_clay_MS = matching_row.find_all('td')[11].text
                    career_tour_l52_clay_TPW = matching_row.find_all('td')[21].text.split("%")[0]
                elif first_column_item == 'Grass':
                    # l52-grass
                    matching_row = row
                    career_tour_l52_grass_M = row.find_all('td')[1].text
                    career_tour_l52_grass_Win_percentage = matching_row.find_all('td')[4].text.split("%")[0]
                    career_tour_l52_grass_MS = matching_row.find_all('td')[11].text
                    career_tour_l52_grass_TPW = matching_row.find_all('td')[21].text.split("%")[0]
    except AttributeError:
        pass
######################################################################################################################
    try:
        # career-challenger
        table_career_challenger = soup.find('table', attrs={'id': 'chall-years'})
        career_challenger_M = table_career_challenger.find_all('tr')[-1].find_all('td')[1].text
        career_challenger_Win_percentage = table_career_challenger.find_all('tr')[-1].find_all('td')[4].text.split("%")[0]
        career_challenger_MS = table_career_challenger.find_all('tr')[-1].find_all('td')[11].text
        career_challenger_TPW = table_career_challenger.find_all('tr')[-1].find_all('td')[21].text.split("%")[0]
    except AttributeError:
        career_challenger_M = ''
        career_challenger_Win_percentage = ''
        career_challenger_MS = ''
        career_challenger_TPW = ''
#######################################################################################################################
    # Initialize variables with default values
    career_challenger_2023_M = ''
    career_challenger_2023_Win_percentage = ''
    career_challenger_2023_MS = ''
    career_challenger_2023_TPW = ''
    career_challenger_2022_M = ''
    career_challenger_2022_Win_percentage = ''
    career_challenger_2022_MS = ''
    career_challenger_2022_TPW = ''
    try:
        # we check if 2023 or 2022 available
        table_career_challenger = soup.find('table', attrs={'id': 'chall-years'})
        rows = table_career_challenger.find_all('tr')
        for row in rows:
            first_column_cell = row.find('td')
            # Extract the text from the first column cell
            if first_column_cell:
                first_column_item = first_column_cell.get_text(strip=True)
                if first_column_item == '2023':
                    matching_row = row
                    # challenger-2023
                    career_challenger_2023_M = matching_row.find_all('td')[1].text
                    career_challenger_2023_Win_percentage = matching_row.find_all('td')[4].text.split("%")[0]
                    career_challenger_2023_MS = matching_row.find_all('td')[11].text
                    career_challenger_2023_TPW = matching_row.find_all('td')[21].text.split("%")[0]
                elif first_column_item == '2022':
                    matching_row = row
                    # challenger-2022
                    career_challenger_2022_M = matching_row.find_all('td')[1].text
                    career_challenger_2022_Win_percentage = matching_row.find_all('td')[4].text.split("%")[
                        0]
                    career_challenger_2022_MS = matching_row.find_all('td')[11].text
                    career_challenger_2022_TPW = matching_row.find_all('td')[21].text.split("%")[0]

    except AttributeError:
        pass

    #################################################################################################################
    # Initialize variables with default values
    career_challenger_l52_hard_M = ''
    career_challenger_l52_hard_Win_percentage = ''
    career_challenger_l52_hard_MS = ''
    career_challenger_l52_hard_TPW = ''
    career_challenger_l52_clay_M = ''
    career_challenger_l52_clay_Win_percentage = ''
    career_challenger_l52_clay_MS = ''
    career_challenger_l52_clay_TPW = ''
    career_challenger_l52_grass_M = ''
    career_challenger_l52_grass_Win_percentage = ''
    career_challenger_l52_grass_MS = ''
    career_challenger_l52_grass_TPW = ''

    try:
        # we check if hard, clay, grass available
        # challenger-l52 hard
        table_challenger_l52_level = soup.find('table', attrs={'id': 'last52-splits-chall'})
        rows = table_challenger_l52_level.find_all('tr')
        for row in rows:
            first_column_cell = row.find('td')
            # Extract the text from the first column cell
            if first_column_cell:
                first_column_item = first_column_cell.get_text(strip=True)
                if first_column_item == 'Hard':
                    matching_row = row
                    career_challenger_l52_hard_M = matching_row.find_all('td')[1].text
                    career_challenger_l52_hard_Win_percentage = matching_row.find_all('td')[4].text.split("%")[0]
                    career_challenger_l52_hard_MS = matching_row.find_all('td')[11].text
                    career_challenger_l52_hard_TPW = matching_row.find_all('td')[21].text.split("%")[0]
                elif first_column_item == 'Clay':
                    matching_row = row
                    # challenger-l52 clay
                    career_challenger_l52_clay_M = matching_row.find_all('td')[1].text
                    career_challenger_l52_clay_Win_percentage = matching_row.find_all('td')[4].text.split("%")[0]
                    career_challenger_l52_clay_MS = matching_row.find_all('td')[11].text
                    career_challenger_l52_clay_TPW = matching_row.find_all('td')[21].text.split("%")[0]
                elif first_column_item == 'Grass':
                    matching_row = row
                    # challenger-l52 grass
                    career_challenger_l52_grass_M = matching_row.find_all('td')[1].text
                    career_challenger_l52_grass_Win_percentage = matching_row.find_all('td')[4].text.split("%")[0]
                    career_challenger_l52_grass_MS = matching_row.find_all('td')[11].text
                    career_challenger_l52_grass_TPW = matching_row.find_all('td')[21].text.split("%")[0]

    except AttributeError:
        pass
    #################################################################################################################
    # Continue with further processing or use the retrieved values as needed

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
        career_tour_l52_hard_M,
        career_tour_l52_hard_Win_percentage,
        career_tour_l52_hard_MS,
        career_tour_l52_hard_TPW,
        career_tour_l52_clay_M,
        career_tour_l52_clay_Win_percentage,
        career_tour_l52_clay_MS,
        career_tour_l52_clay_TPW,
        career_tour_l52_grass_M,
        career_tour_l52_grass_Win_percentage,
        career_tour_l52_grass_MS,
        career_tour_l52_grass_TPW,
        career_challenger_M,
        career_challenger_Win_percentage,
        career_challenger_MS,
        career_challenger_TPW,
        career_challenger_2023_M,
        career_challenger_2023_Win_percentage,
        career_challenger_2023_MS,
        career_challenger_2023_TPW,
        career_challenger_2022_M,
        career_challenger_2022_Win_percentage,
        career_challenger_2022_MS,
        career_challenger_2022_TPW,
        career_challenger_l52_hard_M,
        career_challenger_l52_hard_Win_percentage,
        career_challenger_l52_hard_MS,
        career_challenger_l52_hard_TPW,
        career_challenger_l52_clay_M,
        career_challenger_l52_clay_Win_percentage,
        career_challenger_l52_clay_MS,
        career_challenger_l52_clay_TPW,
        career_challenger_l52_grass_M,
        career_challenger_l52_grass_Win_percentage,
        career_challenger_l52_grass_MS,
        career_challenger_l52_grass_TPW,
    ]
    # formatting data type form string into float
    converted_list = [float(item) if item.replace('.', '', 1).isdigit() else item for item in row_data]
    print(f'{name}: success')

    return converted_list
