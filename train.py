import torch
import os
from options.base_options import TrainOptions
from dataset.dataset import dataset_unpair, dataset_unpair_val
from models import create_model

def main():
    parser = TrainOptions()
    opts = parser.parse()

    print('\n--- load dataset ---')
    dataset = dataset_unpair(opts)
    train_loader = torch.utils.data.DataLoader(
        dataset, batch_size=opts.batch_size, shuffle=True, num_workers=opts.nThreads)
    dataset_val = dataset_unpair_val(opts)
    loader_val = torch.utils.data.DataLoader(
        dataset_val, batch_size=1, shuffle=False, num_workers=opts.nThreads)
    # TODO 加载并打印模型，创建学习率

    # TODO 可视化

    # TODO 加载预训练模型

    # TODO 开始训练


if __name__ == "__main__":
    main()
