case platform
  when "redhat","centos","fedora"
    node.default[:package_type] = "httpd"
    node.default[:conf_file] = "/etc/httpd/conf/httpd.conf"
    node.default[:replace_conf] = "httpd.conf.erb"
    node.default[:php_ini] = "/etc/php.ini"
  when "ubuntu","debian"
    node.default[:package_type] = "apache2"
    node.default[:conf_file] = "/etc/apache2/sites-enabled/000-default.conf"
    node.default[:replace_conf] = "000-default.conf.erb"
    node.default[:php_ini] = "/etc/php5/apache2/php.ini"
  else
    node.default[:package_type] = "apache2"
    node.default[:conf_file] = "/etc/apache2/sites-enabled/000-default.conf"
    node.default[:replace_conf] = "000-default.conf.erb"
    node.default[:php_ini] = "/etc/php5/apache2/php.ini"
end
