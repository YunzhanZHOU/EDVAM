# Overview
This is a 3D eye-tracking dataset for visual attention modeling in a virtual museum. It is also the first 3D eye-tracking dataset in a virtual environment.

[[Paper]](https://doi.org/10.1631/FITEE.2000318) 

[[Raw subset]](https://github.com/YunzhanZHOU/EDVAM/tree/main/raw_subset) [[Practical subset]](https://drive.google.com/drive/folders/11R0xZvpWLzO9ltPblBrFrMu8IOviTAlf?usp=sharing) [[Practical subset usage]](https://github.com/YunzhanZHOU/EDVAM/blob/main/practical%20_subset/usage.py)

[[Museum unity model]](https://drive.google.com/drive/folders/1G4-iare6AGVvW2L2Wye5gs1YA_Yf9LV0?usp=share_link)

# Raw subset
Each person's data corresponds to one CSC file.

Header | Definition
------ | ----------
`index` | index
`time` | timestamp
`L_x` | 3D PoG position x
`L_y` | 3D PoG position y
`L_z` | 3D PoG position z
`C_x` | camera's position x
`C_y` | camera's position y
`C_z` | camera's position z
`F_x` | camera's orientation x
`F_y` | camera's orientation y
`F_z` | camera's orientation z
`confidence` | detector’s measurement confidence
`gaze_norm_pos_x`, `gaze_norm_pos_y` | gaze location in normalized world camera coordinate
`norm_pos_x` ... `projected_sphere_axis_b` | 28 pupil paremeters, referred to [Pupil Labs](https://docs.pupil-labs.com/developer/core/overview/#pupil-datum-format)

# Practical subset
The practical subset is [here](https://drive.google.com/drive/folders/11R0xZvpWLzO9ltPblBrFrMu8IOviTAlf?usp=sharing). The usage is [here](https://github.com/YunzhanZHOU/EDVAM/blob/main/practical%20_subset/usage.py). This dataset is subdivided into a training set and a test set containing 190830 instances and 32530 instances, respectively.

The feature channels for one instance are as follows: 

Number | Feature
------ | -------
1 | `L_x`
2 | `L_y`
3 | `L_z`
4 | `C_x`
5 | `C_y`
6 | `C_z`
7 | `F_x`
8 | `F_y`
9 | `F_z`
10 | `confidence`
11 | `gaze_norm_pos_x`
12 | `gaze_norm_pos_y`
13 | `norm_pos_x`
14 | `norm_pos_y`
15 | `diameter`
16 | `ellipse_center_x`
17 | `ellipse_center_y`
18 | `ellipse_axis_a`
19 | `ellipse_axis_b`
20 | `ellipse_angle`
21 | `diameter_3d`
22 | `model_confidence`
23 | `model_id`
24 | `sphere_center_x`
25 | `sphere_center_y`
26 | `sphere_center_z`
27 | `sphere_radius`
28 | `circle_3d_center_x`
29 | `circle_3d_center_y`
30 | `circle_3d_center_z`
31 | `circle_3d_normal_x`
32 | `circle_3d_normal_y`
33 | `circle_3d_normal_z`
34 | `circle_3d_radius`
35 | `theta`
36 | `phi`
37 | `projected_sphere_center_x`
38 | `projected_sphere_center_y`
39 | `projected_sphere_axis_a`
40 | `projected_sphere_axis_b`
