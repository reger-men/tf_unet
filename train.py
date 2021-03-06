from __future__ import division, print_function

import matplotlib.pyplot as plt
import matplotlib
import numpy as np
plt.rcParams['image.cmap'] = 'gist_earth'
np.random.seed(98765)

from tf_unet import image_gen
from tf_unet import unet
from tf_unet import util

nx = 3072
ny = 3072



generator = image_gen.GrayScaleDataProvider(nx, ny, cnt=20)
x_test, y_test = generator(1)
print(generator.channels)

'''
fig, ax = plt.subplots(1,2, sharey=True, figsize=(8,4))
ax[0].imshow(x_test[0,...,0], aspect="auto")
ax[1].imshow(y_test[0,...,1], aspect="auto")
'''

net = unet.Unet(channels=generator.channels, n_class=generator.n_class, layers=3, features_root=16)
trainer = unet.Trainer(net, optimizer="momentum", opt_kwargs=dict(momentum=0.2))
path = trainer.train(generator, "./unet_trained", training_iters=32, epochs=10, display_step=2)
