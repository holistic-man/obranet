(self.webpackChunk_N_E=self.webpackChunk_N_E||[]).push([[550],{6148:function(e,t,i){(window.__NEXT_P=window.__NEXT_P||[]).push(["/registro",function(){return i(3883)}])},3883:function(e,t,i){"use strict";i.r(t),i.d(t,{Div_ac2a89ea84667d600a059f034bd91dfe:function(){return Div_ac2a89ea84667d600a059f034bd91dfe},Flex_a7fa61015057bd350942b022c7f31e23:function(){return Flex_a7fa61015057bd350942b022c7f31e23},Fragment_cf53a535ae2e610a113dd361eb6ac95b:function(){return Fragment_cf53a535ae2e610a113dd361eb6ac95b},Root_c95b3ecd73ed750af0f4eedca83a45d1:function(){return Root_c95b3ecd73ed750af0f4eedca83a45d1},Text_d42fc0b6a98a6441c8231fcde8070a1f:function(){return Text_d42fc0b6a98a6441c8231fcde8070a1f},Toaster_6e90e5e87a1cac8c96c683214079bef3:function(){return Toaster_6e90e5e87a1cac8c96c683214079bef3},default:function(){return Component}});var n=i(2729),r=i(1965),c=i(7630),a=i(7294),s=i(687),d=i(6608),o=i(9894),l=i(7232),h=i(1352),m=i(3682),f=i(7838),p=i(4778),g=i(8455),u=i(9560),Z=i(917),x=i(4712),_=i(3954),w=i(5301),v=i(1664),b=i.n(v),C=i(3798),k=i(4026),z=i(1507),y=i(9008),B=i.n(y);function _templateObject(){let e=(0,n._)(["\n    0% {\n        opacity: 0;\n    }\n    100% {\n        opacity: 1;\n    }\n"]);return _templateObject=function(){return e},e}function Toaster_6e90e5e87a1cac8c96c683214079bef3(){let{resolvedColorMode:e}=(0,a.useContext)(s.kc);d.xL.__toast=x.A;let[t,i]=(0,a.useContext)(s.DR),n={description:"Check if server is reachable at ".concat((0,d.LH)(_.Ks).href),closeButton:!0,duration:12e4,id:"websocket-error"},[c,o]=(0,a.useState)(!1);return(0,a.useEffect)(()=>{i.length>=2?c||x.A.error("Cannot connect to server: ".concat(i.length>0?i[i.length-1].message:"","."),{...n,onDismiss:()=>o(!0)}):(x.A.dismiss("websocket-error"),o(!1))},[i]),(0,r.tZ)(x.x,{closeButton:!1,expand:!0,position:"bottom-right",richColors:!0,theme:e})}function Root_c95b3ecd73ed750af0f4eedca83a45d1(){let[e,t]=(0,a.useContext)(s.DR),i=(0,a.useCallback)(t=>{let i=t.target;t.preventDefault();let n={...Object.fromEntries(new FormData(i).entries())};e([(0,d.ju)("reflex___state____state.obranet___views___register____form_register_state.handle_submit",{form_data:n})]),i.reset()});return(0,r.tZ)(z.fC,{className:"Root ",css:{width:"100%"},onSubmit:i,children:(0,r.BX)(w.kC,{css:{width:"100%"},direction:"column",gap:"2",children:[(0,r.BX)(w.kC,{css:{"@media screen and (min-width: 0)":{flexDirection:"column"},"@media screen and (min-width: 30em)":{flexDirection:"column"},"@media screen and (min-width: 48em)":{flexDirection:"row"}},gap:"3",children:[(0,r.tZ)(z.gN,{className:"Field ",css:{display:"grid",marginBottom:"10px",width:"100%"},name:"name",children:(0,r.BX)(w.kC,{direction:"column",gap:"1",children:[(0,r.tZ)(z.__,{className:"Label ",css:{fontSize:"15px",fontWeight:"500",lineHeight:"35px"},children:"Nombre Completo"}),(0,r.tZ)(z.oT,{asChild:!0,className:"Control ",children:(0,r.tZ)(w.nv.f,{placeholder:"Nombre Completo",type:"text"})})]})}),(0,r.tZ)(z.gN,{className:"Field ",css:{display:"grid",marginBottom:"10px",width:"100%"},name:"email",children:(0,r.BX)(w.kC,{direction:"column",gap:"1",children:[(0,r.tZ)(z.__,{className:"Label ",css:{fontSize:"15px",fontWeight:"500",lineHeight:"35px"},children:"Correo"}),(0,r.tZ)(z.oT,{asChild:!0,className:"Control ",children:(0,r.tZ)(w.nv.f,{placeholder:"ejemplo@gmail.com",type:"email"})})]})})]}),(0,r.BX)(w.kC,{css:{"@media screen and (min-width: 0)":{flexDirection:"column"},"@media screen and (min-width: 30em)":{flexDirection:"row"},"@media screen and (min-width: 48em)":{flexDirection:"row"}},gap:"3",children:[(0,r.tZ)(z.gN,{className:"Field ",css:{display:"grid",marginBottom:"10px",width:"100%"},name:"phone",children:(0,r.BX)(w.kC,{direction:"column",gap:"1",children:[(0,r.tZ)(z.__,{className:"Label ",css:{fontSize:"15px",fontWeight:"500",lineHeight:"35px"},children:"Celular"}),(0,r.tZ)(z.oT,{asChild:!0,className:"Control ",children:(0,r.tZ)(w.nv.f,{placeholder:"+56 9 1234 5678",type:"tel"})})]})}),(0,r.BX)(w.kC,{css:{width:"100%"},direction:"column",justify:"center",gap:"1",children:[(0,r.tZ)(w.xv,{as:"p",css:{fontSize:"15px"},weight:"medium",children:"A qu\xe9 te dedicas"}),(0,r.BX)(w.Ph.fC,{name:"service",children:[(0,r.tZ)(w.Ph.xz,{placeholder:"Selecciona a qu\xe9 te dedicas"}),(0,r.BX)(w.Ph.VY,{children:[(0,r.tZ)(w.Ph.ck,{value:"pintor",children:"Pintor"}),(0,r.tZ)(w.Ph.ck,{value:"gasfiter",children:"Gasfiter"}),(0,r.tZ)(w.Ph.ck,{value:"jardinero",children:"Jardinero"}),(0,r.tZ)(w.Ph.ck,{value:"electricista",children:"Electricista"}),(0,r.tZ)(w.Ph.ck,{value:"otro",children:"Otro (Detalla en la descripci\xf3n)"})]})]})]})]}),(0,r.BX)(w.kC,{direction:"column",gap:"1",children:[(0,r.tZ)(w.xv,{as:"p",css:{"font-size":"15px","font-weight":"500","line-height":"35px"},children:"Descripci\xf3n"}),(0,r.tZ)(w.Kx,{name:"description",placeholder:"Describe brevemente en qu\xe9 consiste tu servicio y/o experiencia",resize:"vertical"})]}),(0,r.tZ)(z.k4,{asChild:!0,className:"Submit ",children:(0,r.tZ)(w.zx,{children:"Registrar"})})]})})}function Flex_a7fa61015057bd350942b022c7f31e23(){let e=(0,a.useContext)(s.M4.reflex___state____state__obranet___views___register____form_register_state);return(0,r.BX)(w.kC,{align:"start",className:"rx-Stack",css:{height:"100%"},direction:"column",gap:"1",children:[(0,r.tZ)(w.X6,{size:"4",weight:"bold",children:"Registro en Obranet"}),(0,r.tZ)(w.xv,{as:"p",size:"2",children:"Completa el formulario para ofrecer tu trabajo"}),(0,d.oA)(e.did_submit)?e.thank_you:""]})}function Text_d42fc0b6a98a6441c8231fcde8070a1f(){let e=(0,a.useContext)(s.M4.reflex___state____state__obranet___views___register____form_register_state);return(0,r.tZ)(w.xv,{as:"p",children:JSON.stringify(e.form_data)})}function Fallback(e){let{error:t,resetErrorBoundary:i}=e;return(0,r.BX)("div",{children:[(0,r.tZ)("p",{children:"Ooops...Unknown Reflex error has occured:"}),(0,r.tZ)("p",{css:{color:"red"},children:t.message}),(0,r.tZ)("p",{children:"Please contact the support."})]})}function Fragment_cf53a535ae2e610a113dd361eb6ac95b(){let[e,t]=(0,a.useContext)(s.DR);return(0,r.tZ)(a.Fragment,{children:(0,d.oA)(t.length>0)?(0,r.tZ)(a.Fragment,{children:(0,r.tZ)(o.Z,{css:{color:"crimson",zIndex:9999,position:"fixed",bottom:"33px",right:"33px",animation:"".concat(X," 1s infinite")},size:32})}):(0,r.tZ)(a.Fragment,{})})}function Div_ac2a89ea84667d600a059f034bd91dfe(){let[e,t]=(0,a.useContext)(s.DR);return(0,r.tZ)("div",{css:{position:"fixed",width:"100vw",height:"0"},title:"Connection Error: ".concat(t.length>0?t[t.length-1].message:""),children:(0,r.tZ)(Fragment_cf53a535ae2e610a113dd361eb6ac95b,{})})}let X=(0,Z.F4)(_templateObject());function Component(){let[e,t]=(0,a.useContext)(s.DR);return(0,r.BX)(c.SV,{FallbackComponent:Fallback,onError:(t,i)=>{e([(0,d.ju)("reflex___state____state.reflex___state____frontend_event_exception_state.handle_frontend_exception",{stack:t.stack})])},children:[(0,r.BX)(a.Fragment,{children:[(0,r.tZ)(Div_ac2a89ea84667d600a059f034bd91dfe,{}),(0,r.tZ)(Toaster_6e90e5e87a1cac8c96c683214079bef3,{})]}),(0,r.BX)(w.xu,{children:[(0,r.tZ)(w.kC,{align:"center",css:{as:"nav",padding:"1em",borderBottom:"1px solid #dce1e4",background:"#ecf0f3",boxShadow:"0px 4px 6px rgba(0, 0, 0, 0.1)",position:"sticky",zIndex:"1000",top:"0"},justify:"between",children:(0,r.BX)(w.kC,{css:{alignItems:"center",width:"100%"},justify:"between",children:[(0,r.tZ)(w.rU,{asChild:!0,css:{"&:hover":{color:"var(--accent-8)"}},children:(0,r.tZ)(b(),{href:"/",passHref:!0,children:(0,r.BX)(w.kC,{css:{display:"flex",alignItems:"center"},children:[(0,r.tZ)("img",{alt:"Obranet Logo",css:{height:"2.5rem",marginRight:"0.75rem",width:"2.5rem",borderRadius:"25%"},src:"https://reflex-hosting-dev-flexgen.s3.us-west-2.amazonaws.com/replicate/9b19UXt5DfX1HKBUL7bxcG3qTM6G7Nee4zMqyTpfbgTof3UbC/out-0.webp"}),(0,r.tZ)(w.xv,{as:"span",css:{fontWeight:"600",color:"#2563EB",fontSize:"1.25rem",lineHeight:"1.75rem"},children:"Obranet"})]})})}),(0,r.BX)(w.kC,{align:"start",className:"rx-Stack",css:{"@media screen and (min-width: 0)":{display:"none"},"@media screen and (min-width: 30em)":{display:"none"},"@media screen and (min-width: 48em)":{display:"flex"},"@media screen and (min-width: 62em)":{display:"flex"},"@media screen and (min-width: 80em)":{display:"flex"}},direction:"row",gap:"5",children:[(0,r.tZ)(w.rU,{asChild:!0,css:{"&:hover":{color:"var(--accent-8)"}},children:(0,r.tZ)(b(),{href:"/",passHref:!0,children:(0,r.tZ)(w.xv,{as:"p",size:"4",weight:"medium",children:"Inicio"})})}),(0,r.tZ)(w.rU,{asChild:!0,css:{"&:hover":{color:"var(--accent-8)"}},children:(0,r.tZ)(b(),{href:"/registro",passHref:!0,children:(0,r.tZ)(w.xv,{as:"p",size:"4",weight:"medium",children:"Servicios"})})}),(0,r.tZ)(w.rU,{asChild:!0,css:{"&:hover":{color:"var(--accent-8)"}},children:(0,r.tZ)(b(),{href:"/#",passHref:!0,children:(0,r.tZ)(w.xv,{as:"p",size:"4",weight:"medium",children:"Nosotros"})})}),(0,r.tZ)(w.rU,{asChild:!0,css:{"&:hover":{color:"var(--accent-8)"}},children:(0,r.tZ)(b(),{href:"/#",passHref:!0,children:(0,r.tZ)(w.xv,{as:"p",size:"4",weight:"medium",children:"Blog"})})})]}),(0,r.BX)(w.kC,{align:"start",className:"rx-Stack",direction:"row",justify:"end",gap:"4",children:[(0,r.tZ)(w.rU,{asChild:!0,css:{"&:hover":{color:"var(--accent-8)"}},children:(0,r.tZ)(b(),{href:"/registro",passHref:!0,children:(0,r.tZ)(w.zx,{css:{cursor:"pointer"},size:"3",children:"Registrate"})})}),(0,r.BX)(C.dy.Root,{direction:"left",children:[(0,r.tZ)(C.dy.Trigger,{asChild:!0,css:{"@media screen and (min-width: 0)":{display:"flex"},"@media screen and (min-width: 30em)":{display:"flex"},"@media screen and (min-width: 48em)":{display:"none"},"@media screen and (min-width: 62em)":{display:"none"},"@media screen and (min-width: 80em)":{display:"none"},cursor:"pointer"},children:(0,r.tZ)(w.zx,{size:"3",variant:"outline",children:(0,r.tZ)(l.Z,{css:{color:"var(--current-color)"}})})}),(0,r.tZ)(C.dy.Overlay,{css:{position:"fixed",left:"0",right:"0",bottom:"0",top:"0",z_index:50,background:"rgba(0, 0, 0, 0.5)"}}),(0,r.tZ)(C.dy.Portal,{children:(0,r.tZ)(w.Q2,{css:{...k.Z.styles.global[":root"],...k.Z.styles.global.body},children:(0,r.tZ)(C.dy.Content,{css:{left:"0",right:"0",bottom:"0",top:"0",position:"fixed",z_index:50,display:"flex",height:"100%",width:"85%",padding:"1.5em",background:"white"},children:(0,r.BX)(w.kC,{align:"start",className:"rx-Stack",css:{width:"100%"},direction:"column",gap:"3",children:[(0,r.tZ)(w.kC,{align:"start",className:"rx-Stack",css:{width:"100%"},direction:"row",justify:"end",gap:"3",children:(0,r.tZ)(w.kC,{css:{alignItems:"start"},children:(0,r.tZ)(C.dy.Close,{asChild:!0,children:(0,r.tZ)(w.xu,{children:(0,r.tZ)(w.zx,{css:{cursor:"pointer"},variant:"ghost",children:(0,r.tZ)(h.Z,{css:{color:"var(--current-color)"}})})})})})}),(0,r.tZ)(w.X6,{children:"Obranet"}),(0,r.tZ)(w.xv,{as:"p",children:"\n                                    Texto de descripcion\n                                    "}),(0,r.BX)(w.kC,{align:"start",className:"rx-Stack",css:{alignItems:"start",paddingTop:"1em",paddingBottom:"1em"},direction:"column",gap:"5",children:[(0,r.tZ)(w.rU,{asChild:!0,css:{"&:hover":{color:"var(--accent-8)"}},children:(0,r.tZ)(b(),{href:"/#",passHref:!0,children:(0,r.tZ)(w.xv,{as:"p",size:"4",weight:"medium",children:"Inicio"})})}),(0,r.tZ)(w.rU,{asChild:!0,css:{"&:hover":{color:"var(--accent-8)"}},children:(0,r.tZ)(b(),{href:"/#",passHref:!0,children:(0,r.tZ)(w.xv,{as:"p",size:"4",weight:"medium",children:"Servicios"})})}),(0,r.tZ)(w.rU,{asChild:!0,css:{"&:hover":{color:"var(--accent-8)"}},children:(0,r.tZ)(b(),{href:"/#",passHref:!0,children:(0,r.tZ)(w.xv,{as:"p",size:"4",weight:"medium",children:"Nosotros"})})}),(0,r.tZ)(w.rU,{asChild:!0,css:{"&:hover":{color:"var(--accent-8)"}},children:(0,r.tZ)(b(),{href:"/#",passHref:!0,children:(0,r.tZ)(w.xv,{as:"p",size:"4",weight:"medium",children:"Blog"})})}),(0,r.tZ)(w.rU,{asChild:!0,css:{"&:hover":{color:"var(--accent-8)"}},children:(0,r.tZ)(b(),{href:"/registro",passHref:!0,children:(0,r.tZ)(w.zx,{css:{cursor:"pointer"},size:"3",children:"Registrate"})})})]})]})})})})]})]})]})}),(0,r.tZ)(w.W2,{css:{padding:"16px"},size:"3",children:(0,r.tZ)(w.Zb,{size:"3",children:(0,r.BX)(w.kC,{css:{width:"100%"},direction:"column",gap:"4",children:[(0,r.BX)(w.kC,{align:"start",className:"rx-Stack",css:{height:"100%",alignItems:"center",width:"100%"},direction:"row",gap:"4",children:[(0,r.tZ)(w.Ct,{css:{padding:"0.65rem"},radius:"full",children:(0,r.tZ)(m.Z,{css:{color:"var(--current-color)"},size:32})}),(0,r.tZ)(Flex_a7fa61015057bd350942b022c7f31e23,{})]}),(0,r.tZ)(Root_c95b3ecd73ed750af0f4eedca83a45d1,{}),(0,r.tZ)(w.Z0,{size:"4"}),(0,r.tZ)(w.X6,{children:"Results"}),(0,r.tZ)(Text_d42fc0b6a98a6441c8231fcde8070a1f,{})]})})}),(0,r.tZ)(w.xu,{css:{"@media screen and (min-width: 0)":{paddingInlineStart:"5em",paddingInlineEnd:"5em"},"@media screen and (min-width: 30em)":{paddingInlineStart:"5em",paddingInlineEnd:"5em"},"@media screen and (min-width: 48em)":{paddingInlineStart:"5em",paddingInlineEnd:"5em"},"@media screen and (min-width: 62em)":{paddingInlineStart:"8em",paddingInlineEnd:"8em"},paddingTop:"3rem",paddingBottom:"3rem",width:"100%"},children:(0,r.BX)(w.kC,{align:"start",className:"rx-Stack",css:{width:"100%"},direction:"column",gap:"5",children:[(0,r.BX)(w.kC,{css:{"@media screen and (min-width: 0)":{flexDirection:"column"},"@media screen and (min-width: 30em)":{flexDirection:"column"},"@media screen and (min-width: 48em)":{flexDirection:"row"},width:"100%"},justify:"between",gap:"6",children:[(0,r.BX)(w.kC,{align:"start",className:"rx-Stack",css:{"@media screen and (min-width: 0)":{alignItems:"center"},"@media screen and (min-width: 30em)":{alignItems:"center"},"@media screen and (min-width: 48em)":{alignItems:"start"}},direction:"column",gap:"4",children:[(0,r.BX)(w.kC,{align:"start",className:"rx-Stack",css:{alignItems:"center"},direction:"row",gap:"3",children:[(0,r.tZ)("img",{alt:"Obranet Logo",css:{height:"auto",borderRadius:"25%",width:"2.25rem"},src:"https://reflex-hosting-dev-flexgen.s3.us-west-2.amazonaws.com/replicate/9b19UXt5DfX1HKBUL7bxcG3qTM6G7Nee4zMqyTpfbgTof3UbC/out-0.webp"}),(0,r.tZ)(w.X6,{size:"7",weight:"bold",children:"Obranet"})]}),(0,r.tZ)(w.xv,{as:"p",css:{"@media screen and (min-width: 0)":{textAlign:"center"},"@media screen and (min-width: 30em)":{textAlign:"center"},"@media screen and (min-width: 48em)":{textAlign:"start"},maxWidth:"30ch"},size:"3",weight:"medium",children:"Conectando a profesionales h\xe1biles con quien necesite sus servicios para todos los proyectos del hogar."})]}),(0,r.BX)(w.kC,{css:{"@media screen and (min-width: 0)":{textAlign:"center"},"@media screen and (min-width: 30em)":{textAlign:"center"},"@media screen and (min-width: 48em)":{textAlign:"start"},flexDirection:"column"},gap:"4",children:[(0,r.tZ)(w.X6,{as:"h3",size:"4",weight:"bold",children:"NAVEGACION"}),(0,r.tZ)(w.rU,{asChild:!0,css:{"&:hover":{color:"var(--accent-8)"}},children:(0,r.tZ)(b(),{href:"/#",passHref:!0,children:(0,r.tZ)(w.xv,{as:"p",size:"3",children:"Inicio"})})}),(0,r.tZ)(w.rU,{asChild:!0,css:{"&:hover":{color:"var(--accent-8)"}},children:(0,r.tZ)(b(),{href:"/#",passHref:!0,children:(0,r.tZ)(w.xv,{as:"p",size:"3",children:"Nosotros"})})}),(0,r.tZ)(w.rU,{asChild:!0,css:{"&:hover":{color:"var(--accent-8)"}},children:(0,r.tZ)(b(),{href:"/#",passHref:!0,children:(0,r.tZ)(w.xv,{as:"p",size:"3",children:"Servicios"})})}),(0,r.tZ)(w.rU,{asChild:!0,css:{"&:hover":{color:"var(--accent-8)"}},children:(0,r.tZ)(b(),{href:"/#",passHref:!0,children:(0,r.tZ)(w.xv,{as:"p",size:"3",children:"Blog"})})}),(0,r.tZ)(w.rU,{asChild:!0,css:{"&:hover":{color:"var(--accent-8)"}},children:(0,r.tZ)(b(),{href:"/#",passHref:!0,children:(0,r.tZ)(w.xv,{as:"p",size:"3",children:"Contacto"})})})]}),(0,r.BX)(w.kC,{css:{"@media screen and (min-width: 0)":{textAlign:"center"},"@media screen and (min-width: 30em)":{textAlign:"center"},"@media screen and (min-width: 48em)":{textAlign:"start"},flexDirection:"column"},gap:"4",children:[(0,r.tZ)(w.X6,{as:"h3",size:"4",weight:"bold",children:"LEGAL"}),(0,r.tZ)(w.rU,{asChild:!0,css:{"&:hover":{color:"var(--accent-8)"}},children:(0,r.tZ)(b(),{href:"/#",passHref:!0,children:(0,r.tZ)(w.xv,{as:"p",size:"3",children:"T\xe9rminos y condiciones"})})}),(0,r.tZ)(w.rU,{asChild:!0,css:{"&:hover":{color:"var(--accent-8)"}},children:(0,r.tZ)(b(),{href:"/#",passHref:!0,children:(0,r.tZ)(w.xv,{as:"p",size:"3",children:"Pol\xedtica de privacidad"})})}),(0,r.tZ)(w.rU,{asChild:!0,css:{"&:hover":{color:"var(--accent-8)"}},children:(0,r.tZ)(b(),{href:"/#",passHref:!0,children:(0,r.tZ)(w.xv,{as:"p",size:"3",children:"Pol\xedtica de cookies"})})})]})]}),(0,r.tZ)(w.Z0,{size:"4"}),(0,r.BX)(w.kC,{css:{"@media screen and (min-width: 0)":{flexDirection:"column"},"@media screen and (min-width: 30em)":{flexDirection:"column"},"@media screen and (min-width: 48em)":{flexDirection:"row"},width:"100%"},gap:"4",children:[(0,r.BX)(w.kC,{align:"center",className:"rx-Stack",css:{"@media screen and (min-width: 0)":{justifyContent:"center"},"@media screen and (min-width: 30em)":{justifyContent:"center"},"@media screen and (min-width: 48em)":{justifyContent:"start"},width:"100%"},direction:"row",gap:"2",children:[(0,r.tZ)("img",{css:{width:"2em",height:"auto",borderRadius:"25%"},src:"/logo.jpg"}),(0,r.tZ)(w.xv,{as:"p",css:{whiteSpace:"nowrap"},size:"3",weight:"medium",children:"\xa9 2024 Obranet Group"})]}),(0,r.BX)(w.kC,{css:{"@media screen and (min-width: 0)":{justifyContent:"center"},"@media screen and (min-width: 30em)":{justifyContent:"center"},"@media screen and (min-width: 48em)":{justifyContent:"center"},"@media screen and (min-width: 62em)":{justifyContent:"end"},width:"100%"},gap:"3",children:[(0,r.tZ)(w.rU,{asChild:!0,css:{"&:hover":{color:"var(--accent-8)"}},children:(0,r.tZ)(b(),{href:"/#",passHref:!0,children:(0,r.tZ)(f.Z,{css:{color:"var(--current-color)"}})})}),(0,r.tZ)(w.rU,{asChild:!0,css:{"&:hover":{color:"var(--accent-8)"}},children:(0,r.tZ)(b(),{href:"/#",passHref:!0,children:(0,r.tZ)(p.Z,{css:{color:"var(--current-color)"}})})}),(0,r.tZ)(w.rU,{asChild:!0,css:{"&:hover":{color:"var(--accent-8)"}},children:(0,r.tZ)(b(),{href:"/#",passHref:!0,children:(0,r.tZ)(g.Z,{css:{color:"var(--current-color)"}})})}),(0,r.tZ)(w.rU,{asChild:!0,css:{"&:hover":{color:"var(--accent-8)"}},children:(0,r.tZ)(b(),{href:"/#",passHref:!0,children:(0,r.tZ)(u.Z,{css:{color:"var(--current-color)"}})})})]})]})]})})]}),(0,r.BX)(B(),{children:[(0,r.tZ)("title",{children:"Obranet | Registro"}),(0,r.tZ)("meta",{content:"favicon.ico",property:"og:image"})]})]})}}},function(e){e.O(0,[534,301,111,774,888,179],function(){return e(e.s=6148)}),_N_E=e.O()}]);