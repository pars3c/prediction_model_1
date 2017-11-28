import pandas as pd
def data_form2():
    csv_path = "survey_new.csv"
    data = pd.read_csv(csv_path, sep=",")
    df = pd.DataFrame(data)
    df["Country"] = df["Country"].replace(['United States', 'Canada', 'United Kingdom', 'Bulgaria', 'France', 'Portugal',
    'Netherlands', 'Switzerland', 'Latvia', 'Germany', 'Ireland', 'Romania',
    'Belgium', 'Sweden', 'New Zealand', 'Zimbabwe', 'Brazil', 'Spain', 'India',
    'Finland', 'Uruguay', 'Australia', 'Israel', 'Italy', 'Bosnia and Herzegovina',
    'Austria', 'Hungary', 'Singapore', 'Poland', 'Japan', 'Nigeria', 'Russia',
    'South Africa', 'Croatia', 'Norway', 'Thailand', 'Denmark', 'Mexico',
    'Bahamas', 'Greece', 'Moldova', 'Colombia', 'Georgia', 'China',
    'Czech Republic', 'Philippines', 'Slovenia', 'Costa Rica'],['1', '2', '3', '4', '5', '6',
    '7', '8', '9', '10', '11', '12',
    '13', '14', '15', '16', '17', '18', '19',
    '20', '21', '22', '23', '24', '25',
    '26', '27', '28', '29', '30', '31', '32',
    '33', '34', '35', '36', '37', '38',
    '39', '40', '41', '42', '43', '44',
    '45', '46', '47', '48'])
    df["Country"] = df["Country"].astype(int)

    return df["Country"]
def data_form():
    
    csv_path = "survey_new.csv"
    data = pd.read_csv(csv_path, sep=",")
    df = pd.DataFrame(data)

   
    df["Year"] = df.Timestamp.str.split("-").str.get(0)
    df["Year"] = df["Year"].astype(int)
    df["Month"] = df.Timestamp.str.split("-").str.get(1)
    df["Month"] = df["Month"].astype(int)
    df["Day"] = df.Timestamp.str.split("-").str.get(2)
    df["Day"] = df.Day.str.split(" ").str.get(0)
    df["Day"] = df["Day"].astype(int)
    df["Age"] = df["Age"].astype(int)
    df["Gender"] = df["Gender"].astype(int)
    
    df["Country"] = df["Country"].replace(['United States', 'Canada', 'United Kingdom', 'Bulgaria', 'France', 'Portugal',
    'Netherlands', 'Switzerland', 'Latvia', 'Germany', 'Ireland', 'Romania',
    'Belgium', 'Sweden', 'New Zealand', 'Zimbabwe', 'Brazil', 'Spain', 'India',
    'Finland', 'Uruguay', 'Australia', 'Israel', 'Italy', 'Bosnia and Herzegovina',
    'Austria', 'Hungary', 'Singapore', 'Poland', 'Japan', 'Nigeria', 'Russia',
    'South Africa', 'Croatia', 'Norway', 'Thailand', 'Denmark', 'Mexico',
    'Bahamas', 'Greece', 'Moldova', 'Colombia', 'Georgia', 'China',
    'Czech Republic', 'Philippines', 'Slovenia', 'Costa Rica'],['1', '2', '3', '4', '5', '6',
    '7', '8', '9', '10', '11', '12',
    '13', '14', '15', '16', '17', '18', '19',
    '20', '21', '22', '23', '24', '25',
    '26', '27', '28', '29', '30', '31', '32',
    '33', '34', '35', '36', '37', '38',
    '39', '40', '41', '42', '43', '44',
    '45', '46', '47', '48'])
    df["Country"] = df["Country"].astype(int)
    df["state"] = df["state"].fillna("NA").replace(['NA', 'IL', 'IN', 'TX', 'TN', 'MI', 'OH', 'CA', 'CT', 'MD', 'NY', 'NC', 'MA', 'IA', 'PA',
    'WA', 'WI', 'SC', 'OR', 'VT', 'UT', 'SD', 'CO', 'AL', 'OK', 'GA', 'NV', 'NJ', 'NH', 'ID',
    'MS', 'KY', 'AZ', 'VA', 'KS', 'MN', 'FL', 'RI', 'WY', 'MO', 'NM', 'NE', 'LA', 'DC', 'ME',
    'WV'], ['-9999', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15',
    '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30',
    '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45'
    ])
    df["state"] = df["state"].astype(int)
    df['self_employed'] = df['self_employed'].fillna("-9999").replace(["Yes", "No"], ["1", "0"])
    df["self_employed"] = df["self_employed"].astype(int)
    df['family_history'] = df['family_history'].replace(["Yes", "No"], ["1", "0"])
    df["family_history"] = df["family_history"].astype(int)
    df['treatment'] = df['treatment'].replace(["Yes", "No"], ["1", "0"])
    df["treatment"] = df["treatment"].astype(int)
    df['work_interfere'] = df['work_interfere'].fillna("-9999").replace(["Sometimes", "Often", "Rarely", "Never"], ["3", "2", "1", "0"])
    df["work_interfere"] = df["work_interfere"].astype(int)
    df['no_employees'] = df['no_employees'].replace(["1-5", "6-25", "26-100", "100-500", "500-1000", "More than 1000"], ["1", "2", "3", "4", "5", "6"])
    df["no_employees"] = df["no_employees"].astype(int)
    df['remote_work'] = df['remote_work'].replace(["Yes", "No"], ["1", "0"])
    df["remote_work"] = df["remote_work"].astype(int)
    df['tech_company'] = df['tech_company'].replace(["Yes", "No"], ["1", "0"])
    df["tech_company"] = df["tech_company"].astype(int)
    df['benefits'] = df['benefits'].replace(["Yes", "No", "Don't know"], ["1", "0", "-9999"])
    df["benefits"] = df["benefits"].astype(int)
    df['care_options'] = df['care_options'].replace(["Yes", "No", "Not sure"], ["1", "0", "-9999"])
    df["care_options"] = df["care_options"].astype(int)
    df['seek_help'] = df['seek_help'].replace(["Yes", "No", "Don't know"], ["1", "0", "-9999"])
    df["seek_help"] = df["seek_help"].astype(int)
    df['anonymity'] = df['anonymity'].replace(["Yes", "No", "Don't know"], ["1", "0", "-9999"])
    df["anonymity"] = df["anonymity"].astype(int)
    df['leave'] = df['leave'].replace(["Don't know", "Very easy", "Somewhat easy", "Somewhat difficult", "Very difficult"], ["-9999", "1", "2", "3", "4"])
    df["leave"] = df["leave"].astype(int)
    df['mental_health_consequence'] = df['mental_health_consequence'].replace(["Yes", "No", "Maybe"], ["1", "0", "-9999"])
    df["mental_health_consequence"] = df["mental_health_consequence"].astype(int)
    df['phys_health_consequence'] = df['phys_health_consequence'].replace(["Yes", "No", "Maybe"], ["1", "0", "-9999"])
    df["phys_health_consequence"] = df["phys_health_consequence"].astype(int)
    df['coworkers'] = df['coworkers'].replace(["Yes", "No", "Some of them"], ["1", "0", "2"])
    df["coworkers"] = df["coworkers"].astype(int)
    df['supervisor'] = df['supervisor'].replace(["Yes", "No", "Some of them"], ["1", "0", "2"])
    df["supervisor"] = df["supervisor"].astype(int)
    df['mental_health_interview'] = df['mental_health_interview'].replace(["Yes", "No", "Maybe"], ["1", "0", "-9999"])
    df["mental_health_interview"] = df["mental_health_interview"].astype(int)
    df['phys_health_interview'] = df['phys_health_interview'].replace(["Yes", "No", "Maybe"], ["1", "0", "-9999"])
    df["phys_health_interview"] = df["phys_health_interview"].astype(int)
    df['mental_vs_physical'] = df['mental_vs_physical'].replace(["Yes", "No", "Don't know"], ["1", "0", "-9999"])
    df["mental_vs_physical"] = df["mental_vs_physical"].astype(int)
    df['obs_consequence'] = df['obs_consequence'].replace(["Yes", "No"], ["1", "0"])
    df["obs_consequence"] = df["obs_consequence"].astype(int)
    df['wellness_program'] = df['wellness_program'].replace(["Yes", "No", "Don't know"], ["1", "0", "-9999"])
    df["wellness_program"] = df["wellness_program"].astype(int)
    
    return df