# This Puppet manifest sets up the web_static environment
# Create the directory structure
file { '/data':
    ensure => 'directory',
}
file { '/data/web_static':
    ensure => 'directory',
}
file { '/data/web_static/releases':
    ensure => 'directory',
}
file { '/data/web_static/shared':
    ensure => 'directory',
}
# Create symbolic link for current directory
file { '/data/web_static/current':
    ensure => 'link',
    target => '/data/web_static/releases/test',
}
