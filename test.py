import os, time, pickle, argparse, networks, utils
import torch
import torch.nn as nn
import torch.optim as optim
import matplotlib.pyplot as plt
from torchvision import transforms
import config

parser = argparse.ArgumentParser()
parser.add_argument('--in_ngc', type=int, default=3, help='input channel for generator')
parser.add_argument('--out_ngc', type=int, default=3, help='output channel for generator')
parser.add_argument('--ngf', type=int, default=64)
parser.add_argument('--nb', type=int, default=8, help='the number of resnet block layer for generator')
parser.add_argument('--input_size', type=int, default=256, help='input size')
parser.add_argument('--pre_trained_model', default=config.PRE_TRAINED_MODEL_DIR, help='pre_trained cartoongan model path')
parser.add_argument('--image_dir', default=config.SOURCE_DIR, help='test image path')
parser.add_argument('--output_image_dir', default=config.TEST_OUTPUT_DIR, help='output test image path')
args = parser.parse_args()

device = config.DEVICE
if torch.backends.cudnn.enabled:
    torch.backends.cudnn.benchmark = True

G = networks.generator(args.in_ngc, args.out_ngc, args.ngf, args.nb)
if torch.cuda.is_available():
    G.load_state_dict(torch.load(args.pre_trained_model))
else:
    # cpu mode
    G.load_state_dict(torch.load(args.pre_trained_model, map_location=lambda storage, loc: storage))
G.to(device)

src_transform = transforms.Compose([
        transforms.Resize((args.input_size, args.input_size)),
        transforms.ToTensor(),
        transforms.Normalize(mean=(0.5, 0.5, 0.5), std=(0.5, 0.5, 0.5))
])
# utils.data_load(os.path.join('data', args.src_data), 'test', src_transform, 1, shuffle=True, drop_last=True)
image_src = utils.data_load(os.path.join(args.image_dir), 'test', src_transform, 1, shuffle=True, drop_last=True)

print("test starting")
with torch.no_grad():
    G.eval()
    for n, (x, _) in enumerate(image_src):
        x = x.to(device)
        G_recon = G(x)
        result = torch.cat((x[0], G_recon[0]), 2)
        path = os.path.join(args.output_image_dir, str(n + 1) + '.png')
        plt.imsave(path, (result.cpu().numpy().transpose(1, 2, 0) + 1) / 2)
print("test complete")

