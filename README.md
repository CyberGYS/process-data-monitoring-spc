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
   - Synthetic process data is generated using a normal distribution to represent stable manufacturing conditions. Intentional anomalies are introduced to simulate process deviations.
     
2. Statistical Analysis
   - Key statistical parameters are calculated:
     - Mean (process center)
     - Standard deviation (process variation)
       
   - Control limits are defined using the 3-sigma rule:
     - UCL = mean + 3 × standard deviation
     - LCL = mean - 3 × standard deviation
   
3. Anomaly Detection
   - Data points outside the control limits are flagged as anomalies, representing potential process faults.
     
5. Visualization
   - A control chart is generated to display:
      - Process data points
      - Mean line
      - Upper and Lower Control Limits
   - This allows for visual identification of trends and out-of-control conditions. 

# Sample Output
<img width="556" height="435" alt="image" src="https://github.com/user-attachments/assets/cbcab4ed-baa7-4e67-a1fe-a52a953e3e8c" />

# Future Improvements
  - Integration with real manufacturing datasets
  - Real-time data monitoring
  - Implementation of additional SPC rules (e.g., Western Electric rules)
  - Dashboard visualization using Streamlit or Power BI
    
# Learning Outcomes
  - Understanding of SPC concepts in process monitoring
  - Application of statistical methods in engineering contexts
  - Data visualization for anomaly detection
  - Practical experience linking data analysis with manufacturing use case
