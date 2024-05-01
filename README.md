# Monocular Depth Estimation using MiDaS and openCV
Monocular Depth Estimation using MiDaS and openCV
This repository contains a Python script using the MiDaS (Mixed Data Sampling) model for real-time depth estimation. It utilizes OpenCV for webcam input, PyTorch for running the MiDaS model, and matplotlib for displaying the results.

## Overview
The script captures real-time video from your webcam, performs depth estimation using the MiDaS model, and displays the live video along with the corresponding depth map.

## Requirements
- Python 3.x
- OpenCV (`pip install opencv-python`)
- PyTorch (`pip install torch`)
- Matplotlib (`pip install matplotlib`)

## Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/real-time-depth-estimation.git
    cd real-time-depth-estimation
    ```

## Usage
1. Run the script using:
    ```bash
    python depth_estimation.py
    ```

2. Press 'q' to exit the real-time depth estimation.

## Results
- The depth map is displayed in real-time alongside the live webcam feed.
- The depth values are represented by the color map 'viridis'. Brighter regions indicate closer objects, while darker regions indicate farther objects.
- image result is ![midas result](https://github.com/delademf/midascv/assets/106419974/01f48e74-11e5-41af-935e-15218398b54a)


## Contributing
Feel free to contribute to this project by opening issues, suggesting improvements, or submitting pull requests. Your contributions are highly appreciated!

## License
This project is licensed under the [MIT License](LICENSE).

## Acknowledgments
- The MiDaS model is provided by Intel-isl and can be found [here](https://github.com/intel-isl/MiDaS).


