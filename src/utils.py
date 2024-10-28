# Quick File to get the Speaker Name
import numpy as np 
import pandas as pd 

def extract_speaker(file_name):
    # Code to extract the file name
    label = file_name
    # Process it to get superfulous info out
    if "e" in label:
        label = label.split("e")[0].upper().strip()
        
    if "E" in label:
        label = label.split("E")[0].upper().strip()
        
    if "_" in label:
        label = label.split("_")[0].upper().strip()
        
    if "%" in label:
        label = label.split("%")[0].upper().strip()

    if "." in label:
        label = label.split(".")[0].upper().strip()

    return label

# Create a function to apply to the Diagnosis column in demographics.csv
def process_diagnosis(diagnosis):
    if pd.isnull(diagnosis):
        return np.nan
    if diagnosis == "N":
        return "N"
    else:
        return "Y"

def process_age(age):
    if pd.isnull(age):
        return np.nan
    if age < 20:
        return "Teens"
    elif age < 40:
        return "Adult"
    elif age < 65:
        return "Middle Age"
    elif age >= 65:
        return "Senior"
    else:
        return np.nan