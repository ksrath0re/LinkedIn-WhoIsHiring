# LinkedIn WhoIsHiring


This Repo is for the purpose of identifying the managers who are hiring currently from  "**People Also Viewed**" section on a person's LinkedIn Profile. At this moment, You need to login to LinkedIn and go to the profile of Hiring Manager and save that page using a FireFox addon [SingleFile][df1] and place them under **Files** directory.

Now Simply run ``process-linkedin-files.py`` file. It'll export two separate files.
- Hiring Profiles
- Related Profiles

These files have **Name, LinkedIn Profile Link** and **Heading** details.

### Todos

 - Add more functionalities (such as no need to save file first.)

### Note

Saving Webpage using **Ctrl-S** does not save the page properly hence we need to use the files saved by SinglePage Addon.

License
----

MIT


Readme made using [DILLINGER][dl].

[//]: # (These are reference links used in the body of this note and get stripped out when the markdown processor does its job. There is no need to format nicely because it shouldn't be seen. Thanks SO - http://stackoverflow.com/questions/4823468/store-comments-in-markdown-syntax)


   [df1]: <https://addons.mozilla.org/en-US/firefox/addon/single-file/r>
   [dl]: <https://dillinger.io/>
