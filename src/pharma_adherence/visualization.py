import matplotlib.pyplot as plt
import pandas as pd


def plot_hist(df: pd.DataFrame, column: str, label_rotation: int = 45) -> plt.Figure:
    #TODO: Plot a histogram for a numeric column.
    fig, ax = plt.subplots()
    data = df[column].dropna()
    ax.hist(data, bins=30, color='skyblue', edgecolor='black')
    ax.set_xlabel(column)
    ax.set_ylabel("Count")
    ax.tick_params(axis='x', labelrotation=label_rotation)
    ax.set_title(f"Distribution of {column}")
    return fig


def plot_bar(df: pd.DataFrame, categories: str, values: float, label_rotation: int = 45) -> plt.Figure:
    #TODO: Plot a bar plot for numeric categories and values.
    #      For multiple values per category, plot the average value per category
    fig, ax = plt.subplots()
    new_df = df.groupby(categories, dropna=False)[values].mean().sort_values()
    ax.bar(new_df.index, new_df, color='skyblue')
    ax.set_xlabel(categories)
    ax.set_ylabel(values)
    ax.tick_params(axis='x', labelrotation=label_rotation)
    ax.set_title(f"Bar Chart of {values} of {categories}")
    return fig


def plot_scatter(df: pd.DataFrame, x: float, y: float) -> plt.Figure:
    #TODO: Plot a scatter plot for numeric x and y values.
    fig, ax = plt.subplots()
    ax.scatter(df[x], df[y])
    ax.set_title(f"{x} vs {y}")
    ax.set_xlabel(x)
    ax.set_ylabel(y)
    return fig
