
"""
Convolutional layer resorces:
- https://www.kaggle.com/code/milan400/cnn-from-scratch-numpy/notebook
- https://thinkinfi.com/cnn/?utm_content=cmp-true
- https://www.youtube.com/watch?v=2-Ol7ZB0MmU
- https://www.youtube.com/watch?v=FmpDIaiMIeA
- https://www.youtube.com/watch?v=AgkfIQ4IGaM
- https://www.youtube.com/watch?v=HMcx-zY8JSg

"""


import numpy as np

class Conv:
    
    def __init__(self, num_filters):
        self.num_filters = num_filters
        
        #why divide by 9...Xavier initialization
        self.filters = np.random.randn(num_filters, 3, 3)/9
    
    def iterate_regions(self, image):
        #generates all possible 3*3 image regions using valid padding
        
        h,w = image.shape
        
        for i in range(h-2):
            for j in range(w-2):
                im_region = image[i:(i+3), j:(j+3)]
                yield im_region, i, j
                
    def forward(self, input):
        self.last_input = input
        
        h,w = input.shape
        
        output = np.zeros((h-2, w-2, self.num_filters))
        
        for im_regions, i, j in self.iterate_regions(input):
            output[i, j] = np.sum(im_regions * self.filters, axis=(1,2))
        return output
    
    def backprop(self, d_l_d_out, learn_rate):
        '''
        Performs a backward pass of the conv layer.
        - d_L_d_out is the loss gradient for this layer's outputs.
        - learn_rate is a float.
        '''
        d_l_d_filters = np.zeros(self.filters.shape)

        for im_region, i, j in self.iterate_regions(self.last_input):
            for f in range(self.num_filters):
                d_l_d_filters[f] += d_l_d_out[i,j,f] * im_region

        #update filters
        self.filters -= learn_rate * d_l_d_filters

        return None