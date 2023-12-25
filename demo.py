# import argparse
# import models


# # 创建ArgumentParser，并设置formatter_class
# parser = argparse.ArgumentParser(
#     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
# parser.add_argument('--preprocess', type=str, default='resize_and_crop',
#                     help='scaling and cropping of images at load time [resize_and_crop | crop | scale_width | scale_width_and_crop | none]')
# # 添加参数
# parser.add_argument('--no_dropout', action='store_true',
#                     help='no dropout for the generator')
# parser.add_argument('--suffix', default='{preprocess}', type=str,
#                     help='customized suffix: opt.name = opt.name + suffix: e.g., {model}_{netG}_size{load_size}')

# # 解析命令行参数
# opt = parser.parse_args()
# print(opt.preprocess)
# if 'resize' in opt.preprocess:
#     print(1)
# else:
#     print(2)
    
# a = [11, 2]
# b = [3, 4]
# c = a + b
# print(c)
# for i, data in enumerate(c):
#     print(i, data)
# save_suffix = 'iter_%d' % 3
# print(save_suffix)

for i in range(2):
    print(i)