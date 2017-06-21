/*
 * View model for OctoPrint-PanTilt-ESP8266
 *
 * Author: You
 * License: AGPLv3
 */
$(function() {
    function Pantilt_esp8266ViewModel(parameters) {
        var self = this;

        // assign the injected parameters, e.g.:
        // self.loginStateViewModel = parameters[0];
        // self.settingsViewModel = parameters[1];

        // TODO: Implement your plugin's view model here.
    }

    // view model class, parameters for constructor, container to bind to
    OCTOPRINT_VIEWMODELS.push([
        Pantilt_esp8266ViewModel,

        // e.g. loginStateViewModel, settingsViewModel, ...
        [ /* "loginStateViewModel", "settingsViewModel" */ ],

        // e.g. #settings_plugin_OctoPrint-PanTilt-ESP8266, #tab_plugin_OctoPrint-PanTilt-ESP8266, ...
        [ /* ... */ ]
    ]);
});
