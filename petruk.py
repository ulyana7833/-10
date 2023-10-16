def print_star_digits():
    star_digits = {
        '0': [
            '  ***  ',
            ' *   * ',
            '*     *',
            '*     *',
            '*     *',
            ' *   * ',
            '  ***  '
        ],
        '1': [
            '   *   ',
            '  **   ',
            ' * *   ',
            '   *   ',
            '   *   ',
            '   *   ',
            ' ***** '
        ],
        '2': [
            '  ***  ',
            ' *   * ',
            ' *  *  ',
            '   *   ',
            '  *    ',
            ' *     ',
            ' ***** '
        ],
        '3': [
            ' ***** ',
            '     * ',
            '     * ',
            '  **** ',
            '     * ',
            '     * ',
            ' ***** '
        ],
        '4': [
            '    *  ',
            '   **  ',
            '  * *  ',
            ' *  *  ',
            '*******',
            '    *  ',
            '    *  '
        ]
    }
    numbers = input("Введите две цифры через пробел: ").split()
    for number in numbers:
        if number in star_digits:
            for line in star_digits[number]:
                print(line)
        else:
            print("Некорректный ввод. Введите число 0, 1, 2, 3 или 4.")

print_star_digits()