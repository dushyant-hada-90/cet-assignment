def get_components_by_roll(roll):
    """Return a tuple (comp1, comp2) for the given roll number (int).

    Ranges (inclusive):
    1-10: acetone-water
    11-20: methanol-water
    21-30: water-1,4-dioxane
    31-40: methanol-acetonitrile
    41-50: acetone-methanol
    51-60: methyl acetate-methanol
    61-65: methanol-benzene
    """
    if not isinstance(roll, int):
        raise TypeError('roll must be an integer')
    if 1 <= roll <= 10:
        return ('Acetone(1) - Water(2)')
    if 11 <= roll <= 20:
        return ('Methanol(1) - Water(2)')
    if 21 <= roll <= 30:
        return ('Water(1) - 1,4-Dioxane(2)')
    if 31 <= roll <= 40:
        return ('Methanol(1) - Acetonitrile(2)')
    if 41 <= roll <= 50:
        return ('Acetone(1) - Methanol(2)')
    if 51 <= roll <= 60:
        return ('Methyl acetate(1) - Methanol(2)')
    if 61 <= roll <= 65:
        return ('Methanol(1) - Benzene(2)')
    if 106 <= roll <= 116:
        return ('Acetone(1) - Methanol(2)')
    raise ValueError('roll number out of supported range (1-65)')


if __name__ == '__main__':
    try:
        r = int(input('Enter roll number (1-65): ').strip())
    except Exception:
        print('Invalid input')
    else:
        try:
            c1, c2 = get_components_by_roll(r)
            print(f'Roll {r}: {c1} - {c2}')
        except Exception as e:
            print(e)
