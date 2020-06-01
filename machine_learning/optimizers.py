import torch.nn as nn
import torchvision
import torch

   
def get_optimizer(  ml_configs, 
                    model, 
                    checkpoint):
    """
    function for getting the optimizer:
    Args:
        ml_config(dict): machine learning config
        model: machine learning model
        checkpoint(dict): in case of transfer learning
    """
                     
    optimization_method = ml_configs["optimization_method"]
    parameters = ml_configs["optimization_parameters"]

    if optimization_method=="adam": 
        optimizer = torch.optim.Adam(model.parameters(),**parameters) 
    
    if optimization_method=="rmsprop": 
        optimizer = torch.optim.RMSprop(model.parameters(), **parameters)  

    if optimization_method=="sgd": 
        optimizer = torch.optim.SGD(model.parameters(),**parameters)  
    # transfer learning
    if checkpoint is not None:
        optimizer.load_state_dict(checkpoint['optimizer_state_dict'])
    
    return optimizer