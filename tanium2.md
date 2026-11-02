WEBVTT
Kind: captions
Language: en

00:00:11.216 --> 00:00:12.166
Hello and welcome.

00:00:12.166 --> 00:00:13.216
My name is Cameron.

00:00:13.216 --> 00:00:15.266
I'm an enterprise services
engineer at Tanium

00:00:15.766 --> 00:00:18.600
and today will be taking a look
into a live Tanium environment

00:00:18.600 --> 00:00:20.816
and exploring
some of the features and functionality

00:00:20.816 --> 00:00:23.000
that are available to you today
in the console.

00:00:23.666 --> 00:00:26.033
In this video
I'll cover the interact module

00:00:26.566 --> 00:00:29.066
as well as the reports and dashboards

00:00:29.900 --> 00:00:32.366
that are under the data tab.

00:00:32.366 --> 00:00:34.033
I'll show you how to review saved
questions,

00:00:34.033 --> 00:00:37.733
Favorite things that find useful, filter
and export your results,

00:00:37.966 --> 00:00:40.916
and how to build dynamic questions
in the question builder.

00:00:42.233 --> 00:00:45.833
For those of you who've never seen Tanium
before, please don't start here.

00:00:46.883 --> 00:00:51.383
Please visit our Tanium YouTube page
and you can watch our founder, Orion

00:00:51.383 --> 00:00:57.166
Hindawi, give a quick demo on the Tanium
platform, specifically the Tanium Demo:

00:00:57.383 --> 00:01:00.233
“What's the industry's
first converged endpoint management

00:01:00.416 --> 00:01:03.450
platform in Action”

00:01:03.716 --> 00:01:06.050
This high-level overview is critical
to understand

00:01:06.533 --> 00:01:10.100
what sets Tanium apart from other tools
and how it's fundamentally different

00:01:10.100 --> 00:01:13.250
in the way that we gather data
from endpoints in your environment.

00:01:14.400 --> 00:01:16.433
I promise this video is worth your time.

00:01:16.666 --> 00:01:19.883
There are also a lot of other
helpful videos on this page covering

00:01:20.216 --> 00:01:24.166
other modules and abilities
that I won't be covering here today.

00:01:24.900 --> 00:01:27.233
I'll be more focused on the content
that is unique

00:01:27.233 --> 00:01:30.150
to your environment.

00:01:32.066 --> 00:01:34.100
We also have a great Tanium docs

00:01:34.100 --> 00:01:36.450
page at docs.Tanium.com.

00:01:37.616 --> 00:01:40.766
For additional help and guidance
on using the console

00:01:40.850 --> 00:01:43.850
configuration requirements

00:01:44.866 --> 00:01:46.433
and great troubleshooting guides,

00:01:46.433 --> 00:01:50.616
as well as details on other modules
that we offer.

00:01:50.616 --> 00:01:52.716
Here is a list of the timestamps

00:01:53.016 --> 00:01:56.833
for each section
if you prefer to skip ahead.

00:01:58.500 --> 00:02:00.650
With that, let's get started.

00:02:00.650 --> 00:02:03.833
There's no better way to learn Tanium
than to just start asking questions

00:02:03.833 --> 00:02:05.100
and interact.

00:02:05.100 --> 00:02:07.400
There's a wealth of information
available to you today

00:02:07.466 --> 00:02:10.016
about your endpoints
and all we have to do is ask for it.

00:02:10.666 --> 00:02:13.616
We don't even need to know the proper
query syntax to get started.

00:02:13.616 --> 00:02:17.666
So let's just say I want to know what applications are installed in the environment.

00:02:22.433 --> 00:02:23.866
When I press enter,

00:02:23.866 --> 00:02:27.383
the natural language parser gives us
some properly formatted suggestions

00:02:27.650 --> 00:02:32.216
based on what we type. I’ll select “Get
installed applications from our machines”

00:02:33.233 --> 00:02:35.700
And within a couple of seconds
we have some results coming in.

00:02:36.416 --> 00:02:39.800
First column is the name of the
application we have the version and then

00:02:39.800 --> 00:02:43.100
the count of the number of systems
with that particular version installed.

00:02:43.950 --> 00:02:46.466
And on the top left here
we have a percentage counter.

00:02:47.066 --> 00:02:49.516
This indicates
the percentage of the environment

00:02:50.566 --> 00:02:53.666
that has responded to our question.

00:02:53.666 --> 00:02:56.150
Above that,
we have a count of the number of rows

00:02:57.533 --> 00:03:01.283
in our report here,
and then the total count is totaling

00:03:01.650 --> 00:03:05.266
this count column
right here, indicating the total number

00:03:05.266 --> 00:03:07.850
of applications found.

00:03:09.050 --> 00:03:11.583
You can see here that we are viewing
current results.

00:03:11.600 --> 00:03:15.166
This means that these are the live results
coming in from the endpoints.

00:03:16.016 --> 00:03:19.666
You can pause and play those live results
coming in with the options here.

00:03:21.200 --> 00:03:22.283
And then we also

00:03:22.283 --> 00:03:25.400
have, in some cases
a cached or a recent option.

00:03:26.150 --> 00:03:29.900
These will show us results for systems
that are currently offline.

00:03:30.616 --> 00:03:33.950
The cached results will go back
six--I'm sorry, 30 days

00:03:34.500 --> 00:03:37.250
and the recent results
will show the last seven days.

00:03:39.316 --> 00:03:41.216
The cached option will only appear

00:03:41.216 --> 00:03:45.166
if we are tracking this particular data
point in our test database

00:03:45.750 --> 00:03:51.150
and the recent option will appear
if we have a saved question.

00:03:51.900 --> 00:03:53.000
Some questions will also

00:03:53.000 --> 00:03:56.416
have hidden columns
that you can show with this option here,

00:03:56.966 --> 00:03:59.416
such as the silent uninstall string

00:03:59.416 --> 00:04:02.750
for this particular sensor.

00:04:02.750 --> 00:04:05.750
And you can add or remove columns
from your report

00:04:05.750 --> 00:04:09.000
here.

00:04:09.000 --> 00:04:10.650
You can perform a quick filter

00:04:10.650 --> 00:04:14.033
on these results
by using the filter by text box.

00:04:14.183 --> 00:04:16.483
We can say that the results must contain.

00:04:17.150 --> 00:04:20.383
Let's say Firefox.

00:04:26.000 --> 00:04:29.033
You can
see that the number of rows has changed

00:04:29.033 --> 00:04:32.000
as well as the total applications found.

00:04:33.650 --> 00:04:35.966
You can also use the filter
by computer group

00:04:35.966 --> 00:04:39.450
to filter by one of your patch groups.

00:04:39.800 --> 00:04:44.033
If you're going to export these filtered
results, don't use the quick filter.

00:04:44.783 --> 00:04:48.416
We're going to take a look at the filter
builder on the top left of the results

00:04:48.416 --> 00:04:51.316
grid. Hit the arrow next to filters.

00:04:51.316 --> 00:04:55.716
We're going to click on to add a row
and let's do the same filter.

00:04:55.733 --> 00:04:59.066
Let's say the installed application
name must contain

00:05:00.350 --> 00:05:02.016
Firefox,

00:05:02.816 --> 00:05:04.816
but I'll press enter to apply.

00:05:05.566 --> 00:05:07.666
Then I'll add a group.

00:05:08.266 --> 00:05:10.200
Let's get a little more advanced
with this.

00:05:10.200 --> 00:05:12.166
Let's do a version.

00:05:12.166 --> 00:05:16.650
Must start with 108.

00:05:16.650 --> 00:05:21.000
Apply that row, add another.

00:05:21.016 --> 00:05:24.383
Let's say can also start with

00:05:25.350 --> 00:05:28.050
109.

00:05:30.016 --> 00:05:31.016
All right. Okay.

00:05:31.016 --> 00:05:33.016
So make sure you check your boolean logic.

00:05:33.033 --> 00:05:35.816
We want this group to be in order.

00:05:35.816 --> 00:05:39.000
And so to read this and they'll say

00:05:39.016 --> 00:05:42.983
install the application
name contains Firefox and

00:05:44.450 --> 00:05:47.716
this group must be true installed version.

00:05:47.816 --> 00:05:51.016
Starts with one or eight and versions

00:05:51.016 --> 00:05:53.633
or version starts with 109.

00:05:54.650 --> 00:05:57.416
Or apply that filter

00:05:57.616 --> 00:06:00.116
and I'll go ahead and minimize
our filter builder here

00:06:01.850 --> 00:06:05.266
so you can see the filter we applied
next to the filter builder here.

00:06:05.633 --> 00:06:10.350
We can click the x to clear that filter.

00:06:11.416 --> 00:06:15.650
Now keep in mind
if you see some that may have

00:06:16.800 --> 00:06:18.900
the may look like

00:06:18.900 --> 00:06:21.750
the same application,
let's say these two here

00:06:23.783 --> 00:06:24.900
Mozilla Firefox

00:06:24.900 --> 00:06:28.400
64 bit en-US, both of them, 109.

00:06:28.400 --> 00:06:30.200
So why do we have two results here?

00:06:31.733 --> 00:06:32.150
Well,

00:06:32.150 --> 00:06:34.733
keep in
mind that you can have hidden columns

00:06:36.050 --> 00:06:39.566
and you can see here
that they both have different results.

00:06:39.566 --> 00:06:43.316
So since these rows are unique,
it will split them into separate columns.

00:06:45.200 --> 00:06:47.450
You can also click on the

00:06:47.450 --> 00:06:49.916
the headers of the columns to sort,

00:06:50.566 --> 00:06:52.916
if you want to sort
by multiple fields, like

00:06:53.116 --> 00:06:55.950
let's say the name would be your primary,
you can hold the shift

00:06:55.950 --> 00:06:59.183
key and click on version
as a secondary sorting

00:06:59.850 --> 00:07:02.450
and even add a third if you want to.

00:07:07.400 --> 00:07:09.916
Next, we can drill down on systems.

00:07:10.366 --> 00:07:12.683
I'm going to go ahead
and uncheck these two here

00:07:14.100 --> 00:07:16.166
sort by version.

00:07:16.166 --> 00:07:22.050
And let's say
I wanted to drill down on version 109.

00:07:22.050 --> 00:07:27.016
dot zero, let’s just say I wanted to find
out more about these systems.

00:07:28.016 --> 00:07:30.916
You can see that
when I've checked the boxes, it gives me

00:07:30.916 --> 00:07:34.050
a total of the count of systems
that I have selected.

00:07:34.466 --> 00:07:37.100
I have selected
five rows, a total of 13 systems,

00:07:38.566 --> 00:07:41.100
I’m going to select drill down,

00:07:41.483 --> 00:07:44.550
brings us to the drill down selection page.

00:07:45.233 --> 00:07:47.100
We have a couple of saved questions here.

00:07:47.100 --> 00:07:50.250
These are, you know, default
drill down questions.

00:07:50.250 --> 00:07:56.183
You can also check this box
to show all of our saved questions.

00:07:56.183 --> 00:08:00.200
You can also form a new question
using the the question bar here

00:08:01.733 --> 00:08:03.233
or the Question Builder,

00:08:03.233 --> 00:08:05.300
which we can talk more about in
just a moment.

00:08:07.016 --> 00:08:09.900
So I want to get the computer names
from all of the systems

00:08:10.400 --> 00:08:13.500
of those 13 systems
with that particular version of Firefox,

00:08:13.816 --> 00:08:16.583
I could use the computer name
save question here, but

00:08:16.583 --> 00:08:21.150
I want a little more information
like the IP address and operating system.

00:08:21.150 --> 00:08:25.850
So I'm going to select the general
information and select drill down

00:08:30.650 --> 00:08:30.883
here.

00:08:30.883 --> 00:08:35.700
We can see the original question,
the versions of Firefox

00:08:35.700 --> 00:08:37.433
that we selected

00:08:40.250 --> 00:08:42.316
and then below that is our drill down.

00:08:42.966 --> 00:08:45.983
Now we have the computer
names, IP addresses

00:08:45.983 --> 00:08:52.166
and the operating system,
so we can also use the merge option.

00:08:52.283 --> 00:08:56.566
Here is let's say we wanted to add
an additional column to these results.

00:08:56.566 --> 00:09:01.433
Let's say I wanted to also see
if these systems are virtual or not.

00:09:02.150 --> 00:09:03.983
I have the same three options here.

00:09:03.983 --> 00:09:06.450
I'm just going to go to create a question
this time,

00:09:07.350 --> 00:09:09.600
and I don't know what to search,

00:09:09.600 --> 00:09:12.050
So I'll just type virtual

00:09:12.600 --> 00:09:13.850
and it gives me some options.

00:09:13.850 --> 00:09:19.816
Here I'll select is virtual
from all machines.

00:09:19.816 --> 00:09:20.750
And there you have it.

00:09:20.750 --> 00:09:23.516
We have an additional
column added to our results here

00:09:24.683 --> 00:09:25.516
with a yes or no.

00:09:25.516 --> 00:09:30.683
Whether the system is virtual or not,
where the merge button was.

00:09:30.683 --> 00:09:35.516
Now I have an option to edit that merged
question or I can hit the X to clear it.

00:09:35.966 --> 00:09:38.966
I'll go ahead and clear that out, confirm

00:09:42.350 --> 00:09:44.600
and I have a similar option here.

00:09:44.600 --> 00:09:47.666
So I see my original dynamic question
and then the drill

00:09:47.666 --> 00:09:51.116
down to get the general information here.

00:09:51.116 --> 00:09:54.350
I can hit the X here
to go back to my original question,

00:09:55.283 --> 00:10:02.250
which we see here.

00:10:02.250 --> 00:10:06.383
If you wish to export the filter results,
make sure that you've used

00:10:06.383 --> 00:10:10.133
the advanced filter
and not the filter by text box.

00:10:10.950 --> 00:10:14.266
And then on the top right of the results
grid, you're going to hit the export

00:10:14.266 --> 00:10:19.016
icon right here
next to the column selection.

00:10:19.016 --> 00:10:23.266
This export all window
will allow you to set a file name.

00:10:23.633 --> 00:10:27.983
You can choose whether or not to add
the headers of the columns at the top,

00:10:27.983 --> 00:10:32.116
and the flattened rows
option will allow you to take any cell

00:10:32.116 --> 00:10:37.583
that has multiple returns in it and
flatten them into their own separate row.

00:10:37.583 --> 00:10:38.900
And then you select export.

00:10:38.900 --> 00:10:42.716
It will be in a CSV format
and the hidden columns,

00:10:42.716 --> 00:10:46.366
all hidden columns
that that sensor has will be exported

00:10:46.366 --> 00:10:55.766
in the CSV file.

00:10:55.766 --> 00:10:59.866
Now, so far we've been using
very simple tandem questions.

00:11:00.350 --> 00:11:02.266
Let's say
you want to get a lot more detail

00:11:02.266 --> 00:11:06.533
or you wanted to get more granular
with your filters in the questions

00:11:07.216 --> 00:11:09.683
or even find a better way

00:11:09.683 --> 00:11:13.433
of seeing what kinds of other information
you can get out of the team questions.

00:11:13.433 --> 00:11:15.266
For this

00:11:15.266 --> 00:11:17.450
We're going to use the question
builder.

00:11:17.450 --> 00:11:21.100
Now, we've already seen briefly in the drill
down in the merge page,

00:11:21.150 --> 00:11:26.033
you have the tab over here
for the Question Builder.

00:11:26.033 --> 00:11:27.533
After you've asked a question,

00:11:27.533 --> 00:11:30.916
you also get the option here
to copy to Question Builder.

00:11:30.916 --> 00:11:33.116
And that's going to take the
question you've already asked

00:11:34.200 --> 00:11:35.566
and let you

00:11:35.566 --> 00:11:37.950
add or remove parts of that question.

00:11:39.083 --> 00:11:43.166
But you can also start from the home page
or the interact module

00:11:43.283 --> 00:11:46.966
here to build a new question from scratch.

00:11:47.100 --> 00:11:51.600
So that's what we're going to do.

00:11:51.600 --> 00:11:54.866
So let's click build question

00:11:54.866 --> 00:11:57.166
and here we have the question Builder.

00:11:57.166 --> 00:11:58.666
We have two parts of a question.

00:11:58.666 --> 00:12:00.416
The first part is the get statement.

00:12:00.416 --> 00:12:02.516
This is the information
we want to get from the systems

00:12:03.266 --> 00:12:07.283
and then the from clause indicating
which systems we want to respond to.

00:12:07.283 --> 00:12:11.300
Our question Now, to kind of demonstrate
this,

00:12:11.966 --> 00:12:15.833
we're going to we're going to add
a row here using the same sensor

00:12:15.833 --> 00:12:20.733
we did in our previous question,
install applications.

00:12:20.733 --> 00:12:23.000
That's just for simplicity.

00:12:24.050 --> 00:12:26.416
And we're going to add a filter to this.

00:12:27.000 --> 00:12:30.316
We're going to make it a row filter.

00:12:30.316 --> 00:12:32.633
You say that it must contain Chrome

00:12:35.366 --> 00:12:37.366
and I will apply,

00:12:39.233 --> 00:12:41.333
and let's just ask this question,

00:12:41.333 --> 00:12:43.250
see what happens

00:12:45.300 --> 00:12:45.766
right now

00:12:45.766 --> 00:12:49.666
at the top here we have a row
that's no results, no results

00:12:50.366 --> 00:12:53.183
with a good number of systems in it.

00:12:53.216 --> 00:12:54.616
What does that mean?

00:12:54.616 --> 00:12:58.883
This means that there are several systems
that we are asking this question from

00:12:58.883 --> 00:13:01.700
that don't have any results
for Google Chrome,

00:13:02.516 --> 00:13:05.216
but they are being asked to respond
to our question

00:13:05.783 --> 00:13:08.183
from all machines.

00:13:08.366 --> 00:13:10.616
So to get rid of that list, copy this.

00:13:10.616 --> 00:13:12.116
Back to the Question Builder.

00:13:12.116 --> 00:13:15.466
And just for the sake of the example,

00:13:15.466 --> 00:13:17.816
we are going to add

00:13:18.500 --> 00:13:22.616
installed applications,

00:13:22.616 --> 00:13:24.983
add the same row filter contains chrome,

00:13:26.600 --> 00:13:29.716
you know, press enter to apply.

00:13:29.716 --> 00:13:33.416
Now this looks redundant,
but what this is saying is that

00:13:35.150 --> 00:13:36.566
I'm only asking

00:13:36.566 --> 00:13:39.983
systems
that have Chrome installed to respond.

00:13:41.033 --> 00:13:44.516
So the from clause is the first thing
that your endpoint is going to evaluate.

00:13:44.783 --> 00:13:46.166
And if this is false,

00:13:46.166 --> 00:13:48.983
then it's not even going to send anything
for the get statement.

00:13:49.550 --> 00:13:52.850
So from all machines with installed
applications contains Chrome.

00:13:53.600 --> 00:13:55.650
So now when I ask this question,

00:13:56.900 --> 00:13:59.966
the only results that we see
are from systems

00:13:59.966 --> 00:14:07.583
that have a result.

00:14:07.583 --> 00:14:14.216
Well,
let's go back to the question builder.

00:14:14.216 --> 00:14:18.016
Some additional ways
that you can filter in the from clause

00:14:18.683 --> 00:14:22.583
is you can use computer groups here.

00:14:23.516 --> 00:14:27.350
Select any of the default computer groups
such as all computers, all Windows

00:14:28.016 --> 00:14:29.483
or Linux.

00:14:29.483 --> 00:14:31.733
You can say all virtual.

00:14:31.733 --> 00:14:35.633
You also have access
to all of your patching groups, the group

00:14:35.633 --> 00:14:39.800
desktops, group servers.

00:14:39.800 --> 00:14:40.616
You can

00:14:41.850 --> 00:14:45.266
use the sensor computer name

00:14:48.833 --> 00:14:53.700
to search for specific computer names.

00:14:53.700 --> 00:14:57.983
You can use the matches option here
to form regular expressions

00:14:59.183 --> 00:15:03.566
to search for, you know, a
groups of computers based on their naming

00:15:03.566 --> 00:15:04.700
conventions.

00:15:05.300 --> 00:15:07.516
You can use things

00:15:07.516 --> 00:15:10.650
like the IP address sensor

00:15:10.766 --> 00:15:12.916
for IPV four

00:15:13.166 --> 00:15:22.050
things like this.

00:15:22.050 --> 00:15:24.083
Now, I've mentioned sensors
a couple of times.

00:15:24.683 --> 00:15:25.700
A sensor.

00:15:25.700 --> 00:15:29.300
A sensor is essentially a script
that runs on the endpoint

00:15:29.300 --> 00:15:32.183
and returns value to the console here
for us to see.

00:15:33.016 --> 00:15:37.216
You can browse all of the sensors
in the question builder by category

00:15:37.883 --> 00:15:42.050
and see the kinds of things
that you can ask in the environment.

00:15:42.983 --> 00:15:45.950
The deploy module, for instance, will have

00:15:45.950 --> 00:15:49.050
all of the sensors related to the third
party updates that we're doing.

00:15:50.716 --> 00:15:54.300
We have file system information, hardware,

00:15:55.066 --> 00:15:57.683
several categories,
including your patch category here

00:15:59.266 --> 00:16:02.666
and all the patch sensors
that we can get information back

00:16:03.466 --> 00:16:07.050
such as your your skin errors, scan age,

00:16:08.000 --> 00:16:11.250
patch list information.

00:16:11.250 --> 00:16:14.250
Probably the more common ones you'll use
are the deployment errors

00:16:14.250 --> 00:16:17.783
and the deployment results.

00:16:17.783 --> 00:16:23.900
The bottom here we have the patch
installation history option.

00:16:23.900 --> 00:16:26.216
This one has additional parameters

00:16:26.933 --> 00:16:30.050
and you can see in the question text here,
it adds those parameters.

00:16:30.050 --> 00:16:33.166
And I can say that

00:16:33.166 --> 00:16:36.300
we want to see the patch installation
for the last seven days.

00:16:36.300 --> 00:16:37.500
For instance,

00:16:38.300 --> 00:16:40.316
let's say I only want to see the things

00:16:40.316 --> 00:16:42.600
that Tanium installed

00:16:45.350 --> 00:16:56.300
and I'll apply that.

00:16:56.300 --> 00:16:58.350
If you've built a question
that you would like

00:16:58.350 --> 00:17:02.250
to keep for future reference,
you can always copy that text out

00:17:02.783 --> 00:17:03.983
and save it somewhere else.

00:17:05.100 --> 00:17:05.816
But we also

00:17:05.816 --> 00:17:09.166
have several questions
that we have saved in the console

00:17:09.566 --> 00:17:14.116
that are available for you to use
regularly.

00:17:14.116 --> 00:17:23.516
So let's go into the Interact module
and take a look at the saved questions.

00:17:23.516 --> 00:17:26.900
Saved
questions are different than the reports,

00:17:26.900 --> 00:17:30.983
which we'll talk about in a little bit,
just in the way that we form the form,

00:17:30.983 --> 00:17:33.233
the report filter of the data

00:17:33.983 --> 00:17:36.800
and also how we export that data.

00:17:37.966 --> 00:17:40.933
But for now, we're going to take a look
at the saved questions.

00:17:42.750 --> 00:17:44.866
We have several saved questions

00:17:44.866 --> 00:17:48.766
listed here in the in the bottom section.

00:17:48.766 --> 00:17:51.833
You've got categories, dashboards
and saved questions.

00:17:51.833 --> 00:17:56.033
So the categories are just filtering

00:17:56.033 --> 00:18:00.266
the number of safe questions
you see here by the different categories.

00:18:00.800 --> 00:18:07.350
Now the dashboards are just another group
of filtering those saved questions.

00:18:07.350 --> 00:18:09.950
You can also click on these dashboards
to see

00:18:10.500 --> 00:18:13.166
all of those questions asked

00:18:13.166 --> 00:18:15.466
in one in one dashboard.

00:18:16.466 --> 00:18:18.833
These dashboards are different

00:18:18.833 --> 00:18:22.733
than the dashboards under the data tab
that we'll talk about in a bit.

00:18:22.733 --> 00:18:30.150
So the reports here feed these dashboards,
but the panel that you'll focus on

00:18:30.150 --> 00:18:36.750
mostly is just the saved questions
We can click the favorites option

00:18:36.750 --> 00:18:42.050
to see the the different save questions
that we have starred as our favorite.

00:18:42.466 --> 00:18:45.150
The things that we use regularly so

00:18:45.150 --> 00:18:48.233
we can quickly access the
the reports that we care about.

00:18:48.683 --> 00:18:51.050
Now, at first glance,
there's a lot of information here,

00:18:51.750 --> 00:18:54.900
so I'll go over some of the saved
questions that we have created for you

00:18:54.900 --> 00:18:57.900
that we think will be relevant
to what you're looking for.

00:18:58.883 --> 00:19:01.316
First, here at the top,
we can see the third party

00:19:01.316 --> 00:19:14.183
updates by Tanium over the last 90 days.

00:19:14.183 --> 00:19:16.250
Early
on, we have heard some complaints that

00:19:17.150 --> 00:19:20.400
we were looking for specific computers
and they weren't showing up

00:19:20.783 --> 00:19:24.266
and it's
because we were filtering those results

00:19:24.266 --> 00:19:27.016
if they had nothing
to report out of the reports.

00:19:27.683 --> 00:19:29.633
So instead now we're not reporting

00:19:29.633 --> 00:19:32.450
and we're going to show you
all of the systems in your environment

00:19:33.016 --> 00:19:34.816
for whatever
patch group you're looking at.

00:19:35.783 --> 00:19:39.116
And if there are no results to report

00:19:40.366 --> 00:19:43.816
either some patch groups that you're not,
not updating

00:19:44.866 --> 00:19:48.000
or nothing had been installed,
they're going to show up as no matching

00:19:48.000 --> 00:19:49.516
deployments found.

00:19:49.516 --> 00:19:51.150
This is for a third party.

00:19:51.150 --> 00:19:55.066
Again, you can see up top

00:19:55.066 --> 00:19:57.833
we've got the the question text.

00:19:58.816 --> 00:20:02.816
You can click the little icon at the end
here.

00:20:02.816 --> 00:20:06.450
You can copy this into a question
in the question bar or into the question

00:20:06.450 --> 00:20:10.100
builder to make modifications
and tailor it to your needs.

00:20:11.633 --> 00:20:14.750
You can also just like a live question,
you can filter.

00:20:15.750 --> 00:20:18.116
Let's say we didn't want to see the ones

00:20:18.116 --> 00:20:20.116
that say no matching deployments found.

00:20:21.350 --> 00:20:24.716
We can filter by the I.D.

00:20:26.150 --> 00:20:27.000
That's the name.

00:20:27.000 --> 00:20:28.250
Here's the ID

00:20:31.733 --> 00:20:34.666
that does not contain.

00:20:34.666 --> 00:20:36.266
And here's another useful tip.

00:20:36.266 --> 00:20:37.950
If you click on this little button

00:20:37.950 --> 00:20:40.916
in one of the cells,
you have the option to copy the value.

00:20:42.083 --> 00:20:44.966
I can paste it by

00:20:48.750 --> 00:20:49.283
now. I got

00:20:49.283 --> 00:20:52.583
rid of all of the deployments with no, no,

00:20:53.300 --> 00:20:55.400
no data or report

00:21:01.200 --> 00:21:03.750
and other that you might find useful.

00:21:03.750 --> 00:21:06.916
Is the missing application updates.

00:21:06.916 --> 00:21:16.850
This is a new report, but

00:21:19.016 --> 00:21:22.166
as you can see in the question text here,

00:21:22.166 --> 00:21:26.750
we have used a regular expression
to target

00:21:26.750 --> 00:21:29.783
only the applications
that we are updating for you

00:21:31.050 --> 00:21:33.233
to show us a list of systems

00:21:33.233 --> 00:21:37.716
that could be updated or update eligible.

00:21:37.716 --> 00:21:50.716
So you've got the computer name,
the name of the application.

00:21:50.716 --> 00:21:57.766
We also have some saved questions
for patching.

00:21:57.766 --> 00:21:59.516
Let's take a look

00:22:00.716 --> 00:22:03.533
at the patch deployments.

00:22:04.016 --> 00:22:06.083
The patch deployment results succeeded.

00:22:06.900 --> 00:22:09.050
So after you have your patch cycle,

00:22:09.533 --> 00:22:12.200
you can come and check this
report to see which systems

00:22:13.350 --> 00:22:14.450
have installed,

00:22:14.450 --> 00:22:21.300
which patches.

00:22:21.300 --> 00:22:27.533
So you have a computer name
and all of the patches that it installed.

00:22:27.533 --> 00:22:29.966
Keep in mind if you are exporting this

00:22:31.800 --> 00:22:33.916
and you don't flatten the rows,

00:22:33.916 --> 00:22:36.750
you'll have multiple results
in a single cell.

00:22:36.766 --> 00:22:40.550
You might have to expand your row height
to see all of the results

00:22:41.816 --> 00:22:45.116
because you'll have several updates

00:22:45.266 --> 00:22:46.500
per computer

00:22:46.500 --> 00:22:53.250
that were installed.

00:22:53.250 --> 00:22:56.150
Next, we'll look at the same report or

00:22:57.800 --> 00:22:59.783
past deployment results failed, aborted

00:22:59.783 --> 00:23:02.933
or not started.

00:23:02.933 --> 00:23:04.800
This is the same

00:23:04.916 --> 00:23:07.066
sensor in the question

00:23:07.066 --> 00:23:26.216
filtering for those statuses.

00:23:26.216 --> 00:23:44.266
Next,
we'll look at patch deployment errors,

00:23:44.266 --> 00:23:49.666
so you will only see the patch ID
for the group that you're targeting.

00:23:49.700 --> 00:23:52.916
You can filter by the the patching group.

00:23:53.783 --> 00:23:56.000
So all of these should be
the same deployment idea.

00:23:56.000 --> 00:24:00.000
If you just came out of a patch cycle,
the errors

00:24:00.000 --> 00:24:08.850
if then any occurred will show up here.

00:24:08.850 --> 00:24:11.416
Another handy report will be patch

00:24:14.866 --> 00:24:17.000
reboot status.

00:24:17.000 --> 00:24:20.333
After a patch cycle,
you can take a look and see if any of them

00:24:20.333 --> 00:24:23.416
still need any remaining reboots.

00:24:23.416 --> 00:24:25.366
It'll show the computer name, the uptime,

00:24:25.366 --> 00:24:28.016
the reboot status
and if one of them does need

00:24:29.300 --> 00:24:30.800
a restart,

00:24:31.200 --> 00:24:34.066
you can spin this here and see

00:24:34.066 --> 00:24:36.466
which registry

00:24:37.200 --> 00:24:40.816
key is actually indicating
that a reboot is required.

00:24:40.816 --> 00:24:43.466
Some of them have multiple

00:24:45.166 --> 00:24:46.400
as well as the patches

00:24:46.400 --> 00:24:49.433
that were installed
and the source that installed them.

00:24:49.433 --> 00:24:53.850
Some of them SCCM, Windows update...
if it's Tanium,

00:24:53.850 --> 00:24:56.600
it will be listed in here.

00:25:01.816 --> 00:25:02.250
Next

00:25:02.250 --> 00:25:06.533
We can also look at a slightly different report

00:25:06.866 --> 00:25:12.533
from the patch installation history.

00:25:12.533 --> 00:25:18.016
This sensor is not pulling from the patch
deployment from a Tanium log.

00:25:18.016 --> 00:25:20.333
This is pulling from a Windows update log.

00:25:21.050 --> 00:25:24.650
And so this allows us to see more than
just what Tanium installed

00:25:25.800 --> 00:25:27.866
but all of the different install sources.

00:25:28.766 --> 00:25:31.616
Now this is actually specified
in the sensor

00:25:31.616 --> 00:25:35.400
parameter
as 30 days like we looked at earlier.

00:25:35.400 --> 00:25:39.866
We can copy that in the question
builder and modify it if we want.

00:25:39.866 --> 00:25:40.516
By default.

00:25:40.516 --> 00:25:54.650
We are not showing this
report per computer, but

00:25:57.533 --> 00:25:59.783
we also have a saved question

00:25:59.783 --> 00:26:02.416
that includes the computer name

00:26:02.416 --> 00:26:04.816
and then we have one filtered by Tanium

00:26:04.816 --> 00:26:09.650
only. Now

00:26:09.650 --> 00:26:15.300
we have had a request recently to combine
all of these things into one report.

00:26:16.066 --> 00:26:18.983
So we built the Master Patch report.

00:26:20.150 --> 00:26:23.816
Now, depending on which patches we are

00:26:24.416 --> 00:26:28.916
deploying to your systems, you will need
to look at a different report.

00:26:29.400 --> 00:26:33.083
So if we are only patching the critical
and important

00:26:33.083 --> 00:26:36.566
on a couple of your server groups,
you'll want to run

00:26:37.166 --> 00:26:41.483
the critical and important
patch list for those systems.

00:26:42.716 --> 00:26:45.800
The plus number at the end here
is the number of days

00:26:45.800 --> 00:26:49.850
that the patches must have age
to be applicable to the system.

00:26:49.850 --> 00:26:52.766
So if you have a development group
or a test group

00:26:53.150 --> 00:26:57.166
that gets patches immediately
as they're released from from Microsoft,

00:26:58.516 --> 00:27:01.650
it would be the critical and important
or the

00:27:02.366 --> 00:27:06.900
the global patch list.

00:27:06.900 --> 00:27:11.150
If it's a production group, you might have
a couple of days of a delay on it.

00:27:11.150 --> 00:27:12.983
So you have like plus eight days.

00:27:12.983 --> 00:27:16.216
So eight days after that
patch is released, it becomes applicable

00:27:16.216 --> 00:27:17.716
to the systems.

00:27:17.716 --> 00:27:20.266
And so now you can use these reports

00:27:20.266 --> 00:27:22.516
to see which systems are

00:27:23.333 --> 00:27:26.366
that have applicable patches,
not installed,

00:27:27.916 --> 00:27:30.616
and that will take into account
the number of days

00:27:30.616 --> 00:27:35.066
that you are delaying your deployments.

00:27:35.066 --> 00:27:38.116
So keep that in mind when you're looking
at the Master Patch report.

00:27:38.600 --> 00:27:41.400
This master patch report is what's feeding

00:27:41.400 --> 00:27:45.683
the weekly reports
that we are sending to you via email.

00:27:45.683 --> 00:27:49.883
So these weekly reports we have chosen
the patch list that we are sending

00:27:50.966 --> 00:27:55.016
to your systems by Patch Group.

00:27:55.016 --> 00:27:58.800
So it's already filtered for the things
that are relevant to that group.

00:28:00.050 --> 00:28:02.266
But if you come into the safe questions
and you run this,

00:28:02.266 --> 00:28:03.833
maybe you're troubleshooting something.

00:28:03.833 --> 00:28:07.966
You want to run this out of that weekly
schedule and compare the results.

00:28:07.966 --> 00:28:13.550
You can you can find the patch list
for that group and take a look.

00:28:13.550 --> 00:28:14.050
Right

00:28:18.600 --> 00:28:20.250
now, there are several things

00:28:20.250 --> 00:28:23.400
in this report that we're showing here.

00:28:23.400 --> 00:28:26.450
It looks a little chaotic,
but there are really only

00:28:27.416 --> 00:28:29.783
four different sensors
that we're reporting on here.

00:28:30.616 --> 00:28:33.316
So first, we have the computer
name or excuse me, five,

00:28:33.316 --> 00:28:36.200
we have the computer name,
we have the computer group.

00:28:37.133 --> 00:28:41.216
Then the first of the patch sensors
is the patch deployment results.

00:28:42.166 --> 00:28:42.500
Yeah.

00:28:42.500 --> 00:28:46.400
One, two, three, four, five, six, seven

00:28:47.116 --> 00:28:49.316
different columns for that one sensor.

00:28:50.100 --> 00:28:53.850
And then we move on to the next,
which is the deployment errors.

00:28:54.683 --> 00:28:59.400
So we have two different column headers
that said

00:29:00.316 --> 00:29:04.800
deployment ID, That's
because there's two different sources,

00:29:04.800 --> 00:29:07.366
the deployment results
and the deployment errors.

00:29:08.366 --> 00:29:12.050
And so in the email that we're sending,

00:29:12.050 --> 00:29:17.400
we have a way of renaming these columns
and filtering out ones

00:29:17.400 --> 00:29:21.950
that we don't think
are relevant in the report weekly.

00:29:21.950 --> 00:29:25.883
So some of these columns
that you see in here, you won't see

00:29:25.883 --> 00:29:31.500
in your report, but this is the report
that's feeding that that email.

00:29:31.500 --> 00:29:35.716
So the first several columns here
for the first sensor, that's the patch

00:29:35.716 --> 00:29:36.616
deployment results.

00:29:36.616 --> 00:29:39.166
Then we have a couple for
the patch deployment errors

00:29:40.200 --> 00:29:41.566
and then the final sensor

00:29:41.566 --> 00:29:45.050
is the patch list applicability

00:29:45.450 --> 00:29:49.066
based on which parcels
we're deploying to that computer group.

00:29:49.850 --> 00:29:53.600
So we see the patches that were installed

00:29:54.200 --> 00:29:56.700
or failed or aborted and not installed.

00:29:57.533 --> 00:30:00.716
Then we see the patch deployment errors
and then any remaining

00:30:00.716 --> 00:30:11.600
applicable patches,
and that's all we'll cover for.

00:30:11.600 --> 00:30:15.866
Now, with the saved questions,
I recommend looking through here,

00:30:15.900 --> 00:30:18.466
you might find some other things useful

00:30:18.983 --> 00:30:21.833
and the default questions out of the box

00:30:21.833 --> 00:30:23.900
and we will have more
coming in the future.

00:30:23.900 --> 00:30:26.900
If you have any saved questions
that you would like us

00:30:26.900 --> 00:30:31.016
to add to this list for your company,
please let us know.

00:30:31.033 --> 00:30:33.450
So those are our way.

00:30:33.866 --> 00:30:37.283
Next, let's
go ahead and take a look at the dashboards

00:30:37.283 --> 00:30:41.450
under the data tab.

00:30:41.450 --> 00:30:45.300
We've created these dashboards
to hopefully be the starting point

00:30:45.300 --> 00:30:46.583
when you come into the console,

00:30:47.850 --> 00:30:49.666
the two that we'll focus on right now

00:30:49.666 --> 00:30:53.066
are the third party application updates
and the Windows patching.

00:30:54.083 --> 00:30:57.616
The system management
dashboard may be changed

00:30:57.616 --> 00:30:59.966
or moved into the Windows patching.

00:30:59.966 --> 00:31:01.216
We're not sure yet.

00:31:01.216 --> 00:31:06.650
And you will be getting a third dashboard
specifically focused on the Tanium

00:31:06.650 --> 00:31:11.900
client health
so that you can find and report on issues

00:31:11.900 --> 00:31:15.116
with the Tanium client
installed on the endpoints.

00:31:15.983 --> 00:31:18.650
So let's start off
and take a look at the third

00:31:18.650 --> 00:31:21.716
party application updates Right now.

00:31:21.716 --> 00:31:26.550
We spent some time looking over saved
questions and how to build questions,

00:31:26.550 --> 00:31:30.650
and so this will make a lot more sense now
because they are all fed,

00:31:30.650 --> 00:31:34.516
all of these dashboard
panels are fed by Tanium questions.

00:31:35.550 --> 00:31:39.350
So the first thing we have here,
each one of these applications

00:31:39.350 --> 00:31:43.350
or applications that we are updating
for you in some cases,

00:31:43.850 --> 00:31:46.350
and the panel itself

00:31:46.883 --> 00:31:51.116
is fed by reports
coming from the the data tab here.

00:31:52.516 --> 00:31:53.750
This top section is

00:31:53.750 --> 00:31:57.200
a snapshot in time right now.

00:31:57.616 --> 00:32:00.200
It will show the current status

00:32:00.983 --> 00:32:04.016
of the versions of each application.

00:32:04.016 --> 00:32:08.400
So Google Chrome, these are the
the versions that are installed right now.

00:32:08.400 --> 00:32:11.783
And it's also collecting any recent

00:32:11.783 --> 00:32:14.000
data from systems
that are currently offline.

00:32:14.900 --> 00:32:18.750
So this should be a snapshot
of all of the systems in your environment

00:32:20.183 --> 00:32:22.133
that Tanium knows about

00:32:22.133 --> 00:32:25.400
and the number of systems that have that
particular version installed.

00:32:25.400 --> 00:32:29.366
So you can quickly come in here
and see what the latest version is

00:32:29.366 --> 00:32:33.950
and which systems may be on older versions
and need to be updated.

00:32:33.950 --> 00:32:37.800
Maybe there's something wrong with these
systems that need some investigation.

00:32:37.800 --> 00:32:38.600
So what you could do

00:32:38.600 --> 00:32:41.600
is you can actually come in
and you can click on one of these numbers

00:32:42.616 --> 00:32:45.116
to see the report.

00:32:45.750 --> 00:32:48.833
So now we're in the reporting screen here,

00:32:49.583 --> 00:32:52.350
specifically the software versions
for Google Chrome.

00:32:52.700 --> 00:32:55.766
And you can see up here
we already have that

00:32:55.766 --> 00:32:58.966
particular version
that we clicked on filtered.

00:32:59.000 --> 00:33:01.616
So we're only seeing one result

00:33:01.616 --> 00:33:04.166
and the number of systems
that have that one installed,

00:33:04.650 --> 00:33:08.900
you can select here, you can drill down
and interact and get the computer names

00:33:08.900 --> 00:33:12.016
or any other information you want
about those systems for remediation.

00:33:13.733 --> 00:33:16.550
But if we close this tab
and go back to the dashboard

00:33:16.550 --> 00:33:19.283
here,
you can also click on the Google Chrome

00:33:19.650 --> 00:33:24.150
name of the panel here
and we'll get that same report.

00:33:24.150 --> 00:33:27.450
But with all of the versions included.

00:33:28.133 --> 00:33:31.550
So you see all of the versions here.

00:33:31.550 --> 00:33:34.100
Now, like I talked about before,

00:33:34.100 --> 00:33:37.433
we have the no results item here.

00:33:37.433 --> 00:33:38.816
It displays a little different

00:33:38.816 --> 00:33:41.866
when we're looking at reports
instead of the saved questions.

00:33:41.866 --> 00:33:48.233
But that's what that blank row is.

00:33:48.233 --> 00:33:50.783
So again, this is Kurt view.

00:33:51.416 --> 00:33:52.816
If we scroll down here,

00:33:53.933 --> 00:33:54.800
we'll see the

00:33:54.800 --> 00:33:57.350
historical views
of each of these applications.

00:33:59.033 --> 00:34:01.466
As a new update comes out.

00:34:01.466 --> 00:34:04.550
You can see the percentage of that

00:34:05.183 --> 00:34:08.483
that particular version as it gets updated
Throughout the environment,

00:34:09.833 --> 00:34:13.066
the total of all of the versions
should equal up to the number of systems

00:34:13.066 --> 00:34:25.850
in your in your network.

00:34:25.850 --> 00:34:30.616
This view gives us the last 30 days,
and when a new update comes out,

00:34:30.616 --> 00:34:33.950
you'll see it start out at the bottom here
and it will start to grow

00:34:34.466 --> 00:34:37.950
into a larger percentage
of your environment.

00:34:37.950 --> 00:34:41.000
If we're updating it.

00:34:41.000 --> 00:34:48.200
So again, each one of the applications
has its own dashboard.

00:34:48.200 --> 00:34:51.900
And if you don't have
one of these applications in your network,

00:34:52.666 --> 00:34:54.233
this panel will just show up gray

00:34:54.233 --> 00:34:58.300
if you're not using Zoom for Outlook
plugin, this

00:34:58.450 --> 00:35:01.466
this would just show up as a gray panel
grayed out.

00:35:01.466 --> 00:35:05.900
You'll only see the things
that are relevant to your environment.

00:35:05.900 --> 00:35:07.733
So let's go back to the other dashboards.

00:35:07.733 --> 00:35:14.300
Let's take a look at the patching
dashboard now.

00:35:14.300 --> 00:35:18.083
And just as we had in the third party
updates dashboard,

00:35:18.800 --> 00:35:22.066
each of these items are being fed
by a report.

00:35:22.350 --> 00:35:27.000
You can click on the titles of each panel
to view that report, or you can click on

00:35:27.000 --> 00:35:31.516
any of the data points to have a filtered
report for that data point.

00:35:32.900 --> 00:35:34.850
Some of
these are going to be very limited.

00:35:34.850 --> 00:35:37.100
We can't show everything in every report.

00:35:37.100 --> 00:35:40.700
So, you know, if you see ten results here,
there are more.

00:35:40.816 --> 00:35:43.916
You can just click on that report
name to see all of the details.

00:35:44.966 --> 00:35:48.166
Now, again, because everyone is using
a different patch list,

00:35:48.166 --> 00:35:51.566
depending on what the patch group is,

00:35:51.566 --> 00:35:55.650
we have different panels
for each of the patch lists.

00:35:56.116 --> 00:36:01.666
So if we were installing all applicable
patches, it will be the global patch list.

00:36:01.666 --> 00:36:02.666
If we're only installing

00:36:02.666 --> 00:36:05.750
critical and important,
a lot of the server groups are doing this.

00:36:06.716 --> 00:36:09.283
It would be this patch list.

00:36:09.416 --> 00:36:11.566
So these are going to show

00:36:12.416 --> 00:36:14.633
also smaller panels here for the

00:36:15.266 --> 00:36:17.900
plus number of days

00:36:17.900 --> 00:36:23.066
for each of these patch lists.

00:36:23.066 --> 00:36:27.050
As we scroll down here, we're going to see
that the patches installed by Tanium.

00:36:28.283 --> 00:36:30.766
So you can see after your

00:36:31.850 --> 00:36:34.466
your patch maintenance window,

00:36:34.916 --> 00:36:37.500
you can come in here
and see which patches were installed,

00:36:37.500 --> 00:36:41.216
the number of patches that Tanium
has installed in the last 30 days.

00:36:41.666 --> 00:36:44.266
And then we have the same report
filtered by the last

00:36:44.266 --> 00:36:47.866
seven days.

00:36:47.866 --> 00:36:52.250
Then we have like
we talked about before, a different report

00:36:52.250 --> 00:36:55.066
that's looking at the Windows update log

00:36:55.400 --> 00:36:58.950
to see patches by any source.

00:36:59.216 --> 00:37:00.616
So this is going to list

00:37:00.616 --> 00:37:04.316
the same thing that the patches
that were installed in the last 30 days.

00:37:04.616 --> 00:37:09.166
And then that same report right here,
this is going to indicate the source.

00:37:09.983 --> 00:37:13.816
So we have some that are in SCCM, WUSA,

00:37:14.483 --> 00:37:18.150
and some others here.

00:37:18.150 --> 00:37:22.100
And again, for the seven days

00:37:24.383 --> 00:37:27.233
there will be some modifications
coming to these

00:37:28.050 --> 00:37:32.366
dashboards, will add a couple of panels,
some things that we find useful.

00:37:32.783 --> 00:37:37.250
These
take some time to build out and refine,

00:37:37.250 --> 00:37:39.900
and that covers it for the dashboards.

00:37:40.850 --> 00:37:43.250
Again, more to come.

00:37:43.350 --> 00:37:47.966
Next, we'll talk about the reports.

00:37:47.966 --> 00:37:51.833
The reports we've reviewed most of them
already through the dashboards.

00:37:51.950 --> 00:37:54.833
Again, each one of those panels
you can click on brings

00:37:54.833 --> 00:37:57.300
you to one of the associated reports.

00:37:57.833 --> 00:38:00.600
So there are a couple reports in here
that we are

00:38:00.600 --> 00:38:03.683
not using in the dashboard,
so I'll point those out.

00:38:04.316 --> 00:38:08.716
So before we do that, though,
let's take a look over here on the left.

00:38:08.716 --> 00:38:10.050
We have labels.

00:38:10.050 --> 00:38:11.100
Each of these reports

00:38:11.100 --> 00:38:14.400
we can assign to different labels
depending on what they're related to.

00:38:15.266 --> 00:38:18.600
I've assigning some of them
to deploy and patch,

00:38:19.100 --> 00:38:21.600
and we're going to have a Tanium
client health

00:38:21.766 --> 00:38:24.866
panel or label here

00:38:24.866 --> 00:38:27.150
so you can click on one of these labels

00:38:27.616 --> 00:38:31.350
and it will filter
the reports you have here by that label.

00:38:33.016 --> 00:38:35.033
So the first thing I want to show you

00:38:35.033 --> 00:38:37.050
is that the patches installed

00:38:39.683 --> 00:38:43.583
in the dashboard that we just looked down,
there was a patches installed by Tanium.

00:38:43.583 --> 00:38:47.483
30 days, seven days,
and then we have installed by any source

00:38:47.816 --> 00:38:51.016
30 days and seven days.

00:38:51.016 --> 00:38:54.066
But when you click on those panels,
you're not going to see them in a

00:38:54.083 --> 00:38:59.266
in a friendly view, it's
going to be just the patches you can find.

00:38:59.266 --> 00:39:02.566
The sister reports here
to include the computer name

00:39:02.566 --> 00:39:06.383
so you don't have to actually drill down
and get those computer names that way.

00:39:06.900 --> 00:39:09.650
So each
one of those reports has its associated

00:39:10.200 --> 00:39:13.583
computer name report.

00:39:13.583 --> 00:39:18.166
And then we also have some of the
the patch tooling

00:39:18.166 --> 00:39:23.816
status is one,
and there's also a deploy tooling status.

00:39:23.850 --> 00:39:26.900
These are the reports
that I'm going to be creating

00:39:26.900 --> 00:39:30.150
to help feed a dashboard
for the Tanium client health.

00:39:30.566 --> 00:39:31.500
So there are

00:39:31.500 --> 00:39:34.200
there are tools on the endpoint
that the Tanium client uses

00:39:34.200 --> 00:39:35.783
to do the patch installs.

00:39:35.783 --> 00:39:40.583
And then also with the third party
updates, they have the deployed tools.

00:39:41.850 --> 00:39:43.883
So you can look here to see

00:39:44.100 --> 00:39:48.600
if any of the systems the Tanium client
is not installed in in a healthy state.

00:39:48.600 --> 00:39:55.216
It needs attention
or if they're in an optimal state.

00:39:55.216 --> 00:39:58.016
Again, there are more reports
and dashboards to come.

00:39:58.466 --> 00:40:00.650
The last thing I'll cover here before we

00:40:01.850 --> 00:40:03.050
call it

00:40:05.666 --> 00:40:06.916
on your home page here

00:40:06.916 --> 00:40:09.116
you have the dashboards list.

00:40:10.050 --> 00:40:13.133
I think by default, when you log in,
this will be empty.

00:40:13.133 --> 00:40:16.350
You can actually select
the pencil icon here

00:40:16.766 --> 00:40:20.750
and you can select from the different
dashboards that are available

00:40:20.750 --> 00:40:25.700
to populate these by default,
when you log in.

00:40:25.700 --> 00:40:30.766
And that's all I have for this training,
there will be more to come in

00:40:31.283 --> 00:40:34.800
future training regarding the patch module
and some of the things

00:40:34.800 --> 00:40:36.350
that we plan to expose there.

00:40:37.400 --> 00:40:39.466
But that wraps it up for this video.

00:40:39.466 --> 00:40:42.133
Thanks for joining us.

