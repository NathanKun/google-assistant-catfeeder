# google-assistant-catfeeder
Let google assistant feed my cat

## How to ?
<b>feed-my-cat.php</b>  deploy on my vps with domain name and https certificate  
<b>catfeeder.py</b> => deploy on my raspberry pi zero which connect to a servo which use to distribute cat food, this script can control the servo  
<b>feedmycat.py</b> => deploy on my raspberry pi, this script can start a web server and listen to a port which is exposed by my router  
  
Create a project on <b>dialogflow</b>, create an intent, which use a webhook for fulfillment, which call the php file on vps, than the php file will send a post request to the raspberry pi server, which will then turn the servo for feeding my cat :)  
  
And then intergrate the Dialogflow project to google assistant, with the name 'Feed My Cat App', and then create a google assistant routine 'When I say: feed my cat, Do: Talk to Feed My Cat App'  
  
Finally, say 'Hey Google, feed my cat'  
