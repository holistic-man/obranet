(self.webpackChunk_N_E=self.webpackChunk_N_E||[]).push([[161],{8649:function(e,t,r){(window.__NEXT_P=window.__NEXT_P||[]).push(["/demo/list",function(){return r(554)}])},554:function(e,t,r){"use strict";r.r(t),r.d(t,{Div_ac2a89ea84667d600a059f034bd91dfe:function(){return Div_ac2a89ea84667d600a059f034bd91dfe},Fragment_cf53a535ae2e610a113dd361eb6ac95b:function(){return Fragment_cf53a535ae2e610a113dd361eb6ac95b},Toaster_6e90e5e87a1cac8c96c683214079bef3:function(){return Toaster_6e90e5e87a1cac8c96c683214079bef3},default:function(){return Component}});var n=r(2729),o=r(1965),a=r(7630),c=r(7294),i=r(687),s=r(6608),l=r(9894),d=r(917),u=r(4712),h=r(3954),f=r(408),_=r(9008),p=r.n(_);function _templateObject(){let e=(0,n._)(["\n    0% {\n        opacity: 0;\n    }\n    100% {\n        opacity: 1;\n    }\n"]);return _templateObject=function(){return e},e}function Fragment_cf53a535ae2e610a113dd361eb6ac95b(){let[e,t]=(0,c.useContext)(i.DR);return(0,o.tZ)(c.Fragment,{children:(0,s.oA)(t.length>0)?(0,o.tZ)(c.Fragment,{children:(0,o.tZ)(l.Z,{css:{color:"crimson",zIndex:9999,position:"fixed",bottom:"33px",right:"33px",animation:"".concat(m," 1s infinite")},size:32})}):(0,o.tZ)(c.Fragment,{})})}function Toaster_6e90e5e87a1cac8c96c683214079bef3(){let{resolvedColorMode:e}=(0,c.useContext)(i.kc);s.xL.__toast=u.A;let[t,r]=(0,c.useContext)(i.DR),n={description:"Check if server is reachable at ".concat((0,s.LH)(h.Ks).href),closeButton:!0,duration:12e4,id:"websocket-error"},[a,l]=(0,c.useState)(!1);return(0,c.useEffect)(()=>{r.length>=2?a||u.A.error("Cannot connect to server: ".concat(r.length>0?r[r.length-1].message:"","."),{...n,onDismiss:()=>l(!0)}):(u.A.dismiss("websocket-error"),l(!1))},[r]),(0,o.tZ)(u.x,{closeButton:!1,expand:!0,position:"bottom-right",richColors:!0,theme:e})}let m=(0,d.F4)(_templateObject());function Fallback(e){let{error:t,resetErrorBoundary:r}=e;return(0,o.BX)("div",{children:[(0,o.tZ)("p",{children:"Ooops...Unknown Reflex error has occured:"}),(0,o.tZ)("p",{css:{color:"red"},children:t.message}),(0,o.tZ)("p",{children:"Please contact the support."})]})}function Div_ac2a89ea84667d600a059f034bd91dfe(){let[e,t]=(0,c.useContext)(i.DR);return(0,o.tZ)("div",{css:{position:"fixed",width:"100vw",height:"0"},title:"Connection Error: ".concat(t.length>0?t[t.length-1].message:""),children:(0,o.tZ)(Fragment_cf53a535ae2e610a113dd361eb6ac95b,{})})}function Component(){let[e,t]=(0,c.useContext)(i.DR);return(0,o.BX)(a.SV,{FallbackComponent:Fallback,onError:(t,r)=>{e([(0,s.ju)("reflex___state____state.reflex___state____frontend_event_exception_state.handle_frontend_exception",{stack:t.stack})])},children:[(0,o.BX)(c.Fragment,{children:[(0,o.tZ)(Div_ac2a89ea84667d600a059f034bd91dfe,{}),(0,o.tZ)(Toaster_6e90e5e87a1cac8c96c683214079bef3,{})]}),(0,o.tZ)(f.xu,{}),(0,o.BX)(p(),{children:[(0,o.tZ)("title",{children:"Obranet | Demo/List"}),(0,o.tZ)("meta",{content:"favicon.ico",property:"og:image"})]})]})}},7630:function(e,t,r){"use strict";r.d(t,{SV:function(){return ErrorBoundary}});var n=r(7294);let o=(0,n.createContext)(null),a={didCatch:!1,error:null};let ErrorBoundary=class ErrorBoundary extends n.Component{constructor(e){super(e),this.resetErrorBoundary=this.resetErrorBoundary.bind(this),this.state=a}static getDerivedStateFromError(e){return{didCatch:!0,error:e}}resetErrorBoundary(){let{error:e}=this.state;if(null!==e){for(var t,r,n=arguments.length,o=Array(n),c=0;c<n;c++)o[c]=arguments[c];null===(t=(r=this.props).onReset)||void 0===t||t.call(r,{args:o,reason:"imperative-api"}),this.setState(a)}}componentDidCatch(e,t){var r,n;null===(r=(n=this.props).onError)||void 0===r||r.call(n,e,t)}componentDidUpdate(e,t){let{didCatch:r}=this.state,{resetKeys:n}=this.props;if(r&&null!==t.error&&hasArrayChanged(e.resetKeys,n)){var o,c;null===(o=(c=this.props).onReset)||void 0===o||o.call(c,{next:n,prev:e.resetKeys,reason:"keys"}),this.setState(a)}}render(){let{children:e,fallbackRender:t,FallbackComponent:r,fallback:a}=this.props,{didCatch:c,error:i}=this.state,s=e;if(c){let e={error:i,resetErrorBoundary:this.resetErrorBoundary};if("function"==typeof t)s=t(e);else if(r)s=(0,n.createElement)(r,e);else if(null===a||(0,n.isValidElement)(a))s=a;else throw i}return(0,n.createElement)(o.Provider,{value:{didCatch:c,error:i,resetErrorBoundary:this.resetErrorBoundary}},s)}};function hasArrayChanged(){let e=arguments.length>0&&void 0!==arguments[0]?arguments[0]:[],t=arguments.length>1&&void 0!==arguments[1]?arguments[1]:[];return e.length!==t.length||e.some((e,r)=>!Object.is(e,t[r]))}}},function(e){e.O(0,[534,774,888,179],function(){return e(e.s=8649)}),_N_E=e.O()}]);