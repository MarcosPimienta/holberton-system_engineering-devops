#! usr/bin/env bash
file_line { 'Turn off passwd auth':
  ensure => present,
  path   => 'etc/ssh/ssh_config',
  line   => 'PasswordAuthentication no',
  match  => 'PasswordAuthentication yes',
}

file_line { 'Declare Identity':
  ensure => present,
  path   => 'etc/ssh/ssh_config',
  line   => 'IdentityFile ~/.ssh/holberton',
  match  => 'IdentityFile ~/.ssh/holberton',
}