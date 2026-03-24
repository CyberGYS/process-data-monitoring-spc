# Overview
This project demonstrates a basic implementation of Statistical Process Control (SPC) for monitoring process variation and detecting anomalies in manufacturing-style data.

The goal is to simulate how engineers track process stability using statistical methods and identify deviations that may indicate faults or abnormal conditions.

# Objectives
- Monitor process behavior using statistical metrics
- Establish control limits based on process data
- Detect anomalies beyond expected variation
- Visualize process trends using control charts

# Features
- Generation of simulated process data
- Calculation of:
  - Mean
  - Standard deviation
  - Upper Control Limit (UCL)
  - Lower Control Limit (LCL)
- Detection of out-of-control data points
- Visualization using control charts

# Libraries Used
- Python
- Numpy
- Matplotlib

# Methodology
1. Data Simulation
   Synthetic process data is generated using a normal distribution to represent stable manufacturing conditions. Intentional anomalies are introduced to simulate process deviations.
2. Statistical Analysis
   a) Key statistical parameters are calculated:
   - Mean (process center)
   - Standard deviation (process variation)
   
