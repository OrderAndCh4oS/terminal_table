from ansi_colours import AnsiColours as Colour


class Table:
    @staticmethod
    def create(rows, headers, use_ansi=True, row_colours=None, column_colours=None, header_colours=None, header_colour=None):
        if row_colours is None:
            row_colours = []
        if column_colours is None:
            column_colours = []
        if header_colours is None:
            header_colours = []
        col_widths = [len(header) for header in headers]
        for row in rows:
            for i, column in enumerate(row):
                if len(str(column)) > col_widths[i]:
                    col_widths[i] = len(str(column))
        output = ''
        output += "%s\n" % Table.make_row(
            headers,
            col_widths,
            use_ansi,
            column_colours=header_colours,
            row_colour=header_colour
        )
        output += "%s\n" % Table.make_underline(col_widths, use_ansi)
        for i, row in enumerate(rows):
            row_colour = row_colours[i % len(row_colours)] if len(row_colours) else None
            output += "%s\n" % Table.make_row(
                row,
                col_widths,
                use_ansi,
                column_colours=column_colours,
                row_colour=row_colour
            )

        return output

    @staticmethod
    def make_row(row, col_widths, use_ansi=True, separator="|", column_colours=None, row_colour=None):
        if column_colours is None:
            column_colours = []
        if row_colour is None:
            row_colour = []
        separator = Colour.light_grey(separator) if use_ansi else separator
        string = separator
        for i, column in enumerate(row):
            data = str(column)
            if use_ansi:
                colour = column_colours[i] if i < len(column_colours) else row_colour
                if callable(colour):
                    data = colour(data)
            padding = "".join([" " for _ in range(col_widths[i] - len(str(column)) + 2)])
            string += "  " + data + padding + separator

        return string

    @staticmethod
    def make_underline(col_widths, use_ansi=True, separator="|"):
        underline = separator
        for width in col_widths:
            underline += "".join(["-" for _ in range(width + 4)]) + "|"

        return Colour.light_grey(underline) if use_ansi else underline

    # TODO: Implemented as a stub for testing. Remove once #1 is resolved.
    @staticmethod
    def wrap_text(text, width=20):
        return tuple(text[x * width: (x + 1) * width] for x in range(len(text) // width + 1))

if __name__ == '__main__':
    plain = Table.create([[1, 2, 3], [4, 5, 6], [7, 8, 9]], ['a', 'b', 'c'], use_ansi=False)
    print(plain)
    colouredRows = Table.create(
        [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
        ['a', 'b', 'c'],
        row_colours=[Colour.red, Colour.blue]
    )
    print(colouredRows)
    colouredCols = Table.create(
        [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
        ['a', 'b', 'c'],
        column_colours=[Colour.red, Colour.blue, Colour.green]
    )
    print(colouredCols)
    colouredRowsAndCols = Table.create(
        [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
        ['a', 'b', 'c'],
        row_colours=[Colour.red, Colour.blue],
        column_colours=[Colour.green]
    )
    print(colouredRowsAndCols)
    colouredHeaders = Table.create(
        [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
        ['a', 'b', 'c'],
        header_colours=[Colour.red, Colour.yellow, Colour.red],
    )
    print(colouredHeaders)
    colouredHeader = Table.create(
        [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
        ['a', 'b', 'c'],
        header_colour=Colour.cyan,
    )
    print(colouredHeader)
