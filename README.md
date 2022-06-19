# Overview
This is Pytorch implementation of CartoonGAN [1] (CVPR 2018)
## Usage

### 1. Download [VGG19](https://download.pytorch.org/models/vgg19-dcbb9e9d.pth)

### 2. Train
```
python train.py
```
### 3. Test
```
python test.py
```
### Folder structure
The following shows basic folder structure.
```
├── data
│   ├── src_data # src data
│   │   ├── train
│   │   └── test
│   └── tgt_data # target data
│       ├── train
│       └── pair # edge-promoting results to be saved here
├── results
│   ├── test # test.py results to be saved
│   └── train # train.py results to be saved
│       ├── Reconstruction # pre-trained data to be saved
│       └── Transfer # trained data to be saved
│
├── train.py
├── test.py
├── edge_promoting.py
├── utils.py
├── networks.py
```

## Development Environment

* Apple M1 Pro
* python 3.8.13
* pytorch 1.11.0
* torchvision 0.12.0
* opencv 4.6.0

## Reference
[1] Chen, Yang, Yu-Kun Lai, and Yong-Jin Liu. "CartoonGAN: Generative Adversarial Networks for Photo Cartoonization." Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition. 2018.

(Full paper: http://openaccess.thecvf.com/content_cvpr_2018/papers/Chen_CartoonGAN_Generative_Adversarial_CVPR_2018_paper.pdf)
