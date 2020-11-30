import argparse
import numpy as np
import pandas as pd
import torch

from matplotlib import pyplot as plt


if __name__ == '__main__':
    # DO NOT EDIT BLOCK - Required by the Makefile
    parser = argparse.ArgumentParser()
    parser.add_argument('--full', default=False, action='store_true')
    args = parser.parse_args()
    # END OF DO NOT EDIT BLOCK

    # Set random seeds for reproducibility.
    np.random.seed(0)
    torch.backends.cudnn.benchmark = False
    torch.backends.cudnn.deterministic = True
    torch.cuda.manual_seed_all(0)
    torch.manual_seed(0)

    # Add appropriate variables such as num_samples and num_epochs to construct the debug build.
    if args.full:
        num_samples = 200
    else:
        num_samples = 20

    # Create pdf images.
    data = torch.randn(num_samples)
    plt.figure(constrained_layout=True, figsize=(6, 2))
    plt.plot(data)
    plt.grid(True)
    plt.autoscale(enable=True, axis='x', tight=True)
    plt.title('Random data')
    plt.savefig('tmp/image.png')
    plt.close()

    # Create table.
    num_rows = 5
    num_columns = 8
    table = np.random.randn(num_rows, num_columns)
    df = pd.DataFrame(table)
    max_per_column_list = df.max(0)
    formatters = [lambda x,max_per_column=max_per_column: fr'\bf{{{x:.2f}}}' if (x == max_per_column) else f'{x:.2f}' for max_per_column in max_per_column_list]
    df.to_latex('tmp/table.tex', formatters=formatters, bold_rows=True, escape=False)

    # Create variables.
    df = pd.DataFrame({'key': ['num_samples', 'num_rows', 'num_columns'], 'value': [num_samples, num_rows, num_columns]})
    df.to_csv('tmp/keys-values.csv', index=False, float_format='%.1f')
