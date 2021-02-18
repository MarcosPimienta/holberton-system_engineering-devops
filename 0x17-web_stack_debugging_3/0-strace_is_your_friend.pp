# installs puppet-lint 2.1.1
exec { 'modify php':
  path    => ['var/www/html/wp-settings.php', 'var/www/html/wp-settings.php',],
  command => 'sed -i 's/phpp/php/g' /var/www/html/wp-settings.php',
}
