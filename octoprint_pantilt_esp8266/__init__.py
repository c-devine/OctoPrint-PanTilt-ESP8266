# coding=utf-8
from __future__ import absolute_import
from __future__ import division

import urllib
import urllib2

import octoprint.plugin


class Pantilt_esp8266Plugin(octoprint.plugin.SettingsPlugin,
							octoprint.plugin.AssetPlugin,
							octoprint.plugin.TemplatePlugin,
							octoprint.plugin.StartupPlugin,
							octoprint.plugin.ShutdownPlugin):
	def __init__(self):
		self.host = None

	##~~ SettingsPlugin mixin

	def get_template_configs(self):
		return [
			dict(type="settings", custom_bindings=False)
		]

	##~~ SettingsPlugin mixin

	def get_settings_defaults(self):
		return dict(
			host='wifipantilt',
			pan=dict(
				minUs=1000,
				maxUs=2000,
				invert=False
			),
			tilt=dict(
				minUs=1000,
				maxUs=2000,
				invert=False
			)
		)

	##~~ AssetPlugin mixin

	def get_assets(self):
		# Define your plugin's asset files to automatically include in the
		# core UI here.
		return dict(
			js=["js/pantilt_esp8266.js"],
			css=["css/pantilt_esp8266.css"],
			less=["less/pantilt_esp8266.less"]
		)

	##~~ Softwareupdate hook

	def get_update_information(self):
		# Define the configuration for your plugin to use with the Software Update
		# Plugin here. See https://github.com/foosel/OctoPrint/wiki/Plugin:-Software-Update
		# for details.
		return dict(
			pantilt_esp8266=dict(
				displayName="PanTilt-ESP8266 Plugin",
				displayVersion=self._plugin_version,

				# version check: github repository
				type="github_release",
				user="you",
				repo="OctoPrint-PanTilt-ESP8266",
				current=self._plugin_version,

				# update method: pip
				pip="https://github.com/you/OctoPrint-PantTilt-ESP8266/archive/{target_version}.zip"
			)
		)

	##~~ StartupPlugin

	def on_after_startup(self):
		self.host = self._settings.get(['host'])
		self._logger.info('Using host {}'.format(self._settings.get(['host'])))

	##~~ ShutdownPlugin

	def on_shutdown(self):
		self._logger.info('on shutdownn')

	##~~ pantilt command handler hook

	def handle_pantilt(self, values, **kwargs):
		pan = int(values['pan'])
		panMin = int(values['panMin'])
		panMax = int(values['panMax'])
		tilt = int(values['tilt'])
		tiltMin = int(values['tiltMin'])
		tiltMax = int(values['tiltMax'])

		# determine pan and tilt Us values
		panVal = (pan / (panMax - panMin)) * (
			(int(self._settings.get(["pan", "maxUs"])) - int(self._settings.get(["pan", "minUs"])))) + int(
			self._settings.get(
				["pan", "minUs"]))
		tiltVal = (tilt / (tiltMax - tiltMin)) * (
			(int(self._settings.get(["tilt", "maxUs"])) - int(self._settings.get(["tilt", "minUs"])))) + int(
			self._settings.get(
				["tilt", "minUs"]))

		if self.host is not None:
			url = 'http://{}/set_values'.format(self.host)
			data = urllib.urlencode({'command': 'setUs', 'panUs': panVal, 'tiltUs': tiltVal})
			try:
				request = urllib2.Request(url, data)
				response = urllib2.urlopen(request)
				# read the response
				self._logger.info(response.read())
			except Exception as e:
				self._logger.info('Error sending command to {} : {}'.format(self._settings.get(['host']), e))


def __plugin_load__():
	global __plugin_implementation__
	__plugin_implementation__ = Pantilt_esp8266Plugin()

	global __plugin_hooks__
	__plugin_hooks__ = {
		"octoprint.plugin.softwareupdate.check_config": __plugin_implementation__.get_update_information,
		"octoprint.plugin.pantilt_handler": __plugin_implementation__.handle_pantilt
	}
