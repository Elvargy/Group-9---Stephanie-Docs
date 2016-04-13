/**
 * A command that can check if Kassy is alive.
 *
 * Written By:
 * 		Matthew Knox
 *
 * License:
 *		MIT License. All code unless otherwise specified is
 *		Copyright (c) Matthew Knox and Contributors 2015.
 */

var os = require("os");

exports.match = function(text, commandPrefix) {
    return text === commandPrefix + 'ping';
};

exports.run = function(api, event) {
    api.sendMessage(this.packageInfo.name + ' ' + this.packageInfo.version + ' @ ' + os.hostname()
      + ' (' + os.type() + ' ' + os.arch() + ')', event.thread_id);
    return false;
};

exports.help = function(commandPrefix) {
    return [[commandPrefix + 'ping','Checks to see if the platform is alive', 'Also displays the hostname and computer platform']];
};
