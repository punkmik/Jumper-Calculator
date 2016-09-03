
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
note.title = "I'm a test note!"
note.content = '<?xml version="1.0" encoding="UTF-8"?><!DOCTYPE en-note SYSTEM "http://xml.evernote.com/pub/enml2.dtd">'
note.content += '<en-note>Hello, world!</en-note>'
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