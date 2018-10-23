# Alert-report-generator-mulytic
Alerts report regarding ops-genie note and report generates provided right input format

the right input format


alert generation time
container logger status 
container aggregator status
logger log from rabbitmq
aggregator log from rabbitmq
Data last seen time
Data back time

****container status 8,9

0---> no restart --> up
1 --> restart  --> down

*****depending on logger/aggregator status 10,11 will show up

An input format is given:

alert generation time 11.28
logger up down. So 1
aggregator up.So 0
logger logs 133 (as logger status down)
Data last seen time 11.18
Data back time 11.30

So the input of the code is:

11.28
1
0
133
11.18
11.30

*****here "aggregator log from rabbitmq" was not entered as its status is up.So there is no log for aggregator.
