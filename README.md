# ASPC Main Site #

To start hacking on the ASPC main site, you will need [Vagrant]. Once you have
Vagrant installed, navigate to this directory in your shell and run:

    vagrant up

This will set up a virtual machine running the ASPC mainsite application in
something approximating a production configuration. To see it in action, visit 
[http://localhost:8080/]. For development, log in with username `developer` and 
password `developer`.

To run management commands, you'll need to ssh in to the VM:

    $ vagrant ssh
    vagrant$ cd /vagrant
    vagrant$ ./manage.py shell_plus

#### The Briefest Intro to Vagrant ####

When you're done working, free up system resources with a `vagrant halt`. If you
want to start from scratch, `vagrant destroy` and then `vagrant up` anew.

(Applying future changes to the Vagrant setup will be done automatically when 
you `vagrant up`, but you can also run `vagrant provision` yourself.)

## Project Layout ##

Under the main `aspc` folder in this directory are several subfolders, most of
which are Django "apps":

  - `auth` — Django auth backend supporting Pomona College accounts
  - `blog` — The Senate Blog (shown on homepage)
  - `coursesearch` — Course search & schedule builder. 
    Includes management commands to sync with ITS course database
  - `eatshop` — Local business & discount directory
  - `folio` — Simple CMS to add pages to ASPC site
  - `housing` — Housing directory & reviews
  - `minutes` — History of ASPC minutes + summaries
  - `sagelist` — aka SageBooks, student-to-student textbook sales
  - `senate` — Positions, appointments, and documents. Includes functionality
    to apply appropriate permissions to Senators when they log in during or 
    after their tenure as senators

Folders without an `__init__.py` are not apps, but contain supporting files:

  - `fixtures` — Fixture data for Coop Fountain page
  - `maps` — Residence hall maps for Housing app
  - `static` — Static assets (CSS/JavaScript) used in the site
  - `templates` — Certain site-wide templates that don't fit in a
    particular app

And some apps are placeholders that have yet to be fleshed out or removed:

  - `courses` — Currently used only for the Term model
  - `events` — Unused (see Glean project)
  - `map` — Unused
  - `stream` — Unused (see notes on activity stream)
  - `vote` — Unused

[Vagrant]: http://vagrantup.com
[http://localhost:8080/]: http://localhost:8000/