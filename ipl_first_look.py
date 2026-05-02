import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import sys
import io

# 1. FIX: Force UTF-8 so emojis and special characters don't crash the terminal
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

df = pd.read_csv("matches.csv")

# First look
print("Shape:", df.shape)           # how many rows & columns
print("\nColumns:", df.columns.tolist())
print("\nFirst 5 rows:")
print(df.head())

# Basic info
print("\nData types:")
print(df.info())

# Any missing values?
print("\nMissing values:")
print(df.isnull().sum())

# Simple stat
print("\nBasic stats:")
print(df.describe())
