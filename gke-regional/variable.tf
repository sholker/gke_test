variable "region" {
  default = "us-west1"
}

variable "cluster_name" {
  default = "tf-regional"
}

variable "master_version" {
  default = ""
}

variable "node_count" {
  default = 1
}

variable "tags" {
  type        = list(string)
  default = []
}

variable "network" {
  default = "default"
}

variable "subnetwork" {
  default = "default"
}

