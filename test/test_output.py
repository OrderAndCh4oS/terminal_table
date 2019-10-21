from ansi_colours import AnsiColours as Colour

from terminal_table import Table


def test_default():
    assert Table.create(
        [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
        ['a', 'b', 'c'],
        use_ansi=False
    ) == '|  a  |  b  |  c  |\n|-----|-----|-----|\n|  1  |  2  |  3  |\n|-----|-----|-----|\n|  4  |  5  |  6  |\n|-----|-----|-----|\n|  7  |  8  |  9  |\n'


def test_row_colours():
    assert Table.create(
        [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
        ['a', 'b', 'c'],
        row_colours=[Colour.red, Colour.blue]
    ) == '\x1b[0;37m|\x1b[0m  a  \x1b[0;37m|\x1b[0m  b  \x1b[0;37m|\x1b[0m  c  \x1b[0;37m|\x1b[0m\n\x1b[0;37m|-----|-----|-----|\x1b[0m\n\x1b[0;37m|\x1b[0m  \x1b[0;31m1\x1b[0m  \x1b[0;37m|\x1b[0m  \x1b[0;31m2\x1b[0m  \x1b[0;37m|\x1b[0m  \x1b[0;31m3\x1b[0m  \x1b[0;37m|\x1b[0m\n\x1b[0;37m|-----|-----|-----|\x1b[0m\n\x1b[0;37m|\x1b[0m  \x1b[0;34m4\x1b[0m  \x1b[0;37m|\x1b[0m  \x1b[0;34m5\x1b[0m  \x1b[0;37m|\x1b[0m  \x1b[0;34m6\x1b[0m  \x1b[0;37m|\x1b[0m\n\x1b[0;37m|-----|-----|-----|\x1b[0m\n\x1b[0;37m|\x1b[0m  \x1b[0;31m7\x1b[0m  \x1b[0;37m|\x1b[0m  \x1b[0;31m8\x1b[0m  \x1b[0;37m|\x1b[0m  \x1b[0;31m9\x1b[0m  \x1b[0;37m|\x1b[0m\n'


def test_coloured_columns():
    assert Table.create(
        [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
        ['a', 'b', 'c'],
        column_colours=[Colour.red, Colour.blue, Colour.green]
    ) == '\x1b[0;37m|\x1b[0m  a  \x1b[0;37m|\x1b[0m  b  \x1b[0;37m|\x1b[0m  c  \x1b[0;37m|\x1b[0m\n\x1b[0;37m|-----|-----|-----|\x1b[0m\n\x1b[0;37m|\x1b[0m  \x1b[0;31m1\x1b[0m  \x1b[0;37m|\x1b[0m  \x1b[0;34m2\x1b[0m  \x1b[0;37m|\x1b[0m  \x1b[0;32m3\x1b[0m  \x1b[0;37m|\x1b[0m\n\x1b[0;37m|-----|-----|-----|\x1b[0m\n\x1b[0;37m|\x1b[0m  \x1b[0;31m4\x1b[0m  \x1b[0;37m|\x1b[0m  \x1b[0;34m5\x1b[0m  \x1b[0;37m|\x1b[0m  \x1b[0;32m6\x1b[0m  \x1b[0;37m|\x1b[0m\n\x1b[0;37m|-----|-----|-----|\x1b[0m\n\x1b[0;37m|\x1b[0m  \x1b[0;31m7\x1b[0m  \x1b[0;37m|\x1b[0m  \x1b[0;34m8\x1b[0m  \x1b[0;37m|\x1b[0m  \x1b[0;32m9\x1b[0m  \x1b[0;37m|\x1b[0m\n'


def test_rows_and_columns_with_colours():
    assert Table.create(
        [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
        ['a', 'b', 'c'],
        row_colours=[Colour.red, Colour.blue],
        column_colours=[Colour.green]
    ) == '\x1b[0;37m|\x1b[0m  a  \x1b[0;37m|\x1b[0m  b  \x1b[0;37m|\x1b[0m  c  \x1b[0;37m|\x1b[0m\n\x1b[0;37m|-----|-----|-----|\x1b[0m\n\x1b[0;37m|\x1b[0m  \x1b[0;32m1\x1b[0m  \x1b[0;37m|\x1b[0m  \x1b[0;31m2\x1b[0m  \x1b[0;37m|\x1b[0m  \x1b[0;31m3\x1b[0m  \x1b[0;37m|\x1b[0m\n\x1b[0;37m|-----|-----|-----|\x1b[0m\n\x1b[0;37m|\x1b[0m  \x1b[0;32m4\x1b[0m  \x1b[0;37m|\x1b[0m  \x1b[0;34m5\x1b[0m  \x1b[0;37m|\x1b[0m  \x1b[0;34m6\x1b[0m  \x1b[0;37m|\x1b[0m\n\x1b[0;37m|-----|-----|-----|\x1b[0m\n\x1b[0;37m|\x1b[0m  \x1b[0;32m7\x1b[0m  \x1b[0;37m|\x1b[0m  \x1b[0;31m8\x1b[0m  \x1b[0;37m|\x1b[0m  \x1b[0;31m9\x1b[0m  \x1b[0;37m|\x1b[0m\n'


def test_multiple_header_colours():
    assert Table.create(
        [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
        ['a', 'b', 'c'],
        header_colours=[Colour.red, Colour.yellow, Colour.red],
    ) == '\x1b[0;37m|\x1b[0m  \x1b[0;31ma\x1b[0m  \x1b[0;37m|\x1b[0m  \x1b[0;33mb\x1b[0m  \x1b[0;37m|\x1b[0m  \x1b[0;31mc\x1b[0m  \x1b[0;37m|\x1b[0m\n\x1b[0;37m|-----|-----|-----|\x1b[0m\n\x1b[0;37m|\x1b[0m  1  \x1b[0;37m|\x1b[0m  2  \x1b[0;37m|\x1b[0m  3  \x1b[0;37m|\x1b[0m\n\x1b[0;37m|-----|-----|-----|\x1b[0m\n\x1b[0;37m|\x1b[0m  4  \x1b[0;37m|\x1b[0m  5  \x1b[0;37m|\x1b[0m  6  \x1b[0;37m|\x1b[0m\n\x1b[0;37m|-----|-----|-----|\x1b[0m\n\x1b[0;37m|\x1b[0m  7  \x1b[0;37m|\x1b[0m  8  \x1b[0;37m|\x1b[0m  9  \x1b[0;37m|\x1b[0m\n'


def test_header_colour():
    assert Table.create(
        [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
        ['a', 'b', 'c'],
        header_colour=Colour.cyan,
    ) == '\x1b[0;37m|\x1b[0m  \x1b[0;36ma\x1b[0m  \x1b[0;37m|\x1b[0m  \x1b[0;36mb\x1b[0m  \x1b[0;37m|\x1b[0m  \x1b[0;36mc\x1b[0m  \x1b[0;37m|\x1b[0m\n\x1b[0;37m|-----|-----|-----|\x1b[0m\n\x1b[0;37m|\x1b[0m  1  \x1b[0;37m|\x1b[0m  2  \x1b[0;37m|\x1b[0m  3  \x1b[0;37m|\x1b[0m\n\x1b[0;37m|-----|-----|-----|\x1b[0m\n\x1b[0;37m|\x1b[0m  4  \x1b[0;37m|\x1b[0m  5  \x1b[0;37m|\x1b[0m  6  \x1b[0;37m|\x1b[0m\n\x1b[0;37m|-----|-----|-----|\x1b[0m\n\x1b[0;37m|\x1b[0m  7  \x1b[0;37m|\x1b[0m  8  \x1b[0;37m|\x1b[0m  9  \x1b[0;37m|\x1b[0m\n'


long_text = 'Zombie ipsum brains reversus ab cerebellum viral inferno, brein nam rick mend grimes malum cerveau cerebro.'


def test_text_wrap():
    assert Table.create(
        [[long_text[:10], long_text[:55], long_text[:25]],
         [long_text[:5], long_text[:12], long_text[:33]],
         [long_text[:12], long_text, long_text[:2]]],
        ['a', 'b', 'c'],
        max_column_width=20,
        max_column_widths=(None, None, 40),
        use_ansi=False
    ) == '|  a             |  b                     |  c                                  |\n|----------------|------------------------|-------------------------------------|\n|  Zombie ips    |  Zombie ipsum brains   |  Zombie ipsum brains rever          |\n|                |  reversus ab cerebell  |                                     |\n|                |  um viral infern       |                                     |\n|----------------|------------------------|-------------------------------------|\n|  Zombi         |  Zombie ipsum          |  Zombie ipsum brains reversus ab c  |\n|----------------|------------------------|-------------------------------------|\n|  Zombie ipsum  |  Zombie ipsum brains   |  Zo                                 |\n|                |  reversus ab cerebell  |                                     |\n|                |  um viral inferno, br  |                                     |\n|                |  ein nam rick mend gr  |                                     |\n|                |  imes malum cerveau c  |                                     |\n|                |  erebro.               |                                     |\n'


def test_text_wrap_colour():
    assert Table.create(
        [[long_text[:14], long_text[:12], long_text[:35]],
         [long_text[:17], long_text[:4], long_text[:56]],
         [long_text[:21], long_text[:5], long_text]],
        ['a', 'b', 'c'],
        max_column_width=20,
        column_colours=[Colour.red, Colour.blue, Colour.green]
    ) == '\x1b[0;37m|\x1b[0m  a                     \x1b[0;37m|\x1b[0m  b             \x1b[0;37m|\x1b[0m  c                     \x1b[0;37m|\x1b[0m\n\x1b[0;37m|------------------------|----------------|------------------------|\x1b[0m\n\x1b[0;37m|\x1b[0m  \x1b[0;31mZombie ipsum b\x1b[0m        \x1b[0;37m|\x1b[0m  \x1b[0;34mZombie ipsum\x1b[0m  \x1b[0;37m|\x1b[0m  \x1b[0;32mZombie ipsum brains \x1b[0m  \x1b[0;37m|\x1b[0m\n\x1b[0;37m|\x1b[0m                        \x1b[0;37m|\x1b[0m                \x1b[0;37m|\x1b[0m  \x1b[0;32mreversus ab cer\x1b[0m       \x1b[0;37m|\x1b[0m\n\x1b[0;37m|------------------------|----------------|------------------------|\x1b[0m\n\x1b[0;37m|\x1b[0m  \x1b[0;31mZombie ipsum brai\x1b[0m     \x1b[0;37m|\x1b[0m  \x1b[0;34mZomb\x1b[0m          \x1b[0;37m|\x1b[0m  \x1b[0;32mZombie ipsum brains \x1b[0m  \x1b[0;37m|\x1b[0m\n\x1b[0;37m|\x1b[0m                        \x1b[0;37m|\x1b[0m                \x1b[0;37m|\x1b[0m  \x1b[0;32mreversus ab cerebell\x1b[0m  \x1b[0;37m|\x1b[0m\n\x1b[0;37m|\x1b[0m                        \x1b[0;37m|\x1b[0m                \x1b[0;37m|\x1b[0m  \x1b[0;32mum viral inferno\x1b[0m      \x1b[0;37m|\x1b[0m\n\x1b[0;37m|------------------------|----------------|------------------------|\x1b[0m\n\x1b[0;37m|\x1b[0m  \x1b[0;31mZombie ipsum brains \x1b[0m  \x1b[0;37m|\x1b[0m  \x1b[0;34mZombi\x1b[0m         \x1b[0;37m|\x1b[0m  \x1b[0;32mZombie ipsum brains \x1b[0m  \x1b[0;37m|\x1b[0m\n\x1b[0;37m|\x1b[0m  \x1b[0;31mr\x1b[0m                     \x1b[0;37m|\x1b[0m                \x1b[0;37m|\x1b[0m  \x1b[0;32mreversus ab cerebell\x1b[0m  \x1b[0;37m|\x1b[0m\n\x1b[0;37m|\x1b[0m                        \x1b[0;37m|\x1b[0m                \x1b[0;37m|\x1b[0m  \x1b[0;32mum viral inferno, br\x1b[0m  \x1b[0;37m|\x1b[0m\n\x1b[0;37m|\x1b[0m                        \x1b[0;37m|\x1b[0m                \x1b[0;37m|\x1b[0m  \x1b[0;32mein nam rick mend gr\x1b[0m  \x1b[0;37m|\x1b[0m\n\x1b[0;37m|\x1b[0m                        \x1b[0;37m|\x1b[0m                \x1b[0;37m|\x1b[0m  \x1b[0;32mimes malum cerveau c\x1b[0m  \x1b[0;37m|\x1b[0m\n\x1b[0;37m|\x1b[0m                        \x1b[0;37m|\x1b[0m                \x1b[0;37m|\x1b[0m  \x1b[0;32merebro.\x1b[0m               \x1b[0;37m|\x1b[0m\n'


def test_text_wrap_variable():
    assert Table.create(
        [[long_text[:14], long_text[:12], long_text[:35]],
         [long_text[:17], long_text[:4], long_text[:56]],
         [long_text[:21], long_text[:5], long_text]],
        ['a', 'b', 'c'],
        column_colours=[Colour.red, Colour.blue, Colour.green],
        max_column_widths=(30, 10)
    ) == '\x1b[0;37m|\x1b[0m  a                      \x1b[0;37m|\x1b[0m  b           \x1b[0;37m|\x1b[0m\n\x1b[0;37m|-------------------------|--------------|\x1b[0m\n\x1b[0;37m|\x1b[0m  \x1b[0;31mZombie ipsum b\x1b[0m         \x1b[0;37m|\x1b[0m  \x1b[0;34mZombie ips\x1b[0m  \x1b[0;37m|\x1b[0m\n\x1b[0;37m|\x1b[0m                         \x1b[0;37m|\x1b[0m  \x1b[0;34mum\x1b[0m          \x1b[0;37m|\x1b[0m\n\x1b[0;37m|-------------------------|--------------|\x1b[0m\n\x1b[0;37m|\x1b[0m  \x1b[0;31mZombie ipsum brai\x1b[0m      \x1b[0;37m|\x1b[0m  \x1b[0;34mZomb\x1b[0m        \x1b[0;37m|\x1b[0m\n\x1b[0;37m|-------------------------|--------------|\x1b[0m\n\x1b[0;37m|\x1b[0m  \x1b[0;31mZombie ipsum brains r\x1b[0m  \x1b[0;37m|\x1b[0m  \x1b[0;34mZombi\x1b[0m       \x1b[0;37m|\x1b[0m\n'


def test_prepare_max_column_widths_given_max_column_widths_is_none_returns_infinity():
    expected_widths = [float('inf'), float('inf'), float('inf')]
    max_column_widths = Table.prepare_max_column_widths(["a", "b", "c"], None, None)
    assert max_column_widths == expected_widths


def test_prepare_max_column_widths_given_max_column_widths_is_set_returns_max_col_widths_as_list():
    expected_widths = [30, 10]
    max_column_widths = Table.prepare_max_column_widths(["a", "b", "c"], (30, 10), None)
    assert max_column_widths == expected_widths


def test_prepare_max_column_widths_given_max_column_widths_is_string_returns_max_col_widths_string():
    expected_widths = "(30, 10)"
    max_column_widths = Table.prepare_max_column_widths(["a", "b", "c"], "(30, 10)", None)
    assert max_column_widths == expected_widths


def test_prepare_max_column_widths_given_max_column_widths_is_none_returns_max_col_widths_of_max_length():
    expected_widths = [20, 20, 20]
    max_column_widths = Table.prepare_max_column_widths(["a", "b", "c"], None, 20)
    assert max_column_widths == expected_widths


def test_wrap_test_given_text_less_than_width_doesnt_wrap():
    text_ = long_text[:10]
    expected_tuple = (text_,)
    text_tuple = Table.wrap_text(text_, 11)
    assert text_tuple == expected_tuple


def test_wrap_test_given_text_greater_than_width_wraps():
    text_ = long_text[:10]
    expected_tuple = (long_text[:8], long_text[8:10])
    text_tuple = Table.wrap_text(text_, 8)
    assert text_tuple == expected_tuple


def test_wrap_test_given_text_equal_to_width_wraps():
    text_ = long_text[:10]
    expected_tuple = (text_, '')
    text_tuple = Table.wrap_text(text_, 10)
    assert text_tuple == expected_tuple


def test_wrap_test_given_width_is_infinity_returns_text_as_string():
    text = "aaaaaa" * 100000
    expected = ("aaaaaa" * 100000,)
    assert Table.wrap_text(text, float('inf')) == expected


def test_get_row_height_given_cell_with_two_rows_returns_max_height():
    text_ = long_text[:10]
    assert Table.get_row_height([(text_,), (text_, text_), (text_, text_, text_)]) == 3


def test_get_row_height_given_cell_equal_rows_returns_max_height():
    text_ = long_text[:10]
    assert Table.get_row_height([(text_,), (text_,)]) == 1


def test_get_row_height_given_empty_returns_zero():
    assert Table.get_row_height([]) == 0


def test_get_column_widths_for_row_given_empty_returns_empty():
    assert Table.get_column_widths_for_row([]) == []


def test_get_column_widths_for_row_returns_max_widths():
    low_value = 10
    high_value = 25
    row = [(long_text[:low_value],), (long_text[:high_value], 'um')]
    assert Table.get_column_widths_for_row(row) == [low_value, high_value]


def test_get_wrapped_row_given_row_of_data_returns_wrapped_rows():
    expected_wrapped_row = [(long_text[:10],), (long_text[:5],), (long_text[:25],)]
    rows = Table.get_wrapped_row([long_text[:10], long_text[:5], long_text[:25]], [100, 100, 100])
    assert rows == expected_wrapped_row


def test_get_wrapped_row_given_empty_returns_empty():
    assert [] == Table.get_wrapped_row([], [])


def test_get_wrapped_row_given_row_of_data_returns_wrapped_rows():
    expected_wrapped_row = [(long_text[:5], long_text[5:10], '')]
    rows = Table.get_wrapped_row([long_text[:10]], [5])
    assert rows == expected_wrapped_row
