Import aiml
Import yampy
Import os

#Authenticate to Yammer

authenticator = yampy.Authenticator(client_id="TkY64m6RwSIF9bujLky7A",client_secret="01LGoxOAgVrVjrevE4FiRmA3DKTZ44FGF7ETuU8Ro")
yammer = yampy.Yammer(access_token="4006-bzK26lYtX0ILCL6ipBuRg")

# Initiate variable new message to constantly check for new private messages
lastmessageid=0
lastmessagesenderid=0
lastmessagecontent="null"

# Create the kernel and learn AIML files
kernel=aiml.Kernel()

# Set working directory
os.chdir("/home/reddowan/Documents/r2d2")

if os.path.isfile("AFR2D2.brn"):
kernel.bootstrap(brainFile = "AFR2D2.brn")

else:

#load ALICE AIML script, find last version on google. Modify locally to your needs to personalize your bot
kernel.learn("reduction.names.aiml")
kernel.learn("reduction0.safe.aiml")
kernel.learn("reduction1.safe.aiml")
kernel.learn("reduction2.safe.aiml")
kernel.learn("reduction3.safe.aiml")
kernel.learn("reduction4.safe.aiml")
kernel.learn("reductions-update.aiml")

kernel.learn("mp0.aiml")
kernel.learn("mp1.aiml")
kernel.learn("mp2.aiml")
kernel.learn("mp3.aiml")
kernel.learn("mp4.aiml")
kernel.learn("mp5.aiml")
kernel.learn("mp6.aiml")


kernel.learn("ai.aiml")
kernel.learn("alice.aiml")
kernel.learn("astrology.aiml")
kernel.learn("atomic.aiml")
kernel.learn("badanswer.aiml")
kernel.learn("biography.aiml")
kernel.learn("bot.aiml")
kernel.learn("bot_profile.aiml")
kernel.learn("client.aiml")
kernel.learn("client_profile.aiml")
kernel.learn("computers.aiml")
kernel.learn("continuation.aiml")
kernel.learn("date.aiml")
kernel.learn("default.aiml")
kernel.learn("drugs.aiml")
kernel.learn("emotion.aiml")
kernel.learn("food.aiml")
kernel.learn("geography.aiml")
kernel.learn("gossip.aiml")
kernel.learn("history.aiml")
kernel.learn("humor.aiml")
kernel.learn("imponderables.aiml")
kernel.learn("inquiry.aiml")
kernel.learn("interjection.aiml")
kernel.learn("iu.aiml")
kernel.learn("junktest.text")
kernel.learn("knowledge.aiml")
kernel.learn("literature.aiml")
kernel.learn("loebner10.aiml")
kernel.learn("money.aiml")
kernel.learn("movies.aiml")
kernel.learn("music.aiml")
kernel.learn("numbers.aiml")
kernel.learn("personality.aiml")
kernel.learn("phone.aiml")
kernel.learn("pickup.aiml")
kernel.learn("politics.aiml")
kernel.learn("primeminister.aiml")
kernel.learn("primitive-math.aiml")
kernel.learn("psychology.aiml")
kernel.learn("religion.aiml")
kernel.learn("salutations.aiml")
kernel.learn("science.aiml")
kernel.learn("sex.aiml")
kernel.learn("sports.aiml")
kernel.learn("stack.aiml")
kernel.learn("stories.aiml")
kernel.learn("that.aiml")
kernel.learn("wallace.aiml")
kernel.learn("xfind.aiml")
kernel.learn("update_mccormick.aiml")

kernel.learn("update1.aiml")

kernel.saveBrain("AFR2D2.brn")



while True:
#if someone else than the bot wrote the bot will answer
 if yammer.messages.private(limit=1).messages[0].sender_id!=1562046832
  lastmessagesenderid=yammer.messages.private(limit=1).messages[0].sender_id  
  lastmessagecontent=str(yammer.messages.private(limit=1).messages[0].body.plain)
  lastmessageid=yammer.messages.private(limit=1).messages[0].conversation_id
  
  
  lastresponse=kernel.respond(lastmessagecontent)


  yammer.messages.create(lastresponse,replied_to_id=lastmessageid)



