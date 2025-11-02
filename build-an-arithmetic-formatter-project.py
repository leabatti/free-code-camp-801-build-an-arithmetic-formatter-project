** start of main.py **

def arithmetic_arranger(problems, show_answers=False):
    # Limit to a maximum of five problems
    if len(problems) > 5:
        return "Error: Too many problems."

    # Prepare containers for each line of the output
    first_line = []
    second_line = []
    dashes_line = []
    answers_line = []

    for problem in problems:
        parts = problem.split()
        if len(parts) != 3:
            return "Error: Invalid format."

        left, operator, right = parts

        # Validate operator and operands
        if operator not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."
        if not left.isdigit() or not right.isdigit():
            return "Error: Numbers must only contain digits."
        if len(left) > 4 or len(right) > 4:
            return "Error: Numbers cannot be more than four digits."

        # Determine width based on the longest operand
        width = max(len(left), len(right)) + 2

        # Format each part of the problem
        first_line.append(left.rjust(width))
        second_line.append(operator + right.rjust(width - 1))
        dashes_line.append('-' * width)

        # Optionally calculate and format the result
        if show_answers:
            result = str(eval(problem))
            answers_line.append(result.rjust(width))

    # Join all parts with four spaces between problems
    arranged = '    '.join(first_line) + '\n' + \
               '    '.join(second_line) + '\n' + \
               '    '.join(dashes_line)

    if show_answers:
        arranged += '\n' + '    '.join(answers_line)

    return arranged

print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])}')

** end of main.py **

