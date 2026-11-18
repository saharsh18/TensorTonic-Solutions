import numpy as np 
def min_max_scaling(data: list) -> list:
    """
    Returns each data column scaled to the range from 0 through 1.
    """
    # Write code here
    data=np.array(data)
    data_max=np.max(data,axis=0,keepdims=True)
    data_min=np.min(data,axis=0,keepdims=True)
    datascale=data_max-data_min
    datascale=np.where(datascale != 0, datascale, 1)
    data=data-data_min
    data=data/datascale
    return data.tolist()
    pass