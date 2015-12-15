# Apace webserver installation
package node.default[:package_type] do
  action :install
end

#Replace webserver configuration file
template node.default[:conf_file] do
  source node.default[:replace_conf]
  notifies :restart, "service[#{node.default[:package_type]}]"
end

#Replace PHP.INI file
template node.default[:php_ini] do
  source "php.ini.erb"
  notifies :restart, "service[#{node.default[:package_type]}]"
end

#Restart services
service node.default[:package_type] do
  service_name node.default[:package_type]
  action [:enable,:restart]
end
