# import torch
# import torchvision.transforms as transforms
# from PIL import Image
# import numpy as np
# import matplotlib.pyplot as plt
# import os
# from model import CSRNet   # uses your CSRNet definition

# # Load pretrained CSRNet
# def load_model(weight_path="weights/CSRNet_pretrained.pth"):
#     model = CSRNet()
#     checkpoint = torch.load(weight_path, map_location="cpu")
#     model.load_state_dict(checkpoint)
#     model.eval()
#     return model

# # Predict count from an image file
# def predict_image(model, file, save_density=True):
#     transform = transforms.Compose([
#         transforms.ToTensor(),
#         transforms.Normalize(mean=[0.485, 0.456, 0.406],
#                              std=[0.229, 0.224, 0.225])
#     ])

#     image = Image.open(file).convert('RGB')
#     img_tensor = transform(image).unsqueeze(0)

#     with torch.no_grad():
#         output = model(img_tensor)
#         density_map = output.squeeze(0).squeeze(0).numpy()
#         count = float(density_map.sum())

#     # Save density map visualization
#     density_path = None
#     if save_density:
#         filename = os.path.basename(file.filename) if hasattr(file, "filename") else "temp.jpg"
#         density_path = os.path.join("static", "density_" + filename)
#         plt.imshow(density_map, cmap='jet')
#         plt.axis('off')
#         plt.savefig(density_path, bbox_inches='tight')
#         plt.close()

#     return count, density_path

# model.py
# import torch
# import torch.nn as nn
# import torchvision.models as models

# class CSRNet(nn.Module):
#     def __init__(self, load_weights=False):
#         super(CSRNet, self).__init__()
#         self.seen = 0
#         self.frontend_feat = [64, 64, 'M', 128, 128, 'M',
#                               256, 256, 256, 'M', 512, 512, 512]
#         self.backend_feat = [512, 512, 512, 256, 128, 64]

#         self.frontend = make_layers(self.frontend_feat)
#         self.backend = make_layers(self.backend_feat, in_channels=512, dilation=True)
#         self.output_layer = nn.Conv2d(64, 1, kernel_size=1)

#         if load_weights:
#             mod = models.vgg16(pretrained=True)
#             self._initialize_weights()
#             for i, (k, v) in enumerate(self.frontend.state_dict().items()):
#                 v.data[:] = list(mod.state_dict().items())[i][1].data[:]
#         else:
#             self._initialize_weights()

#     def forward(self, x):
#         x = self.frontend(x)
#         x = self.backend(x)
#         x = self.output_layer(x)
#         return x

#     def _initialize_weights(self):
#         for m in self.modules():
#             if isinstance(m, nn.Conv2d):
#                 nn.init.kaiming_normal_(m.weight, mode='fan_out', nonlinearity='relu')
#                 if m.bias is not None:
#                     nn.init.constant_(m.bias, 0)
#             elif isinstance(m, nn.BatchNorm2d):
#                 nn.init.constant_(m.weight, 1)
#                 nn.init.constant_(m.bias, 0)


# def make_layers(cfg, in_channels=3, batch_norm=False, dilation=False):
#     """Helper function to build VGG-style layers."""
#     d_rate = 2 if dilation else 1
#     layers = []
#     for v in cfg:
#         if v == 'M':
#             layers += [nn.MaxPool2d(kernel_size=2, stride=2)]
#         else:
#             conv2d = nn.Conv2d(in_channels, v, kernel_size=3,
#                                padding=d_rate, dilation=d_rate)
#             if batch_norm:
#                 layers += [conv2d, nn.BatchNorm2d(v), nn.ReLU(inplace=True)]
#             else:
#                 layers += [conv2d, nn.ReLU(inplace=True)]
#             in_channels = v
#     return nn.Sequential(*layers)



import torch
import torch.nn as nn
import torchvision.models as models

class CSRNet(nn.Module):
    def __init__(self, load_weights=False):
        super(CSRNet, self).__init__()
        self.seen = 0
        
        # Frontend feature extractor layers (based on VGG16 architecture)
        self.frontend_feat = [64, 64, 'M', 128, 128, 'M',
                              256, 256, 256, 'M', 512, 512, 512]
        
        # Backend feature layers
        self.backend_feat = [512, 512, 512, 256, 128, 64]
        
        # Build the frontend and backend layers
        self.frontend = make_layers(self.frontend_feat)
        self.backend = make_layers(self.backend_feat, in_channels=512, dilation=True)
        
        # Output layer: 1 channel for the density map
        self.output_layer = nn.Conv2d(64, 1, kernel_size=1)
        
        # Initialize weights
        if load_weights:
            # Load weights from a pretrained VGG16 model
            mod = models.vgg16(pretrained=True)
            self._initialize_weights()
            for i, (k, v) in enumerate(self.frontend.state_dict().items()):
                v.data[:] = list(mod.state_dict().items())[i][1].data[:]
        else:
            self._initialize_weights()

    def forward(self, x):
        # Forward pass through the frontend and backend
        x = self.frontend(x)
        x = self.backend(x)
        x = self.output_layer(x)
        return x

    def _initialize_weights(self):
        """Initialize the model weights using He initialization."""
        for m in self.modules():
            if isinstance(m, nn.Conv2d):
                nn.init.kaiming_normal_(m.weight, mode='fan_out', nonlinearity='relu')
                if m.bias is not None:
                    nn.init.constant_(m.bias, 0)
            elif isinstance(m, nn.BatchNorm2d):
                nn.init.constant_(m.weight, 1)
                nn.init.constant_(m.bias, 0)

def make_layers(cfg, in_channels=3, batch_norm=False, dilation=False):
    """Helper function to build VGG-style layers."""
    d_rate = 2 if dilation else 1
    layers = []
    
    for v in cfg:
        if v == 'M':  # Max pooling layer
            layers += [nn.MaxPool2d(kernel_size=2, stride=2)]
        else:
            conv2d = nn.Conv2d(in_channels, v, kernel_size=3, padding=d_rate, dilation=d_rate)
            if batch_norm:
                layers += [conv2d, nn.BatchNorm2d(v), nn.ReLU(inplace=True)]
            else:
                layers += [conv2d, nn.ReLU(inplace=True)]
            in_channels = v
            
    return nn.Sequential(*layers)

