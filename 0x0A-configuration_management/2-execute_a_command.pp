# installs puppet-lint 2.1.1
exec { 'killmenow':
  path    => ['/usr/bin', '/usr/sbin',],
  command => 'pkill killmenow',
}
