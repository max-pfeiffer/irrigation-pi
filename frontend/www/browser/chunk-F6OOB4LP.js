import{a as ye,c as Se,f as P}from"./chunk-PG5KTQWO.js";var n={allRenderFn:!1,cmpDidLoad:!0,cmpDidUnload:!1,cmpDidUpdate:!0,cmpDidRender:!0,cmpWillLoad:!0,cmpWillUpdate:!0,cmpWillRender:!0,connectedCallback:!0,disconnectedCallback:!0,element:!0,event:!0,hasRenderFn:!0,lifecycle:!0,hostListener:!0,hostListenerTargetWindow:!0,hostListenerTargetDocument:!0,hostListenerTargetBody:!0,hostListenerTargetParent:!1,hostListenerTarget:!0,member:!0,method:!0,mode:!0,observeAttribute:!0,prop:!0,propMutable:!0,reflect:!0,scoped:!0,shadowDom:!0,slot:!0,cssAnnotations:!0,state:!0,style:!0,formAssociated:!1,svg:!0,updatable:!0,vdomAttribute:!0,vdomXlink:!0,vdomClass:!0,vdomFunctional:!0,vdomKey:!0,vdomListener:!0,vdomRef:!0,vdomPropOrAttr:!0,vdomRender:!0,vdomStyle:!0,vdomText:!0,watchCallback:!0,taskQueue:!0,hotModuleReplacement:!1,isDebug:!1,isDev:!1,isTesting:!1,hydrateServerSide:!1,hydrateClientSide:!1,lifecycleDOMEvents:!1,lazyLoad:!1,profile:!1,slotRelocation:!0,appendChildSlotFix:!1,cloneNodeFix:!1,hydratedAttribute:!1,hydratedClass:!0,scriptDataOpts:!1,scopedSlotTextContentFix:!1,shadowDomShim:!1,slotChildNodesFix:!1,invisiblePrehydration:!0,propBoolean:!0,propNumber:!0,propString:!0,constructableCSS:!0,cmpShouldUpdate:!0,devTools:!1,shadowDelegatesFocus:!0,initializeNextTick:!1,asyncLoading:!1,asyncQueue:!1,transformTagName:!1,attachStyles:!0,experimentalSlotFixes:!1};var F="app";var ut=Se({});var pt=Object.defineProperty,ht=(e,t)=>{for(var s in t)pt(e,s,{get:t[s],enumerable:!0})},Le={isDev:!!n.isDev,isBrowser:!0,isServer:!1,isTesting:!!n.isTesting},Ds=e=>{let t=new URL(e,h.$resourcesUrl$);return t.origin!==O.location.origin?t.href:t.pathname};var be={},mt="http://www.w3.org/2000/svg",vt="http://www.w3.org/1999/xhtml",gt=e=>e!=null,ue=e=>(e=typeof e,e==="object"||e==="function");function yt(e){var t,s,o;return(o=(s=(t=e.head)==null?void 0:t.querySelector('meta[name="csp-nonce"]'))==null?void 0:s.getAttribute("content"))!=null?o:void 0}var St={};ht(St,{err:()=>He,map:()=>Lt,ok:()=>ne,unwrap:()=>bt,unwrapErr:()=>xt});var ne=e=>({isOk:!0,isErr:!1,value:e}),He=e=>({isOk:!1,isErr:!0,value:e});function Lt(e,t){if(e.isOk){let s=t(e.value);return s instanceof Promise?s.then(o=>ne(o)):ne(s)}if(e.isErr){let s=e.value;return He(s)}throw"should never get here"}var bt=e=>{if(e.isOk)return e.value;throw e.value},xt=e=>{if(e.isErr)return e.value;throw e.value},Dt=0,I=(e,t="")=>{if(n.profile&&performance.mark){let s=`st:${e}:${t}:${Dt++}`;return performance.mark(s),()=>performance.measure(`[Stencil] ${e}() <${t}>`,s)}else return()=>{}},Tt=(e,t)=>n.profile&&performance.mark?(performance.getEntriesByName(e,"mark").length===0&&performance.mark(e),()=>{performance.getEntriesByName(t,"measure").length===0&&performance.measure(t,e)}):()=>{};var Ct="r",It="o",Nt="s",kt="t",oe="s-id",xe="sty-id",De="c-id";var At="slot-fb{display:contents}slot-fb[hidden]{display:none}",Te="http://www.w3.org/1999/xlink",_t=["formAssociatedCallback","formResetCallback","formDisabledCallback","formStateRestoreCallback"],Me=(e,t,...s)=>{let o=null,r=null,i=null,l=!1,c=!1,a=[],$=f=>{for(let p=0;p<f.length;p++)o=f[p],Array.isArray(o)?$(o):o!=null&&typeof o!="boolean"&&((l=typeof e!="function"&&!ue(o))?o=String(o):n.isDev&&typeof e!="function"&&o.$flags$===void 0&&Q(`vNode passed as children has unexpected type.
Make sure it's using the correct h() function.
Empty objects can also be the cause, look for JSX comments that became objects.`),l&&c?a[a.length-1].$text$+=o:a.push(l?B(null,o):o),c=l)};if($(s),t&&(n.isDev&&e==="input"&&Bt(t),n.vdomKey&&t.key&&(r=t.key),n.slotRelocation&&t.name&&(i=t.name),n.vdomClass)){let f=t.className||t.class;f&&(t.class=typeof f!="object"?f:Object.keys(f).filter(p=>f[p]).join(" "))}if(n.isDev&&a.some(re)&&Q(`The <Host> must be the single root component. Make sure:
- You are NOT using hostData() and <Host> in the same component.
- <Host> is used once, and it's the single root component of the render() function.`),n.vdomFunctional&&typeof e=="function")return e(t===null?{}:t,a,Et);let d=B(e,null);return d.$attrs$=t,a.length>0&&(d.$children$=a),n.vdomKey&&(d.$key$=r),n.slotRelocation&&(d.$name$=i),d},B=(e,t)=>{let s={$flags$:0,$tag$:e,$text$:t,$elm$:null,$children$:null};return n.vdomAttribute&&(s.$attrs$=null),n.vdomKey&&(s.$key$=null),n.slotRelocation&&(s.$name$=null),s},wt={},re=e=>e&&e.$tag$===wt,Et={forEach:(e,t)=>e.map(Ce).forEach(t),map:(e,t)=>e.map(Ce).map(t).map(Ut)},Ce=e=>({vattrs:e.$attrs$,vchildren:e.$children$,vkey:e.$key$,vname:e.$name$,vtag:e.$tag$,vtext:e.$text$}),Ut=e=>{if(typeof e.vtag=="function"){let s=ye({},e.vattrs);return e.vkey&&(s.key=e.vkey),e.vname&&(s.name=e.vname),Me(e.vtag,s,...e.vchildren||[])}let t=B(e.vtag,e.vtext);return t.$attrs$=e.vattrs,t.$children$=e.vchildren,t.$key$=e.vkey,t.$name$=e.vname,t},Bt=e=>{let t=Object.keys(e),s=t.indexOf("value");if(s===-1)return;let o=t.indexOf("type"),r=t.indexOf("min"),i=t.indexOf("max"),l=t.indexOf("step");(s<o||s<r||s<i||s<l)&&z('The "value" prop of <input> should be set after "min", "max", "type" and "step"')},Rt=(e,t,s,o)=>{let r=I("hydrateClient",t),i=e.shadowRoot,l=[],c=[],a=n.shadowDom&&i?[]:null,$=o.$vnode$=B(t,null);h.$orgLocNodes$||ae(v.body,h.$orgLocNodes$=new Map),e[oe]=s,e.removeAttribute(oe),ie($,l,c,a,e,e,s),l.map(d=>{let f=d.$hostId$+"."+d.$nodeId$,p=h.$orgLocNodes$.get(f),u=d.$elm$;p&&_&&p["s-en"]===""&&p.parentNode.insertBefore(u,p.nextSibling),i||(u["s-hn"]=t,p&&(u["s-ol"]=p,u["s-ol"]["s-nr"]=u)),h.$orgLocNodes$.delete(f)}),n.shadowDom&&i&&a.map(d=>{d&&i.appendChild(d)}),r()},ie=(e,t,s,o,r,i,l)=>{let c,a,$,d;if(i.nodeType===1){for(c=i.getAttribute(De),c&&(a=c.split("."),(a[0]===l||a[0]==="0")&&($={$flags$:0,$hostId$:a[0],$nodeId$:a[1],$depth$:a[2],$index$:a[3],$tag$:i.tagName.toLowerCase(),$elm$:i,$attrs$:null,$children$:null,$key$:null,$name$:null,$text$:null},t.push($),i.removeAttribute(De),e.$children$||(e.$children$=[]),e.$children$[$.$index$]=$,e=$,o&&$.$depth$==="0"&&(o[$.$index$]=$.$elm$))),d=i.childNodes.length-1;d>=0;d--)ie(e,t,s,o,r,i.childNodes[d],l);if(i.shadowRoot)for(d=i.shadowRoot.childNodes.length-1;d>=0;d--)ie(e,t,s,o,r,i.shadowRoot.childNodes[d],l)}else if(i.nodeType===8)a=i.nodeValue.split("."),(a[1]===l||a[1]==="0")&&(c=a[0],$={$flags$:0,$hostId$:a[1],$nodeId$:a[2],$depth$:a[3],$index$:a[4],$elm$:i,$attrs$:null,$children$:null,$key$:null,$name$:null,$tag$:null,$text$:null},c===kt?($.$elm$=i.nextSibling,$.$elm$&&$.$elm$.nodeType===3&&($.$text$=$.$elm$.textContent,t.push($),i.remove(),e.$children$||(e.$children$=[]),e.$children$[$.$index$]=$,o&&$.$depth$==="0"&&(o[$.$index$]=$.$elm$))):$.$hostId$===l&&(c===Nt?($.$tag$="slot",a[5]?i["s-sn"]=$.$name$=a[5]:i["s-sn"]="",i["s-sr"]=!0,n.shadowDom&&o&&($.$elm$=v.createElement($.$tag$),$.$name$&&$.$elm$.setAttribute("name",$.$name$),i.parentNode.insertBefore($.$elm$,i),i.remove(),$.$depth$==="0"&&(o[$.$index$]=$.$elm$)),s.push($),e.$children$||(e.$children$=[]),e.$children$[$.$index$]=$):c===Ct&&(n.shadowDom&&o?i.remove():n.slotRelocation&&(r["s-cr"]=i,i["s-cn"]=!0))));else if(e&&e.$tag$==="style"){let f=B(null,i.textContent);f.$elm$=i,f.$index$="0",e.$children$=[f]}},ae=(e,t)=>{if(e.nodeType===1){let s=0;for(;s<e.childNodes.length;s++)ae(e.childNodes[s],t);if(e.shadowRoot)for(s=0;s<e.shadowRoot.childNodes.length;s++)ae(e.shadowRoot.childNodes[s],t)}else if(e.nodeType===8){let s=e.nodeValue.split(".");s[0]===It&&(t.set(s[1]+"."+s[2],e),e.nodeValue="",e["s-en"]=s[3])}},Ot=e=>dt.map(t=>t(e)).find(t=>!!t),_s=e=>dt.push(e),ws=e=>x(e).$modeName$,jt=(e,t)=>e!=null&&!ue(e)?n.propBoolean&&t&4?e==="false"?!1:e===""||!!e:n.propNumber&&t&2?parseFloat(e):n.propString&&t&1?String(e):e:e,zt=e=>n.lazyLoad?x(e).$hostElement$:e,zs=(e,t,s)=>{let o=zt(e);return{emit:r=>(n.isDev&&!o.isConnected&&z(`The "${t}" event was emitted, but the dispatcher node is no longer connected to the dom.`),pe(o,t,{bubbles:!!(s&4),composed:!!(s&2),cancelable:!!(s&1),detail:r}))}},pe=(e,t,s)=>{let o=h.ce(t,s);return e.dispatchEvent(o),o},Ie=new WeakMap,Pt=(e,t,s)=>{let o=X.get(e);vs&&s?(o=o||new CSSStyleSheet,typeof o=="string"?o=t:o.replaceSync(t)):o=t,X.set(e,o)},le=(e,t,s)=>{var o;let r=We(t,s),i=X.get(r);if(!n.attachStyles)return r;if(e=e.nodeType===11?e:v,i)if(typeof i=="string"){e=e.head||e;let l=Ie.get(e),c;if(l||Ie.set(e,l=new Set),!l.has(r)){if(n.hydrateClientSide&&e.host&&(c=e.querySelector(`[${xe}="${r}"]`)))c.innerHTML=i;else{c=v.createElement("style"),c.innerHTML=i;let a=(o=h.$nonce$)!=null?o:yt(v);a!=null&&c.setAttribute("nonce",a),(n.hydrateServerSide||n.hotModuleReplacement)&&c.setAttribute(xe,r),e.insertBefore(c,e.querySelector("link"))}t.$flags$&4&&(c.innerHTML+=At),l&&l.add(r)}}else n.constructableCSS&&!e.adoptedStyleSheets.includes(i)&&(e.adoptedStyleSheets=[...e.adoptedStyleSheets,i]);return r},Ft=e=>{let t=e.$cmpMeta$,s=e.$hostElement$,o=t.$flags$,r=I("attachStyles",t.$tagName$),i=le(n.shadowDom&&_&&s.shadowRoot?s.shadowRoot:s.getRootNode(),t,e.$modeName$);(n.shadowDom||n.scoped)&&n.cssAnnotations&&o&10&&(s["s-sc"]=i,s.classList.add(i+"-h"),n.scoped&&o&2&&s.classList.add(i+"-s")),r()},We=(e,t)=>"sc-"+(n.mode&&t&&e.$flags$&32?e.$tagName$+"-"+t:e.$tagName$);var Ne=(e,t,s,o,r,i)=>{if(s!==o){let l=je(e,t),c=t.toLowerCase();if(n.vdomClass&&t==="class"){let a=e.classList,$=ke(s),d=ke(o);a.remove(...$.filter(f=>f&&!d.includes(f))),a.add(...d.filter(f=>f&&!$.includes(f)))}else if(n.vdomStyle&&t==="style"){if(n.updatable)for(let a in s)(!o||o[a]==null)&&(!n.hydrateServerSide&&a.includes("-")?e.style.removeProperty(a):e.style[a]="");for(let a in o)(!s||o[a]!==s[a])&&(!n.hydrateServerSide&&a.includes("-")?e.style.setProperty(a,o[a]):e.style[a]=o[a])}else if(!(n.vdomKey&&t==="key")){if(n.vdomRef&&t==="ref")o&&o(e);else if(n.vdomListener&&(n.lazyLoad?!l:!e.__lookupSetter__(t))&&t[0]==="o"&&t[1]==="n"){if(t[2]==="-"?t=t.slice(3):je(O,c)?t=c.slice(2):t=c[2]+t.slice(3),s||o){let a=t.endsWith(qe);t=t.replace(Mt,""),s&&h.rel(e,t,s,a),o&&h.ael(e,t,o,a)}}else if(n.vdomPropOrAttr){let a=ue(o);if((l||a&&o!==null)&&!r)try{if(e.tagName.includes("-"))e[t]=o;else{let d=o??"";t==="list"?l=!1:(s==null||e[t]!=d)&&(e[t]=d)}}catch{}let $=!1;n.vdomXlink&&c!==(c=c.replace(/^xlink\:?/,""))&&(t=c,$=!0),o==null||o===!1?(o!==!1||e.getAttribute(t)==="")&&(n.vdomXlink&&$?e.removeAttributeNS(Te,t):e.removeAttribute(t)):(!l||i&4||r)&&!a&&(o=o===!0?"":o,n.vdomXlink&&$?e.setAttributeNS(Te,t,o):e.setAttribute(t,o))}}}},Ht=/\s/,ke=e=>e?e.split(Ht):[],qe="Capture",Mt=new RegExp(qe+"$"),Qe=(e,t,s)=>{let o=t.$elm$.nodeType===11&&t.$elm$.host?t.$elm$.host:t.$elm$,r=e&&e.$attrs$||be,i=t.$attrs$||be;if(n.updatable)for(let l of Ae(Object.keys(r)))l in i||Ne(o,l,r[l],void 0,s,t.$flags$);for(let l of Ae(Object.keys(i)))Ne(o,l,r[l],i[l],s,t.$flags$)};function Ae(e){return e.includes("ref")?[...e.filter(t=>t!=="ref"),"ref"]:e}var w,ce,C,he=!1,W=!1,G=!1,b=!1,q=(e,t,s,o)=>{var r;let i=t.$children$[s],l=0,c,a,$;if(n.slotRelocation&&!he&&(G=!0,i.$tag$==="slot"&&(w&&o.classList.add(w+"-s"),i.$flags$|=i.$children$?2:1)),n.isDev&&i.$elm$&&Q(`The JSX ${i.$text$!==null?`"${i.$text$}" text`:`"${i.$tag$}" element`} node should not be shared within the same renderer. The renderer caches element lookups in order to improve performance. However, a side effect from this is that the exact same JSX node should not be reused. For more information please see https://stenciljs.com/docs/templating-jsx#avoid-shared-jsx-nodes`),n.vdomText&&i.$text$!==null)c=i.$elm$=v.createTextNode(i.$text$);else if(n.slotRelocation&&i.$flags$&1)c=i.$elm$=n.isDebug||n.hydrateServerSide?qt(i):v.createTextNode("");else{if(n.svg&&!b&&(b=i.$tag$==="svg"),c=i.$elm$=n.svg?v.createElementNS(b?mt:vt,n.slotRelocation&&i.$flags$&2?"slot-fb":i.$tag$):v.createElement(n.slotRelocation&&i.$flags$&2?"slot-fb":i.$tag$),n.svg&&b&&i.$tag$==="foreignObject"&&(b=!1),n.vdomAttribute&&Qe(null,i,b),(n.shadowDom||n.scoped)&&gt(w)&&c["s-si"]!==w&&c.classList.add(c["s-si"]=w),n.scoped&&ve(c,o),i.$children$)for(l=0;l<i.$children$.length;++l)a=q(e,i,l,c),a&&c.appendChild(a);n.svg&&(i.$tag$==="svg"?b=!1:c.tagName==="foreignObject"&&(b=!0))}return c["s-hn"]=C,n.slotRelocation&&i.$flags$&3&&(c["s-sr"]=!0,c["s-cr"]=ce,c["s-sn"]=i.$name$||"",c["s-rf"]=(r=i.$attrs$)==null?void 0:r.ref,$=e&&e.$children$&&e.$children$[s],$&&$.$tag$===i.$tag$&&e.$elm$&&(n.experimentalSlotFixes?Xe(e.$elm$):j(e.$elm$,!1))),c},Xe=e=>{h.$flags$|=1;let t=e.closest(C.toLowerCase());if(t!=null){let s=Array.from(t.childNodes).find(r=>r["s-cr"]),o=Array.from(e.childNodes);for(let r of s?o.reverse():o)r["s-sh"]!=null&&(L(t,r,s??null),r["s-sh"]=void 0,G=!0)}h.$flags$&=-2},j=(e,t)=>{h.$flags$|=1;let s=Array.from(e.childNodes);if(e["s-sr"]&&n.experimentalSlotFixes){let o=e;for(;o=o.nextSibling;)o&&o["s-sn"]===e["s-sn"]&&o["s-sh"]===C&&s.push(o)}for(let o=s.length-1;o>=0;o--){let r=s[o];r["s-hn"]!==C&&r["s-ol"]&&(L(Ge(r),r,me(r)),r["s-ol"].remove(),r["s-ol"]=void 0,r["s-sh"]=void 0,G=!0),t&&j(r,t)}h.$flags$&=-2},Ke=(e,t,s,o,r,i)=>{let l=n.slotRelocation&&e["s-cr"]&&e["s-cr"].parentNode||e,c;for(n.shadowDom&&l.shadowRoot&&l.tagName===C&&(l=l.shadowRoot);r<=i;++r)o[r]&&(c=q(null,s,r,e),c&&(o[r].$elm$=c,L(l,c,n.slotRelocation?me(t):t)))},Ye=(e,t,s)=>{for(let o=t;o<=s;++o){let r=e[o];if(r){let i=r.$elm$;Ze(r),i&&(n.slotRelocation&&(W=!0,i["s-ol"]?i["s-ol"].remove():j(i,!0)),i.remove())}}},Wt=(e,t,s,o,r=!1)=>{let i=0,l=0,c=0,a=0,$=t.length-1,d=t[0],f=t[$],p=o.length-1,u=o[0],m=o[p],y,g;for(;i<=$&&l<=p;)if(d==null)d=t[++i];else if(f==null)f=t[--$];else if(u==null)u=o[++l];else if(m==null)m=o[--p];else if(H(d,u,r))E(d,u,r),d=t[++i],u=o[++l];else if(H(f,m,r))E(f,m,r),f=t[--$],m=o[--p];else if(H(d,m,r))n.slotRelocation&&(d.$tag$==="slot"||m.$tag$==="slot")&&j(d.$elm$.parentNode,!1),E(d,m,r),L(e,d.$elm$,f.$elm$.nextSibling),d=t[++i],m=o[--p];else if(H(f,u,r))n.slotRelocation&&(d.$tag$==="slot"||m.$tag$==="slot")&&j(f.$elm$.parentNode,!1),E(f,u,r),L(e,f.$elm$,d.$elm$),f=t[--$],u=o[++l];else{if(c=-1,n.vdomKey){for(a=i;a<=$;++a)if(t[a]&&t[a].$key$!==null&&t[a].$key$===u.$key$){c=a;break}}n.vdomKey&&c>=0?(g=t[c],g.$tag$!==u.$tag$?y=q(t&&t[l],s,c,e):(E(g,u,r),t[c]=void 0,y=g.$elm$),u=o[++l]):(y=q(t&&t[l],s,l,e),u=o[++l]),y&&(n.slotRelocation?L(Ge(d.$elm$),y,me(d.$elm$)):L(d.$elm$.parentNode,y,d.$elm$))}i>$?Ke(e,o[p+1]==null?null:o[p+1].$elm$,s,o,l,p):n.updatable&&l>p&&Ye(t,i,$)},H=(e,t,s=!1)=>e.$tag$===t.$tag$?n.slotRelocation&&e.$tag$==="slot"?e.$name$===t.$name$:n.vdomKey&&!s?e.$key$===t.$key$:!0:!1,me=e=>e&&e["s-ol"]||e,Ge=e=>(e["s-ol"]?e["s-ol"]:e).parentNode,E=(e,t,s=!1)=>{let o=t.$elm$=e.$elm$,r=e.$children$,i=t.$children$,l=t.$tag$,c=t.$text$,a;!n.vdomText||c===null?(n.svg&&(b=l==="svg"?!0:l==="foreignObject"?!1:b),(n.vdomAttribute||n.reflect)&&(n.slot&&l==="slot"&&!he?n.experimentalSlotFixes&&e.$name$!==t.$name$&&(t.$elm$["s-sn"]=t.$name$||"",Xe(t.$elm$.parentElement)):Qe(e,t,b)),n.updatable&&r!==null&&i!==null?Wt(o,r,t,i,s):i!==null?(n.updatable&&n.vdomText&&e.$text$!==null&&(o.textContent=""),Ke(o,null,t,i,0,i.length-1)):n.updatable&&r!==null&&Ye(r,0,r.length-1),n.svg&&b&&l==="svg"&&(b=!1)):n.vdomText&&n.slotRelocation&&(a=o["s-cr"])?a.parentNode.textContent=c:n.vdomText&&e.$text$!==c&&(o.data=c)},J=e=>{let t=e.childNodes;for(let s of t)if(s.nodeType===1){if(s["s-sr"]){let o=s["s-sn"];s.hidden=!1;for(let r of t)if(r!==s){if(r["s-hn"]!==s["s-hn"]||o!==""){if(r.nodeType===1&&(o===r.getAttribute("slot")||o===r["s-sn"])||r.nodeType===3&&o===r["s-sn"]){s.hidden=!0;break}}else if(r.nodeType===1||r.nodeType===3&&r.textContent.trim()!==""){s.hidden=!0;break}}}J(s)}},T=[],Je=e=>{let t,s,o;for(let r of e.childNodes){if(r["s-sr"]&&(t=r["s-cr"])&&t.parentNode){s=t.parentNode.childNodes;let i=r["s-sn"];for(o=s.length-1;o>=0;o--)if(t=s[o],!t["s-cn"]&&!t["s-nr"]&&t["s-hn"]!==r["s-hn"]&&(!n.experimentalSlotFixes||!t["s-sh"]||t["s-sh"]!==r["s-hn"]))if(_e(t,i)){let l=T.find(c=>c.$nodeToRelocate$===t);W=!0,t["s-sn"]=t["s-sn"]||i,l?(l.$nodeToRelocate$["s-sh"]=r["s-hn"],l.$slotRefNode$=r):(t["s-sh"]=r["s-hn"],T.push({$slotRefNode$:r,$nodeToRelocate$:t})),t["s-sr"]&&T.map(c=>{_e(c.$nodeToRelocate$,t["s-sn"])&&(l=T.find(a=>a.$nodeToRelocate$===t),l&&!c.$slotRefNode$&&(c.$slotRefNode$=l.$slotRefNode$))})}else T.some(l=>l.$nodeToRelocate$===t)||T.push({$nodeToRelocate$:t})}r.nodeType===1&&Je(r)}},_e=(e,t)=>e.nodeType===1?e.getAttribute("slot")===null&&t===""||e.getAttribute("slot")===t:e["s-sn"]===t?!0:t==="",Ze=e=>{n.vdomRef&&(e.$attrs$&&e.$attrs$.ref&&e.$attrs$.ref(null),e.$children$&&e.$children$.map(Ze))},L=(e,t,s)=>{let o=e==null?void 0:e.insertBefore(t,s);return n.scoped&&ve(t,e),o},Ve=e=>{let t=[];return e&&t.push(...e["s-scs"]||[],e["s-si"],e["s-sc"],...Ve(e.parentElement)),t},ve=(e,t,s=!1)=>{var o;if(e&&t&&e.nodeType===1){let r=new Set(Ve(t).filter(Boolean));if(r.size&&((o=e.classList)==null||o.add(...e["s-scs"]=[...r]),e["s-ol"]||s))for(let i of Array.from(e.childNodes))ve(i,e,!0)}},we=(e,t,s=!1)=>{var o,r,i,l,c;let a=e.$hostElement$,$=e.$cmpMeta$,d=e.$vnode$||B(null,null),f=re(t)?t:Me(null,null,t);if(C=a.tagName,n.isDev&&Array.isArray(t)&&t.some(re))throw new Error(`The <Host> must be the single root component.
Looks like the render() function of "${C.toLowerCase()}" is returning an array that contains the <Host>.

The render() function should look like this instead:

render() {
  // Do not return an array
  return (
    <Host>{content}</Host>
  );
}
  `);if(n.reflect&&$.$attrsToReflect$&&(f.$attrs$=f.$attrs$||{},$.$attrsToReflect$.map(([p,u])=>f.$attrs$[u]=a[p])),s&&f.$attrs$)for(let p of Object.keys(f.$attrs$))a.hasAttribute(p)&&!["key","ref","style","class"].includes(p)&&(f.$attrs$[p]=a[p]);if(f.$tag$=null,f.$flags$|=4,e.$vnode$=f,f.$elm$=d.$elm$=n.shadowDom&&a.shadowRoot||a,(n.scoped||n.shadowDom)&&(w=a["s-sc"]),he=_&&($.$flags$&1)!==0,n.slotRelocation&&(ce=a["s-cr"],W=!1),E(d,f,s),n.slotRelocation){if(h.$flags$|=1,G){Je(f.$elm$);for(let p of T){let u=p.$nodeToRelocate$;if(!u["s-ol"]){let m=n.isDebug||n.hydrateServerSide?Qt(u):v.createTextNode("");m["s-nr"]=u,L(u.parentNode,u["s-ol"]=m,u)}}for(let p of T){let u=p.$nodeToRelocate$,m=p.$slotRefNode$;if(m){let y=m.parentNode,g=m.nextSibling;if(!n.experimentalSlotFixes||g&&g.nodeType===1){let k=(o=u["s-ol"])==null?void 0:o.previousSibling;for(;k;){let S=(r=k["s-nr"])!=null?r:null;if(S&&S["s-sn"]===u["s-sn"]&&y===S.parentNode){for(S=S.nextSibling;S===u||S!=null&&S["s-sr"];)S=S==null?void 0:S.nextSibling;if(!S||!S["s-nr"]){g=S;break}}k=k.previousSibling}}(!g&&y!==u.parentNode||u.nextSibling!==g)&&u!==g&&(!n.experimentalSlotFixes&&!u["s-hn"]&&u["s-ol"]&&(u["s-hn"]=u["s-ol"].parentNode.nodeName),L(y,u,g),u.nodeType===1&&(u.hidden=(i=u["s-ih"])!=null?i:!1)),u&&typeof m["s-rf"]=="function"&&m["s-rf"](u)}else u.nodeType===1&&(s&&(u["s-ih"]=(l=u.hidden)!=null?l:!1),u.hidden=!0)}}W&&J(f.$elm$),h.$flags$&=-2,T.length=0}if(n.experimentalScopedSlotChanges&&$.$flags$&2)for(let p of f.$elm$.childNodes)p["s-hn"]!==C&&!p["s-sh"]&&(s&&p["s-ih"]==null&&(p["s-ih"]=(c=p.hidden)!=null?c:!1),p.hidden=!0);ce=void 0},qt=e=>v.createComment(`<slot${e.$name$?' name="'+e.$name$+'"':""}> (host=${C.toLowerCase()})`),Qt=e=>v.createComment("org-location for "+(e.localName?`<${e.localName}> (host=${e["s-hn"]})`:`[${e.textContent}]`)),et=(e,t)=>{n.asyncLoading&&t&&!e.$onRenderResolve$&&t["s-p"]&&t["s-p"].push(new Promise(s=>e.$onRenderResolve$=s))},Z=(e,t)=>{if(n.taskQueue&&n.updatable&&(e.$flags$|=16),n.asyncLoading&&e.$flags$&4){e.$flags$|=512;return}et(e,e.$ancestorComponent$);let s=()=>Xt(e,t);return n.taskQueue?gs(s):s()},Xt=(e,t)=>{let s=e.$hostElement$,o=I("scheduleUpdate",e.$cmpMeta$.$tagName$),r=n.lazyLoad?e.$lazyInstance$:s;if(!r)throw new Error(`Can't render component <${s.tagName.toLowerCase()} /> with invalid Stencil runtime! Make sure this imported component is compiled with a \`externalRuntime: true\` flag. For more information, please refer to https://stenciljs.com/docs/custom-elements#externalruntime`);let i;return t?(n.lazyLoad&&n.hostListener&&(e.$flags$|=256,e.$queuedListeners$&&(e.$queuedListeners$.map(([l,c])=>D(r,l,c)),e.$queuedListeners$=void 0)),U(s,"componentWillLoad"),n.cmpWillLoad&&(i=D(r,"componentWillLoad"))):(U(s,"componentWillUpdate"),n.cmpWillUpdate&&(i=D(r,"componentWillUpdate"))),U(s,"componentWillRender"),n.cmpWillRender&&(i=Ee(i,()=>D(r,"componentWillRender"))),o(),Ee(i,()=>Yt(e,r,t))},Ee=(e,t)=>Kt(e)?e.then(t):t(),Kt=e=>e instanceof Promise||e&&e.then&&typeof e.then=="function",Yt=(e,t,s)=>P(void 0,null,function*(){var o;let r=e.$hostElement$,i=I("update",e.$cmpMeta$.$tagName$),l=r["s-rc"];n.style&&s&&Ft(e);let c=I("render",e.$cmpMeta$.$tagName$);if(n.isDev&&(e.$flags$|=1024),n.hydrateServerSide?yield Be(e,t,r,s):Be(e,t,r,s),n.isDev&&(e.$renderCount$=e.$renderCount$===void 0?1:e.$renderCount$+1,e.$flags$&=-1025),n.hydrateServerSide)try{st(r),s&&(e.$cmpMeta$.$flags$&1?r["s-en"]="":e.$cmpMeta$.$flags$&2&&(r["s-en"]="c"))}catch(a){N(a,r)}if(n.asyncLoading&&l&&(l.map(a=>a()),r["s-rc"]=void 0),c(),i(),n.asyncLoading){let a=(o=r["s-p"])!=null?o:[],$=()=>Re(e);a.length===0?$():(Promise.all(a).then($),e.$flags$|=4,a.length=0)}else Re(e)}),Ue=null,Be=(e,t,s,o)=>{let r=!!n.allRenderFn,i=!!n.lazyLoad,l=!!n.taskQueue,c=!!n.updatable;try{if(Ue=t,t=(r||t.render)&&t.render(),c&&l&&(e.$flags$&=-17),(c||i)&&(e.$flags$|=2),n.hasRenderFn||n.reflect)if(n.vdomRender||n.reflect){if(n.hydrateServerSide)return Promise.resolve(t).then(a=>we(e,a,o));we(e,t,o)}else{let a=s.shadowRoot;e.$cmpMeta$.$flags$&1?a.textContent=t:s.textContent=t}}catch(a){N(a,e.$hostElement$)}return Ue=null,null};var Re=e=>{let t=e.$cmpMeta$.$tagName$,s=e.$hostElement$,o=I("postUpdate",t),r=n.lazyLoad?e.$lazyInstance$:s,i=e.$ancestorComponent$;n.cmpDidRender&&(n.isDev&&(e.$flags$|=1024),D(r,"componentDidRender"),n.isDev&&(e.$flags$&=-1025)),U(s,"componentDidRender"),e.$flags$&64?(n.cmpDidUpdate&&(n.isDev&&(e.$flags$|=1024),D(r,"componentDidUpdate"),n.isDev&&(e.$flags$&=-1025)),U(s,"componentDidUpdate"),o()):(e.$flags$|=64,n.asyncLoading&&n.cssAnnotations&&tt(s),n.cmpDidLoad&&(n.isDev&&(e.$flags$|=2048),D(r,"componentDidLoad"),n.isDev&&(e.$flags$&=-2049)),U(s,"componentDidLoad"),o(),n.asyncLoading&&(e.$onReadyResolve$(s),i||Gt(t))),n.method&&n.lazyLoad&&e.$onInstanceResolve$(s),n.asyncLoading&&(e.$onRenderResolve$&&(e.$onRenderResolve$(),e.$onRenderResolve$=void 0),e.$flags$&512&&V(()=>Z(e,!1)),e.$flags$&=-517)},Ws=e=>{if(n.updatable&&(Le.isBrowser||Le.isTesting)){let t=x(e),s=t.$hostElement$.isConnected;return s&&(t.$flags$&18)===2&&Z(t,!1),s}return!1},Gt=e=>{n.cssAnnotations&&tt(v.documentElement),n.asyncQueue&&(h.$flags$|=2),V(()=>pe(O,"appload",{detail:{namespace:F}})),n.profile&&performance.measure&&performance.measure(`[Stencil] ${F} initial load (by ${e})`,"st:app:start")},D=(e,t,s)=>{if(e&&e[t])try{return e[t](s)}catch(o){N(o)}},U=(e,t)=>{n.lifecycleDOMEvents&&pe(e,"stencil_"+t,{bubbles:!0,composed:!0,detail:{namespace:F}})},tt=e=>{var t,s;return n.hydratedClass?e.classList.add((t=n.hydratedSelectorName)!=null?t:"hydrated"):n.hydratedAttribute?e.setAttribute((s=n.hydratedSelectorName)!=null?s:"hydrated",""):void 0},st=e=>{let t=e.children;if(t!=null)for(let s=0,o=t.length;s<o;s++){let r=t[s];typeof r.connectedCallback=="function"&&r.connectedCallback(),st(r)}},Jt=(e,t)=>x(e).$instanceValues$.get(t),Zt=(e,t,s,o)=>{let r=x(e);if(n.lazyLoad&&!r)throw new Error(`Couldn't find host element for "${o.$tagName$}" as it is unknown to this Stencil runtime. This usually happens when integrating a 3rd party Stencil component with another Stencil component or application. Please reach out to the maintainers of the 3rd party Stencil component or report this on the Stencil Discord server (https://chat.stenciljs.com) or comment on this similar [GitHub issue](https://github.com/ionic-team/stencil/issues/5457).`);let i=n.lazyLoad?r.$hostElement$:e,l=r.$instanceValues$.get(t),c=r.$flags$,a=n.lazyLoad?r.$lazyInstance$:i;s=jt(s,o.$members$[t][0]);let $=Number.isNaN(l)&&Number.isNaN(s),d=s!==l&&!$;if((!n.lazyLoad||!(c&8)||l===void 0)&&d&&(r.$instanceValues$.set(t,s),n.isDev&&(r.$flags$&1024?z(`The state/prop "${t}" changed during rendering. This can potentially lead to infinite-loops and other bugs.`,`
Element`,i,`
New value`,s,`
Old value`,l):r.$flags$&2048&&z(`The state/prop "${t}" changed during "componentDidLoad()", this triggers extra re-renders, try to setup on "componentWillLoad()"`,`
Element`,i,`
New value`,s,`
Old value`,l)),!n.lazyLoad||a)){if(n.watchCallback&&o.$watchers$&&c&128){let f=o.$watchers$[t];f&&f.map(p=>{try{a[p](s,l,t)}catch(u){N(u,i)}})}if(n.updatable&&(c&18)===2){if(n.cmpShouldUpdate&&a.componentShouldUpdate&&a.componentShouldUpdate(s,l,t)===!1)return;Z(r,!1)}}},nt=(e,t,s)=>{var o;let r=e.prototype;if(n.formAssociated&&t.$flags$&64&&s&1&&_t.forEach(i=>Object.defineProperty(r,i,{value(...l){let c=x(this),a=n.lazyLoad?c.$hostElement$:this,$=n.lazyLoad?c.$lazyInstance$:a;if(!$)c.$onReadyPromise$.then(d=>{let f=d[i];typeof f=="function"&&f.call(d,...l)});else{let d=$[i];typeof d=="function"&&d.call($,...l)}}})),n.member&&t.$members$){n.watchCallback&&e.watchers&&(t.$watchers$=e.watchers);let i=Object.entries(t.$members$);if(i.map(([l,[c]])=>{(n.prop||n.state)&&(c&31||(!n.lazyLoad||s&2)&&c&32)?Object.defineProperty(r,l,{get(){return Jt(this,l)},set(a){if(n.isDev){let $=x(this);!(s&1)&&($&&$.$flags$&8)===0&&c&31&&!(c&1024)&&z(`@Prop() "${l}" on <${t.$tagName$}> is immutable but was modified from within the component.
More information: https://stenciljs.com/docs/properties#prop-mutability`)}Zt(this,l,a,t)},configurable:!0,enumerable:!0}):n.lazyLoad&&n.method&&s&1&&c&64&&Object.defineProperty(r,l,{value(...a){var $;let d=x(this);return($=d==null?void 0:d.$onInstancePromise$)==null?void 0:$.then(()=>{var f;return(f=d.$lazyInstance$)==null?void 0:f[l](...a)})}})}),n.observeAttribute&&(!n.lazyLoad||s&1)){let l=new Map;r.attributeChangedCallback=function(c,a,$){h.jmp(()=>{var d;let f=l.get(c);if(this.hasOwnProperty(f))$=this[f],delete this[f];else{if(r.hasOwnProperty(f)&&typeof this[f]=="number"&&this[f]==$)return;if(f==null){let p=x(this),u=p==null?void 0:p.$flags$;if(u&&!(u&8)&&u&128&&$!==a){let m=n.lazyLoad?p.$hostElement$:this,y=n.lazyLoad?p.$lazyInstance$:m,g=(d=t.$watchers$)==null?void 0:d[c];g==null||g.forEach(k=>{y[k]!=null&&y[k].call(y,$,a,c)})}return}}this[f]=$===null&&typeof this[f]=="boolean"?!1:$})},e.observedAttributes=Array.from(new Set([...Object.keys((o=t.$watchers$)!=null?o:{}),...i.filter(([c,a])=>a[0]&15).map(([c,a])=>{var $;let d=a[1]||c;return l.set(d,c),n.reflect&&a[0]&512&&(($=t.$attrsToReflect$)==null||$.push([c,d])),d})]))}}return e},Oe=(e,t,s,o)=>P(void 0,null,function*(){let r;if(!(t.$flags$&32)){t.$flags$|=32;let c=s.$lazyBundleId$;if((n.lazyLoad||n.hydrateClientSide)&&c){let a=ps(s,t,o);if(a&&"then"in a){let d=Tt(`st:load:${s.$tagName$}:${t.$modeName$}`,`[Stencil] Load module for <${s.$tagName$}>`);r=yield a,d()}else r=a;if(!r)throw new Error(`Constructor for "${s.$tagName$}#${t.$modeName$}" was not found`);n.member&&!r.isProxied&&(n.watchCallback&&(s.$watchers$=r.watchers),nt(r,s,2),r.isProxied=!0);let $=I("createInstance",s.$tagName$);n.member&&(t.$flags$|=8);try{new r(t)}catch(d){N(d)}n.member&&(t.$flags$&=-9),n.watchCallback&&(t.$flags$|=128),$(),$e(t.$lazyInstance$)}else{r=e.constructor;let a=e.localName;customElements.whenDefined(a).then(()=>t.$flags$|=128)}if(n.style&&r&&r.style){let a=r.style;n.mode&&typeof a!="string"&&(t.$modeName$=Ot(e),t.$modeName$&&(a=a[t.$modeName$]),n.hydrateServerSide&&t.$modeName$&&e.setAttribute("s-mode",t.$modeName$));let $=We(s,t.$modeName$);if(!X.has($)){let d=I("registerStyles",s.$tagName$);!n.hydrateServerSide&&n.shadowDom&&n.shadowDomShim&&s.$flags$&8&&(a=yield import("./chunk-LT4YTCCD.js").then(f=>f.scopeCss(a,$,!1))),Pt($,a,!!(s.$flags$&1)),d()}}}let i=t.$ancestorComponent$,l=()=>Z(t,!0);n.asyncLoading&&i&&i["s-rc"]?i["s-rc"].push(l):l()}),$e=e=>{n.lazyLoad&&n.connectedCallback&&D(e,"connectedCallback")},Vt=e=>{if(!(h.$flags$&1)){let t=x(e),s=t.$cmpMeta$,o=I("connectedCallback",s.$tagName$);if(n.hostListenerTargetParent&&fe(e,t,s.$listeners$,!0),t.$flags$&1)fe(e,t,s.$listeners$,!1),t!=null&&t.$lazyInstance$?$e(t.$lazyInstance$):t!=null&&t.$onReadyPromise$&&t.$onReadyPromise$.then(()=>$e(t.$lazyInstance$));else{t.$flags$|=1;let r;if(n.hydrateClientSide&&(r=e.getAttribute(oe),r)){if(n.shadowDom&&_&&s.$flags$&1){let i=n.mode?le(e.shadowRoot,s,e.getAttribute("s-mode")):le(e.shadowRoot,s);e.classList.remove(i+"-h",i+"-s")}Rt(e,s.$tagName$,r,t)}if(n.slotRelocation&&!r&&(n.hydrateServerSide||(n.slot||n.shadowDom)&&s.$flags$&12)&&es(e),n.asyncLoading){let i=e;for(;i=i.parentNode||i.host;)if(n.hydrateClientSide&&i.nodeType===1&&i.hasAttribute("s-id")&&i["s-p"]||i["s-p"]){et(t,t.$ancestorComponent$=i);break}}n.prop&&!n.hydrateServerSide&&s.$members$&&Object.entries(s.$members$).map(([i,[l]])=>{if(l&31&&e.hasOwnProperty(i)){let c=e[i];delete e[i],e[i]=c}}),n.initializeNextTick?V(()=>Oe(e,t,s)):Oe(e,t,s)}o()}},es=e=>{let t=e["s-cr"]=v.createComment(n.isDebug?`content-ref (host=${e.localName})`:"");t["s-cn"]=!0,L(e,t,e.firstChild)},ee=e=>{n.lazyLoad&&n.disconnectedCallback&&D(e,"disconnectedCallback"),n.cmpDidUnload&&D(e,"componentDidUnload")},ts=e=>P(void 0,null,function*(){if(!(h.$flags$&1)){let t=x(e);n.hostListener&&t.$rmListeners$&&(t.$rmListeners$.map(s=>s()),t.$rmListeners$=void 0),n.lazyLoad?t!=null&&t.$lazyInstance$?ee(t.$lazyInstance$):t!=null&&t.$onReadyPromise$&&t.$onReadyPromise$.then(()=>ee(t.$lazyInstance$)):ee(e)}}),ss=(e,t)=>{ot(e),rt(e),rs(e),os(e),ls(e),is(e),as(e),it(e),at(e,t),ns(e)},ot=e=>{let t=e.cloneNode;e.cloneNode=function(s){let o=this,r=n.shadowDom?o.shadowRoot&&_:!1,i=t.call(o,r?s:!1);if(n.slot&&!r&&s){let l=0,c,a,$=["s-id","s-cr","s-lr","s-rc","s-sc","s-p","s-cn","s-sr","s-sn","s-hn","s-ol","s-nr","s-si","s-rf","s-scs"];for(;l<o.childNodes.length;l++)c=o.childNodes[l]["s-nr"],a=$.every(d=>!o.childNodes[l][d]),c&&(n.appendChildSlotFix&&i.__appendChild?i.__appendChild(c.cloneNode(!0)):i.appendChild(c.cloneNode(!0))),a&&i.appendChild(o.childNodes[l].cloneNode(!0))}return i}},rt=e=>{e.__appendChild=e.appendChild,e.appendChild=function(t){let s=t["s-sn"]=lt(t),o=R(this.childNodes,s,this.tagName);if(o){let r=ge(o,s),i=r[r.length-1],l=L(i.parentNode,t,i.nextSibling);return J(this),l}return this.__appendChild(t)}},ns=e=>{e.__removeChild=e.removeChild,e.removeChild=function(t){if(t&&typeof t["s-sn"]<"u"){let s=R(this.childNodes,t["s-sn"],this.tagName);if(s){let r=ge(s,t["s-sn"]).find(i=>i===t);if(r){r.remove(),J(this);return}}}return this.__removeChild(t)}},os=e=>{let t=e.prepend;e.prepend=function(...s){s.forEach(o=>{typeof o=="string"&&(o=this.ownerDocument.createTextNode(o));let r=o["s-sn"]=lt(o),i=R(this.childNodes,r,this.tagName);if(i){let l=document.createTextNode("");l["s-nr"]=o,i["s-cr"].parentNode.__appendChild(l),o["s-ol"]=l;let a=ge(i,r)[0];return L(a.parentNode,o,a.nextSibling)}return o.nodeType===1&&o.getAttribute("slot")&&(o.hidden=!0),t.call(this,o)})}},rs=e=>{e.append=function(...t){t.forEach(s=>{typeof s=="string"&&(s=this.ownerDocument.createTextNode(s)),this.appendChild(s)})}},is=e=>{let t=e.insertAdjacentHTML;e.insertAdjacentHTML=function(s,o){if(s!=="afterbegin"&&s!=="beforeend")return t.call(this,s,o);let r=this.ownerDocument.createElement("_"),i;if(r.innerHTML=o,s==="afterbegin")for(;i=r.firstChild;)this.prepend(i);else if(s==="beforeend")for(;i=r.firstChild;)this.append(i)}},as=e=>{e.insertAdjacentText=function(t,s){this.insertAdjacentHTML(t,s)}},ls=e=>{let t=e.insertAdjacentElement;e.insertAdjacentElement=function(s,o){return s!=="afterbegin"&&s!=="beforeend"?t.call(this,s,o):s==="afterbegin"?(this.prepend(o),o):(s==="beforeend"&&this.append(o),o)}},it=e=>{let t=Object.getOwnPropertyDescriptor(Node.prototype,"textContent");Object.defineProperty(e,"__textContent",t),n.experimentalScopedSlotChanges?Object.defineProperty(e,"textContent",{get(){return" "+de(this.childNodes).map(r=>{var i,l;let c=[],a=r.nextSibling;for(;a&&a["s-sn"]===r["s-sn"];)(a.nodeType===3||a.nodeType===1)&&c.push((l=(i=a.textContent)==null?void 0:i.trim())!=null?l:""),a=a.nextSibling;return c.filter($=>$!=="").join(" ")}).filter(r=>r!=="").join(" ")+" "},set(s){de(this.childNodes).forEach(r=>{let i=r.nextSibling;for(;i&&i["s-sn"]===r["s-sn"];){let l=i;i=i.nextSibling,l.remove()}if(r["s-sn"]===""){let l=this.ownerDocument.createTextNode(s);l["s-sn"]="",L(r.parentElement,l,r.nextSibling)}else r.remove()})}}):Object.defineProperty(e,"textContent",{get(){var s;let o=R(this.childNodes,"",this.tagName);return((s=o==null?void 0:o.nextSibling)==null?void 0:s.nodeType)===3?o.nextSibling.textContent:o?o.textContent:this.__textContent},set(s){var o;let r=R(this.childNodes,"",this.tagName);if(((o=r==null?void 0:r.nextSibling)==null?void 0:o.nodeType)===3)r.nextSibling.textContent=s;else if(r)r.textContent=s;else{this.__textContent=s;let i=this["s-cr"];i&&L(this,i,this.firstChild)}}})},at=(e,t)=>{class s extends Array{item(r){return this[r]}}if(t.$flags$&8){let o=e.__lookupGetter__("childNodes");Object.defineProperty(e,"children",{get(){return this.childNodes.map(r=>r.nodeType===1)}}),Object.defineProperty(e,"childElementCount",{get(){return e.children.length}}),Object.defineProperty(e,"childNodes",{get(){let r=o.call(this);if(!(h.$flags$&1)&&x(this).$flags$&2){let i=new s;for(let l=0;l<r.length;l++){let c=r[l]["s-nr"];c&&i.push(c)}return i}return s.from(r)}})}},de=e=>{let t=[];for(let s of Array.from(e))s["s-sr"]&&t.push(s),t.push(...de(s.childNodes));return t},lt=e=>e["s-sn"]||e.nodeType===1&&e.getAttribute("slot")||"",R=(e,t,s)=>{let o=0,r;for(;o<e.length;o++)if(r=e[o],r["s-sr"]&&r["s-sn"]===t&&r["s-hn"]===s||(r=R(r.childNodes,t,s),r))return r;return null},ge=(e,t)=>{let s=[e];for(;(e=e.nextSibling)&&e["s-sn"]===t;)s.push(e);return s};var Xs=(e,t)=>{let s={$flags$:t[0],$tagName$:t[1]};n.member&&(s.$members$=t[2]),n.hostListener&&(s.$listeners$=t[3]),n.watchCallback&&(s.$watchers$=e.$watchers$),n.reflect&&(s.$attrsToReflect$=[]),n.shadowDom&&!_&&s.$flags$&1&&(s.$flags$|=8),n.experimentalSlotFixes?n.scoped&&s.$flags$&2&&ss(e.prototype,s):(n.slotChildNodesFix&&at(e.prototype,s),n.cloneNodeFix&&ot(e.prototype),n.appendChildSlotFix&&rt(e.prototype),n.scopedSlotTextContentFix&&s.$flags$&2&&it(e.prototype));let o=e.prototype.connectedCallback,r=e.prototype.disconnectedCallback;return Object.assign(e.prototype,{__registerHost(){fs(this,s)},connectedCallback(){Vt(this),n.connectedCallback&&o&&o.call(this)},disconnectedCallback(){ts(this),n.disconnectedCallback&&r&&r.call(this)},__attachShadow(){_?n.shadowDelegatesFocus?this.attachShadow({mode:"open",delegatesFocus:!!(s.$flags$&16)}):this.attachShadow({mode:"open"}):this.shadowRoot=this}}),e.is=s.$tagName$,nt(e,s,3)};var fe=(e,t,s,o)=>{n.hostListener&&s&&(n.hostListenerTargetParent&&(o?s=s.filter(([r])=>r&32):s=s.filter(([r])=>!(r&32))),s.map(([r,i,l])=>{let c=n.hostListenerTarget?$s(e,r):e,a=cs(t,l),$=ds(r);h.ael(c,i,a,$),(t.$rmListeners$=t.$rmListeners$||[]).push(()=>h.rel(c,i,a,$))}))},cs=(e,t)=>s=>{var o;try{n.lazyLoad?e.$flags$&256?(o=e.$lazyInstance$)==null||o[t](s):(e.$queuedListeners$=e.$queuedListeners$||[]).push([t,s]):e.$hostElement$[t](s)}catch(r){N(r)}},$s=(e,t)=>n.hostListenerTargetDocument&&t&4?v:n.hostListenerTargetWindow&&t&8?O:n.hostListenerTargetBody&&t&16?v.body:n.hostListenerTargetParent&&t&32&&e.parentElement?e.parentElement:e,ds=e=>hs?{passive:(e&1)!==0,capture:(e&2)!==0}:(e&2)!==0;var ct=n.hotModuleReplacement?window.__STENCIL_HOSTREFS__||(window.__STENCIL_HOSTREFS__=new WeakMap):new WeakMap,x=e=>ct.get(e);var fs=(e,t)=>{let s={$flags$:0,$hostElement$:e,$cmpMeta$:t,$instanceValues$:new Map};return n.isDev&&(s.$renderCount$=0),n.method&&n.lazyLoad&&(s.$onInstancePromise$=new Promise(o=>s.$onInstanceResolve$=o)),n.asyncLoading&&(s.$onReadyPromise$=new Promise(o=>s.$onReadyResolve$=o),e["s-p"]=[],e["s-rc"]=[]),fe(e,s,t.$listeners$,!1),ct.set(e,s)},je=(e,t)=>t in e,us,N=(e,t)=>(us||console.error)(e,t),$t=n.isTesting?["STENCIL:"]:["%cstencil","color: white;background:#4c47ff;font-weight: bold; font-size:10px; padding:2px 6px; border-radius: 5px"],Q=(...e)=>console.error(...$t,...e),z=(...e)=>console.warn(...$t,...e);var ze=new Map;var ps=(e,t,s)=>{let o=e.$tagName$.replace(/-/g,"_"),r=e.$lazyBundleId$;if(n.isDev&&typeof r!="string"){Q(`Trying to lazily load component <${e.$tagName$}> with style mode "${t.$modeName$}", but it does not exist.`);return}else if(!r)return;let i=n.hotModuleReplacement?!1:ze.get(r);if(i)return i[o];return ut(`./${r}.entry.js${n.hotModuleReplacement&&s?"?s-hmr="+s:""}`).then(l=>(n.hotModuleReplacement||ze.set(r,l),l[o]),N)},X=new Map,dt=[],O=typeof window<"u"?window:{},v=O.document||{head:{}},Vs=O.HTMLElement||class{},h={$flags$:0,$resourcesUrl$:"",jmp:e=>e(),raf:e=>requestAnimationFrame(e),ael:(e,t,s,o)=>e.addEventListener(t,s,o),rel:(e,t,s,o)=>e.removeEventListener(t,s,o),ce:(e,t)=>new CustomEvent(e,t)},en=e=>{Object.assign(h,e)},_=n.shadowDomShim&&n.shadowDom?(v.head.attachShadow+"").indexOf("[native")>-1:!0,hs=(()=>{let e=!1;try{v.addEventListener("e",null,Object.defineProperty({},"passive",{get(){e=!0}}))}catch{}return e})(),ms=e=>Promise.resolve(e),vs=n.constructableCSS?(()=>{try{return new CSSStyleSheet,typeof new CSSStyleSheet().replaceSync=="function"}catch{}return!1})():!1,te=0,K=!1,M=[],A=[],se=[],ft=(e,t)=>s=>{e.push(s),K||(K=!0,t&&h.$flags$&4?V(Y):h.raf(Y))},Pe=e=>{for(let t=0;t<e.length;t++)try{e[t](performance.now())}catch(s){N(s)}e.length=0},Fe=(e,t)=>{let s=0,o=0;for(;s<e.length&&(o=performance.now())<t;)try{e[s++](o)}catch(r){N(r)}s===e.length?e.length=0:s!==0&&e.splice(0,s)},Y=()=>{if(n.asyncQueue&&te++,Pe(M),n.asyncQueue){let e=(h.$flags$&6)===2?performance.now()+14*Math.ceil(te*.1):1/0;Fe(A,e),Fe(se,e),A.length>0&&(se.push(...A),A.length=0),(K=M.length+A.length+se.length>0)?h.raf(Y):te=0}else Pe(A),(K=M.length>0)&&h.raf(Y)},V=e=>ms().then(e),tn=ft(M,!1),gs=ft(A,!0);export{Le as a,Ds as b,Me as c,wt as d,_s as e,ws as f,zs as g,Ws as h,Xs as i,Vs as j,en as k,tn as l,gs as m};