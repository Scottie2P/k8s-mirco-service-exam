# k8s-mirco-service-exam
k8s-mirco-service-exam

These instructions will get you a copy of the project up and running testing and purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

I recommend `gcloud CLI` and `kubectl` manage your command environments.
https://cloud.google.com/sdk/docs/install 
https://kubernetes.io/docs/tasks/tools/


### Installing on GCP Cloud

Create Network VPC On GCP 
https://www.cloudskillsboost.google/focuses/7140?parent=catalog

Create Cluster Kubernetes On GCP 
  ```
  gcloud container clusters create my-k8s-cluster --num-nodes 2 --network vpc-k8s --zone asia-southeast1 --tags private --scopes=storage-rw,compute-ro
  ```
