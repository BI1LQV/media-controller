// ==UserScript==
// @name         mediaControllerHook
// @namespace    http://tampermonkey.net/
// @version      0.1
// @description  try to take over the world!
// @author       BI1LQV
// @match        https://www.bilibili.com/*
// @icon         https://www.google.com/s2/favicons?sz=64&domain=nowcoder.com
// @grant        none
// ==/UserScript==

(function() {
    'use strict';
    let ws = new WebSocket("ws://127.0.0.1:8091");
    ws.onopen = function(evt) {
        console.log("Connection open ...");
        ws.send("Hello WebSockets!");
    };
    window.vedioEle=document.querySelector('video')||document.querySelector('bwp-video');
    ws.onmessage = function(evt) {
        console.log( "Received Message: " + evt.data);
        switch(evt.data){
            case 'fastforward':
                vedioEle.currentTime+=10;
            break;
            case 'rewind':
                vedioEle.currentTime-=10;
            break;
            case 'decelerate':
                vedioEle.decelerate-=0.1;
            break;
            case 'accelerate':
                vedioEle.decelerate+=0.1;
            break;
        }
    };
    ws.onclose = function(evt) {
        console.log("Connection closed.");
    };
})();