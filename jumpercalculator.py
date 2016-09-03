# knitting gauge from swatching
# future - could make the variables be functions that calculate the stitches and rows per inch from a 4 inch input

stitchesperinch = float( raw_input("Please enter your number of stitches per 1 inch: ") )
rowsperinch = float( raw_input("Please enter your number of rows per 1 inch: ") )


# personal measurements

neckwidthinches = float( raw_input("Please enter your desired neck width: ") )

chestcircumferenceinches = float( raw_input("Please enter your desired chest circumference: ") )

backtofrontneckdropinches = float( raw_input("Please enter your desired neck depth: ") )

sleevecircumferenceinches = float( raw_input("Please enter your desired sleeve circumference: ") )

shouldertounderaminches = float( raw_input("Please enter your desired yoke depth: ") )

sleevelenghtinches = float( raw_input("Please enter your desired sleeve length: ") )


# calculations
# cast on count: [back neck width x sts per inch] + [~30% of that number for sleeve top x 2] + [1 front neck st x 2] = CO
castoncount = ( neckwidthinches * stitchesperinch ) + ( ( neckwidthinches * stitchesperinch * 0.3 ) * 2 ) + 2



#Under arm cast on count - after separating sleeves
#desired underarm width (rule of thumb is ~8% of body circumference) x sts per inch = underarm CO count

underarmcastoncount = ( chestcircumferenceinches * 0.08 ) * stitchesperinch



# neck depth: desired drop from back to front neck edge x rows per inch = neck depth
neckdepth = backtofrontneckdropinches * rowsperinch



# front and back stitch count at underarm/chest:
#  1/2 chest circumference x sts per inch = front or back st count***
#NOTE: subtract underarmcastoncount from this number to get the number you are increasing to during the raglan shaping.
frontandbackstitchcountchest = ( chestcircumferenceinches / 2 ) * stitchesperinch - underarmcastoncount



#sleeves stitch count:
#desired sleeve circumference x sts per inch = sleeve st count***
#NOTE: subtract underarmcastoncount from this number to get the number you are increasing to during the raglan shaping

sleevestitchcount = sleevecircumferenceinches * stitchesperinch - underarmcastoncount


#Yoke depth
#desired distance from shoulder to underarm x rows/rounds per inch = yoke depth

yokedepth = shouldertounderaminches * rowsperinch


#desired sleeve lenght: sleeve length x rows per inch
sleevelength = sleevelenghtinches * rowsperinch


#improvPattern = "You need to cast on", castoncount, "stitches." + "Your under arm cast on count is", underarmcastoncount, "stitches." + "You need to knit", neckdepth, "rows for your desired neck depth." + "You need to increase to", frontandbackstitchcountchest, "stitches for front and back." + "You need to increase to", sleevestitchcount, "sleeve stitches." + "You need to knit", yokedepth, "rows for your desired yoke depth." + "You need to knit", sleevelength, "rows for your desired sleeve length.")

#print improvPattern

note_text = "You need to cast on %s stitches." % castoncount
note_text += "\nYour under arm cast on count is %s stitches." % underarmcastoncount
note_text += "\nYou need to knit %s rows for your desired neck depth." % neckdepth
note_text += "\nYou need to increase to %s stitches for front and back." % frontandbackstitchcountchest
note_text += "\nYou need to increase to %s sleeve stitches." % sleevestitchcount
note_text += "\nYou need to knit %s rows for your desired yoke depth." % yokedepth
note_text += "\nYou need to knit %s rows for your desired sleeve length." % sleevelength

print note_text

import hashlib
import binascii
import evernote.edam.userstore.constants as UserStoreConstants
import evernote.edam.type.ttypes as Types

from evernote.api.client import EvernoteClient
#authentication with sandbox


# Real applications authenticate with Evernote using OAuth, but for the
# purpose of exploring the API, you can get a developer token that allows
# you to access your own Evernote account. To get a developer token, visit
# https://sandbox.evernote.com/api/DeveloperToken.action
auth_token = "S=s1:U=92df9:E=15e48a870d7:C=156f0f74480:P=1cd:A=en-devtoken:V=2:H=4199de2941e353c9fd1f45b9aecd41cc"

if auth_token == "your developer token":
    print "Please fill in your developer token"
    print "To get a developer token, visit " \
        "https://sandbox.evernote.com/api/DeveloperToken.action"
    exit(1)

dev_token = "S=s1:U=92df9:E=15e48a870d7:C=156f0f74480:P=1cd:A=en-devtoken:V=2:H=4199de2941e353c9fd1f45b9aecd41cc"
client = EvernoteClient(token=dev_token)
userStore = client.get_user_store()
user = userStore.getUser()
print user.username



#create a new note

noteStore = client.get_note_store()
note = Types.Note()
note.title = "Improv Sweater pattern"
note.content = '<?xml version="1.0" encoding="UTF-8"?><!DOCTYPE en-note SYSTEM "http://xml.evernote.com/pub/enml2.dtd">'
note.content += '<en-note>'
note.content += note_text
note.content += '</en-note>'
note = noteStore.createNote(note)

def makeNote(authToken, noteStore, noteTitle, noteBody, resources=[], parentNotebook=None):
	"""
	Create a Note instance with title and body
	Send Note object to user's account
	"""

	ourNote = Types.Note()
	ourNote.title = noteTitle

	## Build body of note

	nBody = "<?xml version=\"1.0\" encoding=\"UTF-8\"?>"
	nBody += "<!DOCTYPE en-note SYSTEM \"http://xml.evernote.com/pub/enml2.dtd\">"
	nBody += "<en-note>%s" % noteBody
	if resources:
		### Add Resource objects to note body
		nBody += "<br />" * 2
		ourNote.resources = resources
		for resource in resources:
			hexhash = binascii.hexlify(resource.data.bodyHash)
			nBody += "Attachment with hash %s: <br /><en-media type=\"%s\" hash=\"%s\" /><br />" % \
				(hexhash, resource.mime, hexhash)
	nBody += "</en-note>"

	ourNote.content = nBody

	## parentNotebook is optional; if omitted, default notebook is used
	if parentNotebook and hasattr(parentNotebook, 'guid'):
		ourNote.notebookGuid = parentNotebook.guid

	## Attempt to create note in Evernote account
	try:
		note = noteStore.createNote(authToken, ourNote)
	except Errors.EDAMUserException, edue:
		## Something was wrong with the note data
		## See EDAMErrorCode enumeration for error code explanation
		## http://dev.evernote.com/documentation/reference/Errors.html#Enum_EDAMErrorCode
		print "EDAMUserException:", edue
		return None
	except Errors.EDAMNotFoundException, ednfe:
		## Parent Notebook GUID doesn't correspond to an actual notebook
		print "EDAMNotFoundException: Invalid parent notebook GUID"
		return None
	## Return created note object
	return note