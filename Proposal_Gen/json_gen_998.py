#%%
import json
import os
import shutil

#%%

def save_to_json(data, output_file_path):
    with open(output_file_path, 'w') as output_file:
        json.dump(data, output_file, indent=2)

semester2code = { "sp":"01", "spr":"01", "spring":"01", "su":"02", "sum":"02", "summer":"02", "fa":"03", "fall":"03"}
thisfilename = os.path.basename(__file__)

data_to_save = \
    {
        # -----------------------------------------------------------------------------------------------------------------------
        "Version":
            """998""",
        # -----------------------------------------------------------------------------------------------------------------------
        "Year":
            """2024""",
        # -----------------------------------------------------------------------------------------------------------------------
        "Semester":
            """Spring""",
        # -----------------------------------------------------------------------------------------------------------------------
        "project_name":
            """Healthcare Shopping in VT """,
        # -----------------------------------------------------------------------------------------------------------------------
        "Objective":
            """ 
            The purpose of this test is to determine whether the Jan 1, 2021 CMS rule change on hospital price transparency lead to venue shopping for healthcare.
            """,
        # -----------------------------------------------------------------------------------------------------------------------
        "Dataset":
            """
            Vermont All-Payer Claims Database.  
            """,
        # -----------------------------------------------------------------------------------------------------------------------
        "Rationale":
            """
            Significant price variation exists in Vermont hospitals. Cost of echocardiograph ranges from 310-3,000 in Vermont. (2021)
            There is no appreciable quality difference between locations. The purpose of this is to determine whether
            greater transparency led to more venue shopping for patients, which could be a key mechanism for reducing costs in one of the most
            expensive states in the country.
            """,
        # -----------------------------------------------------------------------------------------------------------------------
        "Approach":
            """
            I plan on approaching this capstone through several steps.  

            1. Lit review on price transparency and venue shopping. 
            2. Data cleaning and merging
            2. Generate descriptive statistics on price variation and the sample population
            3. Identify key variables
            4. Create model (probably DID) 
            5. Robustness testing, writeup
            """,
        # -----------------------------------------------------------------------------------------------------------------------
        "Timeline":
            """
            This a rough time line for this project:  

            - (2 Weeks) Lit review 
            - (1 Weeks) Web layout  
            - (1 Weeks) Data cleaning and merging  
            - (4 Weeks) Generating model, robustness testing 
            - (2 Weeks) Creating writeup 
            - (2 Weeks) Finalization and editing
            - (2 Weeks) Documentation
            """,
        # -----------------------------------------------------------------------------------------------------------------------
        "Expected Number Students":
            """
            One (1). 
            """,
        # -----------------------------------------------------------------------------------------------------------------------
        "Possible Issues":
            """
            Data usage and access. The data is proprietary, and most of the work will be conducted locally on another computer.
            """,
        # -----------------------------------------------------------------------------------------------------------------------
        "Proposed by": "Daniel Bandler",
        "Proposed by email": "dbandler@gwu.edu",
        "instructor": "Sushovan Majhi",
        "instructor_email": "SushovanMajhi@gwu.edu",
        "github_repo": "https://github.com/GW-datasci/25-spring-DBandler/blob/adba7de72079b24c85d129317a9451efaf0a5754/Readme.md",
        # -----------------------------------------------------------------------------------------------------------------------
    }
os.makedirs(
    os.getcwd() + f'{os.sep}Proposals{os.sep}{data_to_save["Year"]}{semester2code[data_to_save["Semester"].lower()]}{os.sep}{data_to_save["Version"]}',
    exist_ok=True)
output_file_path = os.getcwd() + f'{os.sep}Proposals{os.sep}{data_to_save["Year"]}{semester2code[data_to_save["Semester"].lower()]}{os.sep}{data_to_save["Version"]}{os.sep}'
save_to_json(data_to_save, output_file_path + "input.json")
shutil.copy(thisfilename, output_file_path)
print(f"Data saved to {output_file_path}")
