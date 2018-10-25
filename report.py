
#input line ki input ditesi oita print er maddome dekhate hobe
#alert generation time
print("enter alert generation time: ")
agt = input()
#agt = agt - 4.00

#container logger--> 1/0  aggregator-->1/0
# 0---> no restart --> up
# 1 --> restart  --> down
print("is logger up/down? : ")
logger = input()
print("is aggregator up/down? : ")
aggregator = input()

#rabbitmq logs (ll = logger log) (al = aggregator log)
if (logger == '1'):
    print("logger log in rabbitmq: ")
    l_l = input()

if (aggregator== '1'):
    print("aggregator log in rabbitmq: ")
    a_l = input()

#data not visualized
print("Data last seen time: ")
start = input()
#star = start - 4.00
print("Data back time: ")
end = input()
#end = end - 4.00

if (logger == '1' and aggregator == '0'):

     print("REPORT EXCEL NOTE---->in site data \n")
     print("Alert Generation time: " +agt+
        "\nData flow visibility interruption time in ES: "+start+ "-"+end+
        "\nContainer logger has been restarted via resin and data flow was visible." +
        "\nNo. of logs in the rabbitmq queue: "+l_l+
        "\nRabbitmq queue size is decreasing")
     print("\nREPORT EXCEL NOTE---->in missing Total And Fleeet Data\n")
     print("Alert Generation time :  " + agt +
          "\nData flow visibility interruption time in ES: "+ start + "-" + end +
          "\nContainer Aggregator  was up and running")

if(logger == '0' and aggregator == '1'):

    print("\nREPORT EXCEL NOTE---->in missing Total And Fleeet Data\n")
    print("Alert Generation time :  " + agt +
          "\nData flow visibility interruption time in ES: "+ start + "-" + end +
          "\nContainer Aggregator  has been restarted via resin and data flow was visible."+
          "\nNo. of logs in the rabbitmq queue: "+a_l+
          "\nRabbitmq queue size is decreasing") 

######  never happens .... but for extreme cases

if(logger == '1' and aggregator == '1'):
    print("REPORT EXCEL NOTE---->in site data \n")
    print("Alert Generation time: " +agt+
        "\nData flow visibility interruption time in ES: "+start+ "-"+end+
        "\nContainer logger has been restarted via resin and data flow was visible." +
        "\nNo. of logs in the rabbitmq queue: "+l_l+
        "\nRabbitmq queue size is decreasing")
    print("\nREPORT EXCEL NOTE---->in missing Total And Fleeet Data\n")
    print("Alert Generation time :  " + agt +
          "\nData flow visibility interruption time in ES: "+ start + "-" + end +
          "\nContainer Aggregator  has been restarted via resin and data flow was visible."+
          "\nNo. of logs in the rabbitmq queue: "+a_l+
          "\nRabbitmq queue size is decreasing")


#alert note in ops genie

print("\n\n")
if (logger == '1' and aggregator == '0'):

    print("OPS-GENIE NOTE---->in site data tab\n")
    print("Data flow visibility interruption time in ES: " + start + "-" + end +
          "\nContainer logger has been restarted via resin and data flow was visible." +
          "\nNo. of logs in the rabbitmq queue: " + l_l +
          "\nRabbitmq queue size is decreasing")
    print("\nOPS-GENIE NOTE---->in missing Total And Fleeet Data\n")
    print("Data flow visibility interruption time in ES: " + start + "-" + end +
          "\nContainer Aggregator  was up and running")

if (logger == '0' and aggregator == '1'):

    print("\nOPS-GENIE NOTE---->in missing Total And Fleeet Data\n")
    print("Alert Generation time :  " + agt +
          "\nData flow visibility interruption time in ES: " + start + "-" + end +
          "\nContainer Aggregator  has been restarted via resin and data flow was visible." +
          "\nNo. of logs in the rabbitmq queue: " + a_l +
          "\nRabbitmq queue size is decreasing")


