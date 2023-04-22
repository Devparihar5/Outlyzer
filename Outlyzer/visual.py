import matplotlib.pyplot as plt

def scatter_plot(data, x_column, y_column):
    """
    Creates a scatter plot of the data with the specified x and y columns.
    
    Parameters:
        -- data (DataFrame): The input data in DataFrame format
        -- x_column (str): The column name for x-axis
        -- y_column (str): The column name for y-axis
    
    Returns:
        None
    """
    plt.scatter(data[x_column], data[y_column])
    plt.xlabel(x_column)
    plt.ylabel(y_column)
    plt.title(f'Scatter plot of {x_column} vs {y_column}')
    plt.show()

def box_plot(data, column):
    """
    Creates a box plot of the data for the specified column.
    
    Parameters:
        -- data (DataFrame): The input data in DataFrame format
        -- column (str): The column name for box plot
    
    Returns:
        None
    """
    plt.boxplot(data[column])
    plt.xlabel(column)
    plt.title(f'Box plot of {column}')
    plt.show()
