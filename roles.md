---
layout: default
title: "Recent roles"
description: "I'm Robin Winslow, a web developer. Here are my recent roles."
---

<nav class="page-navigation">
    <ul>
        <li><a href="#lead-web-developer">Lead web developer</a></li>
        <li><a href="#lead-developer">Lead developer</a></li>
        <li><a href="#full-stack-developer">Full-stack developer</a></li>
        <li><a href="#previous-roles">Previous roles</a></li>
    </ul>
</nav>

Lead web developer
===

[Canonical Ltd.](http://canonical.com) - March 2014
---

Canonical Ltd. are the company behind [Ubuntu](https://en.wikipedia.org/wiki/Ubuntu), the [leading operating system in cloud services](https://www.zdnet.com/article/ubuntu-linux-continues-to-rule-the-cloud/). One of the biggest names in open-source, Canonical are a central contributor to [OpenStack](https://www.openstack.org/), provide market-leading solutions for [OpenStack](https://ubuntu.com/openstack) and [Kubernetes](https://ubuntu.com/kubernetes/install) and run [private clouds](https://ubuntu.com/openstack/managed) for large enterprises [like BT](https://www.theregister.co.uk/2019/07/24/bt_adopts_openstack_5g/),
AT&T, Deutsche Telecom, Tele2, Colt and Sky.

When I joined Canonical, the architecture and stability of [ubuntu.com](https://ubuntu.com), [canonical.com](https://canonical.com) and many other Django sites became my central responsibility. The team had outages on [ubuntu.com](https://ubuntu.com/) almost every [release day](https://ubuntu.com/about/release-cycle) (when we receive a huge spike in visitors). We quickly upgraded Django and made a number of other stability improvements and ubuntu.com hasn’t had a release-day outage since.

In 2016 I took over and the team responsible for build.snapcraft.io, and started managing 4 developers. We shortly started work on [Snapcraft.io](https://snapcraft.io/), a central project for defining our teams’ relationship to the rest of the company.

I architected the web application to communicate with the Snap Store API server-side with delegated authority from the user through [Macaroons](http://hackingdistributed.com/2014/05/16/macaroons-are-better-than-cookies/),
allowing our team complete control over the presentation and hosting of the site while delegating storage and authorization to the API. This API forms a very effective contract between our two teams - a model we now follow with most other teams in Canonical. To support this, we explored various Python caching libraries and ultimately wrote [our own HTTP module](https://pypi.org/project/canonicalwebteam.http/) to standardise our API communication patterns.

Around the same time, I led our initiative to switch our websites from our [Juju-based system](https://docs.openstack.org/project-deploy-guide/charm-deployment-guide/rocky/install-juju.html) over to become the first team in Canonical to adopt [Kubernetes](https://ubuntu.com/kubernetes/features). Our deploy time dropped from about 20 minutes to 3 minutes, and we automated staging deployments. I also led the implementation of our new Discourse-based [documentation model](https://canonical-web-and-design.github.io/practices/project-structure/documentation.html#community-documentation) which we currently use for [Snapcraft docs](https://snapcraft.io/docs),
[MAAS docs](https://maas.io/docs), and [Juju docs](https://jaas.ai/docs).

I became the principal tech lead for the web and design team, defining our technical standards and patterns for managing our repositories,
including our review & merging model, CI systems, frameworks and architectures, team permissions etc. I started [our team practices site](https://canonical-web-and-design.github.io/practices/), and the [process for updating it](https://github.com/canonical-web-and-design/practices/blob/master/CONTRIBUTING.md). This included [architecture recommendations](https://canonical-web-and-design.github.io/practices/project-structure/server-side-frameworks.html) for when to choose Jekyll, Django, Flask or other frameworks, and to facilitate this we created a\() [Flask-base](https://pypi.org/project/canonicalwebteam.flask-base/) module for our sites to extend.

Our overall team has now grown to 32 people, with 16 developers. I manage 5 developers - all the back-end Python developers and a front-end dev. We also continue to take over websites from other teams (recently [certification.ubuntu.com](https://certification.ubuntu.com/)), and are frequently building new microsites (recently [dqlite.io](https://news.ycombinator.com/item?id=20836331)). We currently manage [around 30 websites](https://github.com/canonical-web-and-design?utf8=%E2%9C%93&q=topic%3Awebsite&type=&language=) (mostly Flask or Django) for Canonical, and have de-facto responsibility for all web front-ends in the company.


Lead developer
===

[Hillarys](http://www.hillarys.co.uk ) - August 2012
---

The development team was fairly new when I arrived at Hillarys, consisting of only two developers. I was brought in to lead and develop a modern development team. The team has since grown with the addition of another senior developer.

I advised the team to use [Git](http://git-scm.com/) as our version control system, trained the team in its use, and migrated all existing repositories to [Github](https://github.com/Hillarys/). I helped to train the junior developer in version control, server-management and object-oriented programming. I also [suggested](http://robinwinslow.co.uk/2014/01/10/agile-philosophy/) and implemented morning standups, sprints and planning meetings which are now invaluable team practices.

I learned C# so that I could architect and lead the rebuild of [Arena](http://www.arena-blinds.com). I also made the site (somewhat) responsive at the same time. This project has now become the basis for two more site rebuilds.

My most important role has been to oversee the migration of [Web-blinds](http://web-blinds.com) (8k daily visitors) to being supported in-house. This involved restructuring the repository, recreating the build system and doing considerable maintenance work on the server, alongside a large new international project on the site.

Full-stack developer
===

[IPC Media](http://www.ipcmedia.com ) - January 2011
---

I was a key member of a small team responsible for [Countrylife](http://countrylife.co.uk), [Horse and Hound](http://horseandhound.co.uk), [Golf Monthly](http://golf-monthly.co.uk) and [Shooting UK](http://shootinguk.co.uk), within a large department comprising over 40 developers.

The expertise and experience of the developers at IPC created a wonderful environment for me to learn about full-stack development and the management of large-scale websites. I became very interested in agile project management strategies, web performance, continuous integration, design patterns and behaviour-driven development.

I also learned a lot about [agile project management techniques](http://robinwinslow.co.uk/2014/01/10/agile-philosophy/), and participated in many decisions about new features and prioritisation of work.

I was central to a semi-responsive redesign of [Countrylife](http://countrylife.co.uk), which is still the current design of the site. I maintained and wrote new Symfony modules, and helped to develop our build and continuous integration systems for all our sites.

I also gave two [presentations](/publications#html5-and-how-to-use-it-smallpresentationsmall) on new technologies to the department.

Previous roles
===

[Energise](http://www.energiseconsulting.com/), [Mokoro](http://www.mokoro.co.uk/), [Tamar](http://www.tamar.com/ ) - until 2010
---

During my MSc I advised Energise on a large-scale web project, and built the bulk of the solution in CodeIgniter. I also advised Mokoro on redesigning their intranet for use by their consultants all over the world, and helped build the solution in Drupal.

During my MSc and BSc and during my year in industry I worked for Tamar.com. I was a member of a small team working on large perl projects and ongoing maintenance on ecommerce websites for financial institutions like [Endsleigh](http://endsleigh.co.uk) and online retailers like [Dreams](http://dreams.co.uk).

Tamar was where I started to learn about front-end technologies. I became their CSS expert, and I led JavaScript development and helped develop a new JavaScript library. I also adapted and improved their existing bespoke Perl framework and learned to use Catalyst.
