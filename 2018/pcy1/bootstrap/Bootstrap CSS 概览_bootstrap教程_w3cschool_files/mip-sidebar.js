(window.MIP=window.MIP||[]).push({name:"mip-sidebar",func:function(){define("mip-sidebar/mip-sidebar",["require","customElement","util"],function(t){function e(t){s.call(this)?n.call(this,t):i.call(this)}function i(){var t=this;if(!t.runing)if(t.runing=!0,!s.call(this)){c.css(t.element,{display:"block"}),o.call(t),t.bodyOverflow=getComputedStyle(document.body).overflow,document.body.style.overflow="hidden";var e=setTimeout(function(){t.element.setAttribute("open",""),t.element.setAttribute("aria-hidden","false"),clearTimeout(e)},t.ANIMATION_TIMEOUT)}}function n(t){var e=this;if(!e.runing){e.runing=!0,t.preventDefault(),e.element.removeAttribute("open"),e.element.setAttribute("aria-hidden","true"),r.call(e),document.body.style.overflow=e.bodyOverflow;var i=setTimeout(function(){c.css(e.element,{display:"none"}),clearTimeout(i)},e.ANIMATION_TIMEOUT)}}function o(){var t=this;if(!t.maskElement){const e=document.createElement("div");e.id="MIP-"+t.id.toUpperCase()+"-MASK",e.className="MIP-SIDEBAR-MASK",e.style.display="block",t.element.parentNode.appendChild(e),e.addEventListener("touchmove",function(t){t.preventDefault()},!1),t.maskElement=e}t.maskElement.setAttribute("on","tap:"+t.id+".close"),t.maskElement.style.display="block",u.animate(t.maskElement,{opacity:.2},{duration:500}).start(function(){t.runing=!1})}function r(){var t=this;if(t.maskElement)u.animate(t.maskElement,{opacity:0},{duration:500}).start(function(){t.maskElement.style.display="none",t.runing=!1})}function s(){return this.element.hasAttribute("open")}function a(){var t=this;if(t.maskElement=!1,t.id=t.element.id,t.side=t.element.getAttribute("side"),t.ANIMATION_TIMEOUT=100,"left"!==t.side&&"right"!==t.side)t.side="left",t.element.setAttribute("side",t.side);if(s.call(t))i.call(t);else t.element.setAttribute("aria-hidden","true");document.addEventListener("keydown",function(e){if(27===e.keyCode)n.call(t,e)},!1),t.addEventAction("toggle",function(i){e.call(t,i)}),t.addEventAction("open",function(){i.call(t)}),t.addEventAction("close",function(e){n.call(t,e)})}var l=t("customElement").create(),c=t("util"),u=c.naboo;return l.prototype.build=a,l.prototype.prerenderAllowed=function(){return!0},l}),define("mip-sidebar",["mip-sidebar/mip-sidebar"],function(t){return t}),function(){function t(t,e){t.registerMipElement("mip-sidebar",e,"mip-sidebar{position:fixed !important;top:0;max-height:100% !important;height:100%;max-width:80% !important;background-color:#efefef;min-width:45px !important;overflow-x:hidden !important;overflow-y:auto !important;z-index:9999 !important;-webkit-overflow-scrolling:touch;will-change:transform;display:none}mip-sidebar[side=left]{left:0 !important;-webkit-transform:translateX(-100%) !important;transform:translateX(-100%) !important}mip-sidebar[side=right]{right:0 !important;-webkit-transform:translateX(100%) !important;transform:translateX(100%) !important}mip-sidebar[side]{-webkit-transition:-webkit-transform 233ms cubic-bezier(0, 0, .21, 1);transition:-webkit-transform 233ms cubic-bezier(0, 0, .21, 1);transition:transform 233ms cubic-bezier(0, 0, .21, 1);transition:transform 233ms cubic-bezier(0, 0, .21, 1),-webkit-transform 233ms cubic-bezier(0, 0, .21, 1)}mip-sidebar[side][open]{-webkit-transform:translateX(0) !important;transform:translateX(0) !important}.MIP-SIDEBAR-MASK{position:fixed !important;top:0 !important;left:0 !important;width:100% !important;height:100% !important;opacity:0;background-images:none !important;background-color:#000;z-index:9998 !important;display:none}")}if(window.MIP)require(["mip-sidebar"],function(e){t(window.MIP,e)});else require(["mip","mip-sidebar"],t)}()}});