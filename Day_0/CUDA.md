# CUDA Installation Instructions

Below you will find step-by-step instructions to set up CUDA and cuDNN on your computer.

Please **read carefully and execute all commands in order**. If you run into any issues, don't hesitate to ask for help! :raising_hand:

Let's get started! :rocket:

---

## 1. Check System Compatibility

Before proceeding, ensure that your system meets the following requirements:

- A **NVIDIA GPU** with CUDA Compute Capability ([Check here](https://developer.nvidia.com/cuda-gpus)).
- **Linux or Windows** operating system, Apple computer do not come with NVIDIA Chips.
- **Latest NVIDIA drivers** installed.
- At least **4GB of VRAM**.

If available, you can verify your GPU model (and follow it's usage) using the command:

```bash
nvidia-smi
```
---

## 2. Install NVIDIA Drivers

If you haven’t installed the latest NVIDIA drivers, follow these steps:

### **Windows**
1. From [NVIDIA Driver Downloads](https://www.nvidia.com/download/index.aspx), in the manual driver search.
2. Install the driver and restart your computer.

### **Linux**

Run the following command:

```bash
sudo apt update && sudo apt upgrade -y
sudo apt install -y nvidia-driver-535
```

Replace `535` with the latest driver version available.

After installation, **reboot** your system:

```bash
sudo reboot
```

Once rebooted, check if the driver is working:

```bash
nvidia-smi
```

If you see a list of your GPU(s), you're good to go!

---

## 3. Install CUDA Toolkit

To enable GPU programming, the CUDA Toolkit is necessary.
Download and install the CUDA Toolkit from [NVIDIA’s official site](https://developer.nvidia.com/cuda-downloads).
Follow the selection steps for your OS, architecture and distribution.

### **Windows**
1. Download the **exe (network installer)**.
2. Select **Custom Install** and ensure the CUDA, Visual Studio integration, and Nsight tools are selected.
3. Follow the prompts and complete the installation.
4. Add CUDA to the system PATH:
    - Open `Control Panel > System > Advanced System Settings > Environment Variables`.
    - Edit the `Path` variable and add:
      ```
      C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\12.2\bin
      ```
    - Restart your computer.

### **Linux (Ubuntu-based)**

Follow the steps on the official site and make sure you're using the right version of ubuntu (or any other linux) for your installation. 

1. Download the installer:

   ```bash
   wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2204/x86_64/cuda-keyring_1.1-1_all.deb
   sudo dpkg -i cuda-keyring_1.0-1_all.deb
   ```

2. Install CUDA:

   ```bash
   sudo apt update
   sudo apt install -y cuda-toolkit-12-8
   ```

3. If not done automatically, add CUDA to PATH:

   ```bash
   echo 'export PATH=/usr/local/cuda/bin:$PATH' >> ~/.bashrc
   echo 'export LD_LIBRARY_PATH=/usr/local/cuda/lib64:$LD_LIBRARY_PATH' >> ~/.bashrc
   source ~/.bashrc
   ```

4. Verify installation:

   ```bash
   nvcc --version
   ```

   If you see CUDA version details, it's successfully installed! 🎉

---

## 4. Install cuDNN

Required for torch/tensorflow acceleration. 
Just like the CUDA toolkit, follow the selection steps for your OS, architecture and distribution.

### **Windows**

1. Download cuDNN from the [NVIDIA cuDNN website](https://developer.nvidia.com/cudnn-downloads).
2. Select the version 12 installer.
3. If needed, download the installation instruction: 
   ```powershell
   wget https://developer.download.nvidia.com/compute/cudnn/redist/cudnn/windows-x86_64/cudnn-windows-x86_64-9.8.0.87_cuda12-archive.zip
   ```
4. Restart your computer and verify the installation by running:

   ```powershell
   nvcc --version
   ```

### **Linux (Ubuntu-based)**

1. Download cuDNN from [NVIDIA cuDNN website](https://developer.nvidia.com/cudnn-downloads).
2. Follow the instruction after your architecture and version selection, unbuntu 22.04 example:

   ```bash
   wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2204/x86_64/cuda-keyring_1.1-1_all.deb
   sudo dpkg -i cuda-keyring_1.1-1_all.deb
   sudo apt-get update
   sudo apt-get -y install cudnn
   ```

3. Verify the installation:

   ```bash
   cat /usr/local/cuda/include/cudnn_version.h | grep CUDNN_MAJOR -A 2
   ```

   If you see version details, it's successfully installed! ✅

---

## 5. Verify CUDA and cuDNN Setup

Run the following command to check if CUDA is working correctly:

```bash
deviceQuery
```

If you see your GPU details, CUDA is properly set up! 🚀

To verify cuDNN, run:

```bash
testcudnn
```

If there are no errors, you're all set! 🎉

---

## 6. Install PyTorch with CUDA Support

For deep learning frameworks like PyTorch, install with CUDA acceleration:
The following command is for cuda 12.4, if you installed an other version please check your [pytorch install](https://pytorch.org/get-started/locally/)

```bash
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu124
```

Verify that PyTorch detects CUDA:

```python
import torch
print(torch.cuda.is_available())  # Should print: True
print(torch.cuda.device_count())  # Should print: 1 (or more)
print(torch.cuda.get_device_name(0))  # Should print your GPU name
```

---

## 7. Troubleshooting

- **CUDA not found?** Ensure `nvcc --version` prints a valid version.
- **cuDNN issues?** Check if cuDNN files exist in `/usr/local/cuda/lib64`.
- **PyTorch doesn’t detect CUDA?** Ensure you installed the correct version with `pip`.
- **System crashes or slow performance?** Update your NVIDIA drivers and ensure your system meets CUDA requirements.

---

