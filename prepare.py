import pandas as pd
from sklearn.model_selection import train_test_split


def train_validate_test_split(df, target):
    train_validate, test = train_test_split(df, test_size=0.2,  
                                            stratify=df[target], random_state = 123)
    
    
    train, validate = train_test_split(train_validate, test_size=0.3, 
                                       stratify=train_validate[target], random_state = 123)
    return train, validate, test


def cancer_df(df):
    # Get just type of death for my target (Cancer / No Cancer)
    df = df[df['Type.of.Death'].notna()]

    # Drop columns that I will not use and have to many missing values
    df = df.drop(columns=['Child.Illness.Description', 'Child.Illness.Code', 'Description.of.Disease',
                'Illness.Code', 'Youth.Adult.Illness.Description', 'Code.of.Disease.Adult.Young.',
                'Patient.Code' , 'RCBP.Name', 'Date.of.Birth',
                'TNM', 'Extension', 'Statement', 'Topography.Code', 'Morphology.Description',
                'Code.of.Morphology', 'Description.of.Disease', 'Illness.Code', 'Description.of.Topography',
                'Date.of.Last.Contact', 'Date.of.Diagnostic', 'Distant.metastasis', 'Code.Profession',
                'Name.Occupation','Laterality', 'Date.of.Death','Naturality','Naturality.State', 'Status.Vital'])

    # Had ages at 199 which isnt possible
    df = df[df['Age'] <= 120]

    # Remove rows with missing values
    df = df[df['Diagnostic.means'].notna()]
    df = df[df['Indicator.of.Rare.Case'].notna()]
    df = df[df['Degree.of.Education'].notna()]

    # Fill in missing values with most common variable
    df['Raca.Color'] = df['Raca.Color'].fillna('BRANCO')
    df['Nationality'] = df['Nationality'].fillna('BRASIL')
    df['State.Civil'] = df['State.Civil'].fillna('CASADO')

    # Regex row variables with english names
    df['Degree.of.Education'] = df['Degree.of.Education'].replace(regex={r'^FUNDAMENTAL I .1. A 4. S.RIE.$': 'Fundamental I',
                  r'^FUNDAMENTAL II .5. A 8. S.RIE.$': 'Fundamental II',
                 r'^M.DIO .ANTIGO SEGUNDO GRAU.$': 'Former Second Degree',
                 'SEM ESCOLARIDADE': 'Without Education', 'SUPERIOR COMPLETO' : 'Graduated',
                 'SUPERIOR INCOMPLETO' : 'Incomplete High'})

    df['Type.of.Death'] = df['Type.of.Death'].replace(regex={r'^C.NCER$': 'Cancer', r'^N.O C.NCER$': 'No Cancer'})

    df['Gender'] = df['Gender'].replace(regex={r'^MASCULINO$': 'Male', r'^FEMININO$': 'Female', r'^IGNORADO$' : 'Ignored'})

    # Rename columns
    df.rename(columns={'State.Civil' : 'Legal_Status',
                  'Degree.of.Education' : 'Education',
                   'Type.of.Death' : 'Type_of_Death', 'Status.Address' : 'Status_Address',
                   'City.Address' : 'City_Address', 'Diagnostic.means' : 'Diagnostic_means',
                  'Raca.Color' : 'Race_Color', 'Indicator.of.Rare.Case' : 'Rare_Case'}, inplace=True)

    # Create dummy variables
    dummy_df = pd.get_dummies(df[['Gender', 'Type_of_Death', 'Education', 'Race_Color', 'Legal_Status']],
                             dummy_na = False, drop_first = [True])
    # add them to df
    df = pd.concat([df, dummy_df], axis = 1)

    df['Legal_Status_Casado'] = df['Legal_Status'] == 'CASADO'
    df.Legal_Status_Casado = df.Legal_Status_Casado.astype('uint8')
    
    # Renname new dummy variables
    df.rename(columns={'Type_of_Death_No Cancer': 'has_No_Cancer'}, inplace=True)
    return df