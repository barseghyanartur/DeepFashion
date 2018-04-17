from dataset_create import *



image_path_name = 'fashion_data/Img/img/Faux_Leather-Trim_Blouse/img_00000009.jpg'
dataset_image_path = 'dataset/test/Blouse/img_Faux_Leather-Trim_Blouse_img_00000009.jpg'
gt_x1, gt_y1, gt_x2, gt_y2 = [1, 26, 75, 75]


calculate_bbox_score_and_save_img(
    image_path_name,
    dataset_image_path,
    gt_x1, gt_y1, gt_x2, gt_y2
)
