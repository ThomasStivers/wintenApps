# Windows 10 add-on update and config facility
# Copyright 2017 Joseph Lee, released under GPL.

# Add-on configuration and updates.
# Because the add-on employs continuous delivery model, it is beneficial to provide update facility.
# Base config section was inspired by Read Feeds (Noelia Martinez).
# Overall update check routine comes from StationPlaylist Studio add-on (Joseph Lee).)

import os
import threading
import urllib
import time
import re
import threading
import config
import gui
import wx
import addonHandler

# Add-on config database
confspec = {
	"autoUpdateCheck": "boolean(default=true)",
	"updateChannel": "string(default=dev)",
	"updateCheckTime": "integer(default=0)",
}
config.conf.spec["wintenApps"] = confspec

_addonDir = os.path.join(os.path.dirname(__file__), "..", "..")
addonVersion = addonHandler.Addon(_addonDir).manifest['version']
addonCheckInterval = 86400

channels={
	"stable":"http://addons.nvda-project.org/files/get.php?file=w10",
	"dev":"http://addons.nvda-project.org/files/get.php?file=w10-dev",
}

def updateQualify(url):
	version = re.search("wintenApps-(?P<version>.*).nvda-addon", url.url).groupdict()["version"]
	return None if version == addonVersion else version

# To avoid freezes, a background thread will run after the global plugin constructor calls wx.CallAfter.
def startupUpdateCheck():
	threading.Thread(target=updateCheck, kwargs={"startupCheck":True}).start()

progressDialog = None
def updateCheck(startupCheck=False):
	global progressDialog
	# At least let users know that update check has started with a short beep.
	if startupCheck:
		import tones
		tones.beep(500, 50)
	config.conf["wintenApps"]["updateCheckTime"] = int(time.time())
	updateCandidate = False
	updateURL = channels[config.conf["wintenApps"]["updateChannel"]]
	try:
		url = urllib.urlopen(updateURL)
		url.close()
	except IOError:
		if not startupCheck:
			wx.CallAfter(progressDialog.done)
			progressDialog = None
			# Translators: Error text shown when add-on update check fails.
			wx.CallAfter(gui.messageBox, _("Error checking for update."), _("Studio add-on update"), wx.ICON_ERROR)
		return
	if not startupCheck:
		wx.CallAfter(progressDialog.done)
		progressDialog = None
	if url.code != 200:
		if not startupCheck:
			# Translators: Text shown when update check fails for some odd reason.
			wx.CallAfter(gui.messageBox, _("Add-on update check failed."), _("Windows 10 App Essentials update"))
		return
	else:
		# Am I qualified to update?
		qualified = updateQualify(url)
		if qualified is None:
			if not startupCheck:
				# Translators: Presented when no add-on update is available.
				wx.CallAfter(gui.messageBox, _("No add-on update available."), _("Windows 10 App Essentials update"))
			return
		else:
			# Translators: Text shown if an add-on update is available.
			checkMessage = _("Windows 10 App Essentials {newVersion} is available. Would you like to update?").format(newVersion = qualified)
			# Translators: Title of the add-on update check dialog.
			wx.CallAfter(getUpdateResponse, checkMessage, _("Windows 10 App Essentials update"), updateURL)

def getUpdateResponse(message, caption, updateURL):
	if gui.messageBox(message, caption, wx.YES | wx.NO | wx.CANCEL | wx.CENTER | wx.ICON_QUESTION) == wx.YES:
		os.startfile(updateURL)

class WinTenAppsConfigDialog(wx.Dialog):

	def __init__(self, parent):
		# Translators: The title of a dialog to configure advanced SPL add-on options such as update checking.
		super(WinTenAppsConfigDialog, self).__init__(parent, title=_("Windows 10 App Essentials settings"))

		mainSizer = wx.BoxSizer(wx.VERTICAL)
		w10Helper = gui.guiHelper.BoxSizerHelper(self, orientation=wx.VERTICAL)

		# Translators: A checkbox to toggle automatic add-on updates.
		self.autoUpdateCheckbox=w10Helper.addItem(wx.CheckBox(self,label=_("Automatically check for add-on &updates")))
		self.autoUpdateCheckbox.SetValue(config.conf["wintenApps"]["autoUpdateCheck"])
		# Translators: The label for a setting in SPL add-on settings/advanced options to select automatic update interval in days.
		# Translators: The label for a combo box to select update channel.
		labelText = _("&Add-on update channel:")
		self.channels=w10Helper.addLabeledControl(labelText, wx.Choice, choices=["development", "stable"])
		self.updateChannels = ("dev", "stable")
		self.channels.SetSelection(self.updateChannels.index(config.conf["wintenApps"]["updateChannel"]))
		# Translators: The label of a button to check for add-on updates.
		updateCheckButton = w10Helper.addItem(wx.Button(self, label=_("Check for add-on &update")))
		updateCheckButton.Bind(wx.EVT_BUTTON, self.onUpdateCheck)

		w10Helper.addDialogDismissButtons(self.CreateButtonSizer(wx.OK | wx.CANCEL))
		self.Bind(wx.EVT_BUTTON, self.onOk, id=wx.ID_OK)
		self.Bind(wx.EVT_BUTTON, self.onCancel, id=wx.ID_CANCEL)
		mainSizer.Add(w10Helper.sizer, border=gui.guiHelper.BORDER_FOR_DIALOGS, flag=wx.ALL)
		mainSizer.Fit(self)
		self.Sizer = mainSizer
		self.autoUpdateCheckbox.SetFocus()
		self.Center(wx.BOTH | wx.CENTER_ON_SCREEN)

	def onOk(self, evt):
		config.conf["wintenApps"]["autoUpdateCheck"] = self.autoUpdateCheckbox.Value
		config.conf["wintenApps"]["updateChannel"] = ("dev", "stable")[self.channels.GetSelection()]
		self.Destroy()

	def onCancel(self, evt):
		self.Destroy()

	def onUpdateCheck(self, evt):
		self.onOk(None)
		global progressDialog
		progressDialog = gui.IndeterminateProgressDialog(gui.mainFrame,
		# Translators: The title of the dialog presented while checking for add-on updates.
		_("Add-on update check"),
		# Translators: The message displayed while checking for newer version of Studio add-on.
		_("Checking for new version of Windows 10 App Essentials add-on..."))
		threading.Thread(target=updateCheck).start()

def onConfigDialog(evt):
	gui.mainFrame._popupSettingsDialog(WinTenAppsConfigDialog)
