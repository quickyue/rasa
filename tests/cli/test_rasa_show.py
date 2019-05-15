def test_show_stories_help(run):
    output = run("show", "stories", "--help")

    help_text = """usage: rasa show stories [-h] [-v] [-vv] [--quiet] [-d DOMAIN] [-s STORIES]
                         [-c CONFIG] [--output OUTPUT]
                         [--max-history MAX_HISTORY] [-nlu NLU_DATA]"""

    lines = help_text.split("\n")

    for i, line in enumerate(lines):
        assert output.outlines[i] == line
