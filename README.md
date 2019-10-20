[![CircleCI](https://circleci.com/gh/sarcoma/terminal_table/tree/master.svg?style=svg)](https://circleci.com/gh/sarcoma/terminal_table/tree/master)

# Python Table

Print out headers and rows in to a table in the terminal.

## Example 

```python
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
