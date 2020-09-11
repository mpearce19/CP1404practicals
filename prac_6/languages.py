# 4.
from prac_6.programming_language import ProgrammingLanguage


def main():
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

    print(python)
    languages = [ruby, python, visual_basic]

    print("The dynamically types languages are:")
    for language in languages:
        if language.is_dynamic():
            print(language.name)


main()
