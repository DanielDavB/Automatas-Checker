def u3_grammars(sentence, grammar):
    original = sentence
    res = False

    def S(str="", rule=None):
        nonlocal res
        if not rule:
            rule = list(grammar.keys())[0]
            str = list(grammar.keys())[0]

        rIncluded = any(value in str for value in grammar.keys())
        if rIncluded and len(str) <= len(original):
            for i in range(len(grammar[rule])):
                gen = str.replace(rule, grammar[rule][i])
                left = any(value in gen for value in grammar.keys())
                if left:
                    for index in range(len(grammar.keys())):
                        element = list(grammar.keys())[index]
                        if element in gen:
                            ver = S(gen, element)
                            if ver:
                                return True
                            else:
                                res = ver
                else:
                    if gen == original:
                        print(original + ' = ' + gen)
                        res = True
                        break
                    else:
                        res = False
                        break
        else:
            if str == original:
                return True
            else:
                res = False
        return res

    result = S()
    return result


grammars = {
    "grammar1": {
        "S": ["AB"],
        "A": ["aAA", "aA", "a"],
        "B": ["bB", "b"]
    },
    "grammar2": {
        "S": ["AB", "C"],
        "A": ["aAb", "ab"],
        "B": ["cBd", "cd"],
        "C": ["aCd", "aDd"],
        "D":["bDc", "bc"]
    },
    "grammar3": {
        "E": ["E+T", "T", ""],
        "T": ["T*F", "F"],
        "F": ["(E)", "a"]
    }
}

repeat_program = True

while repeat_program:
    print("Available grammars:")
    for index, grammar_name in enumerate(grammars.keys()):
        print(f"{index+1}. {grammar_name}")

    choice = input("Which grammar do you want to use? ")
    while not choice.isdigit() or int(choice) < 1 or int(choice) > len(grammars):
        choice = input("Invalid choice. Please enter a number between 1 and "
                    f"{len(grammars)}. ")

    selected_grammar_name = list(grammars.keys())[int(choice)-1]
    selected_grammar = grammars[selected_grammar_name]

    word = input(f"Enter a word to check using {selected_grammar_name}: ")
    result = u3_grammars(word, selected_grammar)
    if result:
        print(f"The word '{word}' is valid for {selected_grammar_name}.")
    else:
        print(f"The word '{word}' is not valid for {selected_grammar_name}.")

    repeat = input("Do you want to repeat the program? (y/n) ").lower()
    while repeat not in ['y', 'n']:
        repeat = input("Invalid input. Please enter 'y' or 'n'. ").lower()
    repeat_program = (repeat == 'y')