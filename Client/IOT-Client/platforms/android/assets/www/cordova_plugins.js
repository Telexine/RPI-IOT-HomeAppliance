cordova.define('cordova/plugin_list', function(require, exports, module) {
module.exports = [
    {
        "id": "cordova-plugin-device-name.DeviceName",
        "file": "plugins/cordova-plugin-device-name/www/device-name.js",
        "pluginId": "cordova-plugin-device-name",
        "clobbers": [
            "cordova.plugins.deviceName"
        ]
    }
];
module.exports.metadata = 
// TOP OF METADATA
{
    "cordova-plugin-whitelist": "1.3.2",
    "cordova-plugin-device-name": "1.3.0"
};
// BOTTOM OF METADATA
});