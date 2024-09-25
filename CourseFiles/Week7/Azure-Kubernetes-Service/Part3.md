# Part 3: Scaling the WordPress Application

## Introduction

### **Overview of the Lab Objectives**
- Manually scale the WordPress application deployed in Part 2.
- Understand the impact of scaling on application performance.
- Verify the scaling behavior of the application.

## Environment Setup

### **Prerequisites**
- Ensure you have completed Parts 1 and 2 of the lab.
- Confirm that both `kubectl` and `helm` CLI tools are installed and properly configured.

### **Enable Cluster Autoscaler**
- Update the AKS cluster configuration to enable the cluster autoscaler. Set appropriate minimum and maximum node counts based on your expected workload. 
- *Hint: Use AZ CLI to modify the AKS cluster settings.*

### **Verify Autoscaling Configuration**
- Check that the autoscaler is correctly set up by reviewing the node pool configurations, including the enabled status, and the minimum and maximum node counts.
- *Hint: Use the CLI to query the autoscaler settings.*

## Scale the WordPress Application

### **Check the Current Number of Pods**
- View the current number of WordPress pods running in your cluster.

### **Scale the Deployment**
- Increase the number of replicas in the WordPress deployment to improve availability and load balancing. Adjust the replica count to 3.

### **Verify the Scaling**
- Confirm that additional pods have been created in the deployment.
- *Hint: Check the list of pods in your namespace.*

### **Adjust the Scale Back**
- Reduce the number of replicas in the deployment to 2 to optimize resource usage.

### **Verify Again**
- Verify the current state of the deployment to ensure the number of replicas has been adjusted correctly.

## Next Steps
Proceed to Part 4 where you will learn how to secure and monitor the scaled application in AKS.