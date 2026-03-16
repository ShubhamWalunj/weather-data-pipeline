def clean_data(data):
    # Remove duplicates
    data = data.drop_duplicates()
    # Fill missing values
    data = data.fillna(method='ffill')  # Forward fill as an example
    return data


def validate_data(data):
    # Ensure data conforms to expected types
    if not all(isinstance(value, (int, float)) for value in data['numeric_column']):
        raise ValueError('Numeric column has non-numeric values')
    # Additional validation logic here
    return True


def transform_data(data):
    # Example transformation: scaling a feature
    data['scaled_column'] = data['numeric_column'] / data['numeric_column'].max()
    return data