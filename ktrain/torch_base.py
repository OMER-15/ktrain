class TorchBase:
    """
    Utility methods for working pretrained Torch models
    """

    def __init__(self, device, quantize=False):
        try:
            import torch
        except (ImportError, OSError):
            raise Exception('This capability requires PyTorch to be installed. Please install for your environment: '+\
                            'https://pytorch.org/get-started/locally/')
        self.quantize = quantize
        self.torch_device = device
        if self.torch_device is None: self.torch_device = 'cuda' if torch.cuda.is_available() else 'cpu'


    def quantize_model(self, model):
        """
        quantize a model
        """
        import torch
        if self.torch_device == 'cpu':
            return torch.quantization.quantize_dynamic(model, {torch.nn.Linear}, dtype=torch.qint8)
        elif self.torch_device != 'cpu':
            return model.half()