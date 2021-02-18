# installs puppet-lint 2.1.1
exec { 'modify php':
  path    => ['/bin', '/usr/bin'],
  command => 'sed -i 's/phpp/php/g' /var/www/html/wp-settings.php',
}
