import torch
import torchvision
from torchvision.io import read_image
from torchvision.utils import draw_bounding_boxes


img = read_image('features_checked/1_0.pt')


box = [330,190,660,355]

box = torch.tensor(box)
box = box.unsqueeze(0)

img = draw_bounding_boxes(img, box, width = 5, colors="green", fill=True)

img = torchvision.transforms.ToPILImage()(img)

img.show()