'use strict';

var ACTION_TYPES = require('../constants/action-types');
var dispatcher = require('../dispatcher');
var rpc = require('../lib/rpc');

var platformManagerActionCreators = {
    requestAuthorization: function (username, password) {
        new rpc.Request({
            method: 'getAuthorization',
            params: {
                username: username,
                password: password,
            },
        })
            .call()
            .then(function (result) {
                dispatcher.dispatch({
                    type: ACTION_TYPES.REQUEST_AUTHORIZATION_SUCCESS,
                    authorization: result,
                });
            })
            .catch(rpc.Error, function (error) {
                dispatcher.dispatch({
                    type: ACTION_TYPES.REQUEST_AUTHORIZATION_FAIL,
                    error: error,
                });
            });
    },
    clearAuthorization: function () {
        dispatcher.dispatch({
            type: ACTION_TYPES.CLEAR_AUTHORIZATION,
        });
    }
};

module.exports = platformManagerActionCreators;
