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

--conf      path configuration file path
-h, --help  show this help message and exit
--debug     toggle debug output
--quiet     suppress all output

target-get
----------

Gets the target api wight is currently using.

target-set
----------

parameters
^^^^^^^^^^

* **target** *<api-target-url>* ``positional`` ``required``

Sets target api use with wight.

login
-----

Log-in to wight (or register if user not found).

team-create
-----------

parameters
^^^^^^^^^^

* **team** *<team-name>* ``positional`` ``required``

Create a team.

team-show
---------

parameters
^^^^^^^^^^

* **team** *<team-name>* ``positional`` ``required``

Show the registered team information. The information include the projects registered for the team.

team-update
-----------

parameters
^^^^^^^^^^

* **team** *<actual-team-name>* ``positional`` ``required``
* **new-team** *<new-team-name>* ``positional`` ``required``

Updates a team to change it name.

team-delete
-----------

parameters
^^^^^^^^^^

* **team** *<team-name>* ``positional`` ``required``

Delete a team.

default-get
-----------

Shows the defined default team and/or project::

default-set
-----------

Arguments
^^^^^^^^^

* **--team** *<team-name>* ``not required``
* **--project** *<project-name>* ``not required``

Define default team and/or project to be used in subsequent commands.

project-create
--------------

Arguments
^^^^^^^^^

* **project**  *<project-name>* ``positional``, ``required``
* **--team**  *<team-name>* ``not required`` if has a default team set with :code:`wight default-set` command. Otherwise is ``required``.
* **--repo**  *<git-repository>* ``required``

Creates a project to a team in the current target.

project-update
--------------

parameters
^^^^^^^^^^

* **--project_name** *<new-project-name>* ``not required``
* **--repo** *<new-git-repository>* ``required``
* **--team**  *<team-name>* ``not required`` if has a default team set with :code:`wight default-set` command. Otherwise is ``required``.
* **--project** *<project-name>* ``not required`` if has a default project set with :code:`wight default-set` command. Otherwise is ``required``.

Updates a project to change its repository.

project-delete
--------------

parameters
^^^^^^^^^^

* **project** *<project-name>* - ``positional`` ``required``
* **--team** *<team-name>* - ``required`` (default team not implemented yet)

Deletes a project.

schedule
--------

parameters
^^^^^^^^^^

* **url** *<load-test-target-url>* ``positional`` ``required``
* **--team** *<team-name>* ``not required`` if has a default team set with :code:`wight default-set` command. Otherwise is ``required``.
* **--project** *<project-name>* ``not required`` if has a default project set with :code:`wight default-set` command. Otherwise is ``required``.

Schedules a new load test.

list
----

parameters
^^^^^^^^^^

* **--team** *<team-name>* - ``required`` if you pass **--project**, otherwise ``not-required``
* **--project** *<project-name>* - ``not-required``

List the last 3 load tests and its status (Scheduled, Running, Finished or Failure).
With **--team** will be listed the last 5 load test for each project of that team.
With **--team** and **--project** will be listed the las 20 load test for the project.

show
----

parameters
^^^^^^^^^^

* **load_test_uuid** *<uuid>* ``positional`` ``required``
* **--track** ``not required``

Show a specific load test and it status (Scheduled, Running, Finished or Failure).
If you pass **--track**, the command you run, each 5 sec, in loop to keep track for changes.
If the test finished or fail, the command will stop.

show-result
-----------

parameters
^^^^^^^^^^

* **load_test_uuid** *<uuid>* ``positional`` ``required``

Show a load test result. Will have some data for the test result and a URL to access the report web page for the result.

team-adduser
------------

parameters
^^^^^^^^^^

* **user** *<user-email>* ``positional`` ``required``
* **--team** *<team-name>*   ``required`` (default team not implemented yet)

Adds a user to a team.
You need to be the team owner or a team member to add another user to the team.

team-removeuser
---------------

parameters
^^^^^^^^^^

* **user** *<user-email>* ``positional`` ``required``
* **--team** *<team-name>*   ``required`` (default team not implemented yet)

Removes a user from a team.
You need to be the team owner or a team member to remover another user to the team.

user-info
---------

parameters
^^^^^^^^^^

* **user** *<user-email>* ``positional`` ``required``

Shows user info.

change-password
---------------

Change user password.