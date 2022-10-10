import pytest
from madlib_cli.madlib import read_template, parse_template, merge,parse_template_story


def test_read_template_returns_stripped_string():
    actual = read_template("assets/dark_and_stormy_night_template.txt")
    expected = "It was a {Adjective} and {Adjective} {Noun}."
    assert actual == expected


# @pytest.mark.skip("pending")
def test_parse_template():
    actual_stripped, actual_parts = parse_template(
        "It was a {Adjective} and {Adjective} {Noun}."
    )
    expected_stripped = "It was a {} and {} {}."
    expected_parts = ("Adjective", "Adjective", "Noun")

    assert actual_stripped == expected_stripped
    assert actual_parts == expected_parts


# @pytest.mark.skip("pending")
def test_merge():
    actual = merge("It was a {} and {} {}.", ("dark", "stormy", "night"))
    expected = "It was a dark and stormy night."
    assert actual == expected


# @pytest.mark.skip("pending")
def test_read_template_raises_exception_with_bad_path():

    with pytest.raises(FileNotFoundError):
        path = "missing.txt"
        read_template(path)



#test for the madlib games 
with open("assets/story.txt") as f:
    file=f.read()


def test_parse_template_story():
    actual_stripped, actual_parts = parse_template_story(
        file
    )
    expected_stripped = """Make Me A Video Game!

I the {} and {} {} have {} {}'s {} sister and plan to steal her {} {}!

What are a {} and backpacking {} to do? Before you can help {}, you'll have to collect the {} {} and {} {} that open up the {} worlds connected to A {}'s Lair. There are {} {} and {} {} in the game, along with hundreds of other goodies for you to find."""
    expected_parts = ('Adjective', 'Adjective', 'A_First_Name', 'Past_Tense_Verb', 'A_First_Name', 'Adjective', 'Adjective', 'Plural_Noun', 'Large_Animal', 'Small_Animal', "A_Girl's_Name", 'Adjective', 'Plural_Noun', 'Adjective', 'Plural_Noun', 'Number_1-50', 'First_Name', 'Number', 'Plural_Noun', 'Number', 'Plural_Noun')

    assert actual_stripped == expected_stripped
    assert actual_parts == expected_parts


def test_merge_story():
    actual = merge("""Make Me A Video Game!

I the {} and {} {} have {} {}'s {} sister and plan to steal her {} {}!

What are a {} and backpacking {} to do? Before you can help {}, you'll have to collect the {} {} and {} {} that open up the {} worlds connected to A {}'s Lair. There are {} {} and {} {} in the game, along with hundreds of other goodies for you to find.""", ('Clever',"genius","Walaa","ate","Mazen","bags","cute","angry","dogs","ante","Bayan","smoll","pins","big","water","45","yahya","488","books","888","litter"))
    expected = """Make Me A Video Game!

I the Clever and genius Walaa have ate Mazen's bags sister and plan to steal her cute angry!

What are a dogs and backpacking ante to do? Before you can help Bayan, you'll have to collect the smoll pins and big water that open up the 45 worlds connected to A yahya's Lair. There are 488 books and 888 litter in the game, along with hundreds of other goodies for you to find."""
    assert actual == expected