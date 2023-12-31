#!/usr/bin/python
# -*- coding:utf-8 -*-
from torch import nn
import warnings


# ----------------------------inputsize >=28-------------------------------------------------------------------------
class CNN(nn.Module):
    def __init__(self, in_channel=1, out_channel=4):
        super(CNN, self).__init__()


        self.layer1 = nn.Sequential(
            nn.Conv1d(in_channel, 4, kernel_size=2),  # 16, 26 ,26
            nn.BatchNorm1d(4),
            nn.ReLU(inplace=True))


        self.layer2 = nn.Sequential(
            nn.Conv1d(4, 8, kernel_size=2),  # 32, 24, 24
            nn.BatchNorm1d(8),
            nn.ReLU(inplace=True),
            nn.MaxPool1d(kernel_size=2, stride=2),
            )  # 32, 12,12     (24-2) /2 +1

        self.layer3 = nn.Sequential(
            nn.Conv1d(8, 8, kernel_size=2),  # 64,10,10
            nn.BatchNorm1d(8),
            nn.ReLU(inplace=True))

        self.layer4 = nn.Sequential(
            nn.Conv1d(8, 16, kernel_size=2),  # 128,8,8
            nn.BatchNorm1d(16),
            nn.ReLU(inplace=True),
            # nn.AdaptiveMaxPool1d(4))  # 128, 4,4
            )

        self.layer5 = nn.Sequential(
            nn.Conv1d(16, 16, kernel_size=2),  # 128,8,8
            nn.BatchNorm1d(16),
            nn.ReLU(inplace=True),
            # nn.AdaptiveMaxPool1d(4))  # 128, 4,4
            )

        self.layer6 = nn.Sequential(
            nn.Conv1d(16, 32, kernel_size=2),  # 128,8,8
            nn.BatchNorm1d(32),
            nn.ReLU(inplace=True),
            )  # 128, 4,4



        self.Adaplayer = nn.Sequential(
            nn.AdaptiveMaxPool1d(4))  # 128, 4,4


        self.layer7 = nn.Sequential(
            nn.Linear(4*4, 4),
            nn.ReLU(inplace=True),
            nn.Dropout())




    def forward(self, x):
        x = x.unsqueeze(1)
        x = self.layer1(x)
        # x = self.layer2(x)
        # x = self.layer3(x)
        # x = self.layer4(x)
        # x = self.layer5(x)
        # x = self.layer6(x)
        
        
        x = self.Adaplayer(x)
        x = x.view(x.size(0), -1)
        x = self.layer7(x)

        return x


    def fea(self,x):
        
        x = x.unsqueeze(1)
        x = self.layer1(x)
        # x = self.layer2(x)
        # x = self.layer3(x)
        # x = self.layer4(x)
        # x = self.layer5(x)
        # x = self.layer6(x)
        x = self.Adaplayer(x)
        x = x.view(x.size(0), -1)
        
        return x
        


