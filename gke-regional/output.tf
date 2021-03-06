output "instance_groups" {
  value = "${google_container_cluster.default.instance_group_urls}"
}

output "endpoint" {
  value = "${google_container_cluster.default.endpoint}"
}

output "client_certificate" {
  value = "${google_container_cluster.default.master_auth.0.client_certificate}"
}

output "client_key" {
  value = "${google_container_cluster.default.master_auth.0.client_key}"
}

output "cluster_ca_certificate" {
  value = "${google_container_cluster.default.master_auth.0.cluster_ca_certificate}"
}
