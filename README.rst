Getting Started
===============

Target
------

Setting what wight-api you want to use is as easy as doing :code:`wight target-set <url>`.
This is required to start using wight.

Authenticating
--------------

An user account is required to use wight. To create your account (and subsequently
to authenticate) you should use :code:`wight login`.

Team Management
---------------

All projects being managed by wight must belong to a team. To create a project,
schedule jobs, and many other actions, users need to belong to teams. Look for
commands that end in "-team" for team management. To create a new team just use
:code:`wight create-team <team-name>`.

After the team is created, to add users to it, just use
:code:`wight adduser-team <team-name> <user-email>`.

Project Management
------------------

To schedule a test you need a project. Creating one is simple, once you have a team.
Just use :code:`wight project-create --team=<team-name> --project_name=<project-name> --repo=<git-repository>`.

Wight uses the git repository for the given project to clone it and run your tests.

Commands
========

Optional arguments for all commands:

--conf path configuration file path.
-h, --help  show this help message and exit
--debug     toggle debug output
--quiet     suppress all output

change-password
---------------

Change user password::

    $ wight change-password

default-get
-----------

Shows the defined default team and/or project::

    $ wight default-get

default-set
-----------

Arguments
^^^^^^^^^

* **--team** *<team-name>* ``not required``
* **--project** *<project-name>* ``not required``

Define default team and/or project to be used in subsequent commands::

    $ wight default-set --team <team-name> --project <project-name>

list
----

List load tests::

    $ wight list

login
-----

Log-in to wight (or register if user not found)::

    $ wight login

project-create
--------------

Arguments
^^^^^^^^^

* **project**  *<project-name>* ``positional``, ``required``
* **--team**  *<team-name>* ``not required`` if has a default team set with :code:`wight default-set` command. Otherwise is ``required``.
* **--repo**  *<git-repository>* ``required``

Creates a project to a team in the current target::

    $ wight project-create <project-name> --team <team-name> --repo <git-repository>

project-delete
--------------

parameters
^^^^^^^^^^

* **project** *<project-name>* - ``positional`` ``required``
* **--team** *<team-name>* - ``required`` (default team not implemented yet)

Deletes a project::

    $ wight project-delete <project-name> --team <team-name>


project-update
--------------

parameters
^^^^^^^^^^

* **project** *<project-name>* ``positional`` ``required``
* **--team** *<team-name>* ``required`` (default team not implemented yet)
* **--repo** *<new-git-repository>* ``required``

Updates a project to change its repository::

    $ wight project-update <project-name> --team <team-name> --repo <new-git-repository>

schedule
--------

parameters
^^^^^^^^^^

* **url** *<load-test-target-url>* ``positional`` ``required``
* **--team** *<team-name>* ``not required`` if has a default team set with :code:`wight default-set` command. Otherwise is ``required``.
* **--project** *<project-name>* ``not required`` if has a default project set with :code:`wight default-set` command. Otherwise is ``required``.

Schedules a new load test::

    $ wight schedule <load-test-target-url> --team <team-name> --project <project-name>

show
----

parameters
^^^^^^^^^^

* **load_test_uuid* *<uuid>* ``positional`` ``required``
* **--track** ``not required``


Show load tests

show-result
-----------

parameters
^^^^^^^^^^

* **load_test_uuid* *<uuid>* ``positional`` ``required``

Show load test results.

target-get
----------

Gets the target wight is using currently.

target-set
----------

parameters
^^^^^^^^^^

* **target* *<api-target-url>* ``positional`` ``required``

Sets target for wight to use.

team-adduser
------------

parameters
^^^^^^^^^^

* **user* *<user-email>* ``positional`` ``required``
* **--team* *<team-name>*   ``required`` (default team not implemented yet)

Adds user to a team

team-create
-----------

parameters
^^^^^^^^^^

* **team* *<team-name>* ``positional`` ``required``

Create a team.

team-delete
-----------

parameters
^^^^^^^^^^

* **team* *<team-name>* ``positional`` ``required``

Delete a team.

team-show
---------

parameters
^^^^^^^^^^

* **team* *<team-name>* ``positional`` ``required``

Show the registered team information.

team-update
-----------

parameters
^^^^^^^^^^

* **team* *<team-name>* ``positional`` ``required``

Updates a team.

team-removeuser
---------------

parameters
^^^^^^^^^^

* **user* *<user-email>* ``positional`` ``required``
* **--team* *<team-name>*   ``required`` (default team not implemented yet)

Removes a user from a team

user-info
---------

parameters
^^^^^^^^^^

* **user* *<user-email>* ``positional`` ``required``

Shows user info
