import {
  ChangeDetectionStrategy,
  Component,
  inject,
  signal,
} from '@angular/core';
import {
  IonButtons,
  IonContent,
  IonHeader,
  IonItem,
  IonLabel,
  IonList,
  IonMenuButton,
  IonTitle,
  IonToolbar,
  ViewDidEnter,
} from '@ionic/angular/standalone';
import {
  BoardInfoDisplayMapping,
  RaspberryPiBoardInfo,
} from '../../models/info.models';
import { InfoService } from '../../services/info.service';

@Component({
  selector: 'app-board-info-list',
  templateUrl: './board-info.page.html',
  styleUrls: ['./board-info.page.scss'],
  changeDetection: ChangeDetectionStrategy.OnPush,
  imports: [
    IonHeader,
    IonToolbar,
    IonButtons,
    IonMenuButton,
    IonTitle,
    IonContent,
    IonList,
    IonItem,
    IonLabel,
  ],
})
export class BoardInfoPage implements ViewDidEnter {
  public infoService = inject(InfoService);

  public fields = signal<{ key: string; value: string }[]>([]);

  public ionViewDidEnter(): void {
    this.loadInfo();
  }

  public loadInfo(): void {
    this.infoService.getInfo().subscribe((boardInfo: RaspberryPiBoardInfo) => {
      const _fields = [];
      for (const [key, value] of Object.entries(boardInfo)) {
        _fields.push({
          key: BoardInfoDisplayMapping[key],
          value: value as string,
        });
      }
      this.fields.set(_fields);
    });
  }
}
