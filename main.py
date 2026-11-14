from loader import load_json
from markdown_generator import render_markdown

def main():

    answers = load_json(
        "input/example_build_answers.json"
    )

    questions = load_json(
        "input/example_questions.json"
    )

    profile = build_profile(
        answers,
        questions
    )

    md = render_markdown(profile)

    with open(
        "output/me.md",
        "w",
        encoding="utf-8"
    ) as f:
        f.write(md)

if __name__ == "__main__":
    main()
