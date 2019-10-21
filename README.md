[![CircleCI](https://circleci.com/gh/sarcoma/terminal_table/tree/master.svg?style=svg)](https://circleci.com/gh/sarcoma/terminal_table/tree/master)

# Python Table

Print out headers and rows in to a table in the terminal.

## Install 

Run `pip install terminal_table` to install the package.

## Usage

Pass in a two dimensional `list` or `tuple` of data for the table rows and a `list` or `tuple` for the headers. 

You can optionally pass in some text colours for the header rows and columns with `AnsiColours`

### Import 

`from terminal_table import Table`


https://github.com/sarcoma/Python_ANSI_Colours

```python

    from terminal_table import Table
    from ansi_colours import AnsiColours as Colour
    
    table = Table.create(
        (
            (1, "Johnathon", "Pollitt", "Seres"),
            (2, "Nerita", "Beetham", "Guanshan"),
            [3, "Celia", "Cawsby", "Łaskarzew"],
            [4, "Carolin", "Muggleston", "Beishan"],
            (5, "Homere", "Caird", "Shuangzhu"),
            (6, "Conrado", "Wethey", "Yezhi"),
            (7, "Winifred", "Malloch", "Orekhovo - Borisovo Severnoye"),
            (8, "Ag", "Wardley", "Buenos Aires"),
            (9, "Shelby", "Janiak", "Skänninge"),
            (10, "Sully", "McIlmurray", "Huxiaoqiao")
        ),
        ("ID", "First Name", "Last Name", "City"),
        header_colour=Colour.cyan,
        column_colours=(Colour.green,)
    )
    print(table)
```

![Screenshot of Pagination](/../screenshot/screenshot/table.png?raw=true "Pagination Example")
