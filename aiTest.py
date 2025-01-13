import pandas as pd

tableData = pd.read_html("https://docs.google.com/document/d/e/2PACX-1vQGUck9HIFCyezsrBSnmENk5ieJuYwpt7YHYEzeNJkIb9OSDdx-ov2nRNReKQyey-cwJOoEKUhLmN9z/pub", header=0, flavor='bs4')

tdSorted = tableData[0].sort_values(by=["y-coordinate","x-coordinate"], ignore_index=True)

xcoord = tdSorted['x-coordinate']
ycoord = tdSorted['y-coordinate']
char = tdSorted['Character']

with open('output_grid.txt', 'w', encoding='utf-8') as f:
    
    for i in range(1, len(ycoord)):
        if xcoord[i] - xcoord[i - 1] != 1:
            f.write(" " * int((xcoord[i]) - (xcoord[i - 1]) - 1))
        if (ycoord[i] != (ycoord[i - 1])):
            f.write('\r')
        f.write(char[i]) 
    f.write('\n')


print('done')
