# k8s-mirco-service-exam

[![Maintainability](https://api.codeclimate.com/v1/badges/7512a7b5c9ea8b06855c/maintainability)](https://codeclimate.com/repos/59b917fb42e2ce029e0015f8/maintainability)
[![CircleCI](https://circleci.com/gh/Seekster/api.svg?style=svg&circle-token=9ae970afd0c78faffb756491b02098a2627d6998)](https://circleci.com/gh/Seekster/api)



These instructions will get you a copy of the project up and running testing and purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

I recommend `gcloud CLI` and `kubectl` manage your command environments.

https://cloud.google.com/sdk/docs/install 

https://kubernetes.io/docs/tasks/tools/



## Connect Cluster Kubernetes

   Download Lens install on your computer and add file k8s.config to Lens

    https://k8slens.dev/




   or Connect Kubernetes(GKE) on Google GCP


## Installing on GCP Cloud

  Create Network VPC On GCP 
  https://www.cloudskillsboost.google/focuses/7140?parent=catalog


Create Cluster Kubernetes On GCP 
  ```
  gcloud container clusters create my-k8s-cluster --num-nodes 2 --network vpc-k8s --zone asia-southeast1 --tags private --scopes=storage-rw,compute-ro
  ```


Create Node Pool
  ```
  gcloud container node-pools create engin-pool --cluster=my-k8s-cluster --enable-autorepair --enable-blue-green-upgrade --machine-type=g1-small --enable-autoscaling --num-nodes=1  --min-nodes=1 --max-nodes=3 --max-surge-upgrade=1 --max-unavailable-upgrade=1 --spot --zone=asia-southeast1
  ```
