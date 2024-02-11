if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test

def camel_to_snake(camel_case):
    #break words
    for i in range (len (camel_case)-1):
        if ( (camel_case[i].islower() and camel_case[i+1].isupper())
        or (camel_case[i].isupper() and camel_case[i+1].isupper() and camel_case[i+2].islower())
        ):
            camel_case = camel_case[:i+1] + '_' + camel_case[i+1:] 
            i = i+1
    #lower
    snake_cases = camel_case.lower()
    return (snake_cases)

@transformer
def transform(data, *args, **kwargs):
    # transform column name & add column to partition to bucket
    new_col = []
    for i in data.columns:
        snake = camel_to_snake (i)
        new_col.append (snake)
    data.columns = new_col

    data ['lpep_pickup_date'] = data ['lpep_pickup_datetime'].dt.date

    return data


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
