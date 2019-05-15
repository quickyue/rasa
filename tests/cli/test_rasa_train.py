import os

from rasa.nlu.utils import list_files


def test_train(run_in_default_project):
    temp_dir = os.getcwd()

    run_in_default_project(
        "train",
        "-c",
        "config.yml",
        "-d",
        "domain.yml",
        "--data",
        "data",
        "--out",
        "train_models",
        "--fixed-model-name",
        "test-model",
        "--force",
    )

    assert os.path.exists(os.path.join(temp_dir, "train_models"))
    files = list_files(os.path.join(temp_dir, "train_models"))
    assert len(files) == 1
    assert os.path.basename(files[0]) == "test-model.tar.gz"


def test_train_core(run_in_default_project):
    run_in_default_project(
        "train",
        "core",
        "-c",
        "config.yml",
        "-d",
        "domain.yml",
        "--stories",
        "data",
        "--out",
        "train_rasa_models",
        "--store-uncompressed",
        "--fixed-model-name",
        "rasa-model",
    )

    assert os.path.exists("train_rasa_models")
    assert os.path.exists("train_rasa_models/core-rasa-model")
    assert os.path.isdir("train_rasa_models/core-rasa-model")


def test_train_nlu(run_in_default_project):
    run_in_default_project(
        "train",
        "nlu",
        "-c",
        "config.yml",
        "--nlu",
        "data/nlu.md",
        "--out",
        "train_models",
    )

    assert os.path.exists("train_models")
    files = list_files("train_models")
    assert len(files) == 1
    assert os.path.basename(files[0]).startswith("nlu-")


def test_train_help(run):
    help = run("train", "--help")

    help_text = """usage: rasa train [-h] [-v] [-vv] [--quiet] [--data DATA [DATA ...]]
                  [-c CONFIG] [-d DOMAIN] [--out OUT]
                  [--augmentation AUGMENTATION] [--debug-plots]
                  [--dump-stories] [--fixed-model-name FIXED_MODEL_NAME]
                  [--force] [--store-uncompressed]
                  {core,nlu} ..."""

    lines = help_text.split("\n")

    for i, line in enumerate(lines):
        assert help.outlines[i] == line


def test_train_nlu_help(run):
    help = run("train", "nlu", "--help")

    help_text = """usage: rasa train nlu [-h] [-v] [-vv] [--quiet] [-c CONFIG] [--out OUT]
                      [-u NLU] [--fixed-model-name FIXED_MODEL_NAME]
                      [--store-uncompressed]"""

    lines = help_text.split("\n")

    for i, line in enumerate(lines):
        assert help.outlines[i] == line


def test_train_core_help(run):
    help = run("train", "core", "--help")

    help_text = """usage: rasa train core [-h] [-v] [-vv] [--quiet] [-s STORIES] [-d DOMAIN]
                       [-c CONFIG [CONFIG ...]] [--out OUT]
                       [--augmentation AUGMENTATION] [--debug-plots]
                       [--dump-stories] [--force]
                       [--fixed-model-name FIXED_MODEL_NAME]
                       [--store-uncompressed]
                       [--percentages [PERCENTAGES [PERCENTAGES ...]]]
                       [--runs RUNS]"""

    lines = help_text.split("\n")

    for i, line in enumerate(lines):
        assert help.outlines[i] == line
