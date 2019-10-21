import collections.abc

from ansi_colours import AnsiColours as Colour


class Table:
    @staticmethod
    def create(
            rows,
            headers,
            use_ansi=True,
            row_colours=None,
            column_colours=None,
            header_colours=None,
            header_colour=None,
            max_column_widths=None,
            max_column_width=None,
            add_row_separator=True
    ):
        if row_colours is None:
            row_colours = []
        if column_colours is None:
            column_colours = []
        if header_colours is None:
            header_colours = []

        max_column_widths = Table.prepare_max_column_widths(headers, max_column_widths, max_column_width)
        wrapped_headers = Table.get_wrapped_row(headers, max_column_widths)
        wrapped_rows = [Table.get_wrapped_row(row, max_column_widths) for row in rows]
        col_widths = Table.get_column_widths(wrapped_rows, wrapped_headers, max_column_widths)

        output = [
            "%s\n" % Table.make_row(
                wrapped_headers,
                col_widths,
                use_ansi,
                column_colours=header_colours,
                row_colour=header_colour
            ),
            "%s\n" % Table.make_underline(col_widths, use_ansi)
        ]

        for i, wrapped_row in enumerate(wrapped_rows):
            if add_row_separator and 0 < i < len(wrapped_rows):
                output += "%s\n" % Table.make_underline(col_widths, use_ansi)

            row_colour = row_colours[i % len(row_colours)] if len(row_colours) else None
            output.append("%s\n" % Table.make_row(
                wrapped_row,
                col_widths,
                use_ansi,
                column_colours=column_colours,
                row_colour=row_colour
            ))

        return "".join(output)

    @staticmethod
    def prepare_max_column_widths(headers, max_column_widths, max_column_width):
        if max_column_width is None:
            max_column_width = float('inf')
        if max_column_widths is None:
            max_column_widths = [max_column_width] * len(headers)
        elif isinstance(max_column_widths, collections.abc.Sequence) and not isinstance(max_column_widths, str):
            max_column_widths = [max_column_width if x is None else x for x in max_column_widths]
        return max_column_widths

    @staticmethod
    def make_row(wrapped_row, col_widths, use_ansi=True, separator='|', column_colours=None, row_colour=None):
        if column_colours is None:
            column_colours = []
        if row_colour is None:
            row_colour = []

        separator = Colour.light_grey(separator) if use_ansi else separator
        string = []

        for h in range(Table.get_row_height(wrapped_row)):
            if h > 0:
                string.append('\n')
            string.append(separator)
            for i, column in enumerate(wrapped_row):
                if h < len(column):
                    data = str(column[h])
                    if use_ansi:
                        colour = column_colours[i] if i < len(column_colours) else row_colour
                        if callable(colour):
                            data = colour(data)

                    padding = ' ' * (col_widths[i] - len(column[h]))
                    string.append('  {}{}  {}'.format(data, padding, separator))
                else:
                    padding = ' ' * col_widths[i]
                    string.append('  {}  {}'.format(padding, separator))

        return ''.join(string)

    @staticmethod
    def make_underline(col_widths, use_ansi=True, separator="|"):
        underline = [separator]
        for width in col_widths:
            underline.append("{}{}".format("-" * (width + 4), separator))

        return Colour.light_grey("".join(underline)) if use_ansi else "".join(underline)

    @staticmethod
    def wrap_text(text, width=20):
        text = str(text)
        if width == float('inf'):
            return text,
        return tuple(text[x * width: (x + 1) * width] for x in range(len(text) // width + 1))

    @staticmethod
    def get_column_widths(wrapped_rows, wrapped_headers, max_column_widths):
        col_widths = Table.get_column_widths_for_row(wrapped_headers)

        for wrapped_row in wrapped_rows:
            row_col_widths = Table.get_column_widths_for_row(wrapped_row)
            for i, column in enumerate(wrapped_row):
                col_widths[i] = max(col_widths[i], row_col_widths[i])

        for i in range(len(col_widths)):
            col_widths[i] = min(col_widths[i], max_column_widths[i])

        return col_widths

    @staticmethod
    def get_column_widths_for_row(wrapped_row):
        return [
            max(len(x) for x in col)
            for col in wrapped_row
        ]

    @staticmethod
    def get_wrapped_row(row, max_column_widths):
        return [Table.wrap_text(t, w) for t, w in zip(row, max_column_widths)]

    @staticmethod
    def get_row_height(wrapped_row):
        max_heights = [len(col) for col in wrapped_row]
        return max(max_heights) if max_heights else 0


if __name__ == '__main__':
    long_text = 'Zombie ipsum brains reversus ab cerebellum viral inferno, brein nam rick mend grimes malum cerveau cerebro.'
    wrapped_table = Table.create(
        [[long_text[:10], long_text[:55], long_text[:25]],
         [long_text[:5], long_text[:12], long_text[:33]],
         [long_text[:12], long_text, long_text[:2]]],
        ['a', 'b', 'c'],
        max_column_width=20,
        max_column_widths=(None, None, 40),
        use_ansi=False
    )
    print(repr(wrapped_table))
    coloured_wrapped_table = Table.create(
        [[long_text[:14], long_text[:12], long_text[:35]],
         [long_text[:17], long_text[:4], long_text[:56]],
         [long_text[:21], long_text[:5], long_text]],
        ['a', 'b', 'c'],
        max_column_width=20,
        column_colours=[Colour.red, Colour.blue, Colour.green]
    )
    print(repr(coloured_wrapped_table))

    mixed_wrapped_table = Table.create(
        [[long_text[:14], long_text[:12], long_text[:35]],
         [long_text[:17], long_text[:4], long_text[:56]],
         [long_text[:21], long_text[:5], long_text]],
        ['a', 'b', 'c'],
        column_colours=[Colour.red, Colour.blue, Colour.green],
        max_column_widths=(30, 10)
    )
    print('1', repr(mixed_wrapped_table))

    plain = Table.create(
        [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
        ['a', 'b', 'c'],
        use_ansi=False
    )
    print(repr(plain))
    colouredRows = Table.create(
        [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
        ['a', 'b', 'c'],
        row_colours=[Colour.red, Colour.blue]
    )
    print(repr(colouredRows))
    colouredCols = Table.create(
        [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
        ['a', 'b', 'c'],
        column_colours=[Colour.red, Colour.blue, Colour.green]
    )
    print(repr(colouredCols))
    colouredRowsAndCols = Table.create(
        [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
        ['a', 'b', 'c'],
        row_colours=[Colour.red, Colour.blue],
        column_colours=[Colour.green]
    )
    print(repr(colouredRowsAndCols))
    colouredHeaders = Table.create(
        [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
        ['a', 'b', 'c'],
        header_colours=[Colour.red, Colour.yellow, Colour.red],
    )
    print(repr(colouredHeaders))
    colouredHeader = Table.create(
        [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
        ['a', 'b', 'c'],
        header_colour=Colour.cyan,
    )
    print(repr(colouredHeader))
