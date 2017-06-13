import testinfra.utils.ansible_runner
import json
import pytest

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    '.molecule/ansible_inventory').get_hosts('all')

OMERO = '/opt/omero/web/OMERO.web/bin/omero'


def assert_jcfg(Command, Sudo, key, value, isjson):
    with Sudo('omero-web'):
        cfg = Command.check_output("%s config get %s", OMERO, key)
    if isjson:
        cfg = json.loads(cfg)
    assert cfg == value


@pytest.mark.parametrize("key,value", [
    ('example.string', 'example value'),
])
#    ('example.boolean', True),
#    ('example.integer', 2),
def test_example_config(Command, Sudo, key, value):
    assert_jcfg(Command, Sudo, key, value, False)


def test_omero_web_apps(Command, Sudo):
    assert_jcfg(Command, Sudo, 'omero.web.apps', ["omero_mapr"], True)


def test_omero_web_mapr_config(Command, Sudo):
    expected = [
        [
            {
                "menu": "gene", "config": {
                    "default": ["Gene Symbol"],
                    "case_sensitive": True,
                    "all": ["Gene Symbol", "Gene Identifier"],
                    "ns": ["openmicroscopy.org/mapr/gene"],
                    "label": "Gene"
                }
            },
            {
                "menu": "genesupplementary",
                "config": {
                    "default": [],
                    "all": [],
                    "ns": ["openmicroscopy.org/mapr/gene/supplementary"],
                    "label": "Gene supplementary"
                }
            }
        ]
    ]
    assert_jcfg(Command, Sudo, 'omero.web.mapr.config', expected, True)


def test_omero_web_ui_toplinks(Command, Sudo):
    expected = [
        [
            "Data",
            "webindex",
            {"title": "Browse Data via Projects, Tags etc"}
        ],
        [
            "History",
            "history",
            {"title": "History"}
        ],
        [
            "Help",
            "http://help.openmicroscopy.org/",
            {"target": "new", "title": "Open OMERO user guide in a new tab"}
        ],
        [
            "OMERO",
            {
                "query_string": {"experimenter": -1},
                "viewname": "webindex"
            },
            {"title": "Image Data Repository"}
        ],
        [
            "Genes",
            {
                "query_string": {"experimenter": -1},
                "viewname": "maprindex_gene"
            },
            {"title": "Genes browser"}
        ]
    ]
    assert_jcfg(Command, Sudo, 'omero.web.ui.top_links', expected, True)
