import requests
from bs4 import BeautifulSoup


#url = "your_url"

def draw_coordinate(url_data):
    url = url_data

    response = requests.get(url)
    response.raise_for_status()
    data = response.text

    parse = BeautifulSoup(data, "html.parser")

    table = parse.find("table")

    cells = []
    for row in table.find_all('tr')[1:]:
        tds = row.find_all('td')
        
        if len(tds) >= 3: 
            clean_row = [td.get_text(strip=True) for td in tds]
            cells.append(clean_row)
    
    if not cells:
        return
        

    parsed_points = []
    
    for row in cells:
        if len(row) < 3:
            continue
        try:
            x, char, y = int(row[0]), row[1], int(row[2])
            parsed_points.append((x, y, char))
        except ValueError:
            pass    #there could be some row that does not have vlaues

    if not parsed_points:
        return      


    max_x = max(point[0] for point in parsed_points)
    max_y = max(point[1] for point in parsed_points)

    grid = [[' '] * (max_x + 1) for i in range(max_y + 1)]


    for x, y, char in parsed_points:
        grid[y][x] = char

    #print y coordinate fist cause we want to print from top to down
    for row in reversed(grid):
        print("".join(row))

draw_coordinate("your_url")