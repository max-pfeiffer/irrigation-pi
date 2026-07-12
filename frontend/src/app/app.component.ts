import { Component } from '@angular/core';
import { RouterLink, RouterLinkActive } from '@angular/router';
import {
  IonApp,
  IonContent,
  IonIcon,
  IonLabel,
  IonList,
  IonListHeader,
  IonMenu,
  IonMenuToggle,
  IonNote,
  IonRouterOutlet,
  IonSplitPane,
} from '@ionic/angular/standalone';
import { addIcons } from 'ionicons';
import {
  informationOutline,
  informationSharp,
  timeOutline,
  timerOutline,
  timerSharp,
  timeSharp,
  toggleOutline,
  toggleSharp,
} from 'ionicons/icons';

@Component({
  selector: 'app-root',
  templateUrl: 'app.component.html',
  styleUrls: ['app.component.scss'],
  imports: [
    RouterLink,
    RouterLinkActive,
    IonApp,
    IonSplitPane,
    IonMenu,
    IonContent,
    IonList,
    IonListHeader,
    IonNote,
    IonMenuToggle,
    IonIcon,
    IonLabel,
    IonRouterOutlet,
  ],
})
export class AppComponent {
  public appPages = [
    { title: 'Schedules', url: '/schedules', icon: 'timer' },
    { title: 'Relays', url: '/relays', icon: 'toggle' },
    { title: 'Info', url: '/info', icon: 'information' },
    { title: 'Date & Time', url: '/system-date-time', icon: 'time' },
  ];

  public constructor() {
    addIcons({
      timerOutline,
      timerSharp,
      toggleOutline,
      toggleSharp,
      informationOutline,
      informationSharp,
      timeOutline,
      timeSharp,
    });
  }
}
