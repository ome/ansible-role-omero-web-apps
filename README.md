OMERO Web Applications and Configuration
========================================

[![Build Status](https://travis-ci.org/ome/ansible-role-omero-web-apps.svg)](https://travis-ci.org/ome/ansible-role-omero-web-apps)
[![Ansible Role](https://img.shields.io/ansible/role/41131.svg)](https://galaxy.ansible.com/ome/omero_web_apps/)

Additional OMERO.web configuration.
This is primarily aimed to help with the configuration of OMERO.web applications/plugins, but can also be used to manage standard OMERO.web configuration properties.
This role only works with OMERO.web 5.3+ due to changes in the configuration handling.


Dependencies
------------

Assumes OMERO.web has already been installed in the standard location using the `openmicroscopy.omero-web` role.


Role Variables
--------------

All variables are optional:
- `omero_web_apps_names`: List of web application names to be appended to `omero.web.apps`
- `omero_web_apps_packages`: List of pip installable packages
- `omero_web_apps_top_links`: Lists of top link dictionaries to be appended to `omero.web.ui.top_links`, of the form:
  - `label`: Label
  - `link`: URL or a dict
  - `attrs`: Dictionary of attributes (optional)
- `omero_web_apps_ui_metadata_panes`: Items to be appended to `omero.web.ui.metadata_panes`
- `omero_web_apps_config_append`: Dictionary of other key-[list of values] pairs to be appended (multiple values can be appended to the same key)
- `omero_web_apps_config_set`: Dictionary of other key-value pairs to be set
- `omero_web_apps_config_name`: The basename of the configuration file (`web/config/{{ omero_web_apps_config_name }}.omero`)


Example
-------

TODO


Author Information
------------------

ome-devel@lists.openmicroscopy.org.uk
