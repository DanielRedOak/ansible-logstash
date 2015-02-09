logstash
=========

This role installs, configures, and adds a supervisor service for logstash using tar packages

Requirements
------------

This role installs, configures, and adds a supervisor service for logstash using tar packages

Role Variables
--------------
| variable | description | default | mandatory
|----------|-------------|---------|----------
| `logstash_state` | present or absent | present |
| `logstash_s3_bucket` | S3 bucket where tar file is located | | yes
| `logstash_s3_base` | base path to retrieve tar file from, not including filename | | yes
| `logstash_link` | create a link from the install dir to ./logstash | true |
| `logstash_remove_old` | remove old versions of logstash before installing | true |
| `logstash_setup_supervisor` | setup supervisor to manage the logstash process | true |
| `logstash_autostart` | start automatically on boot | true |
| `logstash_heap_size` | size of the heap to start logstash with | 500m |
| `logstash_java_opts` | java options to pass in at runtime | -Djava.io.tmpdir={{ logstash_install_path }}/logstash |
| `logstash_conf_dir` | path to configuration directory (.d type split configs are accepted by logstash) | /etc/logstash/conf.d |
| `logstash_opts` | extra options to start logstash with |  | no
| `logstash_log_dir` | path to log file logstash will write to | /var/log/logstash |
| `logstash_java_home` | override the java home logstash will use |  | no

Dependencies
------------

No dependencies.

Example Playbook
----------------

An example playbook is included in the test directory, but here is a rundown on typical usage.

    - hosts: all
      roles:
         - { role: logstash,
             logstash_version: 1.5.0.beta1,
             logstash_install_path: /opt,
             logstash_s3_bucket: sps-build-deploy,
             logstash_s3_base: /non-sps/elasticsearch/logstash/,
             logstash_java_home: /opt/java/java8
           }

License
-------

Apache 2.0

Author Information
------------------

Author: Ryan O'Keeffe (okeefferd@gmail.com)
