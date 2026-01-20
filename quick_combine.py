#!/usr/bin/env python
# coding: utf-8
# Quick combine script for aggregate results

import os 
import pandas as pd

folder = 'tmpresults'
filelist = sorted(os.listdir(folder))

print('Combining aggregate results...')
pieces_file = []
for file in filelist:
    filename = os.path.join(folder, file)
    if file.startswith('aggregate_results_TC'):
        print(f"  Adding: {file}")
        df = pd.read_csv(filename)
        pieces_file.append(df)

if pieces_file:
    df_aggregate_results = pd.concat(pieces_file)
    output_file = 'tmpresults/aggregate_results.csv'
    df_aggregate_results.to_csv(output_file, index=False)
    print(f"\n✓ Created: {output_file}")
    print(f"  Total rows: {len(df_aggregate_results)}")
else:
    print("No aggregate_results files found!")

print('\nNow you can run: python imputation.py')
