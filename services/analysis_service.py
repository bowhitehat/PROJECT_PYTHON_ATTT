import os

def run_cleaning():
    os.system("python modules/data_cleaning.py")

def run_analysis():
    os.system("python modules/account_analysis.py")

def run_visualization():
    os.system("python modules/data_visualization.py")
