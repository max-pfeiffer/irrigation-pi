import{a as ue,b as w}from"./chunk-VISD66XU.js";import"./chunk-FNLJE7QV.js";import{a as b,b as ae,i as de}from"./chunk-KYZE6YTB.js";import{A as h,Aa as oe,B as O,C as Q,D as N,E as z,Ea as le,F as H,Fa as se,G as u,H as x,Ha as ce,I as S,J as I,K as $,Ka as L,L as q,M as Y,N as _,P as g,T as C,V as G,e as f,fa as J,ha as y,j as v,l as D,m as T,ma as K,na as U,oa as W,p as R,pa as X,q as l,qa as Z,r as a,t as m,ta as ee,u as P,ua as te,v as B,va as ie,w as s,wa as ne,x as c,xa as re,y as p,z as E}from"./chunk-XX3QOINY.js";import"./chunk-FVSUARKE.js";import"./chunk-NA2OGXLT.js";import"./chunk-GHOA5HSF.js";import"./chunk-SZCERZCG.js";import"./chunk-G3CV3VGG.js";import"./chunk-GFTFUPMB.js";import"./chunk-C4ZWKFGK.js";import"./chunk-F6OOB4LP.js";import"./chunk-4U6PRYVA.js";import"./chunk-6O5TN2LV.js";import"./chunk-JWIEPCRG.js";import"./chunk-QPVVTFFW.js";import"./chunk-J6ICYO4L.js";import"./chunk-LF5XB4YN.js";import{a as j,b as A,d as M,e as i,f as V}from"./chunk-PG5KTQWO.js";var Se=o=>["/schedules/edit/",o],me=(()=>{let n=class n{constructor(r,e,t,d,F){i(this,"scheduleService");i(this,"cdr");i(this,"alertController");i(this,"navController");i(this,"route");i(this,"schedule");i(this,"refreshList",new R);this.scheduleService=r,this.cdr=e,this.alertController=t,this.navController=d,this.route=F,b({trash:de})}toggleActive(){let t=this.schedule,{id:r}=t,e=M(t,["id"]);e=A(j({},e),{active:!this.schedule.active}),this.scheduleService.updateSchedule(r,e).pipe(f(()=>{this.refreshList.emit()})).subscribe()}deleteSchedule(){return V(this,null,function*(){yield(yield this.alertController.create({header:"Are you sure?",message:"Do you really want to delete this schedule?",buttons:[{text:"Yes",role:"destructive",handler:()=>{this.scheduleService.deleteSchedule(this.schedule.id).pipe(f(()=>{this.refreshList.emit()})).subscribe()}},{text:"No",role:"cancel"}]})).present()})}};i(n,"\u0275fac",function(e){return new(e||n)(a(w),a(_),a(ce),a(y),a(C))}),i(n,"\u0275cmp",v({type:n,selectors:[["app-schedule-tile"]],inputs:{schedule:"schedule"},outputs:{refreshList:"refreshList"},standalone:!0,features:[I],decls:18,vars:12,consts:[[3,"routerLink"],["slot","end","color","primary",3,"disabled"],["side","start"],[3,"click","color"],["side","end"],["color","danger",3,"click"],["slot","icon-only","name","trash"]],template:function(e,t){e&1&&(s(0,"ion-item-sliding")(1,"ion-item",0)(2,"ion-label")(3,"h2"),u(4),q(5,"displayString"),c(),s(6,"p"),u(7),p(8,"br"),u(9),c()(),s(10,"ion-chip",1),u(11),c()(),s(12,"ion-item-options",2)(13,"ion-item-option",3),h("click",function(){return t.toggleActive()}),u(14),c()(),s(15,"ion-item-options",4)(16,"ion-item-option",5),h("click",function(){return t.deleteSchedule()}),p(17,"ion-icon",6),c()()()),e&2&&(l(),m("routerLink",$(10,Se,t.schedule.id)),l(3),x(Y(5,8,t.schedule.repeat)),l(3),S(" At ",t.schedule.start_time," o'clock"),l(2),S(" For ",t.schedule.duration," minutes "),l(),m("disabled",!t.schedule.active),l(),x(t.schedule.active?"Active":"Inactive"),l(2),Q("color",t.schedule.active?"danger":"success"),l(),S(" ",t.schedule.active?"Deactivate":"Activate"," "))},dependencies:[g,J,G,ue,ie,ne,W,te,ee,L],changeDetection:0}));let o=n;return o})();var Ie=["scheduleList"],_e=(o,n)=>n.id;function ge(o,n){if(o&1){let k=E();s(0,"app-schedule-tile",8),h("refreshList",function(){D(k);let e=O();return T(e.refreshList())}),c()}if(o&2){let k=n.$implicit;m("schedule",k)}}var He=(()=>{let n=class n{constructor(r,e,t,d){i(this,"schedulerService");i(this,"cdr");i(this,"navController");i(this,"route");i(this,"scheduleList");i(this,"schedules",[]);this.schedulerService=r,this.cdr=e,this.navController=t,this.route=d,b({addOutline:ae})}ionViewDidEnter(){this.refreshList()}refreshList(){this.schedulerService.getSchedules().pipe(f(()=>this.scheduleList.closeSlidingItems().catch(()=>{}))).subscribe({next:r=>{this.schedules=r,this.cdr.detectChanges()}})}addSchedule(){this.navController.navigateForward(["edit"],{relativeTo:this.route})}};i(n,"\u0275fac",function(e){return new(e||n)(a(w),a(_),a(y),a(C))}),i(n,"\u0275cmp",v({type:n,selectors:[["app-schedule-list"]],viewQuery:function(e,t){if(e&1&&N(Ie,5),e&2){let d;z(d=H())&&(t.scheduleList=d.first)}},standalone:!0,features:[I],decls:14,vars:2,consts:[["scheduleList",""],[3,"translucent"],["slot","start"],["slot","end"],[3,"click"],["slot","icon-only","name","add-outline"],[3,"fullscreen"],[3,"schedule"],[3,"refreshList","schedule"]],template:function(e,t){if(e&1){let d=E();s(0,"ion-header",1)(1,"ion-toolbar")(2,"ion-buttons",2),p(3,"ion-menu-button"),c(),s(4,"ion-title"),u(5,"Schedules"),c(),s(6,"ion-buttons",3)(7,"ion-button",4),h("click",function(){return D(d),T(t.addSchedule())}),p(8,"ion-icon",5),c()()()(),s(9,"ion-content",6)(10,"ion-list",null,0),P(12,ge,1,1,"app-schedule-tile",7,_e),c()()}e&2&&(m("translucent",!0),l(9),m("fullscreen",!0),l(3),B(t.schedules))},dependencies:[g,me,Z,se,U,oe,le,K,L,X,re],changeDetection:0}));let o=n;return o})();export{He as ScheduleListPage};
