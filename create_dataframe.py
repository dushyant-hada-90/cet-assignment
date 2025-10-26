import pandas as pd

# Data transcribed from the provided image
rows = [
    {"System": "Acetone(1) - Water(2)", "V1_x10^3": 74.05, "V2_x10^3": 18.07, "Wilson_a12": 1219.5, "Wilson_a21": 6062.5, "NRTL_b12": 2642.1, "NRTL_b21": 5013.3, "alpha": 0.5343},
    {"System": "Methanol(1) - Water(2)", "V1_x10^3": 40.73, "V2_x10^3": 18.07, "Wilson_a12": 449.6, "Wilson_a21": 1965.9, "NRTL_b12": -1062.9, "NRTL_b21": 3538.7, "alpha": 0.2994},
    {"System": "1-Propanol(1) - Water(2)", "V1_x10^3": 75.14, "V2_x10^3": 18.07, "Wilson_a12": 3246.8, "Wilson_a21": 5660.1, "NRTL_b12": 2095.1, "NRTL_b21": 6852.0, "alpha": 0.5081},
    {"System": "Water(1) - 1,4-Dioxane(2)", "V1_x10^3": 18.07, "V2_x10^3": 85.71, "Wilson_a12": 7104.9, "Wilson_a21": -918.5, "NRTL_b12": 2997.6, "NRTL_b21": 2298.1, "alpha": 0.2920},
    {"System": "1,4-Dioxane(1) - Methanol(2)", "V1_x10^3": 85.71, "V2_x10^3": 40.73, "Wilson_a12": 2111.4, "Wilson_a21": 823.8, "NRTL_b12": 1439.0, "NRTL_b21": 1317.1, "alpha": 0.2981},
    {"System": "Acetonitrile(2) - Acetone(1)", "V1_x10^3": 66.30, "V2_x10^3": 74.05, "Wilson_a12": -677.8, "Wilson_a21": 2441.4, "NRTL_b12": 773.3, "NRTL_b21": 932.1, "alpha": 0.3084},
    {"System": "Methanol(2) - Methyl acetate(1)", "V1_x10^3": 40.73, "V2_x10^3": 79.84, "Wilson_a12": -130.6, "Wilson_a21": 3404.6, "NRTL_b12": 1597.1, "NRTL_b21": 1450.9, "alpha": 0.2965},
    {"System": "Methanol(1) - Benzene(2)", "V1_x10^3": 40.73, "V2_x10^3": 89.41, "Wilson_a12": 7261.7, "Wilson_a21": 766.4, "NRTL_b12": 3056.7, "NRTL_b21": 4921.2, "alpha": 0.4743},
    {"System": "766 Ethanol(1) - Toluene(2)", "V1_x10^3": 58.68, "V2_x10^3": 106.85, "Wilson_a12": 6516.5, "Wilson_a21": 881.4, "NRTL_b12": 2987.6, "NRTL_b21": 4805.9, "alpha": 0.5292},
]

cols = ["System", "V1_x10^3", "V2_x10^3", "Wilson_a12", "Wilson_a21", "NRTL_b12", "NRTL_b21", "alpha"]

df = pd.DataFrame(rows, columns=cols)

# Antoine parameters (A, B, C) transcribed from the attached Antoine table image for relevant species.
# Values are taken from the visible portion of the image. If a species is not found, values remain NaN.
antoine = {
    # name keys lowercased, simplified
    'acetone': {'A': 14.3154, 'B': 2756.22, 'C': 276.32},
    'acetic acid': {'A': 15.0717, 'B': 3580.80, 'C': 224.650},
    'acetonitrile': {'A': 14.8950, 'B': 341.0, 'C': 520.523},
    'benzene': {'A': 13.7819, 'B': 2726.81, 'C': 217.572},
    'ethanol': {'A': 16.6716, 'B': 3635.00, 'C': 121.0},
    'methanol': {'A': 15.1788, 'B': 3638.27, 'C': 144.0},
    '1-propanol': {'A': 14.8930, 'B': 3092.09, 'C': 165.0},
    'propanol': {'A': 14.8930, 'B': 3092.09, 'C': 165.0},
    '1-butanol': {'A': 13.6608, 'B': 2154.28, 'C': 289.79},
    'water': {'A': 14.5148, 'B': 3152.82, 'C': -32.0},
    'toluene': {'A': 14.9320, 'B': 3066.96, 'C': 217.625},
    'acetonitrile': {'A': 14.8950, 'B': 3414.0, 'C': 520.523},
    'dioxane': {'A': 13.9874, 'B': 3462.39, 'C': 134.0},
    'methyl acetate': {'A': 14.2366, 'B': 2766.92, 'C': 231.0},
    'methyl acetate': {'A': 14.2366, 'B': 2766.92, 'C': 231.0},
    'methyl acetate(1)': {'A': 14.2366, 'B': 2766.92, 'C': 231.0},
    'acetonitrile': {'A': 14.8950, 'B': 3414.0, 'C': 520.523},
}

import re

def normalize(name):
    # Remove parentheses content, remove digits and commas, normalize hyphens and whitespace, lowercase
    s = re.sub(r"\([^)]*\)", "", name)  # remove parentheses
    s = re.sub(r"[0-9]", "", s)            # remove all digits
    s = s.replace(',', ' ').replace('-', ' ')
    s = re.sub(r"\s+", ' ', s)
    return s.strip().lower()

# For each row, split system into left/right components and lookup Antoine params
def lookup_antoine_for_component(comp):
    key = normalize(comp)
    # Try direct match, then try first token match
    if key in antoine:
        return antoine[key]['A'], antoine[key]['B'], antoine[key]['C']
    first = key.split()[0]
    if first in antoine:
        return antoine[first]['A'], antoine[first]['B'], antoine[first]['C']
    return (float('nan'), float('nan'), float('nan'))

# Add columns
df[['A1','B1','C1']] = pd.DataFrame([[None,None,None]]*len(df))
df[['A2','B2','C2']] = pd.DataFrame([[None,None,None]]*len(df))

for i, row in df.iterrows():
    # split on ' - ' to separate components; if not present, try '-'
    parts = row['System'].split(' - ')
    if len(parts) == 1:
        parts = row['System'].split('-')
    left = parts[0].strip()
    right = parts[1].strip() if len(parts) > 1 else ''
    A1,B1,C1 = lookup_antoine_for_component(left)
    A2,B2,C2 = lookup_antoine_for_component(right)
    df.at[i,'A1'] = A1
    df.at[i,'B1'] = B1
    df.at[i,'C1'] = C1
    df.at[i,'A2'] = A2
    df.at[i,'B2'] = B2
    df.at[i,'C2'] = C2

if __name__ == '__main__':
    print(df.to_string(index=False))
    df.to_csv('table_with_antoine.csv', index=False)
    print('\nSaved table_with_antoine.csv')

if __name__ == '__main__':
    print(df.to_string(index=False))
    df.to_csv('table.csv', index=False)
    print('\nSaved table.csv')
