# puppet resource file /tmp/holberton
file { 'create':
  content => 'I love Puppet',
  group   => 'www-data',
  mode    => '0744',
  owner   => 'www-data',
  path    => '/tmp/holberton',
}
